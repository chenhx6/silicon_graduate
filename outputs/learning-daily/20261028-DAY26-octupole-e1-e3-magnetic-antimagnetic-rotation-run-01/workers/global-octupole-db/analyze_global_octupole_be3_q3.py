#!/usr/bin/env python3
"""Reproducible checks and cross-region summaries for the E3 benchmark CSV.

The input deliberately mixes direct Coulomb-excitation results with older
compiled/evaluated values.  The script therefore keeps provenance columns and
never treats a derived Q3 or a compiled value as a new experiment.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def number(value: str):
    if value is None or value.strip() == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def wu_e3_efm6(a: float, r0: float = 1.2) -> float:
    """Weisskopf E3 unit using B_down = R^6/(16*pi), R=r0*A^(1/3)."""
    radius = r0 * a ** (1.0 / 3.0)
    return radius**6 / (16.0 * math.pi)


def q3_from_b_down(a: float, b_wu: float, r0: float = 1.2) -> float:
    """Axial-rotor conversion Q3 = sqrt(16*pi*B(E3;3->0))."""
    return math.sqrt(16.0 * math.pi * b_wu * wu_e3_efm6(a, r0))


def beta3_from_q3(z: float, a: float, q3: float, beta2: float = 0.0, r0: float = 1.2):
    radius = r0 * a ** (1.0 / 3.0)
    denominator = (3.0 / (4.0 * math.pi)) * z * radius**3 * (1.0 + 0.8 * beta2)
    return q3 / denominator


def linear_fit_log(rows):
    points = []
    for row in rows:
        e = number(row["e3_energy_keV"])
        b = number(row["b_e3_down_wu"])
        if e and b and e > 0 and b > 0:
            points.append((math.log(e), math.log(b)))
    if len(points) < 2:
        return {"n": len(points), "status": "insufficient_numeric_energy_points"}
    xbar = sum(p[0] for p in points) / len(points)
    ybar = sum(p[1] for p in points) / len(points)
    sxx = sum((x - xbar) ** 2 for x, _ in points)
    slope = sum((x - xbar) * (y - ybar) for x, y in points) / sxx if sxx else None
    intercept = ybar - slope * xbar if slope is not None else None
    residuals = [y - (intercept + slope * x) for x, y in points] if slope is not None else []
    sse = sum(x * x for x in residuals)
    r2 = 1.0 - sse / sum((y - ybar) ** 2 for _, y in points) if len(points) > 2 and sum((y - ybar) ** 2 for _, y in points) else None
    return {"n": len(points), "slope_logB_vs_logE": slope, "intercept": intercept, "r2": r2,
            "interpretation": "descriptive only; selection and mass-region effects are unmodelled"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    with args.csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    conversion_checks = []
    for row in rows:
        a = number(row["A"])
        b = number(row["b_e3_down_wu"])
        q = number(row["q3_derived_from_b_wu_efm3"])
        if a and b and q:
            expected = q3_from_b_down(a, b)
            conversion_checks.append({
                "record_id": row["record_id"],
                "q3_csv_efm3": q,
                "q3_recomputed_efm3": round(expected, 3),
                "relative_difference": round((q - expected) / expected, 6),
                "status": "rounding_or_consistent" if abs(q - expected) / expected < 0.02 else "review",
            })

    by_region = defaultdict(list)
    for row in rows:
        by_region[row["region"]].append(row)
    region_summary = {}
    for region, region_rows in sorted(by_region.items()):
        values = [number(r["b_e3_down_wu"]) for r in region_rows]
        values = [v for v in values if v is not None]
        region_summary[region] = {
            "n_records": len(region_rows),
            "n_numeric_B_down": len(values),
            "mean_B_down_Wu": round(sum(values) / len(values), 3) if values else None,
            "min_B_down_Wu": min(values) if values else None,
            "max_B_down_Wu": max(values) if values else None,
            "direct_experiment_records": sum(r["evidence_tier"] == "direct-experiment" for r in region_rows),
            "compiled_records": sum(r["evidence_tier"] == "compiled-evaluation" for r in region_rows),
        }

    q3_beta3_checks = []
    for row in rows:
        z, a, q, beta2, beta3 = (number(row[k]) for k in ("Z", "A", "q3_direct_efm3", "beta2", "beta3_derived"))
        if all(v is not None for v in (z, a, q, beta2, beta3)):
            reconstructed = beta3_from_q3(z, a, q, beta2)
            relative_difference = (beta3 - reconstructed) / reconstructed
            q3_beta3_checks.append({"record_id": row["record_id"], "beta3_csv": beta3,
                                    "beta3_recomputed_from_user_formula": round(reconstructed, 5),
                                    "relative_difference": round(relative_difference, 5),
                                    "status": "consistent" if abs(relative_difference) < 0.20 else "definition_or_conversion_boundary"})

    output = {
        "schema": "global-octupole-be3-q3-v1",
        "input": str(args.csv_path),
        "n_records": len(rows),
        "counts": dict(Counter(r["evidence_tier"] for r in rows)),
        "conversion": {
            "formula": "B_W.u.(E3;3->0)=R0^6/(16*pi), Q3=sqrt(16*pi*B_down), R0=1.2 A^(1/3) fm",
            "checks": conversion_checks,
        },
        "region_summary": region_summary,
        "B_vs_E3": linear_fit_log(rows),
        "q3_beta3_checks": q3_beta3_checks,
        "static_dynamic_readout": {
            "status": "conditional",
            "direct_single_transition": "A large 0+<->3- strength measures octupole collectivity but does not by itself identify a deep static double well.",
            "multi_transition_discriminator": "Butler 2020 reports approximately constant Q3 across several 222Ra links and a near-zero 228Ra 2+->3- link; these rows are not closure-complete.",
            "parity_splitting": "Not computed from this CSV because the database is a transition benchmark, not a level-scheme table; use the Gaffney 2013 level-systematics locator.",
            "ewsr": "not_computable: complete negative-parity final-state coverage and covariance are absent; do not call the lowest-state B(E3) an EWSR exhaustion fraction.",
        },
        "audit_flags": [
            "Compiled/evaluated rows and direct Coulomb-excitation rows are not pooled as independent experiments.",
            "Blank E(3-) values are intentional; no energy was inserted without a locator.",
            "q3_direct and q3_derived_from_b_wu_efm3 are separate observables; rotor conversion and beta3 remain model dependent.",
            "The 144Ba direct Q3 and quoted beta3 do not satisfy the user-specified beta3 formula under a naive R0=1.2 A^(1/3) substitution; retain this as a Q3/shape-convention boundary pending the primary conversion equation.",
        ],
    }
    destination = args.out or args.csv_path.with_name("global_octupole_be3_q3_analysis.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "n_records": len(rows), "n_conversion_checks": len(conversion_checks)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
