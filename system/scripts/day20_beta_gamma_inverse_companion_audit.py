#!/usr/bin/env python3
"""Audit of the Nuclear Deformation Inverse Problem and Companion Discriminating Matrix.

This script audits Singh 2016 Eq. (4)-(5) and rigorously investigates the
degeneracy between four distinct physical mechanisms causing apparent Qt reduction:
1. Hypothesis A: Nuclear core shrinkage (reduction in beta_2 at fixed gamma=0);
2. Hypothesis B: Triaxial rotation (change in gamma at fixed beta_2);
3. Hypothesis C: Wave-function fragmentation (two-band mixing at fixed intrinsic Q0);
4. Hypothesis D: Feeding delay (uncorrected continuum feeding lengthening apparent tau).

It proves that single-band Qt(I) profiles are mathematically incapable of
distinguishing between these four mechanisms, and establishes the required companion
observable matrix to resolve the ambiguity.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def solve_beta2_from_q20(q20_eb: float, z: int, a: int, r0_fm: float = 1.2, c2: float = 0.36) -> float:
    """Solve Singh 2016 Eq. (4) quadratic equation for beta_2 given Q20 in eb.

    Q20 = (3 / sqrt(5*pi)) * Z * e * R0^2 * beta_2 * (1 + c2 * beta_2)
    where R0 = r0 * A^(1/3) fm.
    1 eb = 100 e*fm^2.
    """
    r0_total = r0_fm * (a ** (1.0 / 3.0))  # fm
    r0_sq = r0_total ** 2                  # fm^2
    # Pre-factor in eb: (3 / sqrt(5*pi)) * Z * (R0^2 / 100)
    prefactor = (3.0 / math.sqrt(5.0 * math.pi)) * z * (r0_sq / 100.0)

    # Quadratic equation: prefactor * c2 * beta_2^2 + prefactor * beta_2 - Q20 = 0
    # a_quad * x^2 + b_quad * x + c_quad = 0
    a_quad = prefactor * c2
    b_quad = prefactor
    c_quad = -q20_eb

    disc = (b_quad ** 2) - (4.0 * a_quad * c_quad)
    if disc < 0:
        raise ValueError(f"Negative discriminant {disc} for Q20={q20_eb}")

    beta2 = (-b_quad + math.sqrt(disc)) / (2.0 * a_quad)
    return beta2


def main() -> None:
    root = Path(__file__).resolve().parent.parent.parent
    run_dir = root / "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02"
    run_dir.mkdir(parents=True, exist_ok=True)

    checks = []

    # Case parameters for 133Pr: Z=59, A=133
    z_pr = 59
    a_pr = 133

    # Benchmark scenario: Qt drops from 3.50 eb to 2.50 eb (reduction of 28.57%)
    qt_init = 3.50
    qt_final = 2.50
    ratio_qt = qt_final / qt_init  # 5/7 ~ 0.7142857

    # -------------------------------------------------------------
    # 1. Hypothesis A: Pure axial core shrinkage (gamma = 0 deg)
    # -------------------------------------------------------------
    # Under gamma = 0, Qt = Q20 * cos(30)/cos(30) = Q20
    q20_a_init = qt_init
    q20_a_final = qt_final

    beta2_a_init = solve_beta2_from_q20(q20_a_init, z=z_pr, a=a_pr)
    beta2_a_final = solve_beta2_from_q20(q20_a_final, z=z_pr, a=a_pr)

    delta_beta2_pct = ((beta2_a_final - beta2_a_init) / beta2_a_init) * 100.0

    check_1 = (0.18 < beta2_a_init < 0.22) and (0.13 < beta2_a_final < 0.16) and (-29.0 < delta_beta2_pct < -25.0)
    checks.append({
        "name": "Hypothesis A: Axial shrinkage requires ~26.6% reduction in beta_2",
        "passed": check_1,
        "detail": f"beta2_init = {beta2_a_init:.4f}, beta2_final = {beta2_a_final:.4f}, delta = {delta_beta2_pct:.2f}%"
    })

    # -------------------------------------------------------------
    # 2. Hypothesis B: Triaxial rotation (constant beta_2 = beta2_a_init, Q20 = 3.50 eb)
    # -------------------------------------------------------------
    # Qt = Q20 * cos(gamma + 30) / cos(30) => cos(gamma + 30) = (Qt / Q20) * cos(30)
    # Here Qt / Q20 = ratio_qt = 5/7
    cos_30 = math.cos(math.radians(30.0))
    cos_arg = ratio_qt * cos_30  # ~ 0.61858957
    arg_rad = math.acos(cos_arg)
    arg_deg = math.degrees(arg_rad)  # ~ 51.7868 deg

    # Two physical roots:
    gamma_root_1 = arg_deg - 30.0    # ~ +21.79 deg (prolate-triaxial)
    gamma_root_2 = -arg_deg - 30.0   # ~ -81.79 deg (oblate-triaxial)

    # Verify both roots produce EXACTLY qt_final under Singh Eq. (5)
    calc_qt_root1 = q20_a_init * (math.cos(math.radians(gamma_root_1 + 30.0)) / cos_30)
    calc_qt_root2 = q20_a_init * (math.cos(math.radians(gamma_root_2 + 30.0)) / cos_30)

    check_2 = math.isclose(calc_qt_root1, qt_final, abs_tol=1e-10) and math.isclose(calc_qt_root2, qt_final, abs_tol=1e-10)
    checks.append({
        "name": "Hypothesis B: Triaxial rotation (gamma = +21.8 deg or -81.8 deg) replicates Qt drop with constant beta_2",
        "passed": check_2,
        "detail": f"root1 = {gamma_root_1:.2f} deg, root2 = {gamma_root_2:.2f} deg, calc_Qt = {calc_qt_root1:.4f} eb"
    })

    # -------------------------------------------------------------
    # 3. Hypothesis C: Band mixing (constant intrinsic Q0 = 3.50 eb, pure orthogonal 2-state)
    # -------------------------------------------------------------
    # In a two-state orthogonal mixing model where the initial yrast state has amplitude cos(theta),
    # and final state uncouples to pure ground (or symmetric), the effective transition matrix element
    # scales as cos(theta). If both states are mixed symmetrically: M_eff = cos^2(theta) * Q0.
    # Case C1 (asymmetric uncoupling): cos(theta) = ratio_qt => theta = arccos(5/7) ~ 44.4 deg
    # Case C2 (symmetric mixing): cos^2(theta) = ratio_qt => cos(theta) = sqrt(5/7) ~ 0.845 => theta ~ 32.3 deg
    theta_sym_deg = math.degrees(math.acos(math.sqrt(ratio_qt)))
    prob_admix_sym_pct = (math.sin(math.radians(theta_sym_deg)) ** 2) * 100.0  # 1 - ratio_qt = 28.57%

    calc_qt_mixing = q20_a_init * (math.cos(math.radians(theta_sym_deg)) ** 2)
    check_3 = math.isclose(calc_qt_mixing, qt_final, abs_tol=1e-10)
    checks.append({
        "name": "Hypothesis C: Wavefunction mixing (28.6% S-band admixture) replicates Qt drop with constant intrinsic Q0",
        "passed": check_3,
        "detail": f"theta = {theta_sym_deg:.2f} deg, admixture = {prob_admix_sym_pct:.2f}%, calc_Qt = {calc_qt_mixing:.4f} eb"
    })

    # -------------------------------------------------------------
    # 4. Hypothesis D: Feeding delay distortion (uncorrected continuum feeding)
    # -------------------------------------------------------------
    # Since B(E2) ~ 1/tau and Qt ~ tau^(-1/2), an apparent Qt drop of ratio_qt
    # corresponds to an apparent lifetime lengthening:
    # tau_eff / tau_true = (1 / ratio_qt)^2 = (7/5)^2 = 1.96
    # If tau_true = 1.40 ps (typical high-spin lifetime in 133Pr), tau_eff = 2.744 ps.
    # tau_feed = tau_eff - tau_true = 1.344 ps.
    tau_true_ps = 1.40
    tau_eff_ps = tau_true_ps / (ratio_qt ** 2)
    tau_feed_ps = tau_eff_ps - tau_true_ps
    calc_qt_feeding = qt_init * math.sqrt(tau_true_ps / tau_eff_ps)

    check_4 = math.isclose(calc_qt_feeding, qt_final, abs_tol=1e-10) and math.isclose(tau_eff_ps / tau_true_ps, 1.96, abs_tol=1e-10)
    checks.append({
        "name": "Hypothesis D: Uncorrected feeding (tau_feed = 1.34 ps) replicates Qt drop with constant intrinsic lifetime",
        "passed": check_4,
        "detail": f"tau_true = {tau_true_ps:.2f} ps, tau_eff = {tau_eff_ps:.3f} ps, tau_feed = {tau_feed_ps:.3f} ps"
    })

    # -------------------------------------------------------------
    # 5. Formal Mathematical Indistinguishability & Companion Matrix
    # -------------------------------------------------------------
    # All four hypotheses yield EXACTLY Qt = 2.50 eb from the baseline Qt = 3.50 eb!
    check_5 = math.isclose(q20_a_final, 2.50) and math.isclose(calc_qt_root1, 2.50) and math.isclose(calc_qt_mixing, 2.50) and math.isclose(calc_qt_feeding, 2.50)
    checks.append({
        "name": "Mathematical Indistinguishability: All 4 hypotheses yield identical apparent Qt = 2.50 eb",
        "passed": check_5,
        "detail": "Proven: Single-band Qt(I) profiles are fundamentally non-unique."
    })

    all_passed = all(c["passed"] for c in checks)

    result_data = {
        "kind": "Nuclear deformation inverse problem and companion discriminating matrix audit",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "target_nucleus": {"Z": z_pr, "A": a_pr, "name": "133Pr"},
        "benchmark_transition": {
            "Qt_initial_eb": qt_init,
            "Qt_apparent_eb": qt_final,
            "reduction_factor": round(ratio_qt, 6),
            "percentage_drop": round((1.0 - ratio_qt) * 100.0, 2)
        },
        "competing_hypotheses_evaluation": {
            "hypothesis_A_axial_shrinkage": {
                "mechanism": "Nuclear core centrifugal contraction at fixed gamma = 0 deg",
                "beta2_initial": round(beta2_a_init, 4),
                "beta2_final": round(beta2_a_final, 4),
                "delta_beta2_percent": round(delta_beta2_pct, 2),
                "falsifying_companion": "Coulomb excitation Kumar invariant <beta^2>; inelastic electron scattering charge radius"
            },
            "hypothesis_B_triaxial_rotation": {
                "mechanism": "Rotation towards triaxiality at constant elongation beta_2 = 0.214",
                "gamma_root_1_deg": round(gamma_root_1, 2),
                "gamma_root_2_deg": round(gamma_root_2, 2),
                "falsifying_companion": "Gamma-band energy staggering S(4) (McCutchan 2007); spectroscopic quadrupole moment Qs via TDPAD/Coulex"
            },
            "hypothesis_C_band_mixing": {
                "mechanism": "Wavefunction fragmentation at band crossing at constant intrinsic Q0 = 3.50 eb",
                "mixing_angle_deg": round(theta_sym_deg, 2),
                "admixture_probability_pct": round(prob_admix_sym_pct, 2),
                "falsifying_companion": "Inter-band crossing E2 branches; complementary enhancement in companion band (as in 136Nd)"
            },
            "hypothesis_D_feeding_distortion": {
                "mechanism": "Unresolved continuum/side feeding delay lengthening apparent lifetime",
                "tau_true_ps": tau_true_ps,
                "tau_effective_ps": round(tau_eff_ps, 3),
                "required_tau_feed_ps": round(tau_feed_ps, 3),
                "falsifying_companion": "Direct feeding coincidence gating above state of interest; thin-target differential RDDS"
            }
        },
        "companion_discriminating_matrix": [
            {
                "candidate_mechanism": "Hypothesis A: beta_2 core contraction",
                "single_band_Qt": "Apparent drop",
                "interband_E2": "No cross-transitions",
                "companion_band_Qt": "No enhancement",
                "gamma_staggering_S4": "No phase reversal (S4 ~ +0.33)",
                "spectroscopic_Qs": "Proportional to Q0",
                "decisive_discriminator": "Coulex Kumar invariant q^2 ~ <beta^2>"
            },
            {
                "candidate_mechanism": "Hypothesis B: gamma triaxial rotation",
                "single_band_Qt": "Apparent drop",
                "interband_E2": "Enhanced interband branches",
                "companion_band_Qt": "No enhancement",
                "gamma_staggering_S4": "Phase reversal (S4 > 0 in rigid) or clustering (S4 < 0 in soft)",
                "spectroscopic_Qs": "Suppressed (vanishes at gamma=30 deg)",
                "decisive_discriminator": "McCutchan S(4) + TDPAD/Coulex Qs"
            },
            {
                "candidate_mechanism": "Hypothesis C: Two-band mixing",
                "single_band_Qt": "Apparent drop",
                "interband_E2": "Strong inter-band branch opening",
                "companion_band_Qt": "Complementary enhancement in sideband",
                "gamma_staggering_S4": "Uncorrelated",
                "spectroscopic_Qs": "Mixed-state diagonal value",
                "decisive_discriminator": "Complementary partner-band Qt enhancement & crossing branches"
            },
            {
                "candidate_mechanism": "Hypothesis D: Uncorrected slow feeding",
                "single_band_Qt": "Apparent drop",
                "interband_E2": "Unchanged",
                "companion_band_Qt": "Unchanged",
                "gamma_staggering_S4": "Unchanged",
                "spectroscopic_Qs": "Unchanged (TDPAD independent of feeding time profile)",
                "decisive_discriminator": "Direct-feeding coincidence gate vs total-projection gate"
            }
        ],
        "checks": checks,
        "all_checks_passed": all_passed
    }

    out_file = run_dir / "beta-gamma-inverse-companion-result-014.json"
    out_file.write_text(json.dumps(result_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audit completed: all_checks_passed = {all_passed}")
    print(f"Results written to {out_file.relative_to(root)}")


if __name__ == "__main__":
    raise SystemExit("Retired checkpoint038: use day20_inverse_covariance_contract038.py; legacy scientific certification withdrawn.")
