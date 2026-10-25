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


def inspect_parent_decay(gamma_path, electron_path, adopted_targets):
    body = electron_path.read_text(encoding="latin-1").strip()
    electron = {"response": "no-data-code", "service_code": "0"} if body == "0" else {
        "response": "other-response", "prefix": body[:100]}
    head, keys, rows = read_csv(gamma_path)
    parent_fields = ["p_z", "p_n", "p_symbol", "p_energy_shift", "p_energy", "jp",
                     "half_life", "unit_hl", "decay", "d_z", "d_n", "d_symbol"]
    grouped = Counter(tuple(r[k] for k in parent_fields) for r in rows)
    groups = [{"identity": dict(zip(parent_fields, key)), "export_rows": n}
              for key, n in grouped.items()]
    targets = []
    for adopted in adopted_targets:
        energy = adopted["gamma"]["energy"]
        hits = [r for r in rows if r["energy"] == energy and
                (r["d_z"], r["d_n"], r["d_symbol"]) == ("79", "108", "Au")]
        if len(hits) != 1:
            raise ValueError(f"Nonunique decay-export candidate at {energy} keV")
        r = hits[0]
        targets.append({"decay_export": r,
                        "adopted_export_unc_mr_token": adopted["gamma"]["unc_mr"],
                        "decay_export_unc_mr_token": r["unc_mr"],
                        "level_energy_offsets_keV": {
                            k: str(Decimal(r[k])-Decimal(adopted["gamma"][k]))
                            for k in ["start_level_energy", "end_level_energy"]},
                        "identity_status": "candidate crosswalk; independent adopted notes/row lineage not restored"})
    controls = {
        "parent_Hg187_daughter_Au187_charge_mass_identity": all(
            (r["p_z"], r["p_n"], r["p_symbol"], r["d_z"], r["d_n"], r["d_symbol"])
            == ("80", "107", "Hg", "79", "108", "Au") for r in rows),
        "zero_parent_energy_does_not_merge_shifted_state": len(groups) == 2 and
            {g["identity"]["p_energy_shift"] for g in groups} == {"", "X"} and
            {g["identity"]["p_energy"] for g in groups} == {"0"},
        "blank_initial_lifetime_not_replaced_by_parent_clock": all(
            r["decay_export"]["start_level_hl"] == "" and
            r["decay_export"]["half_life_sec"] != "" for r in targets),
        "all_missing_gamma_intensities_remain_blank": all(r["intensity"] == "" for r in rows),
        "electron_zero_is_service_status_not_measurement": electron["response"] == "no-data-code",
        "two_error_encodings_not_silently_merged": all(
            r["adopted_export_unc_mr_token"] == "0.3" and
            r["decay_export_unc_mr_token"] == "3" for r in targets),
    }
    return {"parent_field_definition": "API jp/half_life/p_energy refer to Hg parent; start_level_hl/start_level_energy refer to daughter gamma initial level.",
            "gamma_rows": len(rows), "intensity_missing_rows": sum(r["intensity"] == "" for r in rows),
            "parent_groups": groups, "targets": targets, "electron_response": electron,
            "input_sha256": {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [gamma_path, electron_path]},
            "controls": controls, "all_controls_pass": all(controls.values()),
            "limitations": ["0 is documented as a valid query with no matching data, not a measured zero electron yield.",
                            "Missing gamma intensities prevent intensity-derived alphaK or observed branching reconstruction.",
                            "Identical p_energy=0 with different shifts/JP is not proof of degenerate states.",
                            "Uncertainty-token semantics and source notes are not reconstructed from the two exports.",
                            "Parent metadata supports Hg-to-Au identity; it does not identify the exact 1998 experiment selection."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gammas", type=Path, required=True)
    p.add_argument("--levels", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--decay-gammas", type=Path)
    p.add_argument("--decay-electrons", type=Path)
    a = p.parse_args()
    result = inspect(a.gammas, a.levels)
    if a.decay_gammas or a.decay_electrons:
        if not (a.decay_gammas and a.decay_electrons):
            p.error("both parent-decay inputs are required")
        result["decay_inspection"] = inspect_parent_decay(
            a.decay_gammas, a.decay_electrons, result["targets"])
        result["all_controls_pass"] &= result["decay_inspection"]["all_controls_pass"]
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"],
                      "rows": [result["gamma_rows"], result["level_rows"]],
                      "duplicate_headers": result["duplicate_level_headers"]}))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
