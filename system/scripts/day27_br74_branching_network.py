#!/usr/bin/env python3
"""Replay reported 74Br same-parent branches; envelopes are not confidence limits."""

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


DATA = [
    {
        "parent_spin": 8,
        "parity": "+",
        "out": {
            "energy_keV": 815.3,
            "initial_band": "B3",
            "final_band": "B1",
            "final_spin": 7,
            "intensity": 12.8,
            "intensity_error": 0.4,
            "delta": -1.1,
            "delta_low": -1.5,
            "delta_high": -0.8,
            "be2": 0.03,
            "bm1": 0.011,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3->Band1 815.3 row",
        },
        "reference": {
            "energy_keV": 682.7,
            "initial_band": "B3",
            "final_band": "B3",
            "final_spin": 6,
            "intensity": 9.2,
            "intensity_error": 1.3,
            "be2": 0.09,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3 682.7 row",
        },
    },
    {
        "parent_spin": 9,
        "parity": "+",
        "out": {
            "energy_keV": 1155.6,
            "initial_band": "B3",
            "final_band": "B1",
            "final_spin": 8,
            "intensity": 2.8,
            "intensity_error": 0.6,
            "delta": 3.1,
            "delta_low": 2.2,
            "delta_high": 4.9,
            "be2": 0.0032,
            "bm1": 0.0003,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3->Band1 1155.6 row",
        },
        "reference": {
            "energy_keV": 811.6,
            "initial_band": "B3",
            "final_band": "B3",
            "final_spin": 7,
            "intensity": 8.9,
            "intensity_error": 1.5,
            "be2": 0.07,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3 811.6 row",
        },
    },
    {
        "parent_spin": 10,
        "parity": "+",
        "out": {
            "energy_keV": 1266.8,
            "initial_band": "B3",
            "final_band": "B1",
            "final_spin": 9,
            "intensity": 5.2,
            "intensity_error": 1.0,
            "delta": 8.0,
            "delta_low": 6.0,
            "delta_high": 11.0,
            "be2": 0.017,
            "bm1": 0.0003,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3->Band1 1266.8 row",
        },
        "reference": {
            "energy_keV": 955.5,
            "initial_band": "B3",
            "final_band": "B3",
            "final_spin": 8,
            "intensity": 6.1,
            "intensity_error": 1.0,
            "be2": 0.08,
            "locator": "Guo2024 Supplement Table I PDF p2, Band3 955.5 row",
        },
    },
]


def e2_fraction(delta):
    return delta * delta / (1 + delta * delta)


def fraction_range(lower, upper):
    endpoints = [e2_fraction(lower), e2_fraction(upper)]
    if lower <= 0 <= upper:
        endpoints.append(0)
    return min(endpoints), max(endpoints)


def branching_ratio(out_intensity, ref_intensity, out_energy, ref_energy, delta):
    return (
        out_intensity
        / ref_intensity
        * (ref_energy / out_energy) ** 5
        * e2_fraction(delta)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parents[2]
    source_note = root / "knowledge/sources/guo-2024-chiral-wobbler-74br.md"
    match = re.search(
        r'^supplementary_raw_file: "([^"]+)"$',
        source_note.read_text(),
        re.MULTILINE,
    )
    if match is None:
        raise AssertionError("Supplement path not found in source metadata")
    supplement = root / match.group(1)
    supplement_hash = hashlib.sha256(supplement.read_bytes()).hexdigest()
    expected_hash = "1eb2c1af4ff7d1bf6460c154baabacb80e3ca7e63fa1832ca1d1b3d58b5ea9a0"
    if supplement_hash != expected_hash:
        raise AssertionError("Supplement identity changed; re-audit table inputs")
    rows = []
    unit_checks = []
    for data in DATA:
        out, ref = data["out"], data["reference"]
        if out["initial_band"] != ref["initial_band"]:
            raise AssertionError("Parent band mismatch")
        if ref["final_spin"] != data["parent_spin"] - 2:
            raise AssertionError("Reference is not the stated DeltaI=2 branch")
        value = branching_ratio(
            out["intensity"],
            ref["intensity"],
            out["energy_keV"],
            ref["energy_keV"],
            out["delta"],
        )
        fractions = fraction_range(out["delta_low"], out["delta_high"])
        kinematic = (ref["energy_keV"] / out["energy_keV"]) ** 5
        lower = (
            (out["intensity"] - out["intensity_error"])
            / (ref["intensity"] + ref["intensity_error"])
            * kinematic
            * fractions[0]
        )
        upper = (
            (out["intensity"] + out["intensity_error"])
            / (ref["intensity"] - ref["intensity_error"])
            * kinematic
            * fractions[1]
        )
        shifted_units = branching_ratio(
            out["intensity"],
            ref["intensity"],
            out["energy_keV"] / 1000,
            ref["energy_keV"] / 1000,
            out["delta"],
        )
        if abs(value - shifted_units) > 1e-14:
            raise AssertionError("Equal-multipole energy-ratio unit invariance failed")
        if not lower <= value <= upper:
            raise AssertionError("Central value outside deterministic input box")
        rate_delta_squared = (
            0.696775642
            * (out["energy_keV"] / 1000) ** 2
            * out["be2"]
            / out["bm1"]
        )
        rows.append(
            {
                "parent_spin": data["parent_spin"],
                "input": data,
                "out_e2_fraction": e2_fraction(out["delta"]),
                "out_e2_fraction_endpoint_range": fractions,
                "be2_out_over_in": value,
                "deterministic_input_box_envelope": [lower, upper],
                "printed_be2_quotient": out["be2"] / ref["be2"],
                "printed_strength_delta_squared_replay": rate_delta_squared,
                "reported_delta_squared": out["delta"] ** 2,
                "note": "Rounded published strengths are dependent derived data, not an independent experiment.",
            }
        )
        unit_checks.append(abs(value - shifted_units))
    zero_fraction = fraction_range(-0.08, 0.07)
    if zero_fraction[0] != 0:
        raise AssertionError("Interval crossing delta=0 must include zero E2")
    result = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "status": "reported-table-algebraic-replay",
        "analysis_level": "L2 derived/readiness; not new experimental fit or standalone L4",
        "source": "Guo et al., PRL132 092501 (2024), Supplement Table I PDF pp1-2",
        "source_note": "knowledge/sources/guo-2024-chiral-wobbler-74br.md",
        "source_supplement_sha256": supplement_hash,
        "formula": "B(E2,out)/B(E2,in)=(Iout/Iin)*(Ein/Eout)^5*delta_out^2/(1+delta_out^2)",
        "assumptions": [
            "same initial physical state, not merely the same spin",
            "efficiency-corrected photon intensities on a common normalization",
            "reference DeltaI=2 branch is pure E2",
            "out branch is truncated to M1/E2",
            "no extra E2 normalization from internal conversion is applied to photon-yield ratio",
        ],
        "uncertainty_boundary": {
            "envelope": "Cartesian product of printed one-error endpoints; not a confidence/credible interval",
            "missing": [
                "joint intensity and mixing-ratio covariance",
                "background and selection response",
                "raw angular/polarization likelihood",
            ],
            "energy_errors": "not propagated; fixed printed energies",
            "independence": "published B values reuse lifetimes/intensities/delta; not independent validation",
        },
        "maximum_same_multipole_energy_unit_error": max(unit_checks),
        "rows": rows,
        "b4_status": "model prediction in Qureshie2026; no fabricated B4 event counts or upper limits",
        "next_test": "Measure both B4->B3 and B4->B2 branches with same-parent identity, multipoles, efficiency and background; fit competing configurations.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = args.output_dir / "br74-branching-network.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": result["status"],
                "rows": [
                    {
                        "I": row["parent_spin"],
                        "f_E2": row["out_e2_fraction"],
                        "B_ratio": row["be2_out_over_in"],
                        "input_box_envelope": row["deterministic_input_box_envelope"],
                        "rounded_published_B_ratio": row["printed_be2_quotient"],
                    }
                    for row in rows
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
