#!/usr/bin/env python3
"""
day27_two_phonon_octupole_anharmonicity_study.py
Two-Phonon Octupole Multiplets and Anharmonic Damping across Mass Regions:
The 0+, 2+, 4+, 6+ Quadruplet in 208Pb vs Anharmonic Fragmentation in 146Gd and Octupole Condensation in 224Ra.
"""

import os
import json
import numpy as np

# Physical constants
HBAR_C = 197.3269804      # MeV fm

# Benchmark octupole datasets across mass regions:
# Nucleus, Z, A, structure_regime, E_3minus_keV, B_E3_Wu, two_phonon_candidates_keV, background_density_per_MeV
# Sources:
# 208Pb: Yeh et al. PRL 76, 1208 (1996); Vetter et al. PRC 58, R2631 (1998); NNDC ENSDF
# 146Gd: Yates et al. PRC 52, 2448 (1995); Kleinheinz et al. Z. Phys. A 290, 279 (1979)
# 224Ra: Butler et al. PRL 124, 042503 (2020); Gaffney et al. Nature 497, 199 (2013)
OCTUPOLE_DATA = {
    "208Pb": {
        "A": 208, "Z": 82, "N": 126, "regime": "Doubly Magic Harmonic Vibrator",
        "E_3minus_keV": 2614.5, "B_E3_Wu": 34.0,
        "harmonic_2phonon_keV": 5229.0,
        "multiplet_members": {
            "0+": {"E_exp_keV": 5241.0, "Delta_E_keV": +12.0, "B_E3_ratio": 1.85},
            "2+": {"E_exp_keV": 5247.0, "Delta_E_keV": +18.0, "B_E3_ratio": 1.70},
            "4+": {"E_exp_keV": 5214.0, "Delta_E_keV": -15.0, "B_E3_ratio": 1.90},
            "6+": {"E_exp_keV": 5211.0, "Delta_E_keV": -18.0, "B_E3_ratio": 1.95}
        },
        "mean_2phonon_E_keV": 5228.3,
        "net_anharmonic_shift_keV": -0.7,
        "background_level_density_per_MeV": 6.5,
        "spreading_width_Gamma_keV": 8.5,
        "is_phonon_coherent": True,
        "is_static_octupole": False
    },
    "146Gd": {
        "A": 146, "Z": 64, "N": 82, "regime": "Semi-Magic Fragmented Vibrator",
        "E_3minus_keV": 1579.3, "B_E3_Wu": 37.0,
        "harmonic_2phonon_keV": 3158.6,
        "multiplet_members": {
            "0+": {"E_exp_keV": 3484.0, "Delta_E_keV": +325.4, "B_E3_ratio": 0.45},
            "2+": {"E_exp_keV": 3280.0, "Delta_E_keV": +121.4, "B_E3_ratio": 0.55},
            "4+": {"E_exp_keV": 3320.0, "Delta_E_keV": +161.4, "B_E3_ratio": 0.60},
            "6+": {"E_exp_keV": 3457.0, "Delta_E_keV": +298.4, "B_E3_ratio": 0.50}
        },
        "mean_2phonon_E_keV": 3385.3,
        "net_anharmonic_shift_keV": +226.7,
        "background_level_density_per_MeV": 82.0,
        "spreading_width_Gamma_keV": 295.0,
        "is_phonon_coherent": False, # Dissolved by spreading width
        "is_static_octupole": False
    },
    "224Ra": {
        "A": 224, "Z": 88, "N": 136, "regime": "Static Pear-Shaped Rotor",
        "E_3minus_keV": 290.0, # Rotational 3- state in alternating parity band
        "B_E3_Wu": 42.0,
        "harmonic_2phonon_keV": 580.0,
        "multiplet_members": {
            "0+": {"E_exp_keV": 0.0, "Delta_E_keV": -580.0, "B_E3_ratio": 0.0},
            "2+": {"E_exp_keV": 84.4, "Delta_E_keV": -495.6, "B_E3_ratio": 0.0},
            "4+": {"E_exp_keV": 250.8, "Delta_E_keV": -329.2, "B_E3_ratio": 0.0},
            "6+": {"E_exp_keV": 479.2, "Delta_E_keV": -100.8, "B_E3_ratio": 0.0}
        },
        "mean_2phonon_E_keV": None, # Non-existent concept
        "net_anharmonic_shift_keV": None,
        "background_level_density_per_MeV": 350.0,
        "spreading_width_Gamma_keV": None,
        "is_phonon_coherent": False,
        "is_static_octupole": True,
        "beta3_deformation": 0.14
    }
}

def spreading_width_model(density_per_MeV, coupling_matrix_element_keV):
    """
    Fermi Golden Rule spreading width: Gamma^down = 2 * pi * <v^2> * rho
    """
    v_MeV = coupling_matrix_element_keV / 1000.0
    return 2.0 * np.pi * (v_MeV ** 2) * density_per_MeV * 1000.0 # in keV

def run_study():
    results = {
        "schema_version": 1,
        "investigation": "Two-Phonon Octupole Multiplets and Anharmonic Damping across Mass Regions",
        "description": "Systematic evaluation of two-phonon octupole states across doubly magic 208Pb (harmonic quadruplet 0+, 2+, 4+, 6+), semi-magic 146Gd (anharmonic fragmentation), and light actinide 224Ra (octupole condensation into static pear-shaped rotor).",
        "systems": []
    }

    print(f"{'Nucleus':<8} {'Regime':<30} {'E(3-)keV':<10} {'Harmonic':<10} {'MeanExp':<10} {'Shift(keV)':<12} {'Gamma_down':<12} {'Phonon Coherent':<16}")
    print("=" * 115)

    for name, d in OCTUPOLE_DATA.items():
        regime = d["regime"]
        e3 = d["E_3minus_keV"]
        harm = d["harmonic_2phonon_keV"]
        mean_exp = d["mean_2phonon_E_keV"]
        shift = d["net_anharmonic_shift_keV"]
        gamma_down = d["spreading_width_Gamma_keV"]
        is_coh = d["is_phonon_coherent"]

        mean_str = f"{mean_exp:.1f}" if mean_exp is not None else "N/A (Rotor)"
        shift_str = f"{shift:+.1f}" if shift is not None else "N/A"
        gamma_str = f"{gamma_down:.1f} keV" if gamma_down is not None else "N/A"
        coh_str = "Harmonic/Coherent" if is_coh else ("Fragmented" if not d["is_static_octupole"] else "Static Pear Rotor")

        print(f"{name:<8} {regime:<30} {e3:<10.1f} {harm:<10.1f} {mean_str:<10} {shift_str:<12} {gamma_str:<12} {coh_str:<16}")

        results["systems"].append({
            "nucleus": name,
            "A": d["A"],
            "Z": d["Z"],
            "N": d["N"],
            "structure_regime": regime,
            "E_3minus_keV": e3,
            "B_E3_single_phonon_Wu": d["B_E3_Wu"],
            "harmonic_2phonon_expectation_keV": harm,
            "mean_experimental_2phonon_E_keV": mean_exp,
            "net_anharmonic_shift_keV": shift,
            "background_level_density_per_MeV": d["background_level_density_per_MeV"],
            "spreading_width_Gamma_down_keV": gamma_down,
            "is_phonon_coherent": is_coh,
            "is_static_octupole": d["is_static_octupole"],
            "multiplet_details": d["multiplet_members"]
        })

    print("=" * 115)
    print("Finding 1 (208Pb Ideal Harmonicity): In 208Pb, the 0+, 2+, 4+, 6+ quadruplet is centered at 5228.3 keV (within -0.7 keV of 2*E(3-)), with small splitting (+/- 18 keV) and B(E3) ~ 1.85x single phonon.")
    print("Finding 2 (146Gd Anharmonic Dissolution): In 146Gd, small subshell gap increases background level density 13x (82 / MeV), generating a 295 keV spreading width that dissolves the two-phonon state into compound states.")
    print("Finding 3 (224Ra Octupole Condensation): In 224Ra, Delta-l = Delta-j = 3 orbitals near the Fermi level drive spontaneous parity breaking, condensing the octupole degree of freedom into a static pear shape, invalidating the phonon concept completely.")

    results["cross_mass_inapplicability_boundaries"] = {
        "boundary_1_harmonic_phonon_to_fragmented_damping": {
            "contrast": "208Pb (ideal 2-phonon) vs 146Gd (fragmented damping)",
            "mechanism": "In doubly magic 208Pb, the 3.5-4.0 MeV shell gap suppresses background 2p-2h level density to rho ~ 6.5 / MeV, keeping spreading width Gamma^down < 9 keV and protecting the multiplet. In 146Gd, the Z=64 subshell gap is only ~1.5 MeV, boosting level density to rho ~ 82 / MeV. Strong mixing (v_mix ~ 24 keV) produces a massive spreading width Gamma^down = 295 keV that fragments the two-phonon octupole strength across >10 states, shifting the 0+ centroid upwards by +325 keV.",
            "failure_signature": "Severe overestimation of two-phonon transition strength and state coherence when transferring the 208Pb harmonic model to semi-magic nuclei."
        },
        "boundary_2_phonon_vibration_to_static_pear_rotor": {
            "contrast": "208Pb (vibrator) vs 224Ra (condensed rotor)",
            "mechanism": "In 208Pb, octupole phonons are dynamic harmonic vibrations around a spherical minimum. In 224Ra, the simultaneous presence of pi(i13/2 - f7/2) and nu(j15/2 - g9/2) intruder pairs near the Fermi surface makes d^2 V / d beta_3^2 < 0, condensing the system into a permanent pear shape (beta_3 = 0.14). The 3- state is not a phonon, but the I=3 member of an alternating-parity rotational band (0+, 1-, 2+, 3-, 4+, 5-). The two-phonon quadruplet does not exist.",
            "failure_signature": "Attempting to assign multiphonon states to alternating-parity rotational bands."
        }
    }

    out_dir = "outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/two-phonon-octupole"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "two_phonon_octupole_results.json")
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results successfully written to {out_file}")

if __name__ == "__main__":
    run_study()
