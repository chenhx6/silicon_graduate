#!/usr/bin/env python3
"""Audit unsigned MR, divided/undivided intensities and calibration identity."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

import numpy as np

from day16_gretina_convention_audit import coefficients
from day16_jones1998_reference_audit import full_trace, point_population
from day16_ni60_reference_audit import decode_uncertainty, records, unique


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gamma_fields(row: dict) -> dict:
    raw = row["raw"].ljust(80)
    mr = row["MR"]
    if not mr:
        sign = "not-recorded"
    elif mr.startswith(("+", "-")):
        sign = "explicit-sign"
    else:
        sign = "unknown-sign-unsigned-token"
    result = dict(row, sign_status=sign, comment_flag_col77=raw[76],
                  coincidence_flag_col78=raw[77], CC=raw[55:62].strip())
    for key in ["LC", "MC"]:
        tokens = [re.search(r"\b"+key+r"=\s*([\d.Ee+-]+)", q["raw"])
                  for q in row["attached"] if q["raw"][5] == "S"]
        found = [float(q.group(1)) for q in tokens if q]
        result[key] = found[0] if found else None
    return result


def normalization(path: Path) -> dict:
    found = [s.ljust(80) for s in path.read_text().splitlines()
             if s.ljust(80)[5:8] == "  N"]
    assert len(found) == 1
    raw = found[0]
    value, error = raw[9:19].strip(), raw[19:21].strip()
    return {"NR_token": value, "DNR_token": error, "NR": float(value),
            "sigma_NR": decode_uncertainty(value, error), "raw": raw}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "N223-FLAGS-SIGNS-AND-COMPANION-01"
    datasets = {}
    for key, source in cfg["files"].items():
        path = Path(source["path"])
        assert sha(path) == source["sha256"]
        data = records(path)
        data["gammas"] = [gamma_fields(g) for g in data["gammas"]]
        datasets[key] = data
    unsigned = []
    for key in ["adopted", "alpha"]:
        level = unique(datasets[key]["levels"], E="342.654")
        assert level["Jpi"] == cfg["selected_unsigned_MR"]["Jpi"]
        g = unique([g for g in datasets[key]["gammas"] if g["parent"] == level], E="62.45")
        assert g["MR"] == "0.29" and g["DMR"] == "5"
        assert g["sign_status"] == "unknown-sign-unsigned-token"
        unsigned.append({"dataset": key, "record": g,
            "sigma_magnitude": decode_uncertainty(g["MR"], g["DMR"]),
            "sign_would_be_lost_by_plain_float": True})
    old = []
    for parent in cfg["doublet_113old"]["parents"]:
        level = unique(datasets["alpha"]["levels"], E=parent)
        g = unique([g for g in datasets["alpha"]["gammas"] if g["parent"] == level], E="113.11")
        assert g["comment_flag_col77"] == "@"
        old.append(g)
    for index, row in enumerate(old):
        for key in ["CC", "LC", "MC"]:
            assert float(row[key]) == cfg["doublet_113old"][key][index]
        assert float(row["RI"]) == cfg["doublet_113old"]["relative_RI"][index]
    ri = np.array([float(g["RI"]) for g in old])
    weights = {"photon": ri, "total": ri*(1+np.array([float(g["CC"]) for g in old])),
               "L_electrons": ri*np.array([g["LC"] for g in old]),
               "M_electrons": ri*np.array([g["MC"] for g in old])}
    fractions = {key: float(value[1]/value.sum()) for key, value in weights.items()}
    assert fractions["L_electrons"] > .94 and fractions["M_electrons"] > .94
    normalized = normalization(Path(cfg["files"]["alpha"]["path"]))
    assert normalized["NR"] == .129 and normalized["sigma_NR"] == .011
    modern = []
    for energy, expected in cfg["xundl_pairs"].items():
        found = [g for g in datasets["xundl2026"]["gammas"] if g["E"] == energy]
        assert len(found) == 2
        assert sorted(g["parent"]["E"] for g in found) == sorted(expected["parent_tokens"])
        assert all(g["comment_flag_col77"] == "&" and float(g["RI"]) == expected["expected_shared_RI"]
                   and g["DRI"] == expected["expected_DRI"] for g in found)
        intensity = float(found[0]["RI"])
        sigma = decode_uncertainty(found[0]["RI"], found[0]["DRI"])
        modern.append({"energy_token": energy, "records": found,
            "one_shared_undivided_I": intensity, "sigma_shared_I": sigma,
            "naive_placement_sum_wrong": sum(float(g["RI"]) for g in found),
            "component_partition_or_covariance_identified": False})
    norm_new = normalization(Path(cfg["files"]["xundl2026"]["path"]))
    assert norm_new["NR"] == 1
    # Rounded duplicate E=342.6 alone is ambiguous; composite identity must survive.
    ambiguous_rejected = False
    try:
        unique(datasets["xundl2026"]["levels"], E="342.6")
    except ValueError:
        ambiguous_rejected = True
    assert ambiguous_rejected
    candidates = []
    for delta in cfg["MRsign_candidates_RB"]:
        case = {"Ji2": 9, "Jf2": 7, "multipole": "mixed", "delta_RB": delta}
        pop = point_population(9)
        native, rb = full_trace(case, pop), full_trace(case, pop, "RB")
        assert max(abs(native[k]-rb[k]) for k in native) < 1e-12
        candidates.append({"delta_RB_assumed": delta, "native_IQUV_model": native,
                           "bridge_residual": max(abs(native[k]-rb[k]) for k in native)})
    old_aggregate = float(ri.sum()*normalized["NR"])
    result = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "source_hashes": {key: source["sha256"] for key, source in cfg["files"].items()},
        "selected_unsigned_MR_records": unsigned, "two_assumed_sign_predictions": candidates,
        "old_divided113_records": old, "conditional_E2_fractions_equal_response": fractions,
        "old_normalization": normalized, "modern_normalization": norm_new,
        "old113_aggregate_photon_per100_central": old_aggregate,
        "modern_undivided_pairs": modern,
        "all_modern_MR_fields_blank": all(not g["MR"] for g in datasets["xundl2026"]["gammas"]),
        "rounded_level_energy_only_selector_rejected": ambiguous_rejected,
        "old_and_new_dataset_difference_significance_calculated": False,
        "actual_J98_gate_fraction_P_or_new_delta_measured": False,
        "boundary": "Old evaluated divided intensities and LC/MC only under equal-response model; modern shared totals do not identify component weights. Unsigned ENSDF MR remains sign unknown."}
    assert result["all_modern_MR_fields_blank"]
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: result[k] for k in ["conditional_E2_fractions_equal_response",
        "old113_aggregate_photon_per100_central", "all_modern_MR_fields_blank",
        "rounded_level_energy_only_selector_rejected", "two_assumed_sign_predictions"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
