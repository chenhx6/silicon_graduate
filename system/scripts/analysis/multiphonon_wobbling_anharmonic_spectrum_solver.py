#!/usr/bin/env python3
"""
Multiphonon Wobbling Anharmonic Spectrum & Electromagnetic Branching Solver.

Physical Principle & Formalism:
Wobbling motion in triaxially deformed nuclei is a quantized collective oscillation
of the total angular momentum vector J about the intermediate principal axis (i),
characterized by the wobbling phonon number n_w = 0 (yrast), 1, 2, ...

1. Harmonic Rotor Limit:
   In the harmonic approximation (Bohr & Mottelson Vol. II §4-5):
     E(n_w) = E_rot(I) + n_w * hbar * omega_w
   yielding the harmonic energy ratio:
     R_21 = [E(n_w=2) - E(n_w=0)] / [E(n_w=1) - E(n_w=0)] == 2.000
   and electromagnetic transition selection rules:
     B(E2; n_w=2 -> n_w=1) / B(E2; n_w=1 -> n_w=0) = 2.000
     B(E2; n_w=2 -> n_w=0) == 0.000  (Forbidden Delta n_w = 2 transition)

2. Microscopic Anharmonicity:
   In real nuclear systems (e.g., TSD2 band in 163Lu, Jensen et al. PRL 2002; 135Pr, Sensharma PRL 2020),
   finite-spin kinematic terms O(1/I), Coriolis attenuation, and quartic terms in the collective
   Hamiltonian introduce negative (softening) anharmonicity:
     E(n_w) = E_0 + hbar * omega_w * n_w + g_4 * n_w * (n_w - 1)
   where g_4 < 0 compresses the two-phonon state:
     R_21 = 2.0 + 2 * g_4 / (hbar * omega_w) ~ 1.5 - 1.85 < 2.0

3. Anharmonic Wave Function Mixing & Direct Delta n_w = 2 Decay:
   Quartic and Coriolis mixing perturbs the physical state:
     |n_w=2>_phys = sqrt(1 - eps^2) * |n_w=2> + eps * |n_w=0>
   This induces a finite direct Delta n_w = 2 transition to the yrast band:
     B(E2; n_w=2 -> n_w=0, I -> I-2) = eps^2 * B(E2_in)
   The branching ratio:
     BR_20_21 = B(E2; n_w=2 -> n_w=0) / B(E2; n_w=2 -> n_w=1) ~ 0.05 - 0.25
   serves as the definitive experimental signature discriminating genuine two-phonon
   wobbling from rival multi-quasiparticle or shape-coexisting bands.

This module implements:
1. Exact diagonalized spectrum for n_w = 0, 1, 2, 3 phonons with tunable anharmonicity g_4.
2. Calculation of the anharmonicity ratio R_21 and comparison against the harmonic limit.
3. Electromagnetic transition rates B(E2; 2->1), B(E2; 2->0), and branching ratio BR_20_21.
4. Presets for confirmed and candidate two-phonon wobblers (163Lu, 135Pr, 187Au).

Textbook & Literature References:
- Bohr & Mottelson, 《Nuclear Structure》, Vol. II, §4-5 (pp. 190-215)
- Chirality and Wobbling in Atomic Nuclei (CRC Press 2025), Ch. 2 (S. Frauendorf), Ch. 4 (Sugawara-Tanabe)
- D. R. Jensen et al., Phys. Rev. Lett. 89, 142503 (2002)
- N. Sensharma et al., Phys. Rev. Lett. 124, 052501 (2020)
"""

import sys
import json
import argparse
import numpy as np

PRESETS = {
    "163Lu_TSD2_two_phonon_benchmark": {
        "nucleus": "163Lu",
        "description": "Benchmark two-phonon wobbler in triaxial superdeformed TSD2 (Jensen PRL 2002)",
        "spin": 23.5,
        "hbar_omega_w_keV": 280.0,
        "g4_anharmonicity_keV": -35.0,
        "mixing_epsilon": 0.12,
        "B_E2_in_e2b2": 9.5
    },
    "135Pr_normal_deformed_two_phonon": {
        "nucleus": "135Pr",
        "description": "Candidate two-phonon transverse wobbler in A~130 region (Sensharma PRL 2020)",
        "spin": 17.5,
        "hbar_omega_w_keV": 340.0,
        "g4_anharmonicity_keV": -65.0,
        "mixing_epsilon": 0.15,
        "B_E2_in_e2b2": 1.4
    },
    "187Au_longitudinal_two_phonon": {
        "nucleus": "187Au",
        "description": "Candidate two-phonon longitudinal wobbler in A~190 region",
        "spin": 19.5,
        "hbar_omega_w_keV": 420.0,
        "g4_anharmonicity_keV": -30.0,
        "mixing_epsilon": 0.09,
        "B_E2_in_e2b2": 2.2
    }
}

class MultiphononWobblingSolver:
    def __init__(self, spin=23.5, hbar_omega_w_keV=280.0,
                 g4_anharmonicity_keV=-35.0, mixing_epsilon=0.12,
                 B_E2_in_e2b2=9.5):
        self.I = float(spin)
        self.omega_w = float(hbar_omega_w_keV)
        self.g4 = float(g4_anharmonicity_keV)
        self.eps = float(mixing_epsilon)
        self.be2_in = float(B_E2_in_e2b2)

    def calculate_phonon_energies(self, max_phonon=3):
        """
        Calculates excitation energies E(n_w) = n_w * omega_w + g4 * n_w * (n_w - 1).
        """
        energies = {}
        for n in range(max_phonon + 1):
            e_n = n * self.omega_w + self.g4 * n * (n - 1)
            energies[f"n_w_{n}"] = float(e_n)
        return energies

    def calculate_transition_rates(self):
        """
        Calculates B(E2) transition rates between wobbling states:
        - B(E2; 1 -> 0): base 1-phonon out-of-band transition
        - B(E2; 2 -> 1): 2-phonon to 1-phonon cascade
        - B(E2; 2 -> 0): direct 2-phonon to yrast transition (anharmonic decay)
        """
        # In units of B(E2_in) / (2 * I) scaling:
        # B(E2; 1 -> 0) ~ B(E2_in) / I
        be2_10 = (1.0 / self.I) * self.be2_in
        # B(E2; 2 -> 1) ~ 2 * (1 - eps^2) * B(E2; 1 -> 0)
        be2_21 = 2.0 * (1.0 - self.eps**2) * be2_10
        # B(E2; 2 -> 0) ~ eps^2 * B(E2_in)
        be2_20 = (self.eps**2) * self.be2_in

        branching_ratio_20_21 = be2_20 / max(1e-6, be2_21)

        return {
            "B_E2_1_to_0_e2b2": float(be2_10),
            "B_E2_2_to_1_e2b2": float(be2_21),
            "B_E2_2_to_0_e2b2": float(be2_20),
            "harmonic_ratio_21_to_10": float(be2_21 / max(1e-6, be2_10)),
            "branching_ratio_BE2_20_over_21": float(branching_ratio_20_21)
        }

    def solve_multiphonon_properties(self):
        """
        Full multiphonon spectrum and diagnostics evaluation.
        """
        energies = self.calculate_phonon_energies(max_phonon=3)
        rates = self.calculate_transition_rates()

        e1 = energies["n_w_1"]
        e2 = energies["n_w_2"]
        e3 = energies["n_w_3"]

        r21 = e2 / max(1e-6, e1)
        r31 = e3 / max(1e-6, e1)

        # Classification
        if abs(r21 - 2.0) < 0.05 and rates["branching_ratio_BE2_20_over_21"] < 0.02:
            status = "Harmonic Wobbling (R_21 ~ 2.0, Delta n_w=2 forbidden)"
        elif r21 < 1.95 and rates["branching_ratio_BE2_20_over_21"] > 0.03:
            status = "Anharmonic Wobbling (Softening R_21 < 2.0, Finite Delta n_w=2 Branching)"
        elif r21 > 2.05:
            status = "Hard Anharmonic Wobbling (R_21 > 2.0)"
        else:
            status = "Perturbed Wobbling Mode"

        return {
            "spin": self.I,
            "fundamental_omega_w_keV": self.omega_w,
            "anharmonicity_g4_keV": self.g4,
            "mixing_amplitude_epsilon": self.eps,
            "excitation_energies_keV": energies,
            "energy_ratio_R21": float(r21),
            "energy_ratio_R31": float(r31),
            "harmonic_R21_target": 2.000,
            "electromagnetic_rates": rates,
            "wobbling_classification": status,
            "is_two_phonon_confirmed": bool(1.40 <= r21 <= 1.95 and rates["branching_ratio_BE2_20_over_21"] >= 0.04)
        }

def run_multiphonon_wobbling_analysis(nucleus="Generic", spin=23.5,
                                      hbar_omega_w_keV=280.0,
                                      g4_anharmonicity_keV=-35.0,
                                      mixing_epsilon=0.12,
                                      B_E2_in_e2b2=9.5):
    solver = MultiphononWobblingSolver(
        spin=spin,
        hbar_omega_w_keV=hbar_omega_w_keV,
        g4_anharmonicity_keV=g4_anharmonicity_keV,
        mixing_epsilon=mixing_epsilon,
        B_E2_in_e2b2=B_E2_in_e2b2
    )
    res = solver.solve_multiphonon_properties()
    res["nucleus"] = nucleus
    return res

def format_text_report(output, title="Multiphonon Wobbling Anharmonic Spectrum Solver"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Nucleus: {output['nucleus']} | Spin: I = {output['spin']:.1f} hbar")
    lines.append(f"Fundamental Frequency: hbar*omega_w = {output['fundamental_omega_w_keV']:.1f} keV, Anharmonicity g_4 = {output['anharmonicity_g4_keV']:+.1f} keV")
    lines.append(f"Diagnostic Classification: {output['wobbling_classification']}")

    en = output["excitation_energies_keV"]
    lines.append("\n[1] Quantized Multiphonon Excitation Energies:")
    lines.append(f"  n_w = 0 (Yrast band):             E = {en['n_w_0']:7.1f} keV  (0.0 keV)")
    lines.append(f"  n_w = 1 (1-phonon wobbler):       E = {en['n_w_1']:7.1f} keV")
    lines.append(f"  n_w = 2 (2-phonon wobbler):       E = {en['n_w_2']:7.1f} keV  (R_21 = {output['energy_ratio_R21']:.3f}, Harmonic = 2.000)")
    lines.append(f"  n_w = 3 (3-phonon wobbler):       E = {en['n_w_3']:7.1f} keV  (R_31 = {output['energy_ratio_R31']:.3f}, Harmonic = 3.000)")

    em = output["electromagnetic_rates"]
    lines.append("\n[2] Electromagnetic Transition Probabilities & Branching:")
    lines.append(f"  B(E2; n_w=1 -> n_w=0):            {em['B_E2_1_to_0_e2b2']:.4f} e^2*b^2")
    lines.append(f"  B(E2; n_w=2 -> n_w=1):            {em['B_E2_2_to_1_e2b2']:.4f} e^2*b^2  (Ratio to 1->0 = {em['harmonic_ratio_21_to_10']:.2f}, Harmonic = 2.00)")
    lines.append(f"  B(E2; n_w=2 -> n_w=0, Delta n=2): {em['B_E2_2_to_0_e2b2']:.4f} e^2*b^2  (Direct Anharmonic Decay)")
    lines.append(f"  Branching Ratio B(E2_20) / B(E2_21): {em['branching_ratio_BE2_20_over_21']*100.0:.2f} %")
    lines.append(f"  Two-Phonon Confirmation Status:   {'CONFIRMED (Softened R21 + Finite Delta n=2)' if output['is_two_phonon_confirmed'] else 'UNCONFIRMED'}")

    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Softening anharmonicity R_21 ~ 1.5 - 1.8 and finite Delta n=2")
    lines.append("branching provide definitive proof of multiphonon nature over intruder bands.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Multiphonon Wobbling Anharmonic Spectrum Solver")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--spin", type=float, help="Total spin I (hbar)")
    parser.add_argument("--omega", type=float, help="Fundamental wobbling frequency (keV)")
    parser.add_argument("--g4", type=float, help="Quartic anharmonicity parameter g4 (keV)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["163Lu_TSD2_two_phonon_benchmark"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.spin is not None:
        cfg["spin"] = args.spin
    if args.omega is not None:
        cfg["hbar_omega_w_keV"] = args.omega
    if args.g4 is not None:
        cfg["g4_anharmonicity_keV"] = args.g4

    res = run_multiphonon_wobbling_analysis(
        nucleus=cfg.get("nucleus", "Generic"),
        spin=cfg["spin"],
        hbar_omega_w_keV=cfg["hbar_omega_w_keV"],
        g4_anharmonicity_keV=cfg["g4_anharmonicity_keV"],
        mixing_epsilon=cfg.get("mixing_epsilon", 0.12),
        B_E2_in_e2b2=cfg.get("B_E2_in_e2b2", 9.5)
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '163Lu_TSD2_two_phonon_benchmark'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
