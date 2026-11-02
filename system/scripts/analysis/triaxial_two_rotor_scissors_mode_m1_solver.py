#!/usr/bin/env python3
"""
Triaxial Two-Rotor Model (TRM) Scissors Mode M1 Excitation & Splitting Solver.

Physical Principle & Formalism:
The Scissors Mode (Lo Iudice & Palumbo 1978, Bohle et al. 1984) is a fundamental
collective magnetic dipole (M1) excitation in deformed nuclei, representing the
counter-rotational out-of-phase oscillation of the proton cloud against the neutron cloud
like the blades of a pair of scissors.

In Axially Symmetric Deformed Nuclei (gamma = 0 deg):
The scissors oscillation occurs solely about the transverse axis perpendicular to the
symmetry axis, producing a single prominent 1^+ magnetic dipole resonance at E_1+ ~ 2.5 - 3.5 MeV
with transition strength B(M1; 0^+ -> 1^+) ~ 2 - 3 mu_N^2.

In Triaxially Deformed Nuclei (0 < gamma < 60 deg):
Axial symmetry is broken, so the proton and neutron ellipsoids have three unequal principal
moments of inertia (J_s, J_i, J_l). The relative rotational displacement vector alpha_pn
decouples into TWO orthogonal scissors modes:
1. Short-Axis Scissors Mode (k = s):
   Proton-neutron counter-oscillation in the intermediate-long plane about the short axis.
   Restoring deformation parameter:
     delta_s = sqrt(15 / pi) * beta_2 * sin(gamma)
2. Long-Axis Scissors Mode (k = l):
   Proton-neutron counter-oscillation in the short-intermediate plane about the long axis.
   Restoring deformation parameter:
     delta_l = sqrt(15 / pi) * beta_2 * sin(pi/3 - gamma)

Restoring Force Parameters C_k:
Governed by the volume symmetry energy b_sym ~ 28 - 32 MeV:
  C_k = (4 * Z * N / A^2) * b_sym * delta_k^2 * (A / 6.0)

Reduced Moment of Inertia J_red,k:
  J_red,k = (Z * N / A^2) * J_k(beta_2, gamma)
where J_k is the collective moment of inertia along axis k.

Excitation Energies & M1 Strengths:
The scissors eigenfrequencies and energies are:
  E_1+,k = hbar * omega_k = hbar * sqrt( C_k / J_red,k )
The reduced magnetic dipole transition strength from the 0^+ ground state is:
  B(M1; 0^+ -> 1_k^+) = (3 / (16 * pi)) * J_red,k * omega_k * (g_p - g_n)^2  (mu_N^2)
where (g_p - g_n) ~ (g_l,p - g_l,n) ~ 1.0 mu_N for orbital current collectivity.

Splitting Signature:
When gamma = 0 deg: delta_s = 0, delta_l = max -> Single scissors peak.
When gamma ~ 20 - 30 deg: Both delta_s and delta_l are non-zero, splitting the M1 resonance
into a clean doublet of 1^+ states separated by Delta E_M1 ~ 0.4 - 1.0 MeV!

This module implements:
1. Exact Two-Rotor Model (TRM) restoring force and reduced inertia tensors for arbitrary (beta_2, gamma).
2. Eigenfrequency and energy calculation for both short-axis and long-axis scissors modes.
3. B(M1; 0^+ -> 1^+) transition strengths, splitting Delta E_M1, and Energy-Weighted Sum Rule (EWSR).
4. Presets for classic axial and triaxial nuclei (156Gd, 134Ba, 196Pt).

Textbook & Literature References:
- K. Heyde, 《Basic Ideas and Concepts in Nuclear Physics》 (3rd Ed.), Ch. 9, §9.4
- W. Greiner & J. A. Maruhn, 《Nuclear Models》 (Springer 1996), Ch. 11
- N. Lo Iudice & F. Palumbo, Phys. Rev. Lett. 41, 1532 (1978)
- D. Bohle et al., Phys. Lett. B 137, 27 (1984)
- A. A. Raduta, 《Nuclear Structure with Coherent States》, Ch. 4
"""

import sys
import json
import argparse
import numpy as np

PRESETS = {
    "156Gd_axial_prolate_baseline": {
        "nucleus": "156Gd",
        "description": "Classic axial prolate scissors mode baseline (beta2=0.34, gamma=0 deg)",
        "A": 156, "Z": 64,
        "beta2": 0.34,
        "gamma_deg": 0.0,
        "b_sym_MeV": 30.0,
        "moi_base_MeV_inv": 35.0,  # hbar^2 / MeV
        "g_p_minus_g_n": 1.00      # mu_N
    },
    "134Ba_triaxial_scissors_doublet": {
        "nucleus": "134Ba",
        "description": "Transitional triaxial nucleus with scissors mode splitting (beta2=0.22, gamma=24 deg)",
        "A": 134, "Z": 56,
        "beta2": 0.22,
        "gamma_deg": 24.0,
        "b_sym_MeV": 29.0,
        "moi_base_MeV_inv": 28.0,
        "g_p_minus_g_n": 0.95
    },
    "196Pt_gamma_soft_oblate": {
        "nucleus": "196Pt",
        "description": "Heavy gamma-soft/oblate scissors mode candidate (beta2=0.15, gamma=45 deg)",
        "A": 196, "Z": 78,
        "beta2": 0.15,
        "gamma_deg": 45.0,
        "b_sym_MeV": 31.0,
        "moi_base_MeV_inv": 42.0,
        "g_p_minus_g_n": 0.92
    }
}

class TriaxialScissorsModeM1Solver:
    def __init__(self, A=134, Z=56, beta2=0.22, gamma_deg=24.0,
                 b_sym_MeV=29.0, moi_base_MeV_inv=28.0, g_diff=1.00):
        self.A = float(A)
        self.Z = float(Z)
        self.N = self.A - self.Z
        self.beta2 = float(beta2)
        self.gamma_deg = float(gamma_deg)
        self.gamma = np.radians(gamma_deg)
        self.b_sym = float(b_sym_MeV)
        self.J_base = float(moi_base_MeV_inv)
        self.g_diff = float(g_diff)

    def calculate_deformation_parameters(self):
        """
        Calculates relative proton-neutron shear deformations delta_s and delta_l:
        delta_s = sqrt(15 / pi) * beta2 * sin(gamma)
        delta_l = sqrt(15 / pi) * beta2 * sin(pi/3 - gamma)
        """
        pref = np.sqrt(15.0 / np.pi) * self.beta2
        delta_s = pref * np.sin(self.gamma)
        delta_l = pref * np.sin(np.pi / 3.0 - self.gamma)
        return float(max(0.0, delta_s)), float(max(0.0, delta_l))

    def calculate_moments_of_inertia(self):
        """
        Calculates principal moments of inertia J_s, J_i, J_l.
        Using rigid/irrotational interpolation:
        J_k = J_base * [1.0 - 0.35 * cos(gamma - 2*pi*k / 3)]
        s: k=1, i: k=2, l: k=3
        """
        j_s = self.J_base * (1.0 - 0.35 * np.cos(self.gamma - 2.0 * np.pi / 3.0))
        j_i = self.J_base * (1.0 - 0.35 * np.cos(self.gamma - 4.0 * np.pi / 3.0))
        j_l = self.J_base * (1.0 - 0.35 * np.cos(self.gamma))
        return float(j_s), float(j_i), float(j_l)

    def solve_scissors_modes(self):
        """
        Solves restoring forces, eigenfrequencies, and B(M1) strengths for both modes.
        """
        delta_s, delta_l = self.calculate_deformation_parameters()
        j_s, j_i, j_l = self.calculate_moments_of_inertia()

        # Restoring force constant C_k:
        # C_k = (4 * Z * N / A^2) * b_sym * delta_k^2 * (A / 6.0) in MeV
        factor_c = (4.0 * self.Z * self.N / (self.A**2)) * self.b_sym * (self.A / 6.0)
        C_s = factor_c * (delta_s**2)
        C_l = factor_c * (delta_l**2)

        # Reduced moment of inertia: J_red = (Z * N / A^2) * J
        factor_j = (self.Z * self.N) / (self.A**2)
        J_red_s = factor_j * j_s
        J_red_l = factor_j * j_l

        # Excitation energies E_1+ = hbar * omega:
        # hbar = 1 in MeV units, omega = sqrt(C / J_red) in MeV
        if delta_s > 1e-4 and J_red_s > 1e-4:
            E_s_MeV = float(np.sqrt(C_s / J_red_s))
            # B(M1) in mu_N^2:
            # B(M1) = (3 / (16 * pi)) * J_red * omega * (g_p - g_n)^2
            # 1 hbar = 1, J_red in MeV^-1, omega in MeV -> J_red * omega is dimensionless angular momentum
            BM1_s = float((3.0 / (16.0 * np.pi)) * (J_red_s * E_s_MeV) * (self.g_diff**2))
        else:
            E_s_MeV = 0.0
            BM1_s = 0.0

        if delta_l > 1e-4 and J_red_l > 1e-4:
            E_l_MeV = float(np.sqrt(C_l / J_red_l))
            BM1_l = float((3.0 / (16.0 * np.pi)) * (J_red_l * E_l_MeV) * (self.g_diff**2))
        else:
            E_l_MeV = 0.0
            BM1_l = 0.0

        # Total M1 strength & Energy-Weighted Sum Rule (EWSR):
        total_BM1 = BM1_s + BM1_l
        ewsr_MeV_muN2 = (E_s_MeV * BM1_s) + (E_l_MeV * BM1_l)
        splitting_MeV = float(abs(E_l_MeV - E_s_MeV)) if (E_s_MeV > 0 and E_l_MeV > 0) else 0.0

        is_split = bool(self.gamma_deg > 3.0 and self.gamma_deg < 57.0 and BM1_s > 0.05 and BM1_l > 0.05)

        return {
            "nucleus_A": self.A, "nucleus_Z": self.Z,
            "beta2": self.beta2, "gamma_deg": self.gamma_deg,
            "shear_deformations": {"delta_s": delta_s, "delta_l": delta_l},
            "moments_of_inertia": {"J_s": j_s, "J_i": j_i, "J_l": j_l},
            "scissors_short_axis": {
                "name": "Short-Axis Mode 1^+_s",
                "energy_MeV": E_s_MeV,
                "BM1_muN2": BM1_s
            },
            "scissors_long_axis": {
                "name": "Long-Axis Mode 1^+_l",
                "energy_MeV": E_l_MeV,
                "BM1_muN2": BM1_l
            },
            "scissors_splitting_MeV": splitting_MeV,
            "total_B_M1_muN2": float(total_BM1),
            "EWSR_MeV_muN2": float(ewsr_MeV_muN2),
            "is_scissors_doublet_split": is_split
        }

def run_scissors_mode_analysis(nucleus="Generic", A=134, Z=56, beta2=0.22,
                               gamma_deg=24.0, b_sym_MeV=29.0,
                               moi_base_MeV_inv=28.0, g_diff=1.00):
    solver = TriaxialScissorsModeM1Solver(
        A=A, Z=Z, beta2=beta2, gamma_deg=gamma_deg,
        b_sym_MeV=b_sym_MeV, moi_base_MeV_inv=moi_base_MeV_inv, g_diff=g_diff
    )
    res = solver.solve_scissors_modes()
    res["nucleus"] = nucleus
    return res

def format_text_report(output, title="Triaxial Two-Rotor Scissors Mode M1 Solver"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Nucleus: {output['nucleus']} (A={int(output['nucleus_A'])}, Z={int(output['nucleus_Z'])})")
    lines.append(f"Deformation: beta_2 = {output['beta2']:.3f}, gamma = {output['gamma_deg']:.1f} deg")
    sd = output["shear_deformations"]
    lines.append(f"Shear Deformations: delta_s = {sd['delta_s']:.3f}, delta_l = {sd['delta_l']:.3f}")

    ms = output["scissors_short_axis"]
    ml = output["scissors_long_axis"]
    lines.append("\n[1] Orthogonal Scissors Eigenmodes:")
    if ms["energy_MeV"] > 0:
        lines.append(f"  Short-Axis Scissors Mode (1^+_s):  E = {ms['energy_MeV']:.3f} MeV,  B(M1) = {ms['BM1_muN2']:.3f} mu_N^2")
    else:
        lines.append(f"  Short-Axis Scissors Mode (1^+_s):  Inactive (Axial Symmetry)")

    if ml["energy_MeV"] > 0:
        lines.append(f"  Long-Axis Scissors Mode (1^+_l):   E = {ml['energy_MeV']:.3f} MeV,  B(M1) = {ml['BM1_muN2']:.3f} mu_N^2")
    else:
        lines.append(f"  Long-Axis Scissors Mode (1^+_l):   Inactive")

    lines.append("\n[2] Triaxial Scissors Splitting & Sum Rules:")
    lines.append(f"  Scissors Energy Splitting:         Delta E_M1 = {output['scissors_splitting_MeV']:.3f} MeV")
    lines.append(f"  Total M1 Excitation Strength:      sum B(M1)  = {output['total_B_M1_muN2']:.3f} mu_N^2")
    lines.append(f"  Energy-Weighted Sum Rule (EWSR):   EWSR       = {output['EWSR_MeV_muN2']:.3f} MeV*mu_N^2")
    lines.append(f"  Resonance Structure:               {'DOUBLET SPLIT (Triaxial Signature)' if output['is_scissors_doublet_split'] else 'SINGLE PEAK (Axial Rotor)'}")

    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Triaxial shape lifts the axial scissors degeneracy,")
    lines.append("splitting the 1+ M1 resonance into a characteristic two-mode doublet.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Triaxial Scissors Mode M1 Solver")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--beta2", type=float, help="Quadrupole deformation beta2")
    parser.add_argument("--gamma", type=float, help="Triaxial deformation gamma (degrees)")
    parser.add_argument("--bsym", type=float, help="Volume symmetry energy b_sym (MeV)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["134Ba_triaxial_scissors_doublet"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.beta2 is not None:
        cfg["beta2"] = args.beta2
    if args.gamma is not None:
        cfg["gamma_deg"] = args.gamma
    if args.bsym is not None:
        cfg["b_sym_MeV"] = args.bsym

    res = run_scissors_mode_analysis(
        nucleus=cfg.get("nucleus", "Generic"),
        A=cfg["A"], Z=cfg["Z"],
        beta2=cfg["beta2"],
        gamma_deg=cfg["gamma_deg"],
        b_sym_MeV=cfg.get("b_sym_MeV", 29.0),
        moi_base_MeV_inv=cfg.get("moi_base_MeV_inv", 28.0),
        g_diff=cfg.get("g_p_minus_g_n", 1.00)
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '134Ba_triaxial_scissors_doublet'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
