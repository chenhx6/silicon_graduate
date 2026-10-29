#!/usr/bin/env python3
"""Toy K-mixing and electromagnetic-decay scan for actinide isomers.

This is a transparent particle-rotor sensitivity model, not an EDF or a
global fit.  An axial beta3*Y30 field breaks reflection symmetry while
preserving K.  K mixing is therefore controlled separately by eps_K, which
stands for Coriolis, triaxial (mu != 0), or octupole-phonon couplings.

The script diagonalizes a finite K basis, evaluates normalized E1/E2/M1/E3
transition strengths, rates using standard practical radiation constants, and
the K-forbidden hindrance factor.  It writes CSV and JSON artifacts beside
this file and does not require repository-local input data.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
K_BASIS = np.arange(0, 9, dtype=float)
E_K = 0.60 * K_BASIS + 0.018 * K_BASIS**2  # MeV, schematic intrinsic spacing
KI = 8.0
KF = 0.0
L_BY_MULTIPOLE = {1: "E1", 2: "E2", 3: "E3"}


def hamiltonian(beta3: float, eps_k: float) -> np.ndarray:
    """Return K-basis Hamiltonian.

    eps_k is a dimensionless transverse-mixing scale.  Adjacent and
    Delta-K=3 terms mimic different microscopic routes to K admixtures.
    The beta3=0 limit is exactly K diagonal.
    """
    h = np.diag(E_K.copy())
    v1 = 0.22 * beta3 * eps_k
    v3 = 0.38 * beta3 * eps_k
    for i in range(len(K_BASIS)):
        for j in (i + 1, i + 3):
            if j < len(K_BASIS):
                v = v1 if j - i == 1 else v3
                h[i, j] = h[j, i] = v
    return h


def eigenstate(beta3: float, eps_k: float) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(hamiltonian(beta3, eps_k))
    # The isomer is the eigenstate with maximum K=8 character; final state is
    # the lowest state with maximum K=0 character.  This avoids level-label
    # jumps during the scan.
    i_iso = int(np.argmax(vectors[-1, :] ** 2))
    i_fin = int(np.argmax(vectors[0, :] ** 2))
    return values, np.column_stack((vectors[:, i_iso], vectors[:, i_fin]))


def intrinsic_amplitude(ci: np.ndarray, cf: np.ndarray, multipole: int) -> float:
    """Normalized intrinsic amplitude with |Delta K| <= L selection rule."""
    amp = 0.0
    for ki, ai in zip(K_BASIS, ci):
        for kf, af in zip(K_BASIS, cf):
            if abs(ki - kf) <= multipole:
                # A smooth angular factor retains the selection rule without
                # pretending this toy basis is a complete rotor calculation.
                angular = math.sqrt(max(0.0, 1.0 - (ki - kf) ** 2 / (multipole + 1) ** 2))
                amp += ai * af * angular
    return float(amp)


def wu_strength(a: float, multipole: int) -> float:
    """Weisskopf unit in e^2 fm^(2L), using a=1.2 A^(1/3) fm."""
    radius = 1.2 * a ** (1.0 / 3.0)
    # Standard single-particle scale; the precise coefficient is a convention
    # and is retained in metadata rather than treated as an experimental input.
    return {
        1: 0.0645 * a ** (2.0 / 3.0),
        2: 0.0594 * a ** (4.0 / 3.0),
        3: 0.0594 * a**2 * radius**2,
    }[multipole]


def rate(multipole: int, egamma_mev: float, b_wu: float, a: float) -> float:
    constants = {1: 1.59e15, 2: 1.22e9, 3: 5.70e2}
    return constants[multipole] * egamma_mev ** (2 * multipole + 1) * b_wu * wu_strength(a, multipole)


def scan() -> tuple[list[dict[str, float | None]], dict[str, object]]:
    rows: list[dict[str, float | None]] = []
    a = 225.0
    # Use a fixed transition energy for sensitivity only.  It is near the
    # evaluated 31.50-keV 225Ra E1 line but is not fitted to that line.
    egamma = 0.0315
    for eps_k in (0.00, 0.15, 0.30, 0.50):
        for beta3 in np.linspace(0.0, 0.20, 21):
            values, states = eigenstate(float(beta3), eps_k)
            ci, cf = states[:, 0], states[:, 1]
            row: dict[str, float | None] = {
                "beta3": float(beta3),
                "eps_K": float(eps_k),
                "isomer_energy_MeV": float(np.dot(ci * ci, values)),
                "K8_probability": float(ci[-1] ** 2),
                "K2_probability": float(ci[2] ** 2),
                "K0_probability": float(ci[0] ** 2),
            }
            for multipole in (1, 2, 3):
                amp = intrinsic_amplitude(ci, cf, multipole)
                b_rel = amp * amp
                b_wu = b_rel  # normalized to one W.u. at unit amplitude
                t_half_w = math.log(2.0) / rate(multipole, egamma, 1.0, a)
                t_half = math.log(2.0) / rate(multipole, egamma, b_wu, a) if b_wu > 0 else math.inf
                nu = max(1.0, KI - KF - multipole)
                hindrance = t_half / t_half_w if math.isfinite(t_half) else math.inf
                fnu = hindrance ** (1.0 / nu) if math.isfinite(hindrance) else math.inf
                prefix = L_BY_MULTIPOLE[multipole]
                row[f"{prefix}_amplitude"] = amp
                row[f"{prefix}_B_relative_WU"] = b_wu
                row[f"{prefix}_rate_s-1"] = rate(multipole, egamma, b_wu, a)
                row[f"{prefix}_half_life_s"] = t_half if math.isfinite(t_half) else None
                row[f"{prefix}_hindrance"] = hindrance if math.isfinite(hindrance) else None
                row[f"{prefix}_f_nu"] = fnu if math.isfinite(fnu) else None
                row[f"{prefix}_nu"] = nu
            # M1 is reported in the same normalized amplitude convention with
            # the practical M1 coefficient; its W.u. scale is one mu_N^2.
            m1_amp = intrinsic_amplitude(ci, cf, 1)
            m1_b = m1_amp * m1_amp
            m1_rate = 1.76e13 * egamma**3 * m1_b
            row["M1_amplitude"] = m1_amp
            row["M1_B_relative_WU"] = m1_b
            row["M1_rate_s-1"] = m1_rate
            row["M1_half_life_s"] = math.log(2.0) / m1_rate if m1_rate > 0 else None
            rows.append(row)
    summary = {
        "model": "finite K-basis particle-rotor sensitivity scan",
        "status": "illustrative_reduced_model_not_EDF_fit",
        "basis_K": K_BASIS.tolist(),
        "equations": {
            "wavefunction": "|Psi> = sum_K C_K |I M K>",
            "hamiltonian": "H_KK'=E_K delta_KK' + beta3*epsK*(V1 delta_|dK|,1 + V3 delta_|dK|,3)",
            "selection": "intrinsic amplitude includes only |K_i-K_f| <= L",
            "rate": "lambda(EL)=c_L E_gamma^(2L+1) B(EL)",
            "hindrance": "f_nu=(T_1/2/T_W)^(1/nu), nu=max(1,DeltaK-L)",
        },
        "constants": {"E1": "1.59e15", "M1": "1.76e13", "E2": "1.22e9", "E3": "5.70e2", "rate_units": "s^-1, E_gamma in MeV"},
        "physical_boundary": "axial beta3 Y30 preserves K; eps_K is required for K mixing and represents Coriolis/triaxial/mu!=0 phonon coupling",
        "reference_transition": {"nucleus": "225Ra", "E_gamma_keV": 31.50, "evaluated_B_E1_WU": 0.00081, "source": "knowledge/sources/nndc-2009-ra225-adopted-parity-doublet.md", "comparison_status": "reference only; toy B values are not a refit and omit internal conversion"},
        "isomer_examples": {"229Th": "current ENSDF adopted scheme has 5/2+ ground state and 3/2+ isomer at 8.355733554 eV; same parity, not an octupole parity doublet", "234U": "6- K=6 bandhead at 1421.275(45) keV with T1/2=33.5(20) microseconds in current adopted scheme", "178Hf": "K=8 ~4 s and K=16 ~31 y review examples"},
        "rows": len(rows),
    }
    return rows, summary


def main() -> None:
    rows, summary = scan()
    csv_path = HERE / "k_mixing_scan.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (HERE / "results.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    chart = {
        "beta3": sorted({r["beta3"] for r in rows}),
        "series": [
            {"eps_K": eps, "beta3": [r["beta3"] for r in rows if r["eps_K"] == eps], "E2_f_nu": [r["E2_f_nu"] for r in rows if r["eps_K"] == eps], "E1_f_nu": [r["E1_f_nu"] for r in rows if r["eps_K"] == eps]}
            for eps in (0.00, 0.15, 0.30, 0.50)
        ],
    }
    (HERE / "chart_data.json").write_text(json.dumps(chart, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
