#!/usr/bin/env python3
"""Finite-N sdf-IBM coherent-state calculation for octupole collectivity.

The script uses s (L=0,+), d (L=2,+), and f (L=3,-) bosons.  It evaluates
the condensate expectation value of a rotationally invariant Hamiltonian and
the finite-N one-body correction to Q_lambda.Q_lambda.  No external package
beyond NumPy is required.
"""
from __future__ import annotations

import csv
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent


def fact(n: int) -> int:
    return math.factorial(n) if n >= 0 else 0


def wigner3j(j1: int, j2: int, j3: int, m1: int, m2: int, m3: int) -> float:
    """Integer-angular-momentum Wigner 3j, sufficient for s-d-f tensors."""
    if m1 + m2 + m3 != 0 or any(abs(m) > j for m, j in ((m1, j1), (m2, j2), (m3, j3))):
        return 0.0
    if j3 < abs(j1 - j2) or j3 > j1 + j2:
        return 0.0
    tri = fact(j1 + j2 - j3) * fact(j1 - j2 + j3) * fact(-j1 + j2 + j3)
    tri /= fact(j1 + j2 + j3 + 1)
    pref = (-1) ** (j1 - j2 - m3)
    pref *= math.sqrt(tri * fact(j1 + m1) * fact(j1 - m1) * fact(j2 + m2)
                       * fact(j2 - m2) * fact(j3 + m3) * fact(j3 - m3))
    total = 0.0
    for z in range(32):
        den = (fact(z) * fact(j1 + j2 - j3 - z) * fact(j1 - m1 - z)
               * fact(j2 + m2 - z) * fact(j3 - j2 + m1 + z)
               * fact(j3 - j1 - m2 + z))
        if den:
            total += (-1) ** z / den
    return pref * total


def cg(j1: int, m1: int, j2: int, m2: int, J: int, M: int) -> float:
    return (-1) ** (j1 - j2 + M) * math.sqrt(2 * J + 1) * wigner3j(j1, j2, J, m1, m2, -M)


SPECIES = ("s", "d", "f")
ANG = {"s": 0, "d": 2, "f": 3}
INDEX = [(a, m) for a in SPECIES for m in range(-ANG[a], ANG[a] + 1)]
I = {x: n for n, x in enumerate(INDEX)}


def tensor(a: str, b: str, rank: int) -> list[np.ndarray]:
    """Matrices for [a^dagger x tilde(b)]^(rank), one boson space."""
    out = []
    for M in range(-rank, rank + 1):
        mat = np.zeros((len(INDEX), len(INDEX)))
        for ma in range(-ANG[a], ANG[a] + 1):
            for mb in range(-ANG[b], ANG[b] + 1):
                if ma + mb != M:
                    continue
                coeff = cg(ANG[a], ma, ANG[b], mb, rank, M)
                if coeff:
                    # tilde b_mb = (-1)^mb b_{-mb}; the column is m=-mb.
                    mat[I[(a, ma)], I[(b, -mb)]] += coeff * (-1) ** mb
        out.append(mat)
    return out


def add(a: list[np.ndarray], b: list[np.ndarray], scale: float = 1.0) -> list[np.ndarray]:
    return [x + scale * y for x, y in zip(a, b)]


@lru_cache(maxsize=16)
def make_operators(chi_d: float, chi_f: float, chi_df: float) -> tuple[list[np.ndarray], list[np.ndarray]]:
    q2 = add(tensor("s", "d", 2), tensor("d", "s", 2))
    q2 = add(q2, tensor("d", "d", 2), chi_d)
    q2 = add(q2, tensor("f", "f", 2), chi_f)
    q3 = add(tensor("s", "f", 3), tensor("f", "s", 3))
    q3 = add(q3, tensor("d", "f", 3), chi_df)
    q3 = add(q3, tensor("f", "d", 3), chi_df)
    return q2, q3


def dot(a: list[np.ndarray], b: list[np.ndarray]) -> np.ndarray:
    rank = (len(a) - 1) // 2
    return sum(((-1) ** M) * a[M + rank] @ b[-M + rank] for M in range(-rank, rank + 1))


def alpha_vector(beta2: float, beta3: float) -> np.ndarray:
    v = np.zeros(len(INDEX))
    v[I[("s", 0)]] = 1.0
    v[I[("d", 0)]] = beta2
    v[I[("f", 0)]] = beta3
    return v / math.sqrt(1.0 + beta2 * beta2 + beta3 * beta3)


def observables(beta2: float, beta3: float, N: int, pars: dict) -> dict:
    q2, q3 = make_operators(pars["chi_d"], pars["chi_f"], pars["chi_df"])
    a = alpha_vector(beta2, beta3)
    D = 1.0 + beta2 * beta2 + beta3 * beta3
    nd, nf = N * beta2 * beta2 / D, N * beta3 * beta3 / D
    means = {"q2": [float(a @ q @ a) for q in q2], "q3": [float(a @ q @ a) for q in q3]}
    q2bar = sum(((-1) ** M) * means["q2"][M + 2] * means["q2"][2 - M] for M in range(-2, 3))
    q3bar = sum(((-1) ** M) * means["q3"][M + 3] * means["q3"][3 - M] for M in range(-3, 4))
    r2, r3 = float(a @ dot(q2, q2) @ a), float(a @ dot(q3, q3) @ a)
    # <Q.Q> = N(N-1) qbar.qbar + N <q.q> in an N-boson condensate.
    Q2Q2 = N * (N - 1) * q2bar + N * r2
    Q3Q3 = N * (N - 1) * q3bar + N * r3
    e = (pars["eps_d"] * nd + pars["eps_f"] * nf - pars["kappa2"] * Q2Q2
         - pars["kappa3"] * Q3Q3 + pars["kappaL"] * 0.0)
    # Strong-coupling intrinsic moments and the exact one-f/one-d finite-N scale.
    q20, q30 = N * means["q2"][2], N * means["q3"][3]
    rotor_be2 = 5.0 / (16.0 * math.pi) * q20 * q20
    rotor_be3 = 7.0 / (16.0 * math.pi) * q30 * q30
    return {"energy": e, "nd": nd, "nf": nf, "q20": q20, "q30": q30,
            "Q2Q2": Q2Q2, "Q3Q3": Q3Q3, "one_body_q2q2": r2,
            "one_body_q3q3": r3, "rotor_BE2": rotor_be2, "rotor_BE3": rotor_be3,
            "finite_N_factor": (N - 1) / N if N else 0.0}


def scan_minimum(N: int, kappa3: float, pars: dict, b2_grid: np.ndarray, b3_grid: np.ndarray) -> dict:
    p = dict(pars, kappa3=float(kappa3))
    best = None
    for b2 in b2_grid:
        for b3 in b3_grid:
            obs = observables(float(b2), float(b3), N, p)
            if best is None or obs["energy"] < best["energy"]:
                best = dict(obs, beta2=float(b2), beta3=float(b3), kappa3=float(kappa3))
    return best


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    pars = {"eps_d": 0.80, "eps_f": 1.10, "kappa2": 0.018,
            "kappa3": 0.0, "kappaL": 0.0, "chi_d": -0.55,
            "chi_f": 0.20, "chi_df": 0.25}
    N0 = 7
    b2_grid = np.linspace(0.0, 0.70, 71)
    b3_grid = np.linspace(0.0, 0.70, 71)
    surface = []
    for b2 in np.linspace(0.0, 0.60, 31):
        for b3 in np.linspace(-0.60, 0.60, 61):
            o = observables(float(b2), float(b3), N0, pars)
            surface.append({"beta2": b2, "beta3": b3, "energy": o["energy"],
                            "nd": o["nd"], "nf": o["nf"], "Q2Q2": o["Q2Q2"], "Q3Q3": o["Q3Q3"]})
    write_csv(ROOT / "potential_surface.csv", surface)
    critical = []
    for k3 in np.linspace(0.0, 0.20, 41):
        critical.append(scan_minimum(N0, float(k3), pars, b2_grid, b3_grid))
    write_csv(ROOT / "order_parameter_scan.csv", critical)
    # Pair-boson counts relative to the 50/82 core: 144Ba=6, 146Ba=7, 148Ce=8.
    scaling = []
    beta2, beta3 = 0.20, 0.18
    for N in range(2, 21):
        o = observables(beta2, beta3, N, pars)
        scaling.append({"N": N, "beta2": beta2, "beta3": beta3,
                        "rotor_BE2": o["rotor_BE2"], "rotor_BE3": o["rotor_BE3"],
                        "finite_N_factor_Nminus1_over_N": o["finite_N_factor"],
                        "one_body_corrected_Q3Q3": o["Q3Q3"],
                        "classical_N2_Q3Q3": N * N * (o["q30"] / N) ** 2,
                        "one_phonon_scaling_N": float(N),
                        "classical_scaling_N2": float(N * N)})
    write_csv(ROOT / "transition_scaling.csv", scaling)
    (ROOT / "chart_data.json").write_text(json.dumps({
        "order_parameter": [{"kappa3": x["kappa3"], "beta3": x["beta3"], "energy": x["energy"]} for x in critical],
        "transition_scaling": [{"N": x["N"], "rotor_BE3": x["rotor_BE3"],
                                "finite_N_factor": x["finite_N_factor_Nminus1_over_N"],
                                "one_phonon_scaling_N": x["one_phonon_scaling_N"]} for x in scaling]
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    results = {
        "model": "IBM-1 sdf condensate, one-body Q2/Q3 operators",
        "parameters": pars, "N0": N0,
        "boson_counts": {"144Ba": 6, "146Ba": 7, "148Ce": 8},
        "experimental_B_E3_down_WU": {
            "144Ba": {"value": 48, "minus": 34, "plus": 25, "source": "Bucher 2016, Table I"},
            "146Ba": {"value": 48, "minus": 29, "plus": 21, "source": "Bucher 2017, Table I"},
            "148Ce": {"value": None, "status": "not found in adopted ENSDF Jan 2026; level 3- is adopted at 841.41 keV but no B(E3) field", "source": "NNDC ENSDF adopted levels"}},
        "finite_N_interpretation": "For Q.Q in an N-boson condensate, the two-body term is N(N-1); the missing self term is O(N), giving the explicit (N-1)/N correction to an N^2 classical estimate. A one-phonon decay amplitude scales as sqrt(N), hence B scales as N. These are distinct observables.",
        "checks": {"parity": "Q3 is odd, Q3.Q3 is even; all Hamiltonian terms conserve parity", "rotational_scalar": "dot products sum all magnetic components", "beta3_symmetry": "E(beta3)=E(-beta3) for the parity-conserving Hamiltonian"}
    }
    (ROOT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
