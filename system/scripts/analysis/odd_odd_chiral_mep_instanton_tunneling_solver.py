#!/usr/bin/env python3
"""
Odd-Odd Chiral Minimum Energy Path (MEP) & Instanton Tunneling Action Solver.

Physical Principle & Formalism:
In odd-odd triaxial nuclei (e.g., 134Pr, 128Cs, 106Ag), chiral doublet bands originate
from the mutual orthogonal coupling of three angular momentum vectors:
1. Valence proton particle j_p (aligned along the short axis s, theta=pi/2, phi=0);
2. Valence neutron hole j_n (aligned along the long axis l, theta=0);
3. Collective core rotation R (preferentially along the intermediate axis i, which has the
   largest moment of inertia J_i > J_s, J_l, corresponding to hydrodynamical or rigid triaxiality).

In 3D Tilted Axis Cranking (TAC), total angular momentum J has orientation angles (theta, phi):
  J_s = I * sin(theta) * cos(phi)
  J_i = I * sin(theta) * sin(phi)
  J_l = I * cos(theta)

The core angular momentum is R = J - j_p - j_n, yielding the classical rotational Routhian:
  E_rot(theta, phi) = 0.5 * [ (J_s - j_p)^2 / J_s + (J_i)^2 / J_i + (J_l - j_n)^2 / J_l ]

Above a critical spin I_crit, the planar solution (phi = 0) becomes a local saddle point
due to the kinematic gain of rotating about the intermediate axis i (J_i > J_s).
A pitchfork bifurcation produces two symmetric, non-planar chiral minima at:
  (theta_0, +phi_0)  [Right-Handed Configuration]
  (theta_0, -phi_0)  [Left-Handed Configuration]

The quantum mechanical restoration of chiral symmetry occurs via quantum tunneling through
the chiral barrier separating these two minima. Along the Minimum Energy Path (MEP)
in (theta, phi) space, the Euclidean Instanton Action is:
  S_inst = int_{MEP} sqrt(2 * B_eff(s) * [V(s) - V_min]) ds
where B_eff is the collective inertia for chiral wobbling/azimuthal angle motion.
The semiclassical chiral energy splitting is given by:
  Delta E_tunnel = (hbar * omega_0 / pi) * exp(-S_inst / hbar)
where hbar * omega_0 is the small-amplitude chiral vibrational frequency at the well minimum.

Textbook & Literature References:
- Chirality and Wobbling in Atomic Nuclei (CRC Press 2025), Ch. 2 (S. Frauendorf), Ch. 10 (Q. B. Chen et al.)
- Chen, Frauendorf, Sun, Phys. Rev. C 96, 051303(R) (2017)
- Frauendorf & Meng, Nucl. Phys. A 617, 131 (1997)
- Bohr & Mottelson, Nuclear Structure, Vol. II, §4-2
"""

import sys
import json
import argparse
import numpy as np
from scipy.optimize import minimize

PRESETS = {
    "134Pr_chiral_mep_instanton": {
        "nucleus": "134Pr",
        "description": "Odd-odd 134Pr pi(h11/2) nu(h11/2)^-1 chiral tunneling at I=17hbar (static regime)",
        "spin": 17.0,
        "j_p": 5.5,
        "j_n": 5.5,
        "gamma_deg": 30.0,
        "moi_s": 15.0,  # MeV^-1 hbar^2
        "moi_i": 38.0,
        "moi_l": 12.0,
        "n_nodes": 25,
    },
    "134Pr_chiral_vibration": {
        "nucleus": "134Pr",
        "description": "Odd-odd 134Pr chiral vibration near critical spin I=13hbar",
        "spin": 13.0,
        "j_p": 5.5,
        "j_n": 5.5,
        "gamma_deg": 30.0,
        "moi_s": 15.0,
        "moi_i": 38.0,
        "moi_l": 12.0,
        "n_nodes": 25,
    },
    "128Cs_chiral_doublet": {
        "nucleus": "128Cs",
        "description": "Odd-odd 128Cs classic chiral doublet band at I=16hbar",
        "spin": 16.0,
        "j_p": 5.5,
        "j_n": 5.5,
        "gamma_deg": 28.0,
        "moi_s": 16.0,
        "moi_i": 40.0,
        "moi_l": 13.0,
        "n_nodes": 25,
    },
    "106Ag_chiral_candidate": {
        "nucleus": "106Ag",
        "description": "A~100 region odd-odd 106Ag pi(g9/2)^-1 nu(h11/2) at I=15hbar",
        "spin": 15.0,
        "j_p": 4.5,  # g9/2 hole along long axis
        "j_n": 5.5,  # h11/2 particle along short axis
        "gamma_deg": 25.0,
        "moi_s": 13.0,
        "moi_i": 30.0,
        "moi_l": 10.0,
        "n_nodes": 25,
    }
}

class OddOddChiralMEPInstantonSolver:
    def __init__(self, spin=17.0, j_p=5.5, j_n=5.5, gamma_deg=30.0,
                 moi_s=15.0, moi_i=38.0, moi_l=12.0):
        self.I = float(spin)
        self.j_p = float(j_p)
        self.j_n = float(j_n)
        self.gamma = np.radians(gamma_deg)
        self.moi_s = float(moi_s)
        self.moi_i = float(moi_i)
        self.moi_l = float(moi_l)

    def potential_routhian(self, theta, phi):
        """
        Evaluate classical Routhian V(theta, phi) in TAC approximation:
        theta: polar angle from l-axis (0 <= theta <= pi)
        phi: azimuthal angle in s-i plane (-pi/2 <= phi <= pi/2)
        """
        Js = self.I * np.sin(theta) * np.cos(phi)
        Ji = self.I * np.sin(theta) * np.sin(phi)
        Jl = self.I * np.cos(theta)

        Rs = Js - self.j_p
        Ri = Ji
        Rl = Jl - self.j_n

        E_rot = 0.5 * (Rs**2 / self.moi_s + Ri**2 / self.moi_i + Rl**2 / self.moi_l)
        return E_rot

    def find_chiral_minima_and_saddle(self):
        """
        Find left-handed and right-handed minima (+phi0, -phi0) and planar saddle point (phi=0).
        """
        # Right-handed minimum search (phi > 0)
        res_r = minimize(lambda p: self.potential_routhian(p[0], p[1]),
                         x0=[np.radians(48.0), np.radians(35.0)],
                         bounds=[(np.radians(15.0), np.radians(75.0)),
                                 (np.radians(2.0), np.radians(85.0))],
                         method='L-BFGS-B')

        # Left-handed minimum search (phi < 0)
        res_l = minimize(lambda p: self.potential_routhian(p[0], p[1]),
                         x0=[np.radians(48.0), np.radians(-35.0)],
                         bounds=[(np.radians(15.0), np.radians(75.0)),
                                 (np.radians(-85.0), np.radians(-2.0))],
                         method='L-BFGS-B')

        # Planar saddle point constrained at phi = 0
        res_saddle = minimize(lambda p: self.potential_routhian(p[0], 0.0),
                              x0=[res_r.x[0]],
                              bounds=[(np.radians(15.0), np.radians(75.0))],
                              method='L-BFGS-B')

        theta_r, phi_r = res_r.x[0], res_r.x[1]
        theta_l, phi_l = res_l.x[0], res_l.x[1]
        theta_saddle = res_saddle.x[0]

        v_min_r = float(res_r.fun)
        v_min_l = float(res_l.fun)
        v_saddle = float(self.potential_routhian(theta_saddle, 0.0))
        barrier = max(0.0, v_saddle - min(v_min_r, v_min_l))

        is_broken = bool(barrier > 0.005 and abs(phi_r) > np.radians(8.0))

        return {
            "right_minimum": {"theta_deg": float(np.degrees(theta_r)), "phi_deg": float(np.degrees(phi_r)), "V_MeV": v_min_r},
            "left_minimum": {"theta_deg": float(np.degrees(theta_l)), "phi_deg": float(np.degrees(phi_l)), "V_MeV": v_min_l},
            "saddle_point": {"theta_deg": float(np.degrees(theta_saddle)), "phi_deg": 0.0, "V_MeV": v_saddle},
            "barrier_height_MeV": float(barrier),
            "is_chiral_broken": is_broken
        }

    def compute_minimum_energy_path(self, n_nodes=25):
        """
        Compute Minimum Energy Path (MEP) using Simplified String Method / NEB
        connecting left minimum to right minimum through the saddle point.
        """
        info = self.find_chiral_minima_and_saddle()
        theta_l = np.radians(info["left_minimum"]["theta_deg"])
        phi_l = np.radians(info["left_minimum"]["phi_deg"])
        theta_r = np.radians(info["right_minimum"]["theta_deg"])
        phi_r = np.radians(info["right_minimum"]["phi_deg"])
        theta_sad = np.radians(info["saddle_point"]["theta_deg"])

        # Initial path passing through saddle point at phi=0
        half = n_nodes // 2
        s1 = np.linspace(0.0, 1.0, half + 1)
        th1 = theta_l + s1 * (theta_sad - theta_l)
        ph1 = phi_l + s1 * (0.0 - phi_l)

        s2 = np.linspace(0.0, 1.0, n_nodes - half)
        th2 = theta_sad + s2 * (theta_r - theta_sad)
        ph2 = 0.0 + s2 * (phi_r - 0.0)

        thetas = np.concatenate([th1[:-1], th2])
        phis = np.concatenate([ph1[:-1], ph2])

        nodes = np.column_stack([thetas, phis])

        # String method relaxation
        step_size = 0.015
        for it in range(80):
            for k in range(1, n_nodes - 1):
                th, ph = nodes[k, 0], nodes[k, 1]
                eps = 1e-4
                dth = (self.potential_routhian(th + eps, ph) - self.potential_routhian(th - eps, ph)) / (2 * eps)
                dph = (self.potential_routhian(th, ph + eps) - self.potential_routhian(th, ph - eps)) / (2 * eps)
                nodes[k, 0] -= step_size * dth
                nodes[k, 1] -= step_size * dph

            # Reparametrize by arc-length
            dists = np.sqrt(np.diff(nodes[:, 0])**2 + np.diff(nodes[:, 1])**2)
            cum_dist = np.insert(np.cumsum(dists), 0, 0.0)
            total_dist = cum_dist[-1]
            if total_dist > 1e-9:
                cum_norm = cum_dist / total_dist
                new_s = np.linspace(0.0, 1.0, n_nodes)
                nodes[:, 0] = np.interp(new_s, cum_norm, nodes[:, 0])
                nodes[:, 1] = np.interp(new_s, cum_norm, nodes[:, 1])

        v_mep = np.array([self.potential_routhian(nodes[k, 0], nodes[k, 1]) for k in range(n_nodes)])
        v_min = min(info["left_minimum"]["V_MeV"], info["right_minimum"]["V_MeV"])
        v_rel = v_mep - v_min

        return {
            "minima_info": info,
            "nodes_theta_deg": np.degrees(nodes[:, 0]).tolist(),
            "nodes_phi_deg": np.degrees(nodes[:, 1]).tolist(),
            "V_along_mep_MeV": v_rel.tolist(),
            "total_arc_length_rad": float(total_dist)
        }

    def solve_instanton_action(self, n_nodes=25):
        """
        Calculate Euclidean Instanton Action S_inst and tunneling splitting Delta E_tunnel.
        """
        mep_data = self.compute_minimum_energy_path(n_nodes)
        thetas = np.radians(mep_data["nodes_theta_deg"])
        phis = np.radians(mep_data["nodes_phi_deg"])
        V_rel = np.array(mep_data["V_along_mep_MeV"])
        barrier = mep_data["minima_info"]["barrier_height_MeV"]

        # Effective collective mass parameter B_eff:
        # B_eff = hbar^2 / (omega_wobbling / I)
        # Semiclassical estimate: B_eff ~ J_i / (2 * sin^2(theta_0))
        th0 = thetas[0]
        B_eff = float(self.moi_i / (2.0 * max(0.2, np.sin(th0)**2)))

        # Harmonic frequency at the minimum
        ph_min = phis[0]
        eps = 1e-3
        curv_phi = (self.potential_routhian(th0, ph_min + eps) - 2 * self.potential_routhian(th0, ph_min)
                    + self.potential_routhian(th0, ph_min - eps)) / (eps**2)
        curv_phi = max(float(curv_phi), 0.05)
        hbar_omega0 = np.sqrt(curv_phi / B_eff)

        if barrier > 0.005 and mep_data["minima_info"]["is_chiral_broken"]:
            # Euclidean Instanton Action S_inst = int sqrt(2 * B_eff * V(s)) ds
            diff_th = np.diff(thetas)
            diff_ph = np.diff(phis)
            ds = np.sqrt(diff_th**2 + diff_ph**2)
            mid_V = 0.5 * (V_rel[:-1] + V_rel[1:])
            integrand = np.sqrt(2.0 * B_eff * np.maximum(0.0, mid_V))
            S_inst = float(np.sum(integrand * ds))
            delta_E_MeV = (hbar_omega0 / np.pi) * np.exp(-S_inst)
        else:
            # Chiral vibrational regime: splitting dominated by zero-point vibrational mode
            S_inst = 0.0
            delta_E_MeV = hbar_omega0 / np.pi

        delta_E_keV = delta_E_MeV * 1000.0

        return {
            "spin": self.I,
            "minima_info": mep_data["minima_info"],
            "barrier_height_MeV": barrier,
            "harmonic_omega0_MeV": float(hbar_omega0),
            "effective_mass_B_eff": float(B_eff),
            "instanton_action_hbar": float(S_inst),
            "tunneling_splitting_keV": float(delta_E_keV),
            "mep_trajectory": {
                "theta_deg": mep_data["nodes_theta_deg"],
                "phi_deg": mep_data["nodes_phi_deg"],
                "V_rel_MeV": mep_data["V_along_mep_MeV"]
            }
        }

def main():
    parser = argparse.ArgumentParser(description="Odd-Odd Chiral MEP & Instanton Tunneling Solver")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--spin", type=float, help="Total angular momentum I (hbar)")
    parser.add_argument("--gamma", type=float, help="Triaxial deformation angle gamma (degrees)")
    parser.add_argument("--moi-i", type=float, help="Intermediate axis moment of inertia")
    parser.add_argument("--nodes", type=int, default=25, help="Number of MEP discretization nodes")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["134Pr_chiral_mep_instanton"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.spin is not None:
        cfg["spin"] = args.spin
    if args.gamma is not None:
        cfg["gamma_deg"] = args.gamma
    if args.moi_i is not None:
        cfg["moi_i"] = args.moi_i
    if args.nodes is not None:
        cfg["n_nodes"] = args.nodes

    solver = OddOddChiralMEPInstantonSolver(
        spin=cfg["spin"],
        j_p=cfg["j_p"],
        j_n=cfg["j_n"],
        gamma_deg=cfg["gamma_deg"],
        moi_s=cfg["moi_s"],
        moi_i=cfg["moi_i"],
        moi_l=cfg["moi_l"]
    )

    results = solver.solve_instanton_action(n_nodes=cfg["n_nodes"])
    results["nucleus"] = cfg.get("nucleus", "Generic")
    results["description"] = cfg.get("description", "")

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"=========================================================================")
        print(f"  Odd-Odd Chiral Minimum Energy Path & Instanton Action Solver (Mod 155) ")
        print(f"=========================================================================")
        print(f"Nucleus: {results['nucleus']} | Spin I = {results['spin']:.1f} hbar")
        print(f"Description: {results['description']}")
        min_info = results["minima_info"]
        print(f"\n[1] 3D-TAC Energy Surface Topology:")
        print(f"  Right-handed Minimum: theta = {min_info['right_minimum']['theta_deg']:.2f} deg, phi = {min_info['right_minimum']['phi_deg']:.2f} deg")
        print(f"  Left-handed Minimum:  theta = {min_info['left_minimum']['theta_deg']:.2f} deg, phi = {min_info['left_minimum']['phi_deg']:.2f} deg")
        print(f"  Planar Saddle Point:  theta = {min_info['saddle_point']['theta_deg']:.2f} deg, phi = 0.00 deg")
        print(f"  Chiral Barrier:       Delta V_barrier = {results['barrier_height_MeV']:.4f} MeV ({results['barrier_height_MeV']*1000:.1f} keV)")
        print(f"  Chiral Symmetry:      {'Spontaneously Broken (Static Chirality)' if min_info['is_chiral_broken'] else 'Chiral Vibration / Unbroken'}")
        print(f"\n[2] Instanton Quantum Tunneling Calculation:")
        print(f"  Small-Amplitude Frequency:        hbar*omega_0 = {results['harmonic_omega0_MeV']:.3f} MeV")
        print(f"  Effective Mass Parameter B_eff:   {results['effective_mass_B_eff']:.2f} hbar^2/MeV")
        print(f"  Euclidean Instanton Action S:     {results['instanton_action_hbar']:.4f} hbar")
        print(f"  Chiral Tunneling Splitting:       Delta E_tunnel = {results['tunneling_splitting_keV']:.2f} keV")
        print(f"=========================================================================")

if __name__ == "__main__":
    main()

def run_chiral_mep_analysis(nucleus="Generic", spin=17.0, j_p=5.5, j_n=5.5,
                            gamma_deg=30.0, moi_s=15.0, moi_i=38.0, moi_l=12.0,
                            n_nodes=25):
    solver = OddOddChiralMEPInstantonSolver(
        spin=spin, j_p=j_p, j_n=j_n, gamma_deg=gamma_deg,
        moi_s=moi_s, moi_i=moi_i, moi_l=moi_l
    )
    res = solver.solve_instanton_action(n_nodes=n_nodes)
    res["nucleus"] = nucleus
    return res

def format_text_report(results, title="Odd-Odd Chiral MEP Instanton Tunneling Analysis"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Nucleus: {results['nucleus']} | Spin I = {results['spin']:.1f} hbar")
    min_info = results["minima_info"]
    lines.append("\n[1] 3D-TAC Energy Surface Topology:")
    lines.append(f"  Right-handed Minimum: theta = {min_info['right_minimum']['theta_deg']:.2f} deg, phi = {min_info['right_minimum']['phi_deg']:.2f} deg")
    lines.append(f"  Left-handed Minimum:  theta = {min_info['left_minimum']['theta_deg']:.2f} deg, phi = {min_info['left_minimum']['phi_deg']:.2f} deg")
    lines.append(f"  Planar Saddle Point:  theta = {min_info['saddle_point']['theta_deg']:.2f} deg, phi = 0.00 deg")
    lines.append(f"  Chiral Barrier:       Delta V_barrier = {results['barrier_height_MeV']:.4f} MeV ({results['barrier_height_MeV']*1000:.1f} keV)")
    lines.append(f"  Chiral Symmetry:      {'Spontaneously Broken (Static Chirality)' if min_info['is_chiral_broken'] else 'Chiral Vibration / Unbroken'}")
    lines.append("\n[2] Instanton Quantum Tunneling Calculation:")
    lines.append(f"  Small-Amplitude Frequency:        hbar*omega_0 = {results['harmonic_omega0_MeV']:.3f} MeV")
    lines.append(f"  Effective Mass Parameter B_eff:   {results['effective_mass_B_eff']:.2f} hbar^2/MeV")
    lines.append(f"  Euclidean Instanton Action S:     {results['instanton_action_hbar']:.4f} hbar")
    lines.append(f"  Chiral Tunneling Splitting:       Delta E_tunnel = {results['tunneling_splitting_keV']:.2f} keV")
    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Large-amplitude collective tunneling along the MEP")
    lines.append("couples polar and azimuthal degrees of freedom, lifting chiral degeneracy.")
    lines.append("=" * 76)
    return "\n".join(lines)
