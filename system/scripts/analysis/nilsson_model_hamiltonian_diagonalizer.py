#!/usr/bin/env python3
"""
nilsson_model_hamiltonian_diagonalizer.py
========================================
Deformed Harmonic Oscillator Nilsson Model Hamiltonian Diagonalizer &
Single-Particle Energy Level Engine.

Physics & Formulation:
----------------------
1. Nilsson Hamiltonian (Nilsson 1955, Bohr-Mottelson Vol. II):
   H = H_0 - (2/3) * epsilon_2 * hbar * omega_0 * sqrt(4*pi/5) * Y_20 -
       2 * kappa * hbar * omega_0 * (l . s) - kappa * mu * hbar * omega_0 * [l^2 - <l^2>_N]
   where:
     hbar * omega_0 = 41.0 * A^(-1/3) MeV
     <l^2>_N = 0.5 * N * (N + 3)
     kappa, mu: standard Nilsson parameters for protons or neutrons.

2. Spherical Basis Representation |N, l, j, Omega>:
   Matrix blocks are partitioned by major shell N and angular momentum projection Omega.
   - Diagonal unperturbed energies:
     E_diag = hbar*omega_0 * (N + 1.5) - kappa*hbar*omega_0 * [j*(j+1) - l*(l+1) - 0.75] -
              kappa*mu*hbar*omega_0 * [l*(l+1) - 0.5*N*(N+3)]
   - Quadrupole deformation coupling:
     <N l' j' Omega | Y_20 | N l j Omega> = (-1)^(j' - Omega) * (j' 2 j; -Omega 0 Omega) *
                                           <N l' j' || Y_2 || N l j>
     where:
       <N l' j' || Y_2 || N l j> = (-1)^(j + 0.5) * sqrt(5 * (2j+1)*(2j'+1) / (4*pi)) *
                                   (j' 2 j; 0.5 0 -0.5) * 0.5 * [1 + (-1)^(l + l')]

3. Jacobi Diagonalization:
   Symmetric matrix diagonalization within each (N, Omega) sub-block yields
   the single-particle eigenvalues e_i(epsilon_2) as a function of deformation.

4. Asymptotic Quantum Numbers Omega[N n_z Lambda]:
   Down-sloping orbitals (large n_z) drive prolate deformation;
   Up-sloping orbitals (small n_z) drive oblate deformation.

References:
  - S. G. Nilsson, Dan. Mat. Fys. Medd. 29, no. 16 (1955).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, Benjamin (1975).
  - 卢希庭, 《原子核物理（修订版）》, 第4章 独立粒子壳模型与变形核.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


# Standard Nilsson parameters (Bengtsson & Ragnarsson 1985 / Ring & Schuck)
NILSSON_PARAMS = {
    "proton": {
        0: {"kappa": 0.120, "mu": 0.0},
        1: {"kappa": 0.120, "mu": 0.0},
        2: {"kappa": 0.105, "mu": 0.0},
        3: {"kappa": 0.090, "mu": 0.25},
        4: {"kappa": 0.065, "mu": 0.57},
        5: {"kappa": 0.060, "mu": 0.65},
        6: {"kappa": 0.054, "mu": 0.69}
    },
    "neutron": {
        0: {"kappa": 0.120, "mu": 0.0},
        1: {"kappa": 0.120, "mu": 0.0},
        2: {"kappa": 0.105, "mu": 0.0},
        3: {"kappa": 0.090, "mu": 0.25},
        4: {"kappa": 0.065, "mu": 0.43},
        5: {"kappa": 0.062, "mu": 0.43},
        6: {"kappa": 0.062, "mu": 0.34}
    }
}


def wigner_3j(j1: float, j2: float, j3: float, m1: float, m2: float, m3: float) -> float:
    """Exact algebraic Wigner 3j symbol calculation using Racah formula."""
    if abs(m1 + m2 + m3) > 1e-5:
        return 0.0
    if j3 < abs(j1 - j2) or j3 > (j1 + j2):
        return 0.0
    if abs(m1) > j1 or abs(m2) > j2 or abs(m3) > j3:
        return 0.0

    j1_2 = int(round(2 * j1))
    j2_2 = int(round(2 * j2))
    j3_2 = int(round(2 * j3))
    m1_2 = int(round(2 * m1))
    m2_2 = int(round(2 * m2))
    m3_2 = int(round(2 * m3))

    # Check triangle integer parity
    if (j1_2 + j2_2 + j3_2) % 2 != 0:
        return 0.0
    if (j1_2 - m1_2) % 2 != 0 or (j2_2 - m2_2) % 2 != 0 or (j3_2 - m3_2) % 2 != 0:
        return 0.0

    # Triangle coefficient Delta
    def tri_coeff(a, b, c):
        f = math.factorial
        num = f((a + b - c) // 2) * f((a - b + c) // 2) * f((-a + b + c) // 2)
        den = f((a + b + c) // 2 + 1)
        return math.sqrt(num / den)

    delta = tri_coeff(j1_2, j2_2, j3_2)
    f = math.factorial

    prefactor = delta * math.sqrt(
        f((j1_2 + m1_2) // 2) * f((j1_2 - m1_2) // 2) *
        f((j2_2 + m2_2) // 2) * f((j2_2 - m2_2) // 2) *
        f((j3_2 + m3_2) // 2) * f((j3_2 - m3_2) // 2)
    )

    # Sum over t
    t_min = max(0, (j2_2 - j3_2 - m1_2) // 2, (j1_2 - j3_2 + m2_2) // 2)
    t_max = min((j1_2 + j2_2 - j3_2) // 2, (j1_2 - m1_2) // 2, (j2_2 + m2_2) // 2)

    s = 0.0
    for t in range(t_min, t_max + 1):
        num = (-1.0) ** t
        den = (
            f(t) *
            f((j1_2 + j2_2 - j3_2) // 2 - t) *
            f((j1_2 - m1_2) // 2 - t) *
            f((j2_2 + m2_2) // 2 - t) *
            f((j3_2 - j2_2 + m1_2) // 2 + t) *
            f((j3_2 - j1_2 - m2_2) // 2 + t)
        )
        s += num / den

    sign_overall = (-1.0) ** int(round(j1 - j2 - m3))
    return sign_overall * prefactor * s


def jacobi_eigenvalues(matrix: List[List[float]], max_iter: int = 100) -> List[float]:
    """Computes eigenvalues of a real symmetric matrix via Jacobi rotation."""
    n = len(matrix)
    if n == 1:
        return [matrix[0][0]]

    A = [row[:] for row in matrix]

    for _ in range(max_iter):
        # Find maximum off-diagonal element
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j

        if max_val < 1e-10:
            break

        app = A[p][p]
        aqq = A[q][q]
        apq = A[p][q]

        theta = 0.5 * math.atan2(2.0 * apq, aqq - app)
        c = math.cos(theta)
        s = math.sin(theta)

        # Rotate A
        for k in range(n):
            if k != p and k != q:
                akp = A[k][p]
                akq = A[k][q]
                A[k][p] = c * akp - s * akq
                A[p][k] = A[k][p]
                A[k][q] = s * akp + c * akq
                A[q][k] = A[k][q]

        A[p][p] = c**2 * app - 2.0 * s * c * apq + s**2 * aqq
        A[q][q] = s**2 * app + 2.0 * s * c * apq + c**2 * aqq
        A[p][q] = 0.0
        A[q][p] = 0.0

    evals = [A[i][i] for i in range(n)]
    return sorted(evals)


def solve_nilsson_subblock(
    N: int,
    Omega: float,
    epsilon_2: float,
    A_mass: int = 130,
    is_neutron: bool = False
) -> List[Dict[str, Any]]:
    """
    Constructs and diagonalizes the Nilsson sub-matrix for a given (N, Omega) block.
    """
    # Basis states |N, l, j>
    basis = []
    l_vals = [l for l in range(N % 2, N + 1, 2)]
    for l in l_vals:
        for j_offset in (-0.5, +0.5):
            j = l + j_offset
            if j >= Omega and j > 0:
                basis.append((l, j))

    dim = len(basis)
    if dim == 0:
        return []

    particle_key = "neutron" if is_neutron else "proton"
    params = NILSSON_PARAMS[particle_key].get(min(N, 6), {"kappa": 0.065, "mu": 0.50})
    kappa = params["kappa"]
    mu = params["mu"]

    hbar_omega0 = 41.0 * (A_mass ** (-1.0 / 3.0))  # MeV
    l2_avg = 0.5 * N * (N + 3)

    # Construct Hamiltonian matrix (in units of hbar*omega0)
    H = [[0.0] * dim for _ in range(dim)]

    for i in range(dim):
        li, ji = basis[i]
        # Diagonal term
        ls_term = ji * (ji + 1.0) - li * (li + 1.0) - 0.75
        l2_term = li * (li + 1.0) - l2_avg
        e_sph = (N + 1.5) - kappa * ls_term - kappa * mu * l2_term
        H[i][i] = e_sph

        # Deformation couplings <i| -2/3 * eps * sqrt(4pi/5) * Y20 |j>
        for k in range(dim):
            lk, jk = basis[k]
            if (li + lk) % 2 != 0:
                continue

            # Wigner 3j coupling
            w3j_m = wigner_3j(ji, 2.0, jk, -Omega, 0.0, Omega)
            w3j_half = wigner_3j(ji, 2.0, jk, 0.5, 0.0, -0.5)

            if abs(w3j_m) > 1e-6 and abs(w3j_half) > 1e-6:
                phase = (-1.0) ** int(round(ji - Omega + jk + 0.5))
                red_mat = phase * math.sqrt(5.0 * (2.0 * ji + 1.0) * (2.0 * jk + 1.0) / (4.0 * math.pi)) * w3j_half
                y20_elem = ((-1.0) ** int(round(ji - Omega))) * w3j_m * red_mat

                # Multiply by -2/3 * eps * sqrt(4pi/5)
                v_def = - (2.0 / 3.0) * epsilon_2 * math.sqrt(4.0 * math.pi / 5.0) * y20_elem
                H[i][k] += v_def

    eigenvalues = jacobi_eigenvalues(H)

    results = []
    for rank, ev in enumerate(eigenvalues):
        # Asymptotic guess: dominant l and j
        diag_idx = min(rank, dim - 1)
        l_dom, j_dom = basis[diag_idx]
        e_MeV = ev * hbar_omega0

        results.append({
            "N": N,
            "Omega": Omega,
            "rank": rank + 1,
            "dominant_l": l_dom,
            "dominant_j": j_dom,
            "eigenvalue_hbar_omega0": round(ev, 4),
            "energy_MeV": round(e_MeV, 3),
            "slope_prolate_driving": "Down-sloping (prolate-stabilizing)" if (ev < (N + 1.5)) else "Up-sloping (oblate-stabilizing)"
        })

    return results


def scan_nilsson_diagram(
    N_list: List[int] = [3, 4, 5],
    epsilon_values: List[float] = [0.0, 0.15, 0.25, 0.35],
    A_mass: int = 130,
    is_neutron: bool = False
) -> Dict[str, Any]:
    """
    Computes single-particle trajectories across a mesh of quadrupole deformations epsilon_2.
    """
    diagram = {}
    for eps in epsilon_values:
        levels = []
        for N in N_list:
            # Omega goes from 1/2 to N + 1/2
            max_omega = N + 0.5
            omega_vals = [0.5 + k for k in range(int(max_omega + 0.5))]
            for om in omega_vals:
                res = solve_nilsson_subblock(N, om, eps, A_mass, is_neutron)
                levels.extend(res)

        levels.sort(key=lambda x: x["energy_MeV"])
        diagram[f"eps_{eps:.2f}"] = levels

    return diagram


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   DEFORMED NILSSON SINGLE-PARTICLE HAMILTONIAN DIAGONALIZER")
    lines.append("=" * 72)
    lines.append(f" Nucleus Mass A: {summary.get('A_mass')}, Specie: {summary.get('particle_type')}")
    lines.append(f" Deformation epsilon_2: {summary.get('epsilon_2')} (beta_2 ~ {summary.get('beta_2_approx'):.2f})")
    lines.append("-" * 72)
    lines.append(f" {'N':<3} {'Omega':<6} {'dom_j':<8} {'Energy (hw0)':<14} {'Energy (MeV)':<14} {'Slope/Drive':<25}")
    lines.append(" " + "-" * 70)

    for lv in summary.get("levels", [])[:15]:
        lines.append(
            f" {lv['N']:<3} {lv['Omega']:<6} {lv['dominant_j']:<8} "
            f"{lv['eigenvalue_hbar_omega0']:<14.3f} {lv['energy_MeV']:<14.2f} {lv['slope_prolate_driving']:<25}"
        )
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Down-sloping orbitals (e.g. high-K, large nz) lower energy under prolate elongation.")
    lines.append("   - Solves single-particle levels for odd-A deformed nuclei (e.g. h11/2, i13/2).")
    lines.append("   - Essential foundation for particle-rotor models, TPSM and high-spin band crossings.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Deformed Nilsson Model Single-Particle Diagonalizer."
    )
    parser.add_argument("-N", "--shell", type=int, default=4, help="Major oscillator shell N (default: 4)")
    parser.add_argument("-e", "--epsilon", type=float, default=0.25, help="Quadrupole deformation epsilon_2 (default: 0.25)")
    parser.add_argument("-A", "--mass", type=int, default=130, help="Mass number A (default: 130)")
    parser.add_argument("--neutron", action="store_true", help="Compute for neutron instead of proton")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    levels = []
    # Run across Omega in shell N
    max_omega = args.shell + 0.5
    omega_vals = [0.5 + k for k in range(int(max_omega + 0.5))]
    for om in omega_vals:
        res = solve_nilsson_subblock(args.shell, om, args.epsilon, args.mass, args.neutron)
        levels.extend(res)

    levels.sort(key=lambda x: x["energy_MeV"])

    summary = {
        "A_mass": args.mass,
        "particle_type": "Neutron" if args.neutron else "Proton",
        "shell_N": args.shell,
        "epsilon_2": args.epsilon,
        "beta_2_approx": round(args.epsilon / 0.63, 2),
        "levels": levels
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
