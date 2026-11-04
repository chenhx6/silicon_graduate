#!/usr/bin/env python3
"""
in_beam_experiment_analysis_pipeline.py
=======================================
Unified In-Beam Experimental Nuclear Spectroscopy Pipeline & Data Analysis Workbench.

Physics & Experimental Architecture:
------------------------------------
This demonstration pipeline combines several analytical components for source-summary replay,
synthetic fixtures, and caller-supplied derived inputs. It is not a raw event-level reduction
producer and does not certify experimental or publication results:

  Stage 1: Entrance Channel Reaction Kinematics & Residue Optimization
           - Calculates E_cm, Coulomb barrier V_B0, and Wong fusion cross section.
           - Evaluates RLDM fission barrier cutoff and xn statistical evaporation optimal beam energy.
  Stage 2: Relativistic Doppler Reconstruction & Array Resolution Budget
           - Evaluates shifted laboratory energy E_lab(theta).
           - Decomposes peak broadening: detector opening angle Delta_E_theta (peaks at 90 deg),
             recoil velocity spread Delta_E_beta, and isotropic neutron recoil straggling Delta_E_strag.
  Stage 3: Angular Distribution & Multipole Mixing Ratio delta(E2/M1) Dual Roots
           - Computes algebraic Yamazaki F-coefficients without look-up tables.
           - Solves the analytic quadratic equation for a_2, returning both mathematically allowed real roots.
  Stage 4: Lifetime Inversion via DSAM (or RDDS Plunger)
           - Inverts excited nuclear state lifetime tau (ps / fs) from Doppler attenuation factor F(tau).
           - Employs LSS stopping powers and Blaugrund multiple scattering corrections.
  Stage 5: Reduced Electromagnetic Transition Probabilities & Quadrupole Deformation
           - Extracts B(E2), B(M1), transition quadrupole moment Q_t, and deformation beta_2.
           - Evaluates Grodzins product rule ratio G and superfluid pairing reduction.
  Stage 6: Physical Mode Diagnostic & Controversy Resolution
           - Wobbling Diagnostic: Checks whether inter-band transition is E2-dominated (|delta| >> 1),
             computes transverse wobbling frequency slope d(omega)/dI, and applies Elena Lawrie TiP criteria.
           - Chiral Doublet Diagnostic: Evaluates twin band energy splitting Delta_E(I), B(M1)/B(E2)
             odd-even staggering, and 3D aplanarity volume metric V_chiral.
           - Low-Count Statistics: Evaluates exact Feldman-Cousins unified physical intervals if n <= 10.

References:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000).
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005).
  - 林承键, 《重离子核反应》, 科学出版社 (2017).
  - 朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006).
  - C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025).
"""

import math
import json
import argparse
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

# Ensure analysis modules can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent))

from heavy_ion_fusion_spin_distribution_wong_calculator import calculate_heavy_ion_fusion_wong
from in_beam_doppler_broadening_array_correction_calculator import calculate_doppler_broadening_budget
from directional_correlation_f_coefficients_calculator import invert_delta_dual_roots
from dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator import invert_lifetime_from_f_tau
from triaxial_wobbling_tip_chiral_analyzer import calculate_transverse_wobbling_spectrum, classify_tip_vs_phonon_wobbling, analyze_chiral_doublet_staggering
from feldman_cousins_unified_confidence_interval_calculator import calculate_poisson_fc_interval
from grodzins_deformation_beta2_quadrupole_inverter import invert_beta2_and_quadrupole


def run_full_in_beam_pipeline(
    Z_p: int, A_p: int,
    Z_t: int, A_t: int,
    E_lab_MeV: float,
    E_gamma_keV: float,
    detector_angle_deg: float = 90.0,
    opening_angle_deg: float = 8.0,
    a2_exp: Optional[float] = None,
    I_initial: float = 7.5,
    I_final: float = 6.5,
    F_tau_exp: Optional[float] = None,
    F_tau_err: Optional[float] = None,
    alpha_stop_ps: float = 0.82,
    n_counts: Optional[int] = None,
    background_counts: float = 0.0,
    candidate_mode: str = "wobbling",
    E_2plus_core_keV: Optional[float] = None,
    B_E2_core_e2_b2: Optional[float] = None,
    data_kind: str = "synthetic_or_source_summary_replay"
) -> Dict[str, Any]:
    """
    Executes a demonstration-derived analysis chain.

    Presets are synthetic or source-summary replay inputs. They do not carry raw event
    data, detector response, feeding covariance, or a paper-level evidence gate.
    """
    pipeline_report = {
        "pipeline_version": "1.0-demonstration-derived",
        "candidate_mode": candidate_mode,
        "data_kind": data_kind,
        "evidence_boundary": [
            "Preset and caller inputs are derived or source-summary values, not raw event data.",
            "Outputs are conditional calculations and screening diagnostics.",
            "Experimental claims require source locators, response, feeding, covariance, and independent observables."
        ]
    }

    # 1. Reaction Kinematics & Fusion Evaporation
    fus_res = calculate_heavy_ion_fusion_wong(Z_p, A_p, Z_t, A_t, E_lab_MeV)
    pipeline_report["stage1_entrance_reaction"] = {
        "reaction": fus_res["reaction"],
        "E_lab_MeV": E_lab_MeV,
        "E_cm_MeV": fus_res["E_cm_MeV"],
        "Wong_cross_section_mb": fus_res["Wong_cross_section_mb"],
        "l_crit_hbar": fus_res["critical_angular_momentum_l_crit_hbar"],
        "compound_nucleus_E_star_MeV": fus_res["compound_nucleus_E_star_MeV"],
        "xn_planning": fus_res["xn_evaporation_planning"]
    }

    # 2. Relativistic Doppler Broadening & Shift
    # Estimate beta from center-of-mass recoil
    A_CN = A_p + A_t
    m_u = 931.494
    E_recoil_MeV = E_lab_MeV * (float(A_p) * float(A_CN)) / ((float(A_CN)) ** 2) # approx
    beta_recoil = math.sqrt(2.0 * E_lab_MeV / (float(A_p) * m_u)) * (float(A_p) / float(A_CN))
    dop_res = calculate_doppler_broadening_budget(
        E0_keV=E_gamma_keV, beta_recoil=beta_recoil, theta_deg=detector_angle_deg, opening_angle_deg=opening_angle_deg
    )
    pipeline_report["stage2_doppler_broadening"] = dop_res

    # 3. Multipole Mixing Ratio delta(E2/M1) Dual Roots
    if a2_exp is not None:
        delta_res = invert_delta_dual_roots(a2_exp, I_initial, I_final)
        pipeline_report["stage3_angular_distribution_delta"] = delta_res
    else:
        pipeline_report["stage3_angular_distribution_delta"] = None

    # 4. Lifetime Inversion via DSAM
    if F_tau_exp is not None:
        lt_res = invert_lifetime_from_f_tau(F_tau_exp, F_tau_err, alpha_stop_ps)
        pipeline_report["stage4_lifetime_dsam"] = lt_res
    else:
        pipeline_report["stage4_lifetime_dsam"] = None

    # 5. Core Deformation & Grodzins Scaling
    Z_CN = Z_p + Z_t
    if E_2plus_core_keV is not None and B_E2_core_e2_b2 is not None:
        grod_res = invert_beta2_and_quadrupole(Z_CN - 2, A_CN - 4, B_E2_core_e2_b2, E_2plus_core_keV)
        pipeline_report["stage5_core_deformation"] = grod_res
    else:
        pipeline_report["stage5_core_deformation"] = None

    # 6. Physical Mode Diagnostic
    diag_summary = {}
    if candidate_mode == "wobbling":
        # Check delta: if delta is small (< 1), E2 dominance fails!
        if a2_exp is not None:
            r1 = delta_res["root1_small_magnitude"]
            r2 = delta_res["root2_large_magnitude"]
            diag_summary["delta_root1"] = r1
            diag_summary["delta_root2"] = r2
            if r1 is not None and abs(r1) < 1.0 and r2 is not None and abs(r2) < 1.0:
                diag_summary["e2_dominance_check"] = "FAILED (Both roots have |delta| < 1 => M1 dominates!)"
                diag_summary["wobbling_verdict"] = "conditional-candidate-screen: pure wobbling branch disfavored by both small-|delta| roots; competing TiP/configuration explanations remain."
            else:
                diag_summary["e2_dominance_check"] = "PASS / AMBIGUOUS (Contains |delta| > 1 root; independent polarization required)."
                diag_summary["wobbling_verdict"] = "conditional-candidate-screen: a large-|delta| branch remains; independent polarization and source-level response checks are required."
    elif candidate_mode == "chiral":
        diag_summary["chiral_criteria"] = "Twin bands require identical parity, Delta_E(I) -> 0, and B(M1)/B(E2) odd-even staggering."

    # 7. Low-Count Statistics
    if n_counts is not None and n_counts <= 15:
        fc_res = calculate_poisson_fc_interval(n_obs=n_counts, background=background_counts, cl=0.90)
        pipeline_report["stage7_low_count_feldman_cousins"] = fc_res
    else:
        pipeline_report["stage7_low_count_feldman_cousins"] = None

    pipeline_report["stage6_mode_diagnostic"] = diag_summary
    return pipeline_report


def format_text_report(pipe: Dict[str, Any]) -> str:
    lines = [
        "=" * 76,
        "   IN-BEAM EXPERIMENTAL NUCLEAR SPECTROSCOPY PIPELINE WORKBENCH",
        "   Integrated Analysis Suite: Kinematics -> Doppler -> DCO -> DSAM -> Modes",
        "=" * 76,
    ]

    # Stage 1
    s1 = pipe["stage1_entrance_reaction"]
    lines.extend([
        f" [STAGE 1] REACTION ENTRANCE CHANNEL & RESIDUE DESIGN:",
        f"   Reaction System             : {s1['reaction']} at E_lab = {s1['E_lab_MeV']:.1f} MeV",
        f"   Wong Fusion Cross Section   : {s1['Wong_cross_section_mb']:.1f} mb (E_cm = {s1['E_cm_MeV']:.2f} MeV)",
        f"   Critical Angular Momentum   : l_crit = {s1['l_crit_hbar']} hbar (E* = {s1['compound_nucleus_E_star_MeV']:.1f} MeV)",
        "   Optimal Residue Channels:",
    ])
    for ch in s1["xn_planning"][:3]:
        lines.append(f"     {ch['channel']:<5} -> {ch['residual_nucleus']:<18} Opt E* = {ch['optimal_E_star_MeV']:5.1f} MeV  (Rec E_lab = {ch['recommended_E_lab_MeV']:5.1f} MeV)")
    lines.append("-" * 76)

    # Stage 2
    s2 = pipe["stage2_doppler_broadening"]
    lines.extend([
        f" [STAGE 2] RELATIVISTIC DOPPLER BROADENING BUDGET (E_0 = {s2['E0_keV']:.1f} keV):",
        f"   Recoil Velocity beta = v/c  : {s2['recoil_velocity_beta']:.4f}  (Detector angle = {s2['detector_angle_deg']:.1f} deg)",
        f"   Observed Lab Shifted Energy : {s2['E_lab_shifted_keV']:.2f} keV (Doppler shift: {s2['Doppler_shift_keV']:+.2f} keV)",
        f"   Opening Angle Broadening    : {s2['broadening_detector_angle_dE_theta_keV']:.2f} keV  (Opening angle = {s2['detector_opening_angle_deg']:.1f} deg)",
        f"   Neutron Straggling Spread   : {s2['broadening_neutron_straggling_dE_strag_keV']:.2f} keV  (Recoil kick deflection: {s2['recoil_angular_straggling_deg']:.2f} deg)",
        f"   Total In-Beam Peak FWHM     : {s2['total_observed_fwhm_keV']:.2f} keV  (Intrinsic: {s2['intrinsic_detector_fwhm_keV']:.1f} keV)",
        "-" * 76,
    ])

    # Stage 3
    if pipe["stage3_angular_distribution_delta"] is not None:
        s3 = pipe["stage3_angular_distribution_delta"]
        lines.extend([
            f" [STAGE 3] ANGULAR DISTRIBUTION & MULTIPOLE MIXING RATIO DUAL ROOTS:",
            f"   Transition Assignment       : {s3['initial_spin_Ii']} -> {s3['final_spin_If']} (Preset/source-summary a_2 = {s3['a2_measured']:.4f})",
            f"   Algebraic Roots for delta   : Root 1 = {s3['root1_small_magnitude']:.4f},  Root 2 = {s3['root2_large_magnitude']:.4f}",
            f"   Root 1 E2 Fraction          : {s3['root1_E2_percentage']:.1f}% E2",
            f"   Root 2 E2 Fraction          : {s3['root2_E2_percentage']:.1f}% E2",
            "-" * 76,
        ])

    # Stage 4
    if pipe["stage4_lifetime_dsam"] is not None:
        s4 = pipe["stage4_lifetime_dsam"]
        lines.extend([
            f" [STAGE 4] DSAM PICOSECOND LIFETIME INVERSION:",
            f"   Doppler Attenuation F_exp   : {s4['F_exp']:.3f} (Stopping scale alpha = {s4['alpha_stop_ps']:.3f} ps)",
            f"   Inverted Level Lifetime     : tau = {s4['tau_ps']:.4f} ps  ({s4['tau_fs']:.1f} fs)",
            f"   Lifetime Classification     : {s4['lifetime_regime']}",
            "-" * 76,
        ])

    # Stage 5
    if pipe["stage5_core_deformation"] is not None:
        s5 = pipe["stage5_core_deformation"]
        lines.extend([
            f" [STAGE 5] RESIDUE DEFORMATION & GRODZINS SYSTEMATICS:",
            f"   Quadrupole Deformation beta2: {s5['quadrupole_deformation_beta2']:.4f}  [{s5['deformation_classification']}]",
            f"   Intrinsic Quadrupole Q_0    : {s5['intrinsic_quadrupole_moment_Q0_eb']:.3f} e*b",
            f"   Superfluid MOI Reduction    : J_exp / J_rig = {s5['superfluid_pairing_reduction_ratio']:.3f}",
            "-" * 76,
        ])

    # Stage 6
    s6 = pipe["stage6_mode_diagnostic"]
    lines.extend([
        f" [STAGE 6] PHYSICAL MODE DIAGNOSTIC & SCIENTIFIC VERDICT ({pipe['candidate_mode'].upper()}):",
    ])
    for k, v in s6.items():
        lines.append(f"   {k:<26} : {v}")
    lines.append("-" * 76)

    # Stage 7
    if pipe["stage7_low_count_feldman_cousins"] is not None:
        s7 = pipe["stage7_low_count_feldman_cousins"]
        lines.extend([
            f" [STAGE 7] LOW-COUNT POISSON FELDMAN-COUSINS PHYSICAL INTERVAL:",
            f"   Observed Counts n_obs       : {s7['n_obs']} (Expected background b = {s7['background_b']:.2f})",
            f"   90% CL Unified Interval     : [{s7['fc_interval_lower']:.3f}, {s7['fc_interval_upper']:.3f}] ({s7['interval_classification']})",
            "-" * 76,
        ])

    lines.extend([
        "=" * 76,
        "   PIPELINE DEMONSTRATION COMPLETE: derived output; source/raw/response review required before experimental or paper use.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Demonstration-derived in-beam spectroscopy analysis chain"
    )
    parser.add_argument("--preset", type=str, default="135Pr_wobbling_audit",
                        choices=["135Pr_wobbling_audit", "134Pr_chiral_audit", "163Lu_tsd_wobbling"],
                        help="Synthetic or source-summary replay preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    if args.preset == "135Pr_wobbling_audit":
        # 14N (Z=7, A=14) + 124Sn (Z=50, A=124) -> 138Pr* -> 135Pr + 3n at 65 MeV
        # Source-summary replay input; not a raw event-level reanalysis.
        # 726.5 keV, a2 and F(tau) remain conditional preset values.
        res = run_full_in_beam_pipeline(
            Z_p=7, A_p=14, Z_t=50, A_t=124, E_lab_MeV=65.0,
            E_gamma_keV=726.5, detector_angle_deg=90.0, opening_angle_deg=8.0,
            a2_exp=-0.18, I_initial=8.5, I_final=7.5,
            F_tau_exp=0.55, F_tau_err=0.04, alpha_stop_ps=0.85,
            candidate_mode="wobbling",
            E_2plus_core_keV=409.2, B_E2_core_e2_b2=0.78
        )
    elif args.preset == "134Pr_chiral_audit":
        # 11B (Z=5, A=11) + 128Te (Z=52, A=128) -> 139Pr* -> 134Pr + 5n at 60 MeV
        # Gated 450 keV chiral transition, a2 = 0.32
        res = run_full_in_beam_pipeline(
            Z_p=5, A_p=11, Z_t=52, A_t=128, E_lab_MeV=60.0,
            E_gamma_keV=450.0, detector_angle_deg=90.0, opening_angle_deg=8.0,
            a2_exp=0.32, I_initial=11.0, I_final=10.0,
            F_tau_exp=0.62, F_tau_err=0.03, alpha_stop_ps=0.80,
            candidate_mode="chiral",
            E_2plus_core_keV=409.2, B_E2_core_e2_b2=0.78
        )
    elif args.preset == "163Lu_tsd_wobbling":
        # 48Ca (Z=20, A=48) + 119Sn (Z=50, A=119) -> 167Lu* -> 163Lu + 4n at 205 MeV
        res = run_full_in_beam_pipeline(
            Z_p=20, A_p=48, Z_t=50, A_t=119, E_lab_MeV=205.0,
            E_gamma_keV=580.0, detector_angle_deg=90.0, opening_angle_deg=8.0,
            a2_exp=0.45, I_initial=17.5, I_final=15.5,
            F_tau_exp=0.70, F_tau_err=0.04, alpha_stop_ps=0.78,
            candidate_mode="wobbling",
            E_2plus_core_keV=80.0, B_E2_core_e2_b2=4.0
        )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
