#!/usr/bin/env python3
"""Transparent Nilsson-like octupole mixing toy for odd-A actinides.

This is a reproducible sensitivity model, not a production Nilsson or blocked
HFB calculation.  It diagonalizes a four-orbital K=1/2 neutron Hamiltonian
with beta3 couplings between Delta-l=Delta-j=3 orbitals, evaluates an
effective intrinsic g_K, a parity-dependent decoupling proxy b0, and the
strong-coupling magnetic-moment expression used in the accompanying note.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent
K = 0.5
I = 0.5
Z_OVER_A_225RA = 88.0 / 225.0
GS_FREE_NEUTRON = -3.82608545
GS_QUENCH = 0.70
GS_EFFECTIVE_NEUTRON = GS_FREE_NEUTRON * GS_QUENCH
MU_225RA_EXP = -0.7338
MU_225RA_EXP_SIGMA = 0.0015


# label, l, j, intrinsic parity, unperturbed energy (MeV)
# The orbitals are schematic representatives of the Ra-region Delta-l=Delta-j=3
# octupole pairs.  They are deliberately kept explicit so the input can be
# replaced by a real Woods-Saxon/Nilsson basis later.
ORBITALS = [
    {"label": "nu_i13/2", "l": 6, "j": 6.5, "parity": +1, "energy": 0.00},
    {"label": "nu_g9/2", "l": 4, "j": 4.5, "parity": +1, "energy": 0.82},
    {"label": "nu_j15/2", "l": 7, "j": 7.5, "parity": -1, "energy": 0.48},
    {"label": "nu_f7/2", "l": 3, "j": 3.5, "parity": -1, "energy": 1.30},
]


def single_particle_l_s_z(l: int, j: float, k: float = K) -> tuple[float, float]:
    """Return <l_z> and <s_z> in |l,j,K>, with s=1/2."""
    jj = j * (j + 1.0)
    ss = 0.75
    lz = k * (jj + l * (l + 1.0) - ss) / (2.0 * jj)
    sz = k * (jj - l * (l + 1.0) + ss) / (2.0 * jj)
    return lz, sz


def orbital_gk(orbital: dict, gs: float = GS_EFFECTIVE_NEUTRON) -> float:
    # Neutron orbital g_l=0.  The function is written so proton g_l can be
    # added without changing the diagonalization or output schema.
    lz, sz = single_particle_l_s_z(orbital["l"], orbital["j"])
    return (0.0 * lz + gs * sz) / K


def orbital_b0(orbital: dict) -> float:
    """A dimensionless K=1/2 decoupling proxy.

    The exact Nilsson expression contains off-diagonal j_+ matrix elements
    and a phase convention.  Here its diagonal stretched-basis analogue is
    retained explicitly; this quantity is therefore a diagnostic proxy, not
    an extracted experimental decoupling parameter.
    """
    j = orbital["j"]
    return orbital["parity"] * np.sqrt(max(j * (j + 1.0) - K * (K + 1.0), 0.0))


def hamiltonian(beta3: float) -> np.ndarray:
    h = np.diag([o["energy"] for o in ORBITALS]).astype(float)
    # Reflection-asymmetric couplings: g9/2 <-> j15/2 and i13/2 <-> f7/2.
    # A smaller cross-channel term represents higher-order configuration mixing.
    couplings = {(1, 2): 1.10, (0, 3): 0.85, (0, 2): 0.16, (1, 3): 0.12}
    for (i, j), v in couplings.items():
        h[i, j] = h[j, i] = beta3 * v
    return h


def branch_for_seed(evecs: np.ndarray, seed: int) -> tuple[int, float]:
    overlaps = np.abs(evecs[seed, :]) ** 2
    idx = int(np.argmax(overlaps))
    return idx, float(overlaps[idx])


def evaluate_branch(vec: np.ndarray, dominant_parity: int) -> dict:
    weights = np.abs(vec) ** 2
    gk = float(sum(w * orbital_gk(o) for w, o in zip(weights, ORBITALS)))
    b0_raw = float(sum(w * orbital_b0(o) for w, o in zip(weights, ORBITALS)))
    # Reflection of the intrinsic wave function changes the sign of the
    # odd-parity component in the parity-projected partner.  This is the
    # minimal source of a b0+/- bifurcation in this toy model.
    odd_weight = float(sum(w for w, o in zip(weights, ORBITALS) if o["parity"] < 0))
    b0 = b0_raw + dominant_parity * 2.0 * odd_weight * np.sqrt(3.0)
    positive_weight = float(sum(w for w, o in zip(weights, ORBITALS) if o["parity"] > 0))
    negative_weight = 1.0 - positive_weight
    return {
        "g_k": gk,
        "b0": b0,
        "b0_raw": b0_raw,
        "positive_weight": positive_weight,
        "negative_weight": negative_weight,
    }


def rotor_mu(gk: float, b0: float, parity_sign: int) -> tuple[float, float, float, float]:
    """Return requested formula, standard form, b0 correction, and corrected sum."""
    gr = Z_OVER_A_225RA
    # Formula requested in the task.
    requested = I / (I + 1.0) * (gr * I + (gk - gr) * K * K / I)
    standard = gr * I + (gk - gr) * K * K / (I + 1.0)
    # Explicit K=1/2 decoupling correction proxy; phase alternates between
    # the two parity-dominant branches.  It is kept separate from requested.
    correction = parity_sign * ((-1.0) ** int(I + 0.5)) * b0 * (gk - gr) / (2.0 * (I + 1.0))
    return requested, standard, correction, requested + correction


def main() -> None:
    rows = []
    betas = np.round(np.arange(0.0, 0.1601, 0.005), 5)
    for beta3 in betas:
        evals, evecs = np.linalg.eigh(hamiltonian(float(beta3)))
        p_idx, p_overlap = branch_for_seed(evecs, 0)
        m_idx, m_overlap = branch_for_seed(evecs, 2)
        if p_idx == m_idx:
            # At an accidental crossing, use the next best negative branch.
            candidates = [i for i in np.argsort(-np.abs(evecs[2, :]) ** 2) if i != p_idx]
            m_idx = int(candidates[0])
            m_overlap = float(np.abs(evecs[2, m_idx]) ** 2)
        for label, idx, dominant, overlap in [
            ("positive-parity-dominant", p_idx, +1, p_overlap),
            ("negative-parity-dominant", m_idx, -1, m_overlap),
        ]:
            branch = evaluate_branch(evecs[:, idx], dominant)
            mu, mu_standard, correction, mu_with_b0 = rotor_mu(branch["g_k"], branch["b0"], dominant)
            rows.append(
                {
                    "beta3": float(beta3),
                    "branch": label,
                    "eigenvalue_MeV": float(evals[idx]),
                    "seed_overlap": overlap,
                    **branch,
                    "mu_requested_formula_muN": mu,
                    "mu_standard_formula_muN": mu_standard,
                    "mu_b0_correction_muN": correction,
                    "mu_requested_plus_b0_muN": mu_with_b0,
                    "mu_225Ra_experiment_muN": MU_225RA_EXP,
                    "mu_225Ra_experiment_sigma_muN": MU_225RA_EXP_SIGMA,
                }
            )

    csv_path = OUT / "nilsson_octupole_magnetic_moments.csv"
    json_path = OUT / "nilsson_octupole_magnetic_moments.json"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    payload = {
        "model": "four-orbital K=1/2 neutron Nilsson-like octupole mixing toy",
        "status": "illustrative sensitivity model; not a production blocked-HFB/Nilsson calculation",
        "beta3_grid": [float(x) for x in betas],
        "parameters": {
            "K": K,
            "I": I,
            "Z_over_A_225Ra": Z_OVER_A_225RA,
            "g_s_free_neutron": GS_FREE_NEUTRON,
            "g_s_quench": GS_QUENCH,
            "g_s_effective_neutron": GS_EFFECTIVE_NEUTRON,
            "mu_225Ra_experiment_muN": MU_225RA_EXP,
            "mu_225Ra_experiment_sigma_muN": MU_225RA_EXP_SIGMA,
        },
        "orbitals": ORBITALS,
        "notes": [
            "beta3 is a dimensionless octupole deformation proxy.",
            "g_K is an intrinsic expectation value with quenched neutron spin g_s.",
            "b0 is a parity-sensitive stretched-basis proxy; it is not the measured decoupling parameter.",
            "225Ra static mu is an external benchmark; no fit to it is performed.",
        ],
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {csv_path}")
    print(f"wrote {json_path}")
    for branch in ("positive-parity-dominant", "negative-parity-dominant"):
        r = [x for x in rows if x["branch"] == branch and abs(x["beta3"] - 0.10) < 1e-9][0]
        print(branch, "beta3=0.10", "gK=", round(r["g_k"], 5), "b0=", round(r["b0"], 5), "mu=", round(r["mu_requested_formula_muN"], 5))


if __name__ == "__main__":
    main()
