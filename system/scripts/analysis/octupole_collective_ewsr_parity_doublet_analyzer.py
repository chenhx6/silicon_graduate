#!/usr/bin/env python3
"""
octupole_collective_ewsr_parity_doublet_analyzer.py
===================================================
Microscopic Octupole Collective Modes, Isoscalar Energy-Weighted Sum Rules (IS-EWSR),
Intrinsic Electric Dipole Moment (D0) & Alternating-Parity Pear-Shaped Dynamics Engine.

Physics & Formalism:
--------------------
1. Octupole Single-Particle Weisskopf Unit:
   Based on 卢希庭《原子核物理（修订版）》第 8 章 §8.3 and Bohr & Mottelson Vol. II §6-3:
     B_Wu(E3) = (1 / (16 * pi)) * R0^6 * e^2 = 0.05944 * A^(2/3) * e^2 * fm^6
     (where R0 = 1.20 * A^(1/3) fm).

2. Isoscalar Octupole Energy-Weighted Sum Rule (IS-EWSR):
   According to Bohr & Mottelson Vol. II Eq. (6-82):
     S_IS(E3) = sum_n (E_n - E_0) * B(E3; 0+ -> 3_n-)
              = (147 / (4 * pi)) * [hbar^2 / (2 * m_N)] * (Z^2 / A) * R0^4
   where hbar^2 / (2 * m_N) = 20.7355 MeV * fm^2.
   The fractional sum rule exhaustion of the lowest 3_1- state is:
     EWSR_pct = [ E(3_1-) * 7 * B(E3; 3- -> 0+) ] / S_IS(E3) * 100%

3. Experimental Alternating-Parity Band Branching Ratio B(E1)/B(E2):
   From experimental peak intensity ratios and transition energies:
     [ B(E1; I -> I-1) / B(E2; I -> I-2) ]_exp = 1.30e-6 * [ E_gamma(E2)^5 / E_gamma(E1)^3 ] * [ I_gamma(E1) / I_gamma(E2) ]  (fm^-2)

4. Alaga Geometric Clebsch-Gordan Ratio & D0 Inversion:
   For K = 0 alternating-parity bands (Butler & Nazarewicz 1996; Gaffney 2013):
     <I 0 1 0 | I-1 0>^2 / <I 0 2 0 | I-2 0>^2 = 2*(2*I - 1) / [ 3*(I - 1) ]
   Theoretical branching:
     B(E1)/B(E2) = (16 / 15) * [ (2*I - 1) / (I - 1) ] * (D0 / Q0)^2
   Inverting for the intrinsic electric dipole moment |D0| (e*fm):
     |D0| = Q0 * sqrt( (15 / 16) * [ (I - 1) / (2*I - 1) ] * [B(E1)/B(E2)]_exp )
   where intrinsic quadrupole moment Q0 = (3 / sqrt(5*pi)) * Z * R0^2 * beta2 (in e*fm^2).

5. Pear-Shaped Octupole Deformation beta3 Inversion:
   In the liquid-drop redistribution model (Leander & Chen 1988):
     D0_LD = C_LD * (N - Z) * Z * e * beta2 * beta3   (with C_LD ~ 0.000687 fm)
     beta3 = |D0| / [ C_LD * (N - Z) * Z * beta2 ]

6. Parity Displacement Staggering delta_E(I):
   delta_E(I) = E(I-) - 0.5 * [ E((I+1)+) + E((I-1)+) ]
   - Rigid pear-shaped rotor: delta_E(I) ~ 0 even at low spin (e.g. 224Ra, 226Ra);
   - Centrifugally stabilized octupole: delta_E(I) large at low spin, collapsing to 0 at high spin;
   - Harmonic octupole vibration: delta_E(I) ~ const >> 0 (e.g. 208Pb).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "224Ra_pear_shaped": {
        "description": "224Ra alternating-parity pear-shaped rotor (Gaffney et al. Nature 2013)",
        "nucleus": "224Ra",
        "A_mass": 224,
        "Z_charge": 88,
        "beta2": 0.190,
        "E_3minus_keV": 290.0,
        "B_E3_down_Wu": 38.0,
        "pos_spins": [0.0, 2.0, 4.0, 6.0, 8.0, 10.0],
        "pos_energies_keV": [0.0, 84.4, 254.0, 479.0, 751.0, 1063.0],
        "neg_spins": [1.0, 3.0, 5.0, 7.0, 9.0],
        "neg_energies_keV": [216.0, 290.0, 433.0, 641.0, 907.0],
        "branching_test": {
            "spin_I": 5.0,
            "E_E1_keV": 179.0,
            "E_E2_keV": 143.0,
            "I_E1": 35.0,
            "I_E2": 100.0
        }
    },
    "144Ba_octupole_deformed": {
        "description": "144Ba octupole deformed fission fragment (Bucher et al. PRL 2016)",
        "nucleus": "144Ba",
        "A_mass": 144,
        "Z_charge": 56,
        "beta2": 0.240,
        "E_3minus_keV": 838.0,
        "B_E3_down_Wu": 48.0,
        "pos_spins": [0.0, 2.0, 4.0, 6.0, 8.0],
        "pos_energies_keV": [0.0, 199.0, 530.0, 959.0, 1469.0],
        "neg_spins": [1.0, 3.0, 5.0, 7.0],
        "neg_energies_keV": [759.0, 838.0, 1076.0, 1442.0],
        "branching_test": {
            "spin_I": 3.0,
            "E_E1_keV": 308.0,
            "E_E2_keV": 79.0,
            "I_E1": 25.0,
            "I_E2": 100.0
        }
    },
    "208Pb_spherical_phonon": {
        "description": "208Pb spherical harmonic octupole phonon benchmark",
        "nucleus": "208Pb",
        "A_mass": 208,
        "Z_charge": 82,
        "beta2": 0.050,
        "E_3minus_keV": 2614.5,
        "B_E3_down_Wu": 34.0,
        "pos_spins": [0.0, 2.0],
        "pos_energies_keV": [0.0, 4085.0],
        "neg_spins": [3.0],
        "neg_energies_keV": [2614.5]
    }
}


def calculate_octupole_ewsr(A_mass, Z_charge, E_3minus_keV, B_E3_down_Wu):
    """
    Calculates single-particle Weisskopf unit, Isoscalar Octupole EWSR (Bohr-Mottelson Eq. 6-82),
    and percentage exhaustion by the 3_1- state.
    """
    R0 = 1.20 * (A_mass**(1.0 / 3.0))
    B_Wu = (1.0 / (16.0 * math.pi)) * (R0**6)
    B_down = B_E3_down_Wu * B_Wu
    B_up = 7.0 * B_down

    hbar2_2m = 20.7355  # MeV * fm^2
    S_IS = (147.0 / (4.0 * math.pi)) * hbar2_2m * (Z_charge**2 / A_mass) * (R0**4)

    E_MeV = E_3minus_keV / 1000.0
    E_times_B = E_MeV * B_up
    ewsr_depletion_pct = (E_times_B / S_IS) * 100.0

    return {
        "R0_fm": float(R0),
        "B_Wu_e2_fm6": float(B_Wu),
        "B_E3_down_e2_fm6": float(B_down),
        "B_E3_up_e2_fm6": float(B_up),
        "S_IS_EWSR_MeV_e2_fm6": float(S_IS),
        "EWSR_exhaustion_percent": float(ewsr_depletion_pct)
    }


def calculate_parity_splitting_ewsr(pos_spins, pos_energies_keV, neg_spins, neg_energies_keV):
    """
    Calculates parity splitting displacement:
      delta_E(I) = E(I-) - 0.5 * [ E((I+1)+) + E((I-1)+) ]
    """
    p_spins = np.array(pos_spins, dtype=float)
    p_energies = np.array(pos_energies_keV, dtype=float)
    n_spins = np.array(neg_spins, dtype=float)
    n_energies = np.array(neg_energies_keV, dtype=float)

    splittings = []
    for idx, I_neg in enumerate(n_spins):
        E_neg = n_energies[idx]
        idx_low = np.where(np.isclose(p_spins, I_neg - 1.0))[0]
        idx_high = np.where(np.isclose(p_spins, I_neg + 1.0))[0]

        if len(idx_low) > 0 and len(idx_high) > 0:
            E_low = p_energies[idx_low[0]]
            E_high = p_energies[idx_high[0]]
            E_pos_avg = 0.5 * (E_low + E_high)
            delta_E = E_neg - E_pos_avg
            splittings.append({
                "spin_I": float(I_neg),
                "E_neg_keV": float(E_neg),
                "E_pos_avg_keV": float(E_pos_avg),
                "delta_E_keV": float(delta_E)
            })

    if splittings:
        dE_low = splittings[0]["delta_E_keV"]
        dE_high = splittings[-1]["delta_E_keV"]
        if abs(dE_low) <= 60.0:
            mode = "rigid_static_pear_shaped_rotor"
        elif abs(dE_high) < abs(dE_low) * 0.50:
            mode = "centrifugally_stabilized_octupole"
        else:
            mode = "harmonic_octupole_vibration"
    else:
        mode = "undetermined"

    return {
        "octupole_mode": mode,
        "splittings": splittings
    }


def invert_intrinsic_dipole_moment(A_mass, Z_charge, beta2, spin_I, E_E1_keV, E_E2_keV, I_E1, I_E2):
    """
    Inverts intrinsic electric dipole moment |D0| (e*fm) and octupole deformation beta3
    from experimental B(E1)/B(E2) branching ratio.
    """
    R0 = 1.20 * (A_mass**(1.0 / 3.0))
    Q0 = (3.0 / math.sqrt(5.0 * math.pi)) * Z_charge * (R0**2) * beta2

    b_ratio_fm2 = 1.30e-6 * ((E_E2_keV**5) / (E_E1_keV**3)) * (I_E1 / I_E2)
    cg_factor = (16.0 / 15.0) * ((2.0 * spin_I - 1.0) / max(1.0, spin_I - 1.0))

    if b_ratio_fm2 > 0 and cg_factor > 0:
        d0_over_q0 = math.sqrt(b_ratio_fm2 / cg_factor)
        D0_e_fm = d0_over_q0 * Q0
    else:
        d0_over_q0 = 0.0
        D0_e_fm = 0.0

    N_neutrons = A_mass - Z_charge
    diff_NZ = max(1.0, float(N_neutrons - Z_charge))
    C_LD = 0.000687
    beta3 = D0_e_fm / max(1e-6, C_LD * diff_NZ * Z_charge * beta2)

    return {
        "spin_I": float(spin_I),
        "Q0_e_fm2": float(Q0),
        "Q0_e_b": float(Q0 / 100.0),
        "B_E1_over_B_E2_fm2": float(b_ratio_fm2),
        "B_E1_over_B_E2_10minus4_fm2": float(b_ratio_fm2 * 1e4),
        "D0_over_Q0_fm_minus1": float(d0_over_q0),
        "D0_intrinsic_dipole_e_fm": float(D0_e_fm),
        "beta3_octupole_deformation": float(min(0.50, beta3))
    }


def run_octupole_analysis(A_mass, Z_charge, beta2, E_3minus_keV, B_E3_down_Wu,
                          pos_spins=None, pos_energies_keV=None, neg_spins=None, neg_energies_keV=None,
                          branching_test=None):
    """
    Complete octupole analysis suite.
    """
    ewsr_res = calculate_octupole_ewsr(A_mass, Z_charge, E_3minus_keV, B_E3_down_Wu)

    split_res = None
    if pos_spins and pos_energies_keV and neg_spins and neg_energies_keV:
        split_res = calculate_parity_splitting_ewsr(pos_spins, pos_energies_keV, neg_spins, neg_energies_keV)

    branch_res = None
    if branching_test:
        branch_res = invert_intrinsic_dipole_moment(
            A_mass=A_mass,
            Z_charge=Z_charge,
            beta2=beta2,
            spin_I=branching_test["spin_I"],
            E_E1_keV=branching_test["E_E1_keV"],
            E_E2_keV=branching_test["E_E2_keV"],
            I_E1=branching_test["I_E1"],
            I_E2=branching_test["I_E2"]
        )

    return {
        "A_mass": A_mass,
        "Z_charge": Z_charge,
        "beta2": beta2,
        "ewsr_analysis": ewsr_res,
        "parity_splitting_analysis": split_res,
        "dipole_moment_inversion": branch_res
    }


def format_text_report(res, title="Microscopic Octupole Modes & Parity Doublet Engine"):
    ewsr = res["ewsr_analysis"]
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: A = {res['A_mass']}, Z = {res['Z_charge']}, Quadrupole Deformation beta2 = {res['beta2']:.3f}")
    lines.append("=" * 76)
    lines.append(f"  Single-Particle Unit B_Wu(E3)   : {ewsr['B_Wu_e2_fm6']:.1f} e^2*fm^6")
    lines.append(f"  Down-Transition B(E3; 3- -> 0+) : {ewsr['B_E3_down_e2_fm6']:.1f} e^2*fm^6")
    lines.append(f"  Up-Transition B(E3; 0+ -> 3-)   : {ewsr['B_E3_up_e2_fm6']:.1f} e^2*fm^6")
    lines.append(f"  Isoscalar Octupole EWSR Limit   : {ewsr['S_IS_EWSR_MeV_e2_fm6']:.2e} MeV*e^2*fm^6")
    lines.append(f"  EWSR Exhaustion Percentage      : {ewsr['EWSR_exhaustion_percent']:.2f}%")
    lines.append("-" * 76)

    if res["parity_splitting_analysis"]:
        ps = res["parity_splitting_analysis"]
        lines.append(f"Parity Splitting Mode: {ps['octupole_mode']}")
        lines.append("   Spin I-   E(I-) [keV]   <E((I+-1)+)> [keV]   delta_E [keV]")
        for sp in ps["splittings"]:
            lines.append(f"     {sp['spin_I']:4.1f}      {sp['E_neg_keV']:8.1f}         {sp['E_pos_avg_keV']:8.1f}       {sp['delta_E_keV']:8.1f}")
        lines.append("-" * 76)

    if res["dipole_moment_inversion"]:
        dp = res["dipole_moment_inversion"]
        lines.append(f"Intrinsic Dipole Moment Inversion at Spin I = {dp['spin_I']:.1f}:")
        lines.append(f"  Transition Ratio B(E1)/B(E2)    : {dp['B_E1_over_B_E2_10minus4_fm2']:.3f} x 10^-4 fm^-2")
        lines.append(f"  Intrinsic Quadrupole Moment Q0  : {dp['Q0_e_b']:.2f} e*b ({dp['Q0_e_fm2']:.1f} e*fm^2)")
        lines.append(f"  Extracted Intrinsic Dipole |D0| : {dp['D0_intrinsic_dipole_e_fm']:.4f} e*fm")
        lines.append(f"  Extracted Octupole Def. beta3   : {dp['beta3_octupole_deformation']:.3f}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Microscopic Octupole Modes, IS-EWSR & Alternating-Parity Pear-Shaped Dynamics Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--charge-z", type=int, help="Atomic number Z")
    parser.add_argument("--beta2", type=float, default=0.20, help="Quadrupole deformation beta2")
    parser.add_argument("--e3-kev", type=float, help="Energy of 3_1- state in keV")
    parser.add_argument("--b-e3-wu", type=float, help="B(E3; 3- -> 0+) in Weisskopf units")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        A_mass = p["A_mass"]
        Z_charge = p["Z_charge"]
        beta2 = p.get("beta2", 0.20)
        E_3minus_keV = p["E_3minus_keV"]
        B_E3_down_Wu = p["B_E3_down_Wu"]
        pos_spins = p.get("pos_spins")
        pos_energies = p.get("pos_energies_keV")
        neg_spins = p.get("neg_spins")
        neg_energies = p.get("neg_energies_keV")
        branching_test = p.get("branching_test")
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.mass_a and args.charge_z and args.e3_kev and args.b_e3_wu:
        A_mass = args.mass_a
        Z_charge = args.charge_z
        beta2 = args.beta2
        E_3minus_keV = args.e3_kev
        B_E3_down_Wu = args.b_e3_wu
        pos_spins = None
        pos_energies = None
        neg_spins = None
        neg_energies = None
        branching_test = None
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_octupole_analysis(
        A_mass=A_mass,
        Z_charge=Z_charge,
        beta2=beta2,
        E_3minus_keV=E_3minus_keV,
        B_E3_down_Wu=B_E3_down_Wu,
        pos_spins=pos_spins,
        pos_energies_keV=pos_energies,
        neg_spins=neg_spins,
        neg_energies_keV=neg_energies,
        branching_test=branching_test
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
