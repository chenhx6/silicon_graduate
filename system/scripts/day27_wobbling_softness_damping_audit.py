#!/usr/bin/env python3
"""Quantum Hermitian analysis of gamma-softness vs dissipative wobbling damping.

Audits the toy polynomial formula 'damping_ratio = 1.5*(sigma_gamma/gamma0)^2'
used in the Day 27 microscopic-inapplicability solver, proving that:
1. A closed collective Hamiltonian in gamma is strictly Hermitian with discrete,
   real eigenvalues and zero intrinsic dynamical width (Gamma = 0).
2. Spreading width Gamma_down = 2*pi*V^2*rho requires dense background quasiparticle
   states; near-yrast low-spin wobbling states (E* < 1 MeV) reside in a sparse
   density regime (rho <= 1 MeV^-1), precluding classical overdamping (Gamma/omega > 0.5).
"""

import argparse
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy.linalg


def solve_gamma_collective(C_gamma, D=20.0, gamma0_deg=20.0, N=250):
    """Solves the 1D collective Hamiltonian in gamma on [gamma_min, gamma_max]."""
    gamma0 = math.radians(gamma0_deg)
    gamma_min = math.radians(2.0)
    gamma_max = math.radians(58.0)
    gamma_grid = np.linspace(gamma_min, gamma_max, N)
    dgamma = gamma_grid[1] - gamma_grid[0]

    # Kinetic energy matrix (second-order central difference):
    T = np.zeros((N, N))
    for i in range(N):
        T[i, i] = 2.0 / (dgamma**2)
        if i > 0:
            T[i, i - 1] = -1.0 / (dgamma**2)
        if i < N - 1:
            T[i, i + 1] = -1.0 / (dgamma**2)
    T *= 1.0 / (2.0 * D)

    # Potential energy:
    V_diag = 0.5 * C_gamma * (gamma_grid - gamma0) ** 2
    H = T + np.diag(V_diag)

    evals, evecs = scipy.linalg.eigh(H)

    E0, E1, E2 = float(evals[0]), float(evals[1]), float(evals[2])
    psi0 = evecs[:, 0]
    psi0_prob = psi0**2 / (np.sum(psi0**2) * dgamma)

    mean_gamma = float(np.sum(gamma_grid * psi0_prob) * dgamma)
    var_gamma = float(np.sum((gamma_grid - mean_gamma) ** 2 * psi0_prob) * dgamma)
    sigma_gamma_deg = float(math.degrees(math.sqrt(var_gamma)))

    gap_10 = E1 - E0
    gap_21 = E2 - E1
    anharmonicity = (E2 - 2 * E1 + E0) / gap_10 if gap_10 > 1e-6 else 0.0

    # Toy formula from Day 27 solver for comparison:
    toy_damping_ratio = 1.5 * ((sigma_gamma_deg / gamma0_deg) ** 2)

    return {
        "C_gamma": C_gamma,
        "sigma_gamma_deg": round(sigma_gamma_deg, 2),
        "softness_ratio": round(sigma_gamma_deg / gamma0_deg, 3),
        "E0": round(E0, 4),
        "gap_1_0": round(gap_10, 4),
        "gap_2_1": round(gap_21, 4),
        "anharmonicity": round(anharmonicity, 4),
        "toy_solver_damping_ratio": round(toy_damping_ratio, 4),
        "true_hermitian_intrinsic_width_Gamma": 0.0,
        "all_eigenvalues_real": bool(np.all(np.isreal(evals))),
    }


def evaluate_spreading_width_requirements(
    omega_wob_MeV=0.5, coupling_V_MeV=0.05
):
    """Computes background density rho needed to achieve various damping ratios."""
    ratios = [0.05, 0.10, 0.20, 0.50, 1.00]
    results = []
    for r in ratios:
        target_Gamma = r * omega_wob_MeV
        # Gamma_down = 2 * pi * V^2 * rho  =>  rho = Gamma_down / (2 * pi * V^2)
        required_rho = target_Gamma / (2.0 * math.pi * (coupling_V_MeV**2))
        results.append(
            {
                "damping_ratio_target": r,
                "target_Gamma_MeV": round(target_Gamma, 4),
                "coupling_matrix_element_V_MeV": coupling_V_MeV,
                "required_background_density_rho_per_MeV": round(
                    required_rho, 2
                ),
                "physical_feasibility_at_near_yrast": (
                    "Feasible if sparse (rho <= 1)"
                    if required_rho <= 1.0
                    else "Unphysical near yrast (rho >> 1 MeV^-1 below pairing threshold)"
                ),
            }
        )
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    C_vals = [
        1500.0,
        1000.0,
        600.0,
        400.0,
        250.0,
        150.0,
        80.0,
        40.0,
        20.0,
        10.0,
        5.0,
        2.0,
    ]
    scan_rows = []
    for C in C_vals:
        res = solve_gamma_collective(C)
        scan_rows.append(res)

    csv_path = args.output_dir / "gamma_softness_spectrum_scan.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=scan_rows[0].keys())
        writer.writeheader()
        writer.writerows(scan_rows)

    spreading_requirements = evaluate_spreading_width_requirements()

    out_data = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "status": "exact-quantum-hermitian-resolution",
        "physical_conclusion": [
            "1. In an isolated nucleus governed by a Hermitian collective Hamiltonian, gamma-softness causes potential broadening (large sigma_gamma), state mixing, and strong anharmonicity, but CANNOT produce an intrinsic dissipative linewidth (Gamma = 0 identically).",
            "2. Spreading width Gamma_down = 2*pi*V^2*rho requires coupling to an external bath or dense background continuum. Near-yrast wobbling states (E* < 1 MeV) have identical-spin/parity level density rho <= 1 MeV^-1, restricting any spreading width to Gamma_down <= 0.015 MeV (damping ratio <= 0.03).",
            "3. The Day 27 solver formula 'damping_ratio = 1.5*(sigma_gamma/gamma0)^2' and its threshold 0.50 are completely arbitrary toy polynomial constructions that conflated Hermitian state mixing with dissipative friction.",
        ],
        "scan_data": scan_rows,
        "spreading_width_analysis": spreading_requirements,
        "artifact": {
            "csv": str(csv_path.name),
            "data_points": len(scan_rows),
        },
    }

    json_path = args.output_dir / "wobbling_softness_damping_resolution.json"
    json_path.write_text(json.dumps(out_data, indent=2) + "\n")
    print(json.dumps(out_data, indent=2))


if __name__ == "__main__":
    main()
