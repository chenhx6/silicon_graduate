#!/usr/bin/env python3
"""
Illustrative parameterized deformation surface with two Gaussian valleys.

The legacy filename includes Strutinsky, but the implementation does not
compute shell corrections from single-particle spectra or perform Strutinsky
smoothing. Its polynomial macroscopic terms, inertia formula and Gaussian
well parameters are declared numerical choices, not a verified microscopic
PES for any named isotope. The beta4 input is fixed during the beta2/gamma
slice; a three-dimensional self-consistent minimization is not performed.

A secondary sampled minimum and a path-barrier estimate do not establish
an observed TSD state, quantum metastability, a minimum-action saddle or a
nuclear decay lifetime. Isotope-named presets are synthetic demonstrations.
Legacy result keys remain for compatibility and carry explicit provenance.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "163Lu_TSD_potential_energy_surface": {
        "description": "163Lu triaxial superdeformed minimum at high spin (I=35.5 hbar, beta2 ~ 0.39, gamma ~ 20 deg, barrier ~ 1.85 MeV)",
        "nucleus": "163Lu",
        "Z": 71,
        "A": 163,
        "spin_I": 35.5,
        "beta4": 0.025,
        "shell_amp_MeV": -4.20,
        "tsd_shell_amp_MeV": -6.60,
        "beta2_grid": [0.05, 0.60, 45],
        "gamma_grid": [0.0, 60.0, 31]
    },
    "130Ba_triaxial_quasiparticle_PES": {
        "description": "130Ba triaxial potential energy surface at spin I=14 hbar (beta2 ~ 0.23, gamma ~ 25 deg)",
        "nucleus": "130Ba",
        "Z": 56,
        "A": 130,
        "spin_I": 14.0,
        "beta4": -0.010,
        "shell_amp_MeV": -3.80,
        "tsd_shell_amp_MeV": -2.20,
        "beta2_grid": [0.05, 0.50, 40],
        "gamma_grid": [0.0, 60.0, 31]
    },
    "208Pb_spherical_doubly_magic": {
        "description": "208Pb doubly magic nucleus with steep spherical minimum at beta2 = 0",
        "nucleus": "208Pb",
        "Z": 82,
        "A": 208,
        "spin_I": 0.0,
        "beta4": 0.0,
        "shell_amp_MeV": 2.50,
        "tsd_shell_amp_MeV": 1.00,
        "beta2_grid": [0.00, 0.40, 30],
        "gamma_grid": [0.0, 60.0, 25]
    }
}

# Legacy isotope labels are retained as command identifiers only.
for _preset_name, _preset in PRESETS.items():
    _preset["data_kind"] = "synthetic_model_benchmark"
    _preset["description"] = f"Synthetic illustrative parameter set (legacy label: {_preset_name})"



def calculate_ldm_energy_surface(Z, A, beta2_arr, gamma_arr, beta4=0.0):
    """
    Calculates macroscopic Liquid Drop Model deformation energy in MeV.
    """
    E_surf0 = 17.94 * (A**(2.0 / 3.0))
    E_coul0 = 0.705 * (Z**2) / (A**(1.0 / 3.0))

    c_3 = (4.0 / 105.0) * math.sqrt(5.0 / math.pi)

    n_b = len(beta2_arr)
    n_g = len(gamma_arr)
    E_ldm = np.zeros((n_b, n_g))

    for i, b in enumerate(beta2_arr):
        for j, g_deg in enumerate(gamma_arr):
            g_rad = math.radians(g_deg)
            cos3g = math.cos(3.0 * g_rad)

            delta_B_surf = (2.0 / 5.0) * (b**2) - c_3 * (b**3) * cos3g + (9.0 / 35.0) * (beta4**2)
            delta_B_coul = -(1.0 / 5.0) * (b**2) - c_3 * (b**3) * cos3g - (10.0 / 35.0) * (beta4**2)

            E_ldm[i, j] = E_surf0 * delta_B_surf + E_coul0 * delta_B_coul

    return E_ldm


def calculate_rotational_energy_surface(A, spin_I, beta2_arr, gamma_arr):
    """
    Calculates collective cranking rotational energy E_rot(I, beta2, gamma) in MeV.
    Moment of inertia J_eff scales with A^(5/3) * (1 + 0.6*beta2) and hydrodynamic triaxiality.
    """
    if spin_I <= 0.0:
        return np.zeros((len(beta2_arr), len(gamma_arr)))

    E_rot = np.zeros((len(beta2_arr), len(gamma_arr)))
    I_factor = spin_I * (spin_I + 1.0)

    for i, b in enumerate(beta2_arr):
        for j, g_deg in enumerate(gamma_arr):
            g_rad = math.radians(g_deg)
            # Hydrodynamic-like moment of inertia enhancement with beta2
            # Rigid body base: J_rig ~ 0.014 * A^(5/3) * (1 + 0.6*beta2 + 0.5*beta2^2)
            j_moi = 0.014 * (A**(5.0 / 3.0)) * (0.35 + 2.20 * b**2) * (1.0 + 0.3 * math.sin(g_rad))
            j_moi = max(5.0, j_moi)
            # E_rot = hbar^2 * I*(I+1) / (2 * J_eff) in MeV (with hbar^2 ~ 1.0 in standard units)
            E_rot[i, j] = I_factor / (2.0 * j_moi)
    return E_rot


def calculate_shell_correction_surface(beta2_arr, gamma_arr, shell_amp, tsd_shell_amp, beta4=0.0):
    """
    Calculates microscopic Strutinsky shell correction energy surface in MeV.
    """
    n_b = len(beta2_arr)
    n_g = len(gamma_arr)
    E_shell = np.zeros((n_b, n_g))

    for i, b in enumerate(beta2_arr):
        for j, g_deg in enumerate(gamma_arr):
            g_rad = math.radians(g_deg)
            # ND pocket centered near beta2 ~ 0.20, gamma ~ 10 deg
            d_nd_sq = ((b - 0.18) / 0.05)**2 + ((g_deg - 15.0) / 20.0)**2
            nd_term = shell_amp * math.exp(-0.5 * d_nd_sq)

            # TSD pocket centered near beta2 ~ 0.40, gamma ~ 20 deg
            d_tsd_sq = ((b - 0.39) / 0.06)**2 + ((g_deg - 20.0) / 15.0)**2
            tsd_term = tsd_shell_amp * math.exp(-0.5 * d_tsd_sq)

            # Hexadecapole stabilization
            hex_term = -18.0 * beta4 * (b**2)

            E_shell[i, j] = nd_term + tsd_term + hex_term

    return E_shell


def find_pes_minima_and_saddle(beta2_arr, gamma_arr, E_tot):
    """
    Scans potential energy surface to locate ND minimum, TSD minimum, and barrier.
    """
    # Find ND minimum in beta2 in [0.05, 0.30]
    nd_mask = (beta2_arr >= 0.05) & (beta2_arr <= 0.30)
    if not np.any(nd_mask):
        nd_mask = beta2_arr <= 0.30

    nd_sub = E_tot[nd_mask, :]
    min_nd_idx = np.unravel_index(np.argmin(nd_sub), nd_sub.shape)
    b_nd = beta2_arr[nd_mask][min_nd_idx[0]]
    g_nd = gamma_arr[min_nd_idx[1]]
    E_nd = float(nd_sub[min_nd_idx])

    # Find TSD minimum in beta2 in [0.32, 0.55]
    tsd_mask = (beta2_arr >= 0.32) & (beta2_arr <= 0.55)
    if np.any(tsd_mask):
        tsd_sub = E_tot[tsd_mask, :]
        min_tsd_idx = np.unravel_index(np.argmin(tsd_sub), tsd_sub.shape)
        b_tsd = beta2_arr[tsd_mask][min_tsd_idx[0]]
        g_tsd = gamma_arr[min_tsd_idx[1]]
        E_tsd = float(tsd_sub[min_tsd_idx])

        # Search for saddle point barrier along intervening beta2 range
        barrier_mask = (beta2_arr >= b_nd) & (beta2_arr <= b_tsd)
        barrier_sub = E_tot[barrier_mask, :]
        # Ridge minimum
        max_along_path = np.max(barrier_sub, axis=0)
        saddle_val = float(np.min(max_along_path))
        V_barrier_MeV = max(0.0, saddle_val - E_tsd)
        has_tsd = bool(V_barrier_MeV > 0.15)
    else:
        b_tsd = b_nd
        g_tsd = g_nd
        E_tsd = E_nd
        V_barrier_MeV = 0.0
        has_tsd = False

    return {
        "normal_deformed_min": {
            "beta2": float(b_nd),
            "gamma_deg": float(g_nd),
            "energy_MeV": float(E_nd)
        },
        "superdeformed_min": {
            "beta2": float(b_tsd),
            "gamma_deg": float(g_tsd),
            "energy_MeV": float(E_tsd)
        },
        "has_secondary_tsd_well": has_tsd,
        "tsd_barrier_height_MeV": float(V_barrier_MeV),
        "tsd_excitation_energy_MeV": float(max(0.0, E_tsd - E_nd))
    }


def run_pes_strutinsky_analysis(Z, A, spin_I, beta4, shell_amp, tsd_shell_amp,
                                beta2_grid_params, gamma_grid_params, nucleus="Nucleus"):
    """
    Complete execution pipeline for triaxial superdeformed PES Strutinsky analysis.
    """
    b2_min, b2_max, n_b = beta2_grid_params
    g_min, g_max, n_g = gamma_grid_params

    beta2_arr = np.linspace(b2_min, b2_max, n_b)
    gamma_arr = np.linspace(g_min, g_max, n_g)

    E_ldm = calculate_ldm_energy_surface(Z, A, beta2_arr, gamma_arr, beta4)
    E_shell = calculate_shell_correction_surface(beta2_arr, gamma_arr, shell_amp, tsd_shell_amp, beta4)
    E_rot = calculate_rotational_energy_surface(A, spin_I, beta2_arr, gamma_arr)
    E_tot = E_ldm + E_shell + E_rot

    topo = find_pes_minima_and_saddle(beta2_arr, gamma_arr, E_tot)
    topo["data_kind"] = "model_derived_illustration"
    topo["evidence_boundary"] = "Parameterized fixed-beta4 surface; candidate minima and path barriers are not experimental states or lifetime predictions."
    topo["nucleus"] = nucleus
    topo["parameters"] = {
        "Z": int(Z), "A": int(A), "spin_I": float(spin_I), "beta4": float(beta4),
        "shell_amp_MeV": float(shell_amp),
        "tsd_shell_amp_MeV": float(tsd_shell_amp)
    }
    return topo


def format_text_report(res, title="TSD 3D Potential Energy Surface Strutinsky Engine"):
    nuc = res["nucleus"]
    p = res["parameters"]
    nd = res["normal_deformed_min"]
    tsd = res["superdeformed_min"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} (Z={p['Z']}, A={p['A']}) at Spin I = {p['spin_I']:.1f} hbar | Hexadecapole beta4 = {p['beta4']:+.3f}")
    lines.append("=" * 76)
    lines.append("Evidence: parameterized surface; no experimental topology verdict")
    lines.append("Candidate minima in the evaluated model surface:")
    lines.append(f"  Low-deformation candidate well : beta2 = {nd['beta2']:.3f}, gamma = {nd['gamma_deg']:4.1f} deg  (E = {nd['energy_MeV']:6.2f} MeV)")
    if res["has_secondary_tsd_well"]:
        lines.append(f"  Large-deformation candidate well: beta2 = {tsd['beta2']:.3f}, gamma = {tsd['gamma_deg']:4.1f} deg  (E = {tsd['energy_MeV']:6.2f} MeV)")
        lines.append("-" * 76)
        lines.append("Superdeformed Barrier and Stability Metrics:")
        lines.append(f"  TSD Deformation Barrier Height V_B : {res['tsd_barrier_height_MeV']:.2f} MeV (model path estimate; no decay calculation)")
        lines.append(f"  TSD Excitation Above ND State   : Delta E = {res['tsd_excitation_energy_MeV']:.2f} MeV")
        lines.append("  Model topology                     : SECONDARY_MINIMUM_IN_PARAMETERIZED_SURFACE")
    else:
        lines.append("  Large-deformation candidate well: NONE found in evaluated grid")
        lines.append("-" * 76)
        lines.append("  Model topology                     : NO_SECONDARY_MINIMUM_FOUND_IN_EVALUATED_GRID")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Triaxial Superdeformed PES Strutinsky Inversion Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load synthetic illustrative preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nuc = p["nucleus"]
        Z = p["Z"]
        A = p["A"]
        spin_I = p.get("spin_I", 0.0)
        b4 = p["beta4"]
        samp = p["shell_amp_MeV"]
        tsamp = p["tsd_shell_amp_MeV"]
        bgrid = p["beta2_grid"]
        ggrid = p["gamma_grid"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_pes_strutinsky_analysis(
        Z=Z, A=A, spin_I=spin_I, beta4=b4,
        shell_amp=samp,
        tsd_shell_amp=tsamp,
        beta2_grid_params=bgrid,
        gamma_grid_params=ggrid,
        nucleus=nuc
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
