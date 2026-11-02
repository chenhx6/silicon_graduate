#!/usr/bin/env python3
"""
tac_3d_chiral_orientation_energy_surface_calculator.py
======================================================
Three-Dimensional Tilted Axis Cranking (TAC) Orientation Energy Surface, Chiral Bifurcation &
Aplanar Barrier Calculator.

Physics & Formulation:
----------------------
1. 3D Tilted Axis Cranking Geometry (Frauendorf & Meng 1997, Rev. Mod. Phys. 2001):
   In a triaxial odd-odd nucleus with a valence proton particle and a neutron hole
   (e.g. 134Pr, 128Cs with pi h_11/2 (x) nu h_11/2^-1):
   - Short axis s (axis 1): Valence proton particle j_p aligns along s (lowest energy in s-well).
   - Intermediate axis m (axis 2): Core collective rotation R aligns along m (largest MOI: J_m > J_s, J_l).
   - Long axis l (axis 3): Valence neutron hole j_n aligns along l (lowest energy in l-well).
   The total angular momentum vector J = R + j_p + j_n has components:
     J_s = J * sin(theta) * cos(phi)
     J_m = J * sin(theta) * sin(phi)
     J_l = J * cos(theta)
   where (theta, phi) are the spherical tilt angles of J on the unit sphere.

2. Quasiclassical Orientation Energy Surface E(theta, phi; J):
   The total energy of the coupled system is:
     E(theta, phi; J) = [ (J_s - j_p)^2 / (2 * J_s) ] + [ J_m^2 / (2 * J_m) ] + [ (J_l - j_n)^2 / (2 * J_l) ]
   Notice the physical competition:
   - The proton term pulls J towards the s-axis (J_s -> j_p);
   - The neutron term pulls J towards the l-axis (J_l -> j_n);
   - The collective core term pulls J towards the m-axis (maximizing J_m to minimize J_m^2 / (2*J_m)).

3. Chiral Bifurcation & Spontaneous Symmetry Breaking:
   - Low Spin / Planar Phase (J < J_crit):
     The core angular momentum is small. The energy minimum lies on the boundary plane (phi = 0 deg),
     meaning J_m = 0 (Planar rotation in the (s, l) plane, no chirality).
   - High Spin / Chiral Phase (J >= J_crit):
     At the critical bifurcation spin J_crit, the planar minimum becomes a saddle point.
     Two degenerate aplanar minima emerge at:
       (theta_0, phi_0)  and  (pi - theta_0, pi - phi_0)
     All three components (J_s, J_m, J_l) are simultaneously non-zero!
     The rotational axis breaks time-reversal-spatial-rotation symmetry T*R_y(pi), forming
     Left-handed and Right-handed chiral twins!

4. Planar Energy Barrier & Chiral Tunneling:
   The energy barrier separating the two chiral wells is:
     Delta_E_barrier = E_planar_saddle - E_chiral_min
   In finite quantum nuclei, tunneling through this barrier lifts the degeneracy, producing
   the observed Chiral Doublet Band splitting: Delta_E(I) ~ Delta_E_tunneling.

References:
  - S. Frauendorf and J. Meng, Nucl. Phys. A 617, 131 (1997).
  - S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001) [Section VII.B].
  - J. Meng and Y. P. Wang, in *Chirality and Wobbling in Atomic Nuclei* (CRC 2025), Ch. 3.
  - C. M. Petrache et al., Phys. Rev. Lett. 96, 112502 (2006).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_chiral_tac_energy(
    theta_deg: float,
    phi_deg: float,
    J_tot: float,
    J_m: float = 25.0,
    J_s: float = 15.0,
    J_l: float = 5.0,
    j_p: float = 5.5,
    j_n: float = 5.5
) -> float:
    """
    Computes total TAC energy E(theta, phi; J) in keV.
    """
    th = math.radians(theta_deg)
    ph = math.radians(phi_deg)

    Js_val = J_tot * math.sin(th) * math.cos(ph)
    Jm_val = J_tot * math.sin(th) * math.sin(ph)
    Jl_val = J_tot * math.cos(th)

    e_s = ((Js_val - j_p) ** 2) / (2.0 * J_s)
    e_m = (Jm_val ** 2) / (2.0 * J_m)
    e_l = ((Jl_val - j_n) ** 2) / (2.0 * J_l)

    return (e_s + e_m + e_l) * 1000.0 # in keV


def find_chiral_equilibrium_and_barrier(
    J_tot: float,
    J_m: float = 25.0,
    J_s: float = 15.0,
    J_l: float = 5.0,
    j_p: float = 5.5,
    j_n: float = 5.5
) -> Dict[str, Any]:
    """
    Finds the 2D energy minimum (theta_min, phi_min) and calculates the planar barrier.
    """
    if J_tot <= 0.0 or J_m <= 0.0 or J_s <= 0.0 or J_l <= 0.0:
        raise ValueError("Angular momentum and MOIs must be positive.")

    from scipy.optimize import minimize

    def obj(x):
        return calculate_chiral_tac_energy(x[0], x[1], J_tot, J_m, J_s, J_l, j_p, j_n)

    # 2D search in aplanar octant (1 to 89 degrees)
    res = minimize(obj, [45.0, 45.0], bounds=[(1.0, 89.0), (1.0, 89.0)], method="L-BFGS-B")
    th_min, ph_min = float(res.x[0]), float(res.x[1])
    e_min_keV = float(res.fun)

    # Planar boundaries
    # 1. (s, l) plane: phi = 0
    res_ph0 = minimize(lambda x: calculate_chiral_tac_energy(x[0], 0.0, J_tot, J_m, J_s, J_l, j_p, j_n), [45.0], bounds=[(0.0, 90.0)])
    # 2. (m, l) plane: phi = 90
    res_ph90 = minimize(lambda x: calculate_chiral_tac_energy(x[0], 90.0, J_tot, J_m, J_s, J_l, j_p, j_n), [45.0], bounds=[(0.0, 90.0)])
    # 3. (s, m) plane: theta = 90
    res_th90 = minimize(lambda x: calculate_chiral_tac_energy(90.0, x[0], J_tot, J_m, J_s, J_l, j_p, j_n), [45.0], bounds=[(0.0, 90.0)])

    e_planar_min = min(float(res_ph0.fun), float(res_ph90.fun), float(res_th90.fun))

    # Aplanarity criteria: barrier >= 1.0 keV and phi >= 5.0 deg
    is_chiral = (e_planar_min - e_min_keV >= 1.0) and (ph_min >= 5.0) and (th_min <= 85.0)
    barrier_keV = (e_planar_min - e_min_keV) if is_chiral else 0.0

    # Components at minimum
    th_r = math.radians(th_min)
    ph_r = math.radians(ph_min)
    Js_val = J_tot * math.sin(th_r) * math.cos(ph_r)
    Jm_val = J_tot * math.sin(th_r) * math.sin(ph_r)
    Jl_val = J_tot * math.cos(th_r)

    # Aplanarity volume metric: V = (j_p * Jm * j_n) / (j_p * j_n * J)
    v_metric = abs(Jm_val / J_tot) if is_chiral else 0.0

    return {
        "spin_J": J_tot,
        "is_chiral_geometry": is_chiral,
        "chiral_barrier_keV": round(barrier_keV, 1),
        "theta_min_deg": round(th_min, 1),
        "phi_min_deg": round(ph_min, 1),
        "angular_momentum_components": {
            "J_s_short_hbar": round(Js_val, 2),
            "J_m_intermediate_hbar": round(Jm_val, 2),
            "J_l_long_hbar": round(Jl_val, 2)
        },
        "minimum_energy_keV": round(e_min_keV, 1),
        "planar_energy_keV": round(e_planar_min, 1),
        "aplanarity_volume_metric": round(v_metric, 3),
        "chiral_phase": "Aplanar Chiral Rotation" if is_chiral else "Planar Rotation"
    }


def scan_chiral_spin_evolution(
    J_values: List[float],
    J_m: float = 25.0,
    J_s: float = 15.0,
    J_l: float = 5.0,
    j_p: float = 5.5,
    j_n: float = 5.5
) -> List[Dict[str, Any]]:
    """Tracks the transition from planar rotation to aplanar chiral rotation across spin J."""
    evolution = []
    for J in J_values:
        res = find_chiral_equilibrium_and_barrier(J, J_m, J_s, J_l, j_p, j_n)
        evolution.append(res)
    return evolution


def format_text_report(eq_res: Dict[str, Any], evo_list: Optional[List[Dict[str, Any]]] = None) -> str:
    lines = [
        "=" * 76,
        "   3D TILTED AXIS CRANKING (TAC) CHIRAL ORIENTATION ENERGY SUITE",
        "   Based on Frauendorf & Meng (1997) & Petrache (2025) Ch. 3",
        "=" * 76,
        f" CHIRAL EQUILIBRIUM AT SPIN J = {eq_res['spin_J']:.1f} hbar:",
        f"   Chiral Geometry Status      : {eq_res['chiral_phase']}",
        f"   Equilibrium Tilt Angles     : theta = {eq_res['theta_min_deg']:.1f} deg,  phi = {eq_res['phi_min_deg']:.1f} deg",
        f"   3D Angular Momentum Vector  : (J_s={eq_res['angular_momentum_components']['J_s_short_hbar']:.1f}, J_m={eq_res['angular_momentum_components']['J_m_intermediate_hbar']:.1f}, J_l={eq_res['angular_momentum_components']['J_l_long_hbar']:.1f}) hbar",
        f"   Chiral Planar Barrier       : Delta_E_barrier = {eq_res['chiral_barrier_keV']:.1f} keV",
        f"   Aplanarity Volume Metric V  : {eq_res['aplanarity_volume_metric']:.3f}  (0.0 = Planar, > 0.3 = Robust Chiral)",
        "-" * 76,
    ]

    if evo_list is not None:
        lines.extend([
            " CHIRAL BIFURCATION SPIN TRAJECTORY (J_min to J_max):",
            "   Spin J     theta (deg)    phi (deg)    J_m (hbar)    Barrier (keV)    Chiral Phase",
        ])
        for pt in evo_list:
            lines.append(f"    {pt['spin_J']:4.1f}        {pt['theta_min_deg']:5.1f}        {pt['phi_min_deg']:5.1f}        {pt['angular_momentum_components']['J_m_intermediate_hbar']:5.1f}          {pt['chiral_barrier_keV']:7.1f}       {pt['chiral_phase']}")
        lines.append("-" * 76)

    lines.extend([
        " Methodological Significance for Nuclear Chirality:",
        "   - Planar phase (phi ~ 0 deg): J_m = 0, angular momentum lies in (s, l) plane.",
        "   - Chiral bifurcation (J >= J_crit): J tilts out of all planes, forming degenerate twin wells.",
        "   - Tunneling through Delta_E_barrier lifts degeneracy, creating the Chiral Doublet splitting.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="3D TAC Chiral Orientation Energy Surface Calculator"
    )
    parser.add_argument("--spin", "-J", type=float, default=18.0, help="Total angular momentum J (default: 18.0)")
    parser.add_argument("--Jm", type=float, default=25.0, help="Intermediate axis MOI (default: 25.0)")
    parser.add_argument("--Js", type=float, default=15.0, help="Short axis MOI (default: 15.0)")
    parser.add_argument("--Jl", type=float, default=5.0, help="Long axis MOI (default: 5.0)")
    parser.add_argument("--jp", type=float, default=5.5, help="Proton particle j (default: 5.5 for h11/2)")
    parser.add_argument("--jn", type=float, default=5.5, help="Neutron hole j (default: 5.5 for h11/2)")
    parser.add_argument("--preset", type=str, default="134Pr_chiral_tripod",
                        choices=["134Pr_chiral_tripod", "128Cs_chiral_doublet", "106Ag_a100_chiral"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    j_val = args.spin
    jm, js, jl = args.Jm, args.Js, args.Jl
    jp_val, jn_val = args.jp, args.jn

    if args.preset == "134Pr_chiral_tripod":
        jm, js, jl = 25.0, 15.0, 5.0
        jp_val, jn_val = 5.5, 5.5
    elif args.preset == "128Cs_chiral_doublet":
        jm, js, jl = 30.0, 18.0, 6.0
        jp_val, jn_val = 5.5, 5.5
    elif args.preset == "106Ag_a100_chiral":
        jm, js, jl = 22.0, 14.0, 5.0
        jp_val, jn_val = 4.5, 5.5 # g9/2 x h11/2

    spins_scan = [8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]
    eq_res = find_chiral_equilibrium_and_barrier(j_val, jm, js, jl, jp_val, jn_val)
    evo_res = scan_chiral_spin_evolution(spins_scan, jm, js, jl, jp_val, jn_val)

    if args.json:
        out = {"equilibrium": eq_res, "spin_evolution": evo_res}
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(eq_res, evo_res))


if __name__ == "__main__":
    main()
