#!/usr/bin/env python3
"""Reconstruct same-parent E1/E3 ratios without a common E2 denominator.

Inputs are published photon intensities or photon-branch ratios. This program
does not infer absolute strengths, lifetimes, a shape, or statistical significance.
Uncertainty scenarios are first-order calculations, not recovered covariances.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


HBARC_MEV_FM = 197.3269804


def radiation_factor(order: int) -> float:
    """Common 1/hbar and electric-charge factors cancel between electric ranks."""
    double_factorial = math.prod(range(1, 2 * order + 2, 2))
    return (
        8 * math.pi * (order + 1)
        / (order * double_factorial**2)
        / HBARC_MEV_FM ** (2 * order + 1)
    )


def zero_projection_cg_squared(j: int, rank: int, jf: int) -> float:
    """Closed factorial expression for (j 0 rank 0 | jf 0)^2."""
    total = j + rank + jf
    if total % 2 or abs(j - rank) > jf or jf > j + rank:
        return 0.0
    g = total // 2
    triangle = (
        math.factorial(total - 2 * j)
        * math.factorial(total - 2 * rank)
        * math.factorial(total - 2 * jf)
        / math.factorial(total + 1)
    )
    amplitude = math.factorial(g) / (
        math.factorial(g - j)
        * math.factorial(g - rank)
        * math.factorial(g - jf)
    )
    return (2 * jf + 1) * triangle * amplitude**2


def analyze(data: dict) -> dict:
    c31 = radiation_factor(3) / radiation_factor(1)
    exact_c31 = 2 / 3675 / HBARC_MEV_FM**4
    assert math.isclose(c31, exact_c31, rel_tol=1e-14)
    rows = []
    checks = []
    for item in data["rows"]:
        # Both inputs share exactly the E2 denominator in the branch-ratio case.
        numerator = item["e1_photon_input"]
        denominator = item["e3_photon_input"]
        e1 = item["e1_energy_kev"] / 1000
        e3 = item["e3_energy_kev"] / 1000
        ratio = numerator / denominator * c31 * e3**7 / e1**3
        r1 = item["e1_input_sigma"] / numerator
        r3 = item["e3_input_sigma"] / denominator
        scenarios = {}
        for rho in [-1.0, 0.0, 0.5, 1.0]:
            # For ratios to E2, rho includes that shared denominator and other
            # correlations. Its value cannot be recovered from marginal errors.
            scenarios[str(rho)] = math.sqrt(max(0, r1*r1 + r3*r3 - 2*rho*r1*r3))
        spin = item["initial_spin"]
        cg1 = zero_projection_cg_squared(spin, 1, spin - 1)
        cg3 = zero_projection_cg_squared(spin, 3, spin - 3)
        intrinsic_proxy = ratio * cg3 / cg1
        from_reported_b_ratios = item["reported_b1_b2_fm_minus2"] / item["reported_b3_b2_fm2"]
        rounding_delta = ratio / from_reported_b_ratios - 1
        # Rounded printed strengths are a comparison, never substituted for
        # the primitive inputs or treated as a separate experiment.
        checks.append({
            "id": item["id"],
            "relative_difference_from_printed_B_ratio_quotient": rounding_delta,
            "within_one_percent": abs(rounding_delta) < 0.01,
        })
        if not abs(rounding_delta) < 0.01:
            raise ValueError(f"Published-column mismatch requires review: {item['id']}")
        # A common E2 denominator cancels even when its arbitrary scale changes.
        for scale in [0.1, 0.5, 1.0, 2.0, 10.0]:
            assert math.isclose(
                (numerator / scale) / (denominator / scale),
                numerator / denominator, rel_tol=1e-14
            )
        rows.append({
            "id": item["id"],
            "nucleus": item["nucleus"],
            "initial_spin": spin,
            "initial_energy_kev": item["initial_energy_kev"],
            "B_E1_over_B_E3_fm_minus4": ratio,
            "relative_sigma_scenarios": scenarios,
            "energy_relative_sigma_if_independent": math.sqrt(
                (7*item["e3_energy_sigma_kev"]/item["e3_energy_kev"])**2
                + (3*item["e1_energy_sigma_kev"]/item["e1_energy_kev"])**2
            ) if "e3_energy_sigma_kev" in item else None,
            "K0_CG_E1_squared": cg1,
            "K0_CG_E3_squared": cg3,
            "conditional_K0_intrinsic_amplitude_ratio_squared_fm_minus4": intrinsic_proxy,
            "input_kind": item["input_kind"],
            "locator": item["locator"],
        })
    changes = []
    for nucleus in ["98Mo", "100Ru"]:
        low, high = sorted(
            (r for r in rows if r["nucleus"] == nucleus),
            key=lambda r: r["initial_spin"]
        )
        changes.append({
            "nucleus": nucleus,
            "raw_ratio_spin7_over_spin5": high["B_E1_over_B_E3_fm_minus4"] / low["B_E1_over_B_E3_fm_minus4"],
            "conditional_K0_proxy_spin7_over_spin5": high["conditional_K0_intrinsic_amplitude_ratio_squared_fm_minus4"] / low["conditional_K0_intrinsic_amplitude_ratio_squared_fm_minus4"],
            "statistical_significance": None,
            "reason": "Joint intensity/efficiency/gate covariance and K assignments unavailable.",
        })
    return {
        "schema": "same-parent-e1-e3-v1",
        "data_scope": "Published low-spin branches; no absolute B and no new measurement",
        "coefficient_C_E3_over_C_E1_MeV_minus4_fm_minus4": c31,
        "rows": rows,
        "spin_changes": changes,
        "printed_column_comparisons": checks,
        "checks": {
            "coefficient_general_equals_closed_form": True,
            "shared_E2_scale_invariance_cases": len(rows)*5,
            "K0_CG_independent_reference": {
                "5_E1": math.isclose(zero_projection_cg_squared(5,1,4),5/11),
                "5_E3": math.isclose(zero_projection_cg_squared(5,3,2),50/231),
                "7_E1": math.isclose(zero_projection_cg_squared(7,1,6),7/15),
                "7_E3": math.isclose(zero_projection_cg_squared(7,3,4),35/143),
            },
        },
        "limitations": data["limitations"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    for original in data["originals"]:
        original_path = Path(original["path"])
        actual_hash = hashlib.sha256(original_path.read_bytes()).hexdigest()
        if actual_hash != original["sha256"]:
            raise ValueError(f"Original hash mismatch: {original_path}")
    result = analyze(data)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output/"constraints.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    )
    fields = [
        "id", "nucleus", "initial_spin", "initial_energy_kev",
        "B_E1_over_B_E3_fm_minus4",
        "conditional_K0_intrinsic_amplitude_ratio_squared_fm_minus4",
        "input_kind",
    ]
    with (output/"constraints.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(result["rows"])
    hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [output/"constraints.json", output/"constraints.csv"]
    }
    provenance = {
        "producer": Path(__file__).resolve().as_posix(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input": args.input.resolve().as_posix(),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "outputs": hashes,
        "run_command": [
            "python3", "system/scripts/e1_e3_same_parent_constraints.py",
            "--input", args.input.as_posix(), "--output", args.output.as_posix()
        ],
        "actual_original_files": data["originals"],
        "scope": "Derived quantities and explicitly conditional models, not original evidence",
    }
    (output/"run-provenance.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"rows":len(result["rows"]), "output":str(output), "checks":result["checks"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
