#!/usr/bin/env python3
"""Reduced beta3-beta4-beta5 coupling model.

This is a transparent sensitivity model, not an EDF calculation.  It keeps
the parity-allowed terms requested in the study brief and reports the change
when those terms are switched on.  All energies are MeV and deformation
coordinates are dimensionless.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def newton_shape(beta2: float, beta3: float, coupling: bool) -> tuple[float, float, float]:
    """Minimize the beta4/beta5 sector by damped Newton iteration."""
    c234 = -250.0 if coupling else 0.0
    c345 = -42.0 if coupling else 0.0
    c4, u4, c5, u5 = 100.0, 500.0, 70.0, 420.0
    b4 = b5 = 0.0
    for _ in range(80):
        f4 = c4 * b4 + u4 * b4**3 + c234 * beta2 * beta3**2 + c345 * beta3 * b5
        f5 = c5 * b5 + u5 * b5**3 + c345 * beta3 * b4
        h44 = c4 + 3.0 * u4 * b4**2
        h55 = c5 + 3.0 * u5 * b5**2
        h45 = c345 * beta3
        det = h44 * h55 - h45 * h45
        if det <= 0.0:
            break
        d4 = (h55 * f4 - h45 * f5) / det
        d5 = (-h45 * f4 + h44 * f5) / det
        scale = 1.0
        while scale > 1e-5:
            n4, n5 = b4 - scale * d4, b5 - scale * d5
            if abs(n4) < 1.0 and abs(n5) < 1.0:
                b4, b5 = n4, n5
                break
            scale *= 0.5
        if max(abs(d4), abs(d5)) * scale < 1e-11:
            break
    e = 0.5 * c4 * b4**2 + 0.25 * u4 * b4**4
    e += 0.5 * c5 * b5**2 + 0.25 * u5 * b5**4
    e += c234 * beta2 * beta3**2 * b4 + c345 * beta3 * b4 * b5
    return b4, b5, e


def fission_base(q: float) -> float:
    """A two-hump reference path used only to expose coupling sensitivity."""
    first = 10.0 * math.exp(-((q - 0.30) / 0.16) ** 2)
    second = 8.0 * math.exp(-((q - 0.70) / 0.17) ** 2)
    return first + second + 0.35 * q


def fission_path() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for i in range(401):
        q = i / 400.0
        beta2 = 0.24 + 1.16 * q
        beta3 = 0.32 * math.sin(math.pi * q)
        beta5 = 0.07 * math.sin(2.0 * math.pi * q)
        b40, b50, e0 = newton_shape(beta2, beta3, False)
        b4, b5, ec = newton_shape(beta2, beta3, True)
        # beta5_path is a diagnostic coordinate; the local minimizer is the
        # model's beta5 response and is intentionally reported separately.
        rows.append(
            {
                "q": q,
                "beta2": beta2,
                "beta3": beta3,
                "beta5_external": beta5,
                "V_no_coupling": fission_base(q) + e0,
                "V_coupled": fission_base(q) + ec,
                "beta4_no_coupling": b40,
                "beta5_no_coupling": b50,
                "beta4_coupled": b4,
                "beta5_coupled": b5,
                "delta_V": ec - e0,
            }
        )
    return rows


def barrier(rows: list[dict[str, float]], key: str, lo: float, hi: float) -> tuple[float, float]:
    subset = [r for r in rows if lo <= r["q"] <= hi]
    row = max(subset, key=lambda r: r[key])
    return row["q"], row[key]


def parity_effective(beta2: float, a3: float, coupling: bool) -> tuple[float, float, float, float, float]:
    """Return quartic coefficient, minimum, barrier, action and splitting.

    The beta4 coordinate is integrated out at local static order.  With
    beta5=0 this gives u_eff = u3 - 2*C234^2*beta2^2/C4.  This algebra makes
    the sign and the validity boundary explicit.
    """
    c234 = -20.0 if coupling else 0.0
    c4, u3, d3 = 40.0, 10.0, 10.0
    ueff = u3 - 2.0 * c234**2 * beta2**2 / c4
    if ueff <= 0.0:
        raise ValueError("quartic coefficient became non-positive")

    # Solve a3 + ueff*x^2 + .75*d3*x^4 = 0 for x^2.
    disc = ueff * ueff - 3.0 * d3 * a3
    y = (-ueff + math.sqrt(disc)) / (1.5 * d3) if a3 < 0 else 0.0
    x0 = math.sqrt(max(y, 0.0))

    def potential(x: float) -> float:
        return 0.5 * a3 * x * x + 0.25 * ueff * x**4 + d3 * x**6 / 6.0

    emin = potential(x0)
    barrier_height = max(0.0, potential(0.0) - emin)
    # Instanton action at the bottom of the well.  The mass is dimensionless
    # here; its role is to expose sensitivity to the inertia prescription.
    mass = 38.0
    n = 4000
    h = x0 / n if x0 else 0.0
    integral = 0.0
    for j in range(n + 1):
        x = j * h
        val = max(0.0, potential(x) - emin)
        weight = 1.0 if j in (0, n) else (4.0 if j % 2 else 2.0)
        integral += weight * math.sqrt(val)
    integral *= h / 3.0
    action = 2.0 * math.sqrt(2.0 * mass) * integral
    prefactor = math.sqrt(max(abs(a3), 1e-12) / mass) / math.pi
    splitting = prefactor * math.exp(-action)
    return ueff, x0, barrier_height, action, splitting


def parity_table() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for n in range(130, 143, 2):
        # A deliberately non-monotone stiffness profile, representing the
        # isotope-dependent single-particle/pairing input that an EDF would
        # determine rather than a fitted experimental law.
        beta2 = 0.22 + 0.045 * math.exp(-((n - 136.0) / 3.7) ** 2)
        a3 = -1.15 + 0.030 * (n - 136.0) ** 2
        base = parity_effective(beta2, a3, False)
        coup = parity_effective(beta2, a3, True)
        rows.append(
            {
                "N": n,
                "beta2_input": beta2,
                "a3_input": a3,
                "u3_eff_no_coupling": base[0],
                "u3_eff_coupled": coup[0],
                "x0_no_coupling": base[1],
                "x0_coupled": coup[1],
                "barrier_no_coupling_MeV": base[2],
                "barrier_coupled_MeV": coup[2],
                "action_no_coupling": base[3],
                "action_coupled": coup[3],
                "splitting_no_coupling_arb": base[4],
                "splitting_coupled_arb": coup[4],
                "splitting_ratio_coupled_over_base": coup[4] / base[4] if base[4] else 0.0,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    fission = fission_path()
    parity = parity_table()
    q1, v1 = barrier(fission, "V_no_coupling", 0.10, 0.50)
    q2, v2 = barrier(fission, "V_coupled", 0.10, 0.50)
    q3, v3 = barrier(fission, "V_no_coupling", 0.52, 0.90)
    q4, v4 = barrier(fission, "V_coupled", 0.52, 0.90)
    summary = {
        "model": "parity-allowed beta2-beta3-beta4-beta5 Landau sensitivity model",
        "status": "illustrative_reduced_model_not_EDF_fit",
        "equations": {
            "coupling": "E_c = C234*beta2*beta3^2*beta4 + C345*beta3*beta4*beta5",
            "reflection_rule": "beta3,beta5 -> -beta3,-beta5; beta2,beta4 -> unchanged",
            "integrated_out_beta4": "u3_eff = u3 - 2*C234^2*beta2^2/C4 (when beta5=0)",
        },
        "coefficients": {"fission_C234": -250.0, "fission_C345": -42.0, "parity_C234": -20.0},
        "fission_barriers": {
            "first_no_coupling": {"q": q1, "MeV": v1},
            "first_coupled": {"q": q2, "MeV": v2},
            "first_delta_coupled_minus_base_MeV": v2 - v1,
            "second_no_coupling": {"q": q3, "MeV": v3},
            "second_coupled": {"q": q4, "MeV": v4},
            "second_delta_coupled_minus_base_MeV": v4 - v3,
        },
        "parity_scope": "dimensionless WKB sensitivity; splitting is not a fitted Ra/Th level energy",
        "parity_rows": len(parity),
        "source_locators": [
            "Warda et al., Phys. Rev. C 66, 014310 (2002), arXiv:nucl-th/0203057, PDF pp.4,7-13",
            "Giuliani et al., Phys. Rev. C 97, 034323 (2018), arXiv:1704.00554, PDF pp.1,3-11",
            "Butler et al., Phys. Rev. Lett. 124, 042503 (2020), PDF pp.3-5, Table I and Fig.4",
            "Nomura et al., Phys. Rev. C 102, 064326 (2020), arXiv:2008.08870, PDF pp.2-4, Fig.1",
            "Butler and Nazarewicz, Rev. Mod. Phys. 68, 349 (1996), PDF Secs. II-III and IV-VII",
        ],
    }
    write_csv(HERE / "fission_path.csv", fission)
    write_csv(HERE / "parity_doublet_wkb.csv", parity)
    (HERE / "results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
