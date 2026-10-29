#!/usr/bin/env python3
"""Four-blade AMR angle phonon and zero-point fluctuation solver.

Units: energies in MeV, angles in rad, M in hbar^2/MeV, and hbar=1.
The E2 mapping is deliberately an effective geometry diagnostic, not a
microscopic electromagnetic calculation.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent


def ho_operators(n: int):
    a = np.zeros((n, n))
    for k in range(1, n):
        a[k - 1, k] = np.sqrt(k)
    ad = a.T
    return a, ad


def solve(theta0, mass, curvature, k3, k4, q_eff=0.35, n_basis=80):
    """Diagonalize the local non-harmonic Hamiltonian in an HO basis."""
    omega = np.sqrt(curvature / mass)
    sigma2 = 1.0 / (2.0 * mass * omega)
    a, ad = ho_operators(n_basis)
    x = np.sqrt(sigma2) * (a + ad)
    p = 1j * (a - ad) / (2.0 * np.sqrt(sigma2))
    ident = np.eye(n_basis)
    h = p @ p / (2.0 * mass) + 0.5 * curvature * (x @ x)
    h += (k3 / 6.0) * (x @ x @ x) + (k4 / 24.0) * (x @ x @ x @ x)
    vals, vecs = np.linalg.eigh(h)
    psi = vecs[:, 0]
    def expect(op):
        return float(np.real(np.vdot(psi, op @ psi)))
    x2, x4 = expect(x @ x), expect(x @ x @ x @ x)
    theta = theta0 * ident + x
    theta2 = theta @ theta
    theta4 = theta2 @ theta2
    return {
        "theta0_rad": theta0,
        "theta0_deg": np.degrees(theta0),
        "mass_hbar2_per_MeV": mass,
        "C_MeV_per_rad2": curvature,
        "kappa3_MeV_per_rad3": k3,
        "kappa4_MeV_per_rad4": k4,
        "omega_MeV": omega,
        "E_ZPE_harmonic_MeV": 0.5 * omega,
        "E_ground_exact_MeV": float(vals[0]),
        "E_ZPE_anharmonic_MeV": float(vals[0]),
        "delta_theta2_rad2": expect(theta2),
        "delta_x2_rad2": x2,
        "theta4_expectation_rad4": expect(theta4),
        "B_E2_res_effective_e2b2": q_eff * q_eff * expect(theta4),
        "q_eff_eb": q_eff,
    }


def main():
    nominal = dict(mass=10.0, curvature=0.50, k3=0.02, k4=0.40, q_eff=0.35)
    rows = [solve(t, **nominal) for t in np.linspace(0.0, 0.35, 36)]
    # Endpoint uncertainty band: expose how the claimed residual scale depends
    # on inertia, curvature and effective E2 charge.
    endpoint = []
    for mass in (8.0, 10.0, 12.0):
        for curvature in (0.40, 0.50, 0.60):
            for q_eff in (0.30, 0.35, 0.40):
                endpoint.append(solve(0.0, mass, curvature, 0.02, 0.40, q_eff))
    fields = list(rows[0])
    with (OUT / "phonon_scan.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    with (OUT / "endpoint_sensitivity.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(endpoint)
    payload = {
        "model": "local four-blade AMR angle phonon",
        "hamiltonian": "p_theta^2/(2M)+C*x^2/2+kappa3*x^3/6+kappa4*x^4/24",
        "coordinate": "x=theta-theta0; hbar=1; theta in radians",
        "nominal_parameters": nominal,
        "harmonic_formulas": {
            "omega": "sqrt(C/M)",
            "E_ZPE": "0.5*hbar*omega",
            "sigma2": "hbar/(2*M*omega)",
            "endpoint_theta4_harmonic": "3*sigma2^2",
            "B_E2_mapping": "q_eff^2*<theta^4> (effective diagnostic)"
        },
        "endpoint_nominal": rows[0],
        "endpoint_B_range_e2b2": [min(x["B_E2_res_effective_e2b2"] for x in endpoint), max(x["B_E2_res_effective_e2b2"] for x in endpoint)],
        "boundary": "A nonzero <theta^4> is not a proof that every one-phonon E2 matrix element is nonzero; parity and the chosen transition still matter. q_eff is not a measured intrinsic quadrupole moment."
    }
    (OUT / "phonon_scan.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    try:
        import matplotlib.pyplot as plt
        x = [r["theta0_deg"] for r in rows]
        y = [r["B_E2_res_effective_e2b2"] for r in rows]
        fig, ax = plt.subplots(figsize=(6.2, 4.0)); ax.plot(x, y, lw=2)
        ax.axhspan(0.01, 0.03, color="tab:orange", alpha=.2, label="0.01--0.03 $e^2b^2$")
        ax.set(xlabel=r"classical angle $\theta_0$ (deg)", ylabel=r"$q_{eff}^2\langle\theta^4\rangle$ ($e^2b^2$)")
        ax.legend(frameon=False); fig.tight_layout(); fig.savefig(OUT / "zero_point_residual.svg"); plt.close(fig)
    except ImportError:
        pass
    print(json.dumps({"output": str(OUT), "endpoint": rows[0], "B_range": payload["endpoint_B_range_e2b2"]}, indent=2))


if __name__ == "__main__":
    main()
