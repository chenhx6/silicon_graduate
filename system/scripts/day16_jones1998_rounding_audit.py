#!/usr/bin/env python3
"""Check simultaneous coefficient cells over fixed printed-delta rounding cells.

These are representation intervals, not measurement confidence intervals.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np

from day16_gretina_convention_audit import coefficients
from day16_jones1998_reference_audit import point_population


def coefficients_polynomial(row, key):
    p = point_population(row["Ji2"])
    a = coefficients(row["Ji2"], row["Jf2"], p, 0.)[key]
    c = coefficients(row["Ji2"], row["Jf2"], p, None)[key]
    b = 2*coefficients(row["Ji2"], row["Jf2"], p, 1.)[key]-a-c
    return np.array([a, b, c], dtype=float)


def roots(poly):
    result = np.polynomial.polynomial.polyroots(np.trim_zeros(poly, "b"))
    return [float(z.real) for z in result if abs(z.imag) < 1e-10]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    results = []
    for row in cfg["rows"]:
        if row["multipole"] != "mixed":
            continue
        central = row["delta_RB"]
        # Exact intended precision of these selected printed central values.
        unit = .1 if (row["parent_keV"], row["gamma_keV"]) in [(329.86, 250.35), (334.38, 272.93), (376.28, 201.6)] else .01
        lo, hi = central-unit/2, central+unit/2
        polys = {key: coefficients_polynomial(row, key) for key in ["a2", "a4"]}
        years = {}
        for year in [1998, 2002]:
            if row[f"a2_{year}"] is None:
                continue
            cuts = [lo, hi]
            bounds = {key: (row[f"{key}_{year}"]-.005, row[f"{key}_{year}"]+.005) for key in polys}
            for key, poly in polys.items():
                for value in bounds[key]:
                    for point in roots(poly-value*np.array([1., 0., 1.])):
                        if lo < point < hi:
                            cuts.append(point)
            cuts = sorted(set(cuts))
            intervals = []
            for left, right in zip(cuts, cuts[1:]):
                mid = (left+right)/2
                if all(a-1e-12 <= np.polynomial.polynomial.polyval(mid, polys[key])/(1+mid*mid) <= b+1e-12
                       for key, (a, b) in bounds.items()):
                    intervals.append([left, right])
            years[str(year)] = {"simultaneous_2dp_cells_feasible": bool(intervals),
                                "delta_rounding_subintervals": intervals}
        results.append({"identity": {k: row[k] for k in ["parent_keV", "gamma_keV", "Ji2", "Jf2"]},
            "delta_RB_printed": central, "delta_rounding_cell": [lo, hi],
            "coefficient_numerator_polynomials_ascending": {key: v.tolist() for key, v in polys.items()},
            "years": years})
    special = next(row for row in cfg["rows"] if row["parent_keV"] == 342.84 and row["gamma_keV"] == 62.45)
    reversed_delta = coefficients(special["Ji2"], special["Jf2"], point_population(special["Ji2"]), -special["delta_RB"])
    output = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "contract_sha256": hashlib.sha256(args.contract.read_bytes()).hexdigest(),
        "coefficient_cell_rule": "Declared ±.005 for both columns, including displayed zero. Not original error bars or certified unrounded production.",
        "rows": results,
        "opposite_delta_for_342p84_62p45_control": {"delta_RB": -special["delta_RB"],
            "a2": reversed_delta["a2"], "a4": reversed_delta["a4"],
            "source_measurement_or_row_repaired": False},
        "remaining_1998_simultaneous_nonclosures": [row["identity"] for row in results
            if not row["years"]["1998"]["simultaneous_2dp_cells_feasible"]],
        "all_present_2002_simultaneous_cells_feasible": all(row["years"]["2002"]["simultaneous_2dp_cells_feasible"]
            for row in results if "2002" in row["years"]),
        "actual_delta_or_joint_fit_recovered": False}
    assert output["all_present_2002_simultaneous_cells_feasible"]
    args.output.write_text(json.dumps(output, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: output[key] for key in ["remaining_1998_simultaneous_nonclosures",
        "opposite_delta_for_342p84_62p45_control", "all_present_2002_simultaneous_cells_feasible"]}, indent=2))


if __name__ == "__main__":
    main()
