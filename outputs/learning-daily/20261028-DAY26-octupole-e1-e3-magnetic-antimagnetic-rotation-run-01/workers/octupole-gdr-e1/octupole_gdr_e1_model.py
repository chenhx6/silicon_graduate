#!/usr/bin/env python3
"""Phenomenological octupole/IVGDR response and E1 EWSR ledger.

This is a transparent toy response model, not a self-consistent QRPA/RPA
calculation.  It scans an axial beta3-induced two-level mixing of the usual
K=0 and K=1 IVGDR branches, applies the center-of-mass corrected intrinsic
dipole identity, and partitions the E1 TRK sum rule.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


HBAR2_OVER_2M = 20.73553  # MeV fm^2
E2 = 1.0  # e^2 is retained in the output units
KAPPA = 0.20
GAMMA_MEV = 3.8
R0_COEFF = 1.20

NUCLEI = {
    "144Ba": {"A": 144, "Z": 56, "beta2": 0.20, "beta3": 0.10, "skin_fm": 0.15},
    "146Ba": {"A": 146, "Z": 56, "beta2": 0.20, "beta3": 0.11, "skin_fm": 0.17},
    "224Ra": {"A": 224, "Z": 88, "beta2": 0.16, "beta3": 0.12, "skin_fm": 0.19},
    "226Th": {"A": 226, "Z": 90, "beta2": 0.18, "beta3": 0.11, "skin_fm": 0.20},
}


def gdr_centroid(A: int) -> float:
    """Standard empirical centroid proxy in MeV."""
    return 31.2 * A ** (-1.0 / 3.0) + 20.6 * A ** (-1.0 / 6.0)


def trk_ewsr(A: int, Z: int, kappa: float = KAPPA) -> float:
    """User-specified E1 TRK energy-weighted sum in MeV e^2 fm^2."""
    N = A - Z
    return (9.0 / (4.0 * math.pi)) * HBAR2_OVER_2M * E2 * (N * Z / A) * (1.0 + kappa)


def intrinsic_dipole(A: int, Z: int, beta3: float, skin_fm: float) -> tuple[float, float]:
    """Return (delta_z, D0) using a labelled phenomenological displacement.

    The identity D0=e*N*Z/A*(<z_p>-<z_n>) is exact.  The delta_z closure
    below is only a scale-setting ansatz for sensitivity scans.
    """
    N = A - Z
    neutron_excess = (N - Z) / A
    # 0.018 fm is an illustrative scale chosen to keep the induced D0 in the
    # sub-e fm range; it is not fitted to a measured Ba/Ra displacement.
    delta_z = 0.018 * beta3 * (1.0 + 2.0 * neutron_excess) * (1.0 + 0.5 * skin_fm / 0.20)
    return delta_z, (N * Z / A) * delta_z


def split_branch(E0: float, beta2: float, beta3: float, K: int) -> tuple[float, float, float, float]:
    """Return unmixed energy, lower/upper energies, and lower-state weight.

    beta2 creates the conventional K=0/K=1 deformation splitting.  beta3
    mixes each branch with an opposite-parity doorway.  The labels after
    mixing are response components, not exact laboratory parities.
    """
    if K == 0:
        E_base = E0 * (1.0 - 0.55 * beta2)
    else:
        E_base = E0 * (1.0 + 0.275 * beta2)
    coupling = E0 * beta3 * (0.35 + 0.15 * ((K + 1) / 2.0))
    half_gap = 0.5 * E0 * beta3 * 0.25
    separation = math.sqrt(half_gap * half_gap + coupling * coupling)
    lower = E_base - separation
    upper = E_base + separation
    lower_weight = 0.5 * (1.0 + half_gap / separation) if separation else 0.5
    return E_base, lower, upper, lower_weight


def lorentzian(E: float, center: float, gamma: float = GAMMA_MEV) -> float:
    half = 0.5 * gamma
    return half / (math.pi * ((E - center) ** 2 + half * half))


def response_points(A: int, Z: int, beta2: float, beta3: float, n_points: int = 181) -> list[dict]:
    """Return a normalized E1 response curve from 6 to 24 MeV."""
    E0 = gdr_centroid(A)
    branches = []
    for K in (0, 1):
        _, low, high, low_w = split_branch(E0, beta2, beta3, K)
        branch_weight = 0.5
        branches.extend(((low, branch_weight * low_w), (high, branch_weight * (1.0 - low_w))))
    values = []
    for i in range(n_points):
        E = 6.0 + 18.0 * i / (n_points - 1)
        strength = sum(weight * lorentzian(E, center) for center, weight in branches)
        values.append({"energy_MeV": round(E, 6), "relative_strength": strength})
    return values


def scan_rows(name: str, cfg: dict) -> list[dict]:
    A, Z = cfg["A"], cfg["Z"]
    E0 = gdr_centroid(A)
    rows = []
    for i in range(11):
        beta3 = 0.02 * i
        delta_z, D0 = intrinsic_dipole(A, Z, beta3, cfg["skin_fm"])
        peaks = {}
        for K in (0, 1):
            E_base, low, high, low_w = split_branch(E0, cfg["beta2"], beta3, K)
            peaks[f"K{K}_base_MeV"] = E_base
            peaks[f"K{K}_low_MeV"] = low
            peaks[f"K{K}_high_MeV"] = high
            peaks[f"K{K}_low_weight"] = low_w
        rows.append(
            {
                "nucleus": name,
                "A": A,
                "Z": Z,
                "N": A - Z,
                "beta2": cfg["beta2"],
                "beta3": beta3,
                "E_GDR_centroid_MeV": E0,
                "K0_K1_base_splitting_MeV": peaks["K1_base_MeV"] - peaks["K0_base_MeV"],
                "octupole_lowest_peak_MeV": min(peaks["K0_low_MeV"], peaks["K1_low_MeV"]),
                "octupole_highest_peak_MeV": max(peaks["K0_high_MeV"], peaks["K1_high_MeV"]),
                "delta_z_fm": delta_z,
                "D0_efm": D0,
                **peaks,
            }
        )
    return rows


def ewsr_rows() -> list[dict]:
    """Partition the E1 EWSR and expose the measured-like 146Ba example."""
    rows = []
    for name, cfg in NUCLEI.items():
        A, Z = cfg["A"], cfg["Z"]
        S = trk_ewsr(A, Z)
        E_low = 1.05 if name == "146Ba" else 1.0
        # Bucher 2017 Table I: 0.000223 eb^(1/2), converted to e^2 fm^2.
        measured_like_B = 0.000223**2 * 100.0 if name == "146Ba" else None
        measured_share = E_low * measured_like_B / S if measured_like_B is not None else None
        for requested_share in (0.001, 0.003, 0.010):
            B_required = requested_share * S / E_low
            # Axial K=0 rotor convention: B(E1;0->1)=3/(4*pi)*D0^2.
            D0_equivalent = math.sqrt((4.0 * math.pi / 3.0) * B_required)
            rows.append(
                {
                    "nucleus": name,
                    "A": A,
                    "Z": Z,
                    "N": A - Z,
                    "kappa": KAPPA,
                    "S_TRK_MeV_e2fm2": S,
                    "E_low_MeV": E_low,
                    "requested_low_fraction": requested_share,
                    "B_low_required_e2fm2": B_required,
                    "D0_equivalent_efm_K0_rotor": D0_equivalent,
                    "146Ba_table_amplitude_B_e2fm2": measured_like_B,
                    "146Ba_table_amplitude_fraction": measured_share,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    out = Path(__file__).resolve().parent
    all_rows = []
    curves = {}
    for name, cfg in NUCLEI.items():
        rows = scan_rows(name, cfg)
        all_rows.extend(rows)
        curves[name] = response_points(cfg["A"], cfg["Z"], cfg["beta2"], cfg["beta3"])
    ew_rows = ewsr_rows()
    write_csv(out / "gdr_splitting_scan.csv", all_rows)
    write_csv(out / "e1_ewsr_partition.csv", ew_rows)
    (out / "response_curve.csv").write_text(
        "nucleus,energy_MeV,relative_strength\n"
        + "\n".join(
            f"{name},{point['energy_MeV']},{point['relative_strength']}"
            for name, points in curves.items()
            for point in points
        )
        + "\n",
        encoding="utf-8",
    )
    result = {
        "schema": "octupole-gdr-e1-ewsr/v1",
        "status": "phenomenological_scan_provisional",
        "model_scope": [
            "axial K=0/K=1 IVGDR branches",
            "beta3-induced two-level doorway mixing",
            "center-of-mass corrected intrinsic E1 identity",
            "user-specified E1 TRK EWSR with kappa=0.20",
        ],
        "not_claimed": [
            "not a self-consistent QRPA/RPA calculation",
            "not a measurement of beta3 or GDR splitting in any listed nucleus",
            "no experimental proof of a common-final-state IVGDR interference phase",
        ],
        "constants": {
            "hbar2_over_2m_MeV_fm2": HBAR2_OVER_2M,
            "kappa": KAPPA,
            "gamma_MeV": GAMMA_MEV,
        },
        "nuclei": NUCLEI,
        "gdr_scan": all_rows,
        "e1_ewsr_partition": ew_rows,
        "response_curves": curves,
        "equations": {
            "intrinsic_dipole": "D0 = e*N*Z/A*(<z_p>-<z_n>)",
            "trk": "S(E1)=(9/(4*pi))*(hbar^2*e^2/(2m))*(N*Z/A)*(1+kappa)",
            "mixing": "E_+-E_- = 2*sqrt((Delta/2)^2+g3^2), g3 proportional to beta3",
            "low_energy_fraction": "f_low = E_low*B(E1;low)/S_TRK",
        },
        "source_boundary": [
            "Butler-Nazarewicz 1996, RMP 68, Secs. II-III and IV-VII: E1 is isovector/cancellation-sensitive; E3 is more collective; static and soft octupole cases differ.",
            "Bucher 2016/2017: direct Ba E3 remains strong while E1 varies; SCCM assigns variation to occupancy/cancellation.",
            "The IVGDR mixing scan is an explicit testable hypothesis, not a source-reported Ba/Ra calculation.",
        ],
    }
    (out / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
