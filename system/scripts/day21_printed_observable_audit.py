#!/usr/bin/env python3
"""Transform transcribed published inputs; never infer experimental coverage.

This exercise checks percent units and rounding consistency. It does not fit
events, reconstruct a reaction calculation, or certify any structural claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal as D
from pathlib import Path


def depletion_interval(center: D, maximum: D, half_step: D) -> tuple[D, D]:
    if not D(0) <= half_step < center <= maximum - 2 * half_step:
        raise ValueError("positive density intervals with center below maximum required")
    return (1 - (center + half_step) / (maximum - half_step),
            1 - (center - half_step) / (maximum + half_step))


def calculate(data: dict) -> dict:
    ko = data["knockout"]
    sigma = D(ko["inclusive_mb"])
    rows = []
    for state in ko["states"]:
        percent = D(state["population_percent"])
        if not 0 <= percent <= 100:
            raise ValueError("population is a percent, not an unbounded weight")
        rows.append({"state_keV": state["state_keV"],
                     "population_percent": str(percent),
                     "partial_mb": str(sigma * percent / 100)})
    if sum(D(row["population_percent"]) for row in rows) > 100:
        raise ValueError("selected final-state populations exceed inclusive population")
    printed = []
    for table in data["density_tables"]:
        for row in table["rows"]:
            c, m, f = (D(row[key]) for key in ["center", "maximum", "F_printed"])
            lo, hi = depletion_interval(c, m, D(table["density_half_rounding_step"]))
            df = D(table["F_half_rounding_step"])
            printed.append({"table": table["table"], "density_object": table["object"],
                            "state": row["state"], "F_from_printed_centers": str(1-c/m),
                            "F_printed": str(f),
                            "rounding_envelope": [str(lo), str(hi)],
                            "overlap_with_printed_F_rounding": max(lo, f-df) <= min(hi, f+df)})
    n34, extra, n36 = (D(ko[key]) for key in ["occupancy_34", "extra_assigned_occupancy_34", "occupancy_36"])
    return {
        "scope": "printed-input arithmetic and declared nearest-rounding compatibility only",
        "knockout_partial_cross_sections": rows,
        "selected_sum_mb": str(sum(D(row["partial_mb"]) for row in rows)),
        "occupancy_ratio_centers": str(n34/n36),
        "occupancy_ratio_with_all_four_weak_states_assigned_l0": str((n34+extra)/n36),
        "density_rounding_rows": printed,
        "boundary": [
            "KO final-state population is not a gamma-decay branching fraction",
            "no covariance or new experimental confidence interval is inferred",
            "printed densities are model outputs, not measured density samples",
            "occupancy ratio does not equal central density depletion",
            "rounding envelope assumes nearest rounding; original unrounded outputs were not obtained",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    result = calculate(data)
    result["input_sha256"] = hashlib.sha256(args.input.read_bytes()).hexdigest()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"rows": len(result["density_rounding_rows"]),
                      "rounding_compatible": sum(row["overlap_with_printed_F_rounding"]
                                                 for row in result["density_rounding_rows"]),
                      "selected_sum_mb": result["selected_sum_mb"],
                      "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
