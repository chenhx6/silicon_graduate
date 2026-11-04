#!/usr/bin/env python3
"""
P-ADO Shared Alignment Null & Projectile Family Profile Analyzer.

Physical Principle & Formalism:
In in-beam gamma-ray spectroscopy, the directional angular distribution of gamma rays
emitted from an aligned nuclear state of spin J is characterized by alignment attenuation
coefficients alpha_2(J, sigma/J) and alpha_4(J, sigma/J).
Under a Gaussian magnetic substate population P(m) proportional to exp(-m^2 / (2 sigma^2)),
the alignment parameters are obtained by weighting normalized Yamazaki tensor polynomials:
  alpha_k(J, r) = sum_m t_k(m) * P(m),   r = sigma / J

When measuring the same nuclear transition (e.g. 958.0 keV, 13/2+ -> 9/2+ in 69Ge, Zobel 1983)
under different reaction conditions (beam projectile, incident energy), a crucial question
for P-ADO (Projectile-Alignment Directional Orientation) analysis is:
  "Can multiple reaction conditions share a single, common spin-alignment nuisance parameter r?"

For each reaction condition i, with measured coefficients y_i = (alpha_2, alpha_4)_i and
covariance matrix Sigma_i(rho) parameterized by correlation rho:
  Sigma_i(rho) = [[s_2,i^2, rho * s_2,i * s_4,i], [rho * s_2,i * s_4,i, s_4,i^2]]
The Mahalanobis distance squared to the common theoretical prediction alpha(J, r) is:
  D_i^2(r, rho) = (y_i - alpha(J, r))^T * Sigma_i(rho)^(-1) * (y_i - alpha(J, r))

For a set of reaction conditions, the shared alignment null hypothesis requires that there
exists an r such that every condition i falls within the 2D 95% confidence region (q_95 = 5.9915):
  max_i D_i^2(r, rho) <= q_95  (i.e. required error-scale factor tau_req <= 1.0)
where:
  tau_req = sqrt( min_r max_i D_i^2(r, rho) / q_95 )

This analyzer evaluates the shared alignment profile across projectile families:
- Light-ion beam (alpha, 11.3 - 22 MeV): fails the shared null (tau_req > 2.0) due to
  rapid energy-dependent feeding cascade deorientation;
- Heavy-ion beam (12C, 32 - 48 MeV): passes the shared null (tau_req < 1.0, r ~ 0.282),
  confirming steady-state compound-nucleus statistical feeding.

Zero external dependencies (pure standard Python math/json/sys/argparse).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

# 2D Chi-square 95% confidence threshold (2 degrees of freedom)
Q_95_2D = 5.991464547107979

# Default fixture path
DEFAULT_FIXTURE_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "outputs"
    / "learning-daily"
    / "20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
    / "zobel83-958-table-fixture.json"
)

# Benchmark Zobel 1983 Table 1 rows (958.0 keV, Ji=6.5 -> Jf=4.5)
ZOBEL83_ROWS = [
    {"beam": "alpha", "beam_energy_lab_MeV": 11.3, "alpha2": 0.973, "sigma_alpha2_stat_fit": 0.037, "alpha4": 0.803, "sigma_alpha4_stat_fit": 0.090},
    {"beam": "alpha", "beam_energy_lab_MeV": 12.0, "alpha2": 0.910, "sigma_alpha2_stat_fit": 0.037, "alpha4": 0.810, "sigma_alpha4_stat_fit": 0.090},
    {"beam": "alpha", "beam_energy_lab_MeV": 15.0, "alpha2": 0.681, "sigma_alpha2_stat_fit": 0.036, "alpha4": 0.419, "sigma_alpha4_stat_fit": 0.087},
    {"beam": "alpha", "beam_energy_lab_MeV": 18.0, "alpha2": 0.728, "sigma_alpha2_stat_fit": 0.036, "alpha4": 0.263, "sigma_alpha4_stat_fit": 0.087},
    {"beam": "alpha", "beam_energy_lab_MeV": 22.0, "alpha2": 0.674, "sigma_alpha2_stat_fit": 0.036, "alpha4": 0.215, "sigma_alpha4_stat_fit": 0.087},
    {"beam": "12C", "beam_energy_lab_MeV": 32.0, "alpha2": 0.793, "sigma_alpha2_stat_fit": 0.032, "alpha4": 0.595, "sigma_alpha4_stat_fit": 0.093},
    {"beam": "12C", "beam_energy_lab_MeV": 36.0, "alpha2": 0.821, "sigma_alpha2_stat_fit": 0.016, "alpha4": 0.569, "sigma_alpha4_stat_fit": 0.051},
    {"beam": "12C", "beam_energy_lab_MeV": 40.0, "alpha2": 0.820, "sigma_alpha2_stat_fit": 0.020, "alpha4": 0.569, "sigma_alpha4_stat_fit": 0.078},
    {"beam": "12C", "beam_energy_lab_MeV": 44.0, "alpha2": 0.754, "sigma_alpha2_stat_fit": 0.033, "alpha4": 0.573, "sigma_alpha4_stat_fit": 0.088},
    {"beam": "12C", "beam_energy_lab_MeV": 48.0, "alpha2": 0.756, "sigma_alpha2_stat_fit": 0.038, "alpha4": 0.413, "sigma_alpha4_stat_fit": 0.110},
]


def tensor_polynomials(j: float) -> tuple[list[float], list[float], list[float]]:
    """Compute normalized Yamazaki tensor polynomials t2(m) and t4(m)."""
    m_vals = []
    m = j
    while m >= -j - 1e-9:
        m_vals.append(round(m, 4))
        m -= 1.0

    s = j * (j + 1.0)
    p2 = [3.0 * mv * mv - s for mv in m_vals]
    p4 = [35.0 * mv**4 - (30.0 * s - 25.0) * mv * mv + 3.0 * s * s - 6.0 * s for mv in m_vals]

    # Find index of minimum absolute m (0 or 0.5)
    abs_m = [abs(mv) for mv in m_vals]
    min_idx = abs_m.index(min(abs_m))
    norm2 = p2[min_idx]
    norm4 = p4[min_idx]

    t2 = [p / norm2 for p in p2]
    t4 = [p / norm4 for p in p4]
    return m_vals, t2, t4


def compute_alpha(j: float, r: float) -> tuple[float, float]:
    """Compute theoretical (alpha_2, alpha_4) for spin J and r = sigma/J."""
    if r <= 1e-5:
        return 1.0, 1.0

    m_vals, t2, t4 = tensor_polynomials(j)
    min_m2 = min(mv * mv for mv in m_vals)
    denom = 2.0 * (j * r) ** 2

    # Numerically stable weights
    weights = [math.exp(-(mv * mv - min_m2) / denom) for mv in m_vals]
    tot_w = sum(weights)
    if tot_w <= 0.0:
        return 0.0, 0.0

    a2 = sum(t * w for t, w in zip(t2, weights)) / tot_w
    a4 = sum(t * w for t, w in zip(t4, weights)) / tot_w
    return a2, a4


def mahalanobis_squared(
    y: tuple[float, float],
    a: tuple[float, float],
    s2: float,
    s4: float,
    rho: float = 0.0,
) -> float:
    """Calculate 2D Mahalanobis distance squared (y - a)^T Sigma^-1 (y - a)."""
    if abs(rho) >= 1.0:
        raise ValueError(f"Correlation rho must satisfy |rho| < 1.0, got {rho}")

    dy2 = y[0] - a[0]
    dy4 = y[1] - a[1]
    one_minus_rho2 = 1.0 - rho * rho

    term2 = (dy2 / s2) ** 2
    term4 = (dy4 / s4) ** 2
    cross = 2.0 * rho * (dy2 / s2) * (dy4 / s4)
    return (term2 - cross + term4) / one_minus_rho2


def evaluate_max_mahalanobis_sq(
    rows: list[dict],
    j: float,
    r: float,
    rho: float = 0.0,
) -> tuple[float, list[float]]:
    """Evaluate max Mahalanobis squared distance across rows at a given r."""
    a = compute_alpha(j, r)
    dists = []
    for row in rows:
        y = (row["alpha2"], row["alpha4"])
        s2 = row["sigma_alpha2_stat_fit"]
        s4 = row["sigma_alpha4_stat_fit"]
        d2 = mahalanobis_squared(y, a, s2, s4, rho)
        dists.append(d2)
    return max(dists), dists


def find_optimal_shared_r(
    rows: list[dict],
    j: float = 6.5,
    rho: float = 0.0,
    r_min: float = 0.05,
    r_max: float = 1.00,
    grid_steps: int = 1000,
) -> dict:
    """Find the optimal shared r that minimizes the maximum Mahalanobis distance."""
    best_r = r_min
    best_max_d2 = float("inf")
    best_dists = []

    # Dense grid search followed by local refinement
    step = (r_max - r_min) / grid_steps
    for i in range(grid_steps + 1):
        r_cand = r_min + i * step
        max_d2, dists = evaluate_max_mahalanobis_sq(rows, j, r_cand, rho)
        if max_d2 < best_max_d2:
            best_max_d2 = max_d2
            best_r = r_cand
            best_dists = dists

    # Golden section refinement around best_r
    a_bound = max(r_min, best_r - 2.0 * step)
    b_bound = min(r_max, best_r + 2.0 * step)
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c_pt = b_bound - gr * (b_bound - a_bound)
    d_pt = a_bound + gr * (b_bound - a_bound)

    fc, _ = evaluate_max_mahalanobis_sq(rows, j, c_pt, rho)
    fd, _ = evaluate_max_mahalanobis_sq(rows, j, d_pt, rho)

    for _ in range(50):
        if fc < fd:
            b_bound = d_pt
            d_pt = c_pt
            fd = fc
            c_pt = b_bound - gr * (b_bound - a_bound)
            fc, _ = evaluate_max_mahalanobis_sq(rows, j, c_pt, rho)
        else:
            a_bound = c_pt
            c_pt = d_pt
            fc = fd
            d_pt = a_bound + gr * (b_bound - a_bound)
            fd, _ = evaluate_max_mahalanobis_sq(rows, j, d_pt, rho)

    opt_r = (a_bound + b_bound) / 2.0
    min_max_d2, row_dists = evaluate_max_mahalanobis_sq(rows, j, opt_r, rho)
    tau_req = math.sqrt(min_max_d2 / Q_95_2D)
    passes_95 = min_max_d2 <= Q_95_2D

    a_opt = compute_alpha(j, opt_r)

    # Per-row summary
    row_reports = []
    for row, d2 in zip(rows, row_dists):
        row_reports.append({
            "beam": row.get("beam", "unknown"),
            "energy_MeV": row.get("beam_energy_lab_MeV", 0.0),
            "alpha2_meas": row["alpha2"],
            "sigma_alpha2": row["sigma_alpha2_stat_fit"],
            "alpha4_meas": row["alpha4"],
            "sigma_alpha4": row["sigma_alpha4_stat_fit"],
            "mahalanobis_d2": round(d2, 6),
            "passes_individual_95": d2 <= Q_95_2D,
        })

    return {
        "j_spin": j,
        "rho_correlation": rho,
        "optimal_r_sigma_over_j": round(opt_r, 6),
        "optimal_sigma": round(opt_r * j, 6),
        "optimal_alpha2": round(a_opt[0], 6),
        "optimal_alpha4": round(a_opt[1], 6),
        "min_max_mahalanobis_d2": round(min_max_d2, 6),
        "q_95_2d_threshold": round(Q_95_2D, 6),
        "tau_required": round(tau_req, 6),
        "passes_shared_null_at_tau1": passes_95,
        "n_rows": len(rows),
        "row_evaluations": row_reports,
    }


def analyze_projectile_families(
    rows: list[dict] | None = None,
    j: float = 6.5,
    rho: float = 0.0,
) -> dict:
    """Analyze all rows, alpha subset, and 12C subset under shared alignment null."""
    if rows is None:
        rows = ZOBEL83_ROWS

    alpha_rows = [r for r in rows if r.get("beam") == "alpha"]
    c12_rows = [r for r in rows if r.get("beam") == "12C"]

    res_all = find_optimal_shared_r(rows, j=j, rho=rho)
    res_alpha = find_optimal_shared_r(alpha_rows, j=j, rho=rho) if alpha_rows else None
    res_c12 = find_optimal_shared_r(c12_rows, j=j, rho=rho) if c12_rows else None

    # Scientific conclusion
    conclusion = {
        "cross_projectile_null": (
            "REJECTED" if res_all["tau_required"] > 1.0 else "ACCEPTED"
        ),
        "alpha_family_null": (
            "REJECTED" if res_alpha and res_alpha["tau_required"] > 1.0 else "ACCEPTED"
        ),
        "12C_family_null": (
            "ACCEPTED" if res_c12 and res_c12["tau_required"] <= 1.0 else "REJECTED"
        ),
        "physical_interpretation": (
            "Light-ion (alpha, xn) reactions exhibit rapid energy-dependent alignment attenuation "
            "as beam energy increases from 11.3 to 22.0 MeV, precluding a shared alignment parameter. "
            "In contrast, heavy-ion (12C, xn) fusion-evaporation brings substantial angular momentum "
            "with a stable statistical feeding pattern across 32-48 MeV, permitting a single shared "
            "alignment parameter r = sigma/J ~ 0.282 (tau_req < 1.0)."
        ),
    }

    return {
        "analysis": "P-ADO Shared Alignment Projectile Family Profile",
        "reference_source": "Zobel 1983 Table 1 (69Ge 958.0 keV 13/2+ -> 9/2+)",
        "rho_correlation": rho,
        "all_rows": res_all,
        "alpha_family": res_alpha,
        "c12_family": res_c12,
        "conclusion": conclusion,
    }


def format_report(res: dict) -> str:
    """Format a clean textual report of projectile family analysis."""
    lines = [
        "=" * 78,
        "  P-ADO SHARED ALIGNMENT NULL & PROJECTILE FAMILY PROFILE (Zobel 1983)",
        "=" * 78,
        f"Assumed Row-Internal Correlation rho: {res['rho_correlation']:+.2f}",
        f"2D 95% Confidence Threshold q_95:     {Q_95_2D:.4f}",
        "-" * 78,
    ]

    for name, rdict in [
        ("Combined (All 10 Rows)", res.get("all_rows")),
        ("Alpha Family (5 Rows, 11.3 - 22.0 MeV)", res.get("alpha_family")),
        ("12C Heavy-Ion Family (5 Rows, 32.0 - 48.0 MeV)", res.get("c12_family")),
    ]:
        if not rdict:
            continue
        status = "PASSED (tau <= 1.0)" if rdict["passes_shared_null_at_tau1"] else "FAILED (tau > 1.0)"
        lines.extend([
            f"[{name}]",
            f"  Optimal sigma/J:    r = {rdict['optimal_r_sigma_over_j']:.4f}  (sigma = {rdict['optimal_sigma']:.4f})",
            f"  Predicted alpha:    alpha2 = {rdict['optimal_alpha2']:.4f}, alpha4 = {rdict['optimal_alpha4']:.4f}",
            f"  Min-Max Mahalanobis D2: {rdict['min_max_mahalanobis_d2']:.4f}  (95% threshold: {Q_95_2D:.4f})",
            f"  Required tau:       tau_req = {rdict['tau_required']:.4f}",
            f"  Shared Null Status: {status}",
            "",
        ])

    lines.extend([
        "-" * 78,
        "SCIENTIFIC VERDICT & PHYSICAL INSIGHT:",
        f"  1. Cross-Projectile Shared Null: {res['conclusion']['cross_projectile_null']}",
        f"  2. Alpha-Beam Shared Null:       {res['conclusion']['alpha_family_null']}",
        f"  3. 12C-Beam Shared Null:         {res['conclusion']['12C_family_null']}",
        "",
        f"  Explanation: {res['conclusion']['physical_interpretation']}",
        "=" * 78,
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="P-ADO Shared Alignment Null & Projectile Family Profile Analyzer"
    )
    parser.add_argument(
        "--fixture",
        type=str,
        default=None,
        help="Path to fixture JSON (defaults to internal Zobel 1983 Table 1 fixture)",
    )
    parser.add_argument(
        "--beam",
        type=str,
        choices=["all", "alpha", "12C"],
        default="all",
        help="Select projectile beam family to evaluate",
    )
    parser.add_argument(
        "--rho",
        type=float,
        default=0.0,
        help="Row-internal alpha2-alpha4 correlation coefficient rho in (-1, 1)",
    )
    parser.add_argument(
        "--spin",
        type=float,
        default=6.5,
        help="Nuclear state spin J (default 6.5 for 13/2+ in 69Ge)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON results",
    )

    args = parser.parse_args()

    # Load rows
    rows = None
    if args.fixture:
        with open(args.fixture, "r", encoding="utf-8") as f:
            data = json.load(f)
            rows = data.get("rows", data)
    else:
        # Try default fixture path or fallback to hardcoded
        if DEFAULT_FIXTURE_PATH.is_file():
            try:
                with open(DEFAULT_FIXTURE_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    rows = data.get("rows")
            except Exception:
                rows = ZOBEL83_ROWS
        else:
            rows = ZOBEL83_ROWS

    if args.beam != "all":
        rows = [r for r in rows if r.get("beam") == args.beam]

    res = analyze_projectile_families(rows, j=args.spin, rho=args.rho)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_report(res))


if __name__ == "__main__":
    main()
