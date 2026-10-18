#!/usr/bin/env python3
"""Audit frozen A=25 ENSDF identities and the version/phase crosswalk.

The weighted means replay a declared independent-error arithmetic model, not
the evaluator's unpublished procedure or the underlying experimental fits.
No lifetime, transition-strength, or new experimental delta is inferred.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def records(path: Path) -> dict:
    lines = path.read_text().splitlines()
    levels, gammas, parent, current = [], [], None, None
    for no, raw in enumerate(lines, 1):
        s = raw.ljust(80)
        if s[5:7] == "  " and s[7] == "L":
            parent = {"line": no, "E": s[9:19].strip(),
                      "DE": s[19:21].strip(), "Jpi": s[21:39].strip()}
            levels.append(parent)
            current = None
        elif s[5:7] == "  " and s[7] == "G":
            current = {"line": no, "parent": parent, "E": s[9:19].strip(),
                       "DE": s[19:21].strip(), "M": s[31:41].strip(),
                       "MR": s[41:49].strip(), "DMR": s[49:55].strip(),
                       "flags": s[76:77].strip(), "raw": raw, "attached": []}
            gammas.append(current)
        elif s[7] == "G" and current is not None:
            if ("FLAG=" in s or "A2=" in s or "POL=" in s
                    or any(token in s for token in ["MR$", "MR,", "M,MR$", "M$", "E$"])):
                current["attached"].append({"line": no, "raw": raw})
            if "FLAG=" in s:
                current["flags"] += s.split("FLAG=", 1)[1].strip()
    return {"lines": lines, "levels": levels, "gammas": gammas}


def select(data: dict, parent: str, energy: str) -> dict:
    found = [g for g in data["gammas"] if g["parent"]["E"] == parent
             and g["E"] == energy]
    if len(found) != 1:
        raise ValueError(f"Ambiguous or missing identity: {parent}, {energy}")
    return found[0]


def weighted(items: list[dict]) -> dict:
    w = [1 / c["sigma"]**2 for c in items]
    mean = sum(a*c["MR"] for a, c in zip(w, items)) / sum(w)
    return {"central": mean, "sigma_if_independent": math.sqrt(1/sum(w)),
            "weights_normalized": [x/sum(w) for x in w],
            "sum_squared_residuals": sum(a*(c["MR"]-mean)**2 for a, c in zip(w, items)),
            "independence_established": False,
            "evaluator_error_algorithm_recovered": False}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "A25-GRETINA-TARGET-AND-MR-CROSSWALK-02"
    basepath = Path(cfg["base_input"])
    assert sha(basepath) == cfg["base_input_sha256"]
    base = json.loads(basepath.read_text())
    objects = {}
    for item in base["object_snapshots"]:
        path = Path(item["path"])
        assert sha(path) == item["sha256"]
        objects[item["label"]] = records(path)
        assert len(objects[item["label"]]["lines"]) == item["lines"]
    oldspec = cfg["archive_object"]
    oldpath = Path(oldspec["path"])
    assert sha(oldpath) == oldspec["sha256"]
    old = records(oldpath)
    assert "CUT=1-Feb-2008" in "\n".join(old["lines"])
    assert "09NDS    200908" in old["lines"][0]
    targets = []
    for case in base["selected_target_cases"]:
        data = objects[case["object"]]
        g = select(data, case["parent_E"], case["gamma_E"])
        for field in ["M", "MR", "DMR"]:
            if field in case:
                assert g[field] == case[field], (case["label"], field, g[field])
        child = [l for l in data["levels"] if l["E"] == case["candidate_child_E"]]
        assert len(child) == 1
        gap = float(g["parent"]["E"]) - float(child[0]["E"])
        # M=25u is a declared scale estimate, not an evaluated nuclear mass.
        recoil = float(g["E"])**2 / (2*25*931494.10242)
        targets.append({"label": case["label"], "gamma": g, "candidate_child": child[0],
                        "gap_minus_Egamma_keV": gap-float(g["E"]),
                        "recoil_scale_M25u_keV": recoil,
                        "gap_minus_Egamma_minus_recoil_keV": gap-float(g["E"])-recoil,
                        "energy_covariance_known": False})
    old_targets = []
    for case, cited in zip(cfg["old_target_cases"], base["L26_old2009_RB_knownMR"]):
        g = select(old, case["parent_E"], case["gamma_E"])
        assert all(g[field] == case[field] for field in ["M", "MR", "DMR"])
        assert -float(g["MR"]) == cited["d_RB"]
        unit = 10**(-len(g["MR"].split(".")[1]))
        assert math.isclose(int(g["DMR"])*unit, cited["sigma"], abs_tol=1e-14)
        old_targets.append({"gamma": g, "delta_RB_after_declared_KS_bridge": -float(g["MR"]),
                            "matches_L26_cited_value_and_error": True})
    flagged = []
    for case in cfg["reference_flag_expectations"]:
        g = select(objects[case["object"]], case["parent_E"], case["gamma_E"])
        assert all(g[f] == case[f] for f in ["MR", "DMR"])
        for f in ["energy_flag", "MR_flag"]:
            if case[f]:
                assert case[f] in g["flags"]
        if case["MR_flag"] == "F":
            assert "MR(F)$From 1972Ke13" in "\n".join(objects[case["object"]]["lines"])
            assert "MR$From 1975Bu14 except as noted" in "\n".join(objects[case["object"]]["lines"])
        flagged.append({"gamma": g, "provenance_after_field_override": case["provenance"]})
    nx = select(objects["25Na-new-XUNDL"], "3459", "1041")
    attached = "\n".join(r["raw"] for r in nx["attached"])
    assert nx["MR"] == nx["DMR"] == ""
    assert "MR$0.0 {I2}" in attached and "POL=+0.043 8" in attached
    mx = select(objects["25Mg-new-XUNDL"], "3971", "3971")
    assert "POL=+0.025 8" in "\n".join(r["raw"] for r in mx["attached"])
    assert all(g["MR"] == "" for label in ["25Na-new-XUNDL", "25Mg-new-XUNDL"]
               for g in objects[label]["gammas"])
    # Actual field flags fail a naive default-reference assignment at3970.
    assert flagged[-1]["provenance_after_field_override"] != "default1975Bu14"
    # A missing MR is semantically different from a measured numerical zero.
    assert number(nx["MR"]) is None and number("0.0") == 0.0
    wm1612 = weighted(base["current1612_adopted_weighted_components"])
    wm1793 = weighted(base["current1793_adopted_weighted_components"])
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input),
              "script_sha256": sha(Path(__file__)), "objects_verified": len(objects)+1,
              "current_targets": targets, "old_targets": old_targets,
              "reference_flag_audit": flagged,
              "conditional_weighted_means": {"1612": wm1612, "1793": wm1793},
              "adopted_1793_sigma": 0.02,
              "adopted_1793_sigma_is_not_literal_independent_formula": not math.isclose(wm1793["sigma_if_independent"], .02, abs_tol=.005),
              "XUNDL_Na1041_MR_stored_in_comment_not_numeric_field": True,
              "XUNDL_POL_matches_source_A0_object_not_physical_P": True,
              "XUNDL_Mg3971_gamma": mx,
              "XUNDL3971_not_nearest_keV_of_current_adopted3970p3": round(3970.3) != int(mx["E"]),
              "independent_new_XUNDL_experiment": False,
              "joint_covariance_or_experimental_refit_recovered": False,
              "all_identity_and_failure_controls_passed": True}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k not in
                     ["current_targets", "old_targets", "reference_flag_audit", "XUNDL_Mg3971_gamma"]},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
