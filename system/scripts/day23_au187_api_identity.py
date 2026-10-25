#!/usr/bin/env python3
"""Inspect an official CSV snapshot without converting evaluated fields to new data."""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


def read_csv(path):
    # This API response ends with an empty CSV record; it is not a data row.
    rows = [row for row in csv.reader(path.read_text(encoding="latin-1").splitlines()) if row]
    head = rows[0]
    counts = Counter(head)
    # Retain duplicate uncertainty columns by their actual positional index.
    keys = [f"{name}@{idx}" if counts[name] > 1 else name for idx, name in enumerate(head)]
    if any(len(row) != len(head) for row in rows[1:]):
        raise ValueError("CSV width mismatch")
    return head, keys, [dict(zip(keys, row)) for row in rows[1:]]


def unique_spin(jp):
    values = re.findall(r"\d+(?:/\d+)?", jp)
    return Fraction(values[0]) if len(values) == 1 else None


def inspect(gammas_path, levels_path):
    gh, gkeys, gs = read_csv(gammas_path)
    lh, lkeys, levels = read_csv(levels_path)
    level_by_id = {r["idx"]: r for r in levels}
    if len(level_by_id) != len(levels):
        raise ValueError("Duplicate level identifiers")
    selected = []
    for key in [("16", "2", "2"), ("38", "10", "3")]:
        hits = [r for r in gs if tuple(r[k] for k in
                ["start_level_idx", "end_level_idx", "gamma_idx"]) == key]
        if len(hits) != 1:
            raise ValueError(f"Missing or nonunique snapshot row {key}")
        r = hits[0]
        parent = level_by_id[r["start_level_idx"]]
        child = level_by_id[r["end_level_idx"]]
        selected.append({"gamma": r, "parent": parent, "child": child,
                         "printed_energy_residual_keV": str(Decimal(r["start_level_energy"])
                             - Decimal(r["end_level_energy"]) - Decimal(r["energy"]))})
    near = next(r for r in gs if (r["start_level_idx"], r["end_level_idx"], r["gamma_idx"]) == ("92", "48", "0"))
    delta_spin = abs(unique_spin(near["start_level_jp"])-unique_spin(near["end_level_jp"]))
    controls = {
        "same_nuclide_parent_and_child_joins": all(
            a["gamma"][k] == a["parent"][k] == a["child"][k]
            for a in selected for k in ["z", "n", "symbol"]) and all(
            (a["gamma"]["z"], a["gamma"]["n"], a["gamma"]["symbol"]) == ("79", "108", "Au")
            for a in selected),
        "joined_level_energies_are_identical_tokens": all(
            a["gamma"]["start_level_energy"] == a["parent"]["energy"] and
            a["gamma"]["end_level_energy"] == a["child"]["energy"] for a in selected),
        "missing_parent_lifetimes_remain_empty": all(a["parent"]["half_life"] == "" for a in selected),
        "duplicate_half_life_error_columns_retained": len([k for k in lkeys if k.startswith("unc_hl@")]) == 2,
        "436p6_is_delta_spin_zero_not_SP_delta_spin_one": delta_spin == 0,
        "total_conversion_is_separate_from_K_shell": "tot_conv_coeff" in gh and not any(k in gh for k in ["alpha_K", "alpha_k"]),
    }
    return {"scope": "IAEA public evaluation/API field identity; no new independent experiment, alphaK, sign convention, lifetime, delta fit or confidence level established.",
            "input_sha256": {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [gammas_path, levels_path]},
            "source_urls": ["https://www-nds.iaea.org/relnsd/v0/data?fields=gammas&nuclides=187au",
                            "https://www-nds.iaea.org/relnsd/v0/data?fields=levels&nuclides=187au"],
            "gamma_rows": len(gs), "level_rows": len(levels),
            "duplicate_level_headers": {k: v for k, v in Counter(lh).items() if v > 1},
            "level_header_positions": {k: [i for i, h in enumerate(lh) if h == k]
                                       for k, n in Counter(lh).items() if n > 1},
            "targets": selected, "near_energy_counterexample": near,
            "near_energy_delta_spin": str(delta_spin),
            "controls": controls, "all_controls_pass": all(controls.values()),
            "limitations": ["Snapshot-specific level/gamma indices must be paired with the source hash/version.",
                            "Extraction_date does not replace ENSDF publication cutoff.",
                            "Mixing_ratio tokens are reported without inferring the phase/sign convention.",
                            "Reference notes, K-shell measurement and detector covariance are absent from this export.",
                            "The half-life error headers are duplicated in this actual response; generic DictReader overwrites the first.",
                            "Raw files remain temporary; formal evidence archival is deferred under the protected-raw boundary."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gammas", type=Path, required=True)
    p.add_argument("--levels", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    result = inspect(a.gammas, a.levels)
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"],
                      "rows": [result["gamma_rows"], result["level_rows"]],
                      "duplicate_headers": result["duplicate_level_headers"]}))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
