#!/usr/bin/env python3
"""Audit selected official104Mo objects without treating labels as new delta.

Keeps object-specific level/gamma energies, explicit empty MR fields, band
markers and the pre-2018 evaluation boundary. Time conversion only checks the
identity of an EL18 calibration input; it is not a lifetime remeasurement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def records(path: Path) -> dict:
    lines = path.read_text().splitlines()
    levels, gammas, parent = [], [], None
    for no, raw in enumerate(lines, 1):
        s = raw.ljust(80)
        if s[:5] != "104MO":
            continue
        if s[5:7] == "  " and s[7] == "L":
            parent = {"line": no, "energy": float(s[9:19]),
                      "energy_uncertainty_literal": s[19:21],
                      "Jpi": s[21:39].strip(), "T_literal": s[39:49].strip(),
                      "DT_literal": s[49:55].strip(), "band_marker": s[76], "raw": raw}
            levels.append(parent)
        elif s[5:7] == "  " and s[7] == "G":
            gammas.append({"line": no, "energy": float(s[9:19]),
                           "energy_uncertainty_literal": s[19:21], "parent": parent,
                           "RI_literal": s[21:29], "DRI_literal": s[29:31],
                           "M_literal": s[31:41].strip(), "MR_literal": s[41:49].strip(),
                           "DMR_literal": s[49:55].strip(), "CC_literal": s[55:62].strip(),
                           "raw": raw})
    return {"lines": lines, "levels": levels, "gammas": gammas}


def gamma(data: dict, parent: float, energy: float) -> dict:
    selected = [r for r in data["gammas"] if abs(r["parent"]["energy"] - parent) < 1e-6
                and abs(r["energy"] - energy) < 1e-6]
    assert len(selected) == 1, (parent, energy, len(selected))
    return selected[0]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--objects-dir", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "DAY16-N104-EL18-REFERENCE-CROSSWALK-01"
    d = {}
    for item in cfg["objects"]:
        path = a.objects_dir / (item["record"] + ".ens")
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        d[item["record"]] = records(path)
    companion = a.objects_dir / "104042004.ens"
    assert hashlib.sha256(companion.read_bytes()).hexdigest() == "d00045878869edafeb02a3e76e5c0928a4565ff1571ac5dbd679735227e4c3a6"
    d["104042004"] = records(companion)
    adopted, cf, cm = [d[k] for k in ["104042001", "104042005", "104042004"]]
    target_ad = gamma(adopted, 1028.35, 836.3)
    target_cf = gamma(cf, 1027.9, 835.5)
    target_cm = gamma(cm, 1028.0, 835.8)
    ref_ad, ref_cf, ref_cm = [gamma(t, parent, energy) for t, parent, energy in
                             [(adopted, 192.19, 192.2), (cf, 192.4, 192.4), (cm, 192.1, 192.0)]]
    assert target_ad["parent"]["Jpi"] == target_cf["parent"]["Jpi"] == target_cm["parent"]["Jpi"] == "3+"
    assert target_ad["parent"]["band_marker"] == target_cf["parent"]["band_marker"] == target_cm["parent"]["band_marker"] == "B"
    assert target_ad["M_literal"] == "M1" and target_cf["M_literal"] == target_cm["M_literal"] == ""
    assert all(x["MR_literal"] == x["DMR_literal"] == "" for x in
               [target_ad, target_cf, target_cm, ref_ad, ref_cf, ref_cm])
    assert "M$From DCO in {+248}Cm SF decay" in "\n".join(adopted["lines"])
    assert "CUT=30-Mar-2007" in "\n".join(adopted["lines"])
    # No target-specific DCO ratio/geometry is actually supplied by the Cm object.
    assert "DCO" not in "\n".join(cm["lines"])
    calibration = next(x for x in adopted["levels"] if x["energy"] == 192.19)
    assert calibration["T_literal"] == "0.97 NS" and calibration["DT_literal"] == "8"
    time = cfg["calibration_time_conversion_only"]
    mean_time = [v / math.log(2) for v in time["source_half_life_ns"]]
    feeders = {"adopted555p5": gamma(adopted, 1583.5, 555.5),
               "Cf555p5": gamma(cf, 1583.4, 555.5),
               "Cf477p4": gamma(cf, 2060.8, 477.4)}
    result = {"identity": cfg["identity"],
              "input_sha256": hashlib.sha256(a.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "targets": {"adopted": target_ad, "Cf": target_cf, "Cm": target_cm},
              "references": {"adopted": ref_ad, "Cf": ref_cf, "Cm": ref_cm},
              "selected_feeders": feeders,
              "band_B_identification": "B=GAMMA BAND/gamma band in these objects; permits a band/spin crosswalk, not a certified EL18 peak-ledger match.",
              "adopted_target_energy_closure_residual_keV": 1028.35 - 836.3 - 192.19,
              "Cf_target_energy_closure_residual_keV": 1027.9 - 835.5 - 192.4,
              "energies_averaged_or_silently_substituted": False,
              "all_selected_target_and_reference_MR_fields_empty": True,
              "adopted_M_source_rule": "DCO in248Cm object; inspected96line object gives no actual target DCO ratio, reference gate, angles or MR.",
              "cutoff_precedes_EL18": True,
              "evaluation_base": "200709/07NDS, 30-Mar-2007 cutoff; adopted14-Dec-2007ERR and2012Q composite update do not create new2018gamma evaluation.",
              "calibration_mean_lifetime_conversion_ns": mean_time,
              "EL18_printed_calibration_tau_ns": time["EL18_mean_lifetime_ns"],
              "conversion_interpretation": "T1/2/ln2 matches1.40(.12) input precision; no new tau measurement or next-day card credit.",
              "all_internal_field_and_identity_checks_passed": True,
              "independent_EL18_delta_confirmation": False,
              "source_2018_actual_gate_response_covariance_recovered": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in result if k not in ["targets", "references", "selected_feeders"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
