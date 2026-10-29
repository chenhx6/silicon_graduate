#!/usr/bin/env python3
"""Two-level avoided-crossing proxy for octupole collective inertia.

This is a dimensionless diagnostic model, not an EDF/ATDHFB calculation for a
particular nucleus.  It keeps the denominator structure of perturbative
cranking moments and adds a finite pairing/frequency response scale.  Outputs
are written next to this script and can be regenerated with only NumPy.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent
HBAR = 1.0


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def avoided_crossing(beta2: float, beta3: float, *, v: float = 0.015) -> tuple[float, float, np.ndarray]:
    """Return single-particle splitting, derivative coupling and q gradients."""
    # The crossing coordinate is tilted by beta2 so B23 is nonzero.
    x = beta3 - 0.105 + 0.25 * (beta2 - 0.20)
    a = 4.0  # MeV per dimensionless beta3 coordinate
    eps = float(np.sqrt((a * x) ** 2 + v**2))
    d_offdiag = a * v / eps
    gradients = np.array([0.25 * d_offdiag, d_offdiag])
    return eps, d_offdiag, gradients


def moments(gradients: np.ndarray, qp_energy: float, response_scale: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """M_-1, M_-2, M_-3 with a small transverse diagnostic regularizer."""
    denom = max(response_scale, 1.0e-10)
    outer = np.outer(gradients, gradients)
    # The diagonal term represents all omitted 2qp states in this two-level toy.
    transverse = 1.0e-4 * np.eye(2)
    return (
        outer / denom + transverse,
        outer / denom**2 + transverse,
        outer / denom**3 + transverse,
    )


def mass_tensors(beta2: float, beta3: float, *, delta: float, omega: float, v: float = 0.015) -> dict[str, float]:
    eps, _, gradients = avoided_crossing(beta2, beta3, v=v)
    qp = float(np.sqrt(eps**2 + delta**2))
    # Adiabatic IB uses (E_mu+E_nu)^3.  The finite-frequency proxy replaces
    # that scale by sqrt[(2E)^2 + (hbar*omega)^2].
    response = float(np.sqrt((2.0 * qp) ** 2 + (HBAR * omega) ** 2))
    m1, m2, m3 = moments(gradients, qp, response)
    inv_m1 = np.linalg.inv(m1)
    gcm = HBAR**2 * inv_m1 @ m2 @ inv_m1
    atdhfb = HBAR**2 * inv_m1 @ m3 @ inv_m1
    ib = HBAR**2 * np.outer(gradients, gradients) / response**3
    # A transparent Thouless-Valatin proxy: induced fields screen/enhance the
    # bare response.  This is not a QRPA solution and is marked as such.
    tv = 1.25 * atdhfb
    return {
        "B22_IB": float(ib[0, 0]),
        "B23_IB": float(ib[0, 1]),
        "B33_IB": float(ib[1, 1]),
        "B22_GCM": float(gcm[0, 0]),
        "B23_GCM": float(gcm[0, 1]),
        "B33_GCM": float(gcm[1, 1]),
        "B22_ATDHFB": float(atdhfb[0, 0]),
        "B23_ATDHFB": float(atdhfb[0, 1]),
        "B33_ATDHFB": float(atdhfb[1, 1]),
        "B22_TV_proxy": float(tv[0, 0]),
        "B23_TV_proxy": float(tv[0, 1]),
        "B33_TV_proxy": float(tv[1, 1]),
        "det_IB": float(np.linalg.det(ib)),
        "det_ATDHFB": float(np.linalg.det(atdhfb)),
        "qp_energy": qp,
        "response_scale": response,
    }


def potential(beta3: np.ndarray | float, beta2: float = 0.20) -> np.ndarray | float:
    """Symmetric beta3 double well used only for the period diagnostic."""
    q = np.asarray(beta3)
    q0 = 0.12 + 0.10 * (beta2 - 0.20)
    return 60.0 * (q**2 - q0**2) ** 2


def period_for_amplitude(amplitude: float, *, delta: float = 0.35, omega: float = 0.40) -> float:
    """Energy-conservation period in toy units for a cross-well orbit."""
    energy = float(potential(amplitude))
    q = np.linspace(-amplitude, amplitude, 20001)
    kinetic = np.maximum(energy - potential(q), 1.0e-10)
    b33 = np.array([mass_tensors(0.20, float(value), delta=delta, omega=omega)["B33_ATDHFB"] for value in q])
    integrand = np.sqrt(2.0 * b33 / kinetic)
    # The endpoint square-root singularity is integrable; clipping keeps the
    # diagnostic stable without pretending to resolve a turning-point layer.
    return float(2.0 * np.trapezoid(integrand[1:-1], q[1:-1]))


def main() -> None:
    beta2_values = np.linspace(0.10, 0.30, 41)
    beta3_values = np.linspace(-0.25, 0.25, 101)
    surface_rows: list[dict[str, float | str]] = []
    for beta2 in beta2_values:
        for beta3 in beta3_values:
            bare = mass_tensors(float(beta2), float(beta3), delta=0.0, omega=0.0)
            paired = mass_tensors(float(beta2), float(beta3), delta=0.80, omega=0.0)
            dynamic = mass_tensors(float(beta2), float(beta3), delta=0.35, omega=0.40)
            surface_rows.append({
                "beta2": float(beta2),
                "beta3": float(beta3),
                "B22_IB_bare": bare["B22_IB"], "B23_IB_bare": bare["B23_IB"], "B33_IB_bare": bare["B33_IB"],
                "B22_ATDHFB_paired": paired["B22_ATDHFB"], "B23_ATDHFB_paired": paired["B23_ATDHFB"], "B33_ATDHFB_paired": paired["B33_ATDHFB"],
                "B22_ATDHFB_dynamic": dynamic["B22_ATDHFB"], "B23_ATDHFB_dynamic": dynamic["B23_ATDHFB"], "B33_ATDHFB_dynamic": dynamic["B33_ATDHFB"],
                "B33_TV_proxy_dynamic": dynamic["B33_TV_proxy"],
                "det_dynamic": dynamic["det_ATDHFB"],
            })
    write_csv(OUT / "mass_surface.csv", surface_rows)

    curve_rows: list[dict[str, float | str]] = []
    for beta3 in beta3_values:
        bare = mass_tensors(0.20, float(beta3), delta=0.0, omega=0.0)
        paired = mass_tensors(0.20, float(beta3), delta=0.80, omega=0.0)
        dynamic = mass_tensors(0.20, float(beta3), delta=0.35, omega=0.40)
        curve_rows.append({
            "beta3": float(beta3),
            "B33_IB_bare": bare["B33_IB"],
            "B33_ATDHFB_paired": paired["B33_ATDHFB"],
            "B33_ATDHFB_dynamic": dynamic["B33_ATDHFB"],
            "B33_TV_proxy_dynamic": dynamic["B33_TV_proxy"],
            "qp_bare": bare["qp_energy"],
            "qp_paired": paired["qp_energy"],
        })
    write_csv(OUT / "mass_curves_beta3.csv", curve_rows)

    scaling_rows: list[dict[str, float | str]] = []
    for v in np.geomspace(1.0e-4, 0.10, 80):
        bare = mass_tensors(0.20, 0.105, delta=0.0, omega=0.0, v=float(v))
        paired = mass_tensors(0.20, 0.105, delta=0.80, omega=0.0, v=float(v))
        dynamic = mass_tensors(0.20, 0.105, delta=0.35, omega=0.40, v=float(v))
        scaling_rows.append({"coupling_V": float(v), "B33_bare": bare["B33_IB"], "B33_pairing": paired["B33_IB"], "B33_dynamic": dynamic["B33_IB"]})
    write_csv(OUT / "avoided_crossing_scaling.csv", scaling_rows)

    amplitudes = [0.18, 0.19, 0.20, 0.22, 0.24]
    period_rows = [{"beta3_amplitude": amp, "energy": float(potential(amp)), "period_dynamic": period_for_amplitude(amp)} for amp in amplitudes]
    write_csv(OUT / "large_amplitude_periods.csv", period_rows)

    summary = {
        "model": "two-level avoided crossing with beta2-beta3 tilted coordinate",
        "status": "illustrative_reduced_model_not_EDF_or_QRPA_fit",
        "warning": "dimensionless proxy; not a calibrated EDF, QRPA, or nucleus-specific ATDHFB calculation",
        "parameters": {"crossing_beta3": 0.105, "slope_a": 4.0, "coupling_V": 0.015, "pairing_gap": 0.80, "dynamic_pairing_floor": 0.35, "hbar_omega": 0.40, "tv_proxy_factor": 1.25},
        "formula_conventions": {"ib": "hbar^2 sum F_i* F_j/(E_mu+E_nu)^3", "gcm": "hbar^2 M_-1^-1 M_-2 M_-1^-1", "atdhfb": "hbar^2 M_-1^-1 M_-3 M_-1^-1", "dynamic": "[(2E)^2+(hbar omega)^2]^(1/2) response scale"},
        "outputs": ["mass_surface.csv", "mass_curves_beta3.csv", "avoided_crossing_scaling.csv", "large_amplitude_periods.csv"],
        "key_results": {
            "bare_crossing_growth_first_to_last": scaling_rows[0]["B33_bare"] / scaling_rows[-1]["B33_bare"],
            "paired_crossing_range": [scaling_rows[-1]["B33_pairing"], scaling_rows[0]["B33_pairing"]],
            "dynamic_crossing_range": [scaling_rows[-1]["B33_dynamic"], scaling_rows[0]["B33_dynamic"]],
            "periods": period_rows,
        },
        "checks": {"surface_rows": len(surface_rows), "curve_rows": len(curve_rows), "scaling_rows": len(scaling_rows), "period_rows": len(period_rows), "all_dynamic_determinants_positive": bool(all(row["det_dynamic"] > 0 for row in surface_rows))},
    }
    (OUT / "results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary["checks"], sort_keys=True))


if __name__ == "__main__":
    main()
