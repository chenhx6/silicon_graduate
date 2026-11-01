#!/usr/bin/env python3
"""
multiphonon_wobbling_anharmonic_calculator.py
=============================================
Multi-Phonon Wobbling Hierarchy (n_w = 0, 1, 2), Anharmonicity Parameter &
Electromagnetic Selection Rule Auditor.

Physics & Formulation:
----------------------
1. Harmonic Wobbling Energy Hierarchy:
   In ideal harmonic wobbling (Bohr-Mottelson / Frauendorf):
     E(I, n_w) - E(I, 0) = n_w * hbar * omega_wob(I)
     Ratio R_21 = [ E(I, 2) - E(I, 0) ] / [ E(I, 1) - E(I, 0) ] == 2.0

2. Anharmonicity Shift & Parameter A_anharm:
   Non-linear rotor terms introduce an anharmonic shift Delta_anharm:
     E(I, n_w) = E(I, 0) + n_w * hbar*omega + 0.5 * n_w * (n_w - 1) * Delta_anharm
     A_anharm = (R_21 / 2.0) - 1.0 = Delta_anharm / (2 * hbar * omega)
   - A_anharm == 0: Pure harmonic vibrator.
   - A_anharm < 0: Phonon softening (sub-harmonic, common in 163Lu, 165Lu).
   - A_anharm > 0: Phonon stiffening.

3. Multi-Phonon Electromagnetic Selection Rules:
   - Harmonic phonon transitions obey Delta_n_w = +/- 1 strictly:
     B(E2; n_w=2 -> n_w=1) ~ 2.0 * B(E2; n_w=1 -> n_w=0)
   - Cross-over transition Delta_n_w = 2 is forbidden:
     B(E2; n_w=2 -> n_w=0) == 0 (harmonic limit)
   - Anharmonic branching ratio limit:
     R_crossover = B(E2; 2 -> 0) / B(E2; 2 -> 1) < 0.10 for valid multi-phonon wobbling.

References:
  - C. M. Petrache, Chirality and Wobbling in Atomic Nuclei, Springer (2024).
  - K. Tanabe and K. Sugawara-Tanabe, Phys. Rev. C 95, 064315 (2017).
  - D. R. Jensen et al., Phys. Rev. Lett. 89, 142503 (2002) [Multi-phonon in 163Lu].
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def evaluate_multiphonon_wobbling_energies(
    omega_wob_keV: float = 350.0,
    Delta_anharm_keV: float = -40.0
) -> Dict[str, Any]:
    """
    Computes theoretical energies for n_w = 0, 1, 2 wobbling phonon states.
    """
    E0 = 0.0
    E1 = E0 + omega_wob_keV
    E2 = E0 + 2.0 * omega_wob_keV + Delta_anharm_keV

    r_21 = (E2 - E0) / max(E1 - E0, 1e-4)
    a_anharm = (r_21 / 2.0) - 1.0

    if abs(a_anharm) < 0.03:
        status = "Harmonic_Phonon (A_anharm ~ 0, R_21 ~ 2.0)"
    elif a_anharm < 0:
        status = f"Subharmonic_Softening (A_anharm = {a_anharm*100:.1f}%, 2-phonon lower than harmonic)"
    else:
        status = f"Anharmonic_Stiffening (A_anharm = +{a_anharm*100:.1f}%)"

    return {
        "one_phonon_energy_E1_keV": round(E1, 1),
        "two_phonon_energy_E2_keV": round(E2, 1),
        "anharmonic_shift_Delta_keV": round(Delta_anharm_keV, 1),
        "energy_ratio_R21": round(r_21, 3),
        "anharmonicity_parameter_A": round(a_anharm, 4),
        "classification": status
    }


def audit_multiphonon_wobbling_candidate(
    E0_keV: float,
    E1_keV: float,
    E2_keV: float,
    be2_2_to_1: float = 0.60,
    be2_1_to_0: float = 0.35,
    be2_2_to_0: float = 0.02
) -> Dict[str, Any]:
    """
    Audits an experimental 3-band candidate against multi-phonon wobbling criteria:
    1. E(2) - E(0) ~ 2 * [E(1) - E(0)].
    2. B(E2; 2->1) / B(E2; 1->0) ~ 2.0.
    3. B(E2; 2->0) / B(E2; 2->1) < 0.10 (crossover suppression).
    """
    dE1 = E1_keV - E0_keV
    dE2 = E2_keV - E0_keV

    r21 = dE2 / max(dE1, 1e-4)
    a_anharm = (r21 / 2.0) - 1.0

    ratio_be2_step = be2_2_to_1 / max(be2_1_to_0, 1e-6)
    ratio_be2_cross = be2_2_to_0 / max(be2_2_to_1, 1e-6)

    checks = []
    score = 0
    total = 3

    # Check 1: Energy ratio R_21 in [1.5, 2.3]
    if 1.5 <= r21 <= 2.3:
        checks.append(f"PASS: Energy ratio R_21 = {r21:.2f} within multi-phonon window [1.5, 2.3]")
        score += 1
    else:
        checks.append(f"FAIL: Energy ratio R_21 = {r21:.2f} violates multi-phonon expectation (~2.0)")

    # Check 2: B(E2; 2->1) enhanced relative to 1->0 (~ 1.5 to 2.5)
    if 1.3 <= ratio_be2_step <= 2.8:
        checks.append(f"PASS: B(E2; 2->1) / B(E2; 1->0) = {ratio_be2_step:.2f} ~ 2 (Harmonic phonon enhancement)")
        score += 1
    else:
        checks.append(f"FAIL: B(E2; 2->1) / B(E2; 1->0) = {ratio_be2_step:.2f} deviates from harmonic scaling (~2.0)")

    # Check 3: Crossover Delta_nw = 2 suppressed (< 0.10)
    if ratio_be2_cross <= 0.10:
        checks.append(f"PASS: Crossover B(E2; 2->0) / B(E2; 2->1) = {ratio_be2_cross:.3f} <= 0.10 (Delta_nw = 2 forbidden)")
        score += 1
    else:
        checks.append(f"FAIL: Crossover B(E2; 2->0) / B(E2; 2->1) = {ratio_be2_cross:.3f} > 0.10 (Significant Delta_nw = 2 leakage)")

    if score == total:
        verdict = "CONFIRMED_TWO_PHONON_WOBBLING (Jensen/Petrache standard satisfied)"
    elif score >= 2:
        verdict = "ANHARMONIC_TWO_PHONON_CANDIDATE"
    else:
        verdict = "REJECTED_AS_TWO_PHONON_WOBBLING (Spurious alignment or quasiparticle band)"

    return {
        "energy_splitting_1_phonon_keV": round(dE1, 1),
        "energy_splitting_2_phonon_keV": round(dE2, 1),
        "energy_ratio_R21": round(r21, 3),
        "anharmonicity_index_A": round(a_anharm, 4),
        "be2_ratio_stepover": round(ratio_be2_step, 2),
        "be2_ratio_crossover": round(ratio_be2_cross, 4),
        "score": f"{score}/{total}",
        "verdict": verdict,
        "audit_checks": checks
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   MULTI-PHONON WOBBLING (n_w = 0, 1, 2) & ANHARMONICITY ANALYZER")
    lines.append("=" * 72)

    th = summary["theoretical_model"]
    lines.append(" MULTI-PHONON THEORETICAL HIERARCHY:")
    lines.append(f"   One-Phonon State n_w = 1       : {th['one_phonon_energy_E1_keV']} keV")
    lines.append(f"   Two-Phonon State n_w = 2       : {th['two_phonon_energy_E2_keV']} keV (Shift = {th['anharmonic_shift_Delta_keV']} keV)")
    lines.append(f"   Energy Ratio R_21              : {th['energy_ratio_R21']} (Harmonic limit = 2.000)")
    lines.append(f"   Anharmonicity Parameter A      : {th['anharmonicity_parameter_A']}")
    lines.append(f"   Regime Classification          : {th['classification']}")
    lines.append("-" * 72)

    if "experimental_audit" in summary:
        ea = summary["experimental_audit"]
        lines.append(" EXPERIMENTAL MULTI-PHONON WOBBLING AUDIT:")
        lines.append(f"   Verdict                        : {ea['verdict']} ({ea['score']})")
        lines.append(f"   B(E2; 2->1) / B(E2; 1->0) Ratio: {ea['be2_ratio_stepover']}")
        lines.append(f"   Crossover B(E2; 2->0) / B(E2; 2->1): {ea['be2_ratio_crossover']}")
        lines.append("   Audit Check Findings:")
        for chk in ea["audit_checks"]:
            lines.append(f"     * {chk}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Harmonic wobbling requires R_21 = 2.0 and B(E2; 2->1) ~ 2 * B(E2; 1->0).")
    lines.append("   - Cross-over transition Delta_n_w = 2 is strictly forbidden by selection rules.")
    lines.append("   - Benchmark established in triaxial superdeformed 163Lu and 165Lu (Jensen 2002).")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Phonon Wobbling Hierarchy & Anharmonicity Analyzer."
    )
    parser.add_argument("--hw", type=float, default=320.0, help="One-phonon wobbling energy in keV (default: 320.0)")
    parser.add_argument("--delta-anharm", type=float, default=-40.0, help="Anharmonic shift Delta in keV (default: -40.0)")
    parser.add_argument("--audit", action="store_true", help="Perform experimental candidate audit")
    parser.add_argument("--e0", type=float, default=0.0, help="Bandhead 0 energy in keV")
    parser.add_argument("--e1", type=float, default=320.0, help="1-phonon band energy in keV")
    parser.add_argument("--e2", type=float, default=600.0, help="2-phonon band energy in keV")
    parser.add_argument("--be2-21", type=float, default=0.62, help="B(E2; 2->1) in e^2 b^2")
    parser.add_argument("--be2-10", type=float, default=0.32, help="B(E2; 1->0) in e^2 b^2")
    parser.add_argument("--be2-20", type=float, default=0.015, help="B(E2; 2->0) in e^2 b^2")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    th_res = evaluate_multiphonon_wobbling_energies(args.hw, args.delta_anharm)
    summary = {"theoretical_model": th_res}

    if args.audit or args.e2 != 600.0:
        ea_res = audit_multiphonon_wobbling_candidate(
            args.e0, args.e1, args.e2, args.be2_21, args.be2_10, args.be2_20
        )
        summary["experimental_audit"] = ea_res
    elif args.hw == 320.0:
        ea_res = audit_multiphonon_wobbling_candidate(0.0, 320.0, 600.0, 0.62, 0.32, 0.015)
        summary["experimental_audit"] = ea_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
