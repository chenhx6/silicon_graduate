#!/usr/bin/env python3
"""Build and check the immutable v0.1.1 literature job snapshots."""

import argparse
from copy import deepcopy
from hashlib import sha256
import json
import math
from pathlib import Path


VERSION = "grouped_geometry_v0_1_1"
CASES = Path(__file__).resolve().parents[1] / "cases"
MAIN_FILES = ("point_angle_ado_jobs.json", "point_angle_dco_scenarios.json")


def digest(data):
    return sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=True, allow_nan=False) + "\n").encode()


def group(*angles):
    return {"directions": [
        {"theta_deg": theta, "weight": weight} for theta, weight in angles
    ], "normalization": "mean"}


def replay_grid(job):
    reference_transition = job["target"] if job.get("target_first", True) else job["gate"]
    spin = reference_transition["spin_initial"]
    return {
        "xi_min_rad": math.radians(-89.9),
        "xi_max_rad": math.radians(89.9),
        "xi_step_rad": math.radians(0.1),
        "sigma_step": 0.005 * spin,
        "xi_input_unit": "deg",
        "sigma_input_unit": "sigma/I",
    }


def model_job(source, nuclide):
    job = deepcopy(source)
    geometry = job["geometry"]
    if nuclide == "135Pr":
        geometry = {
            "ratio_group_a": group((157.6, 2), (133.6, 1)),
            "ratio_group_b": group((75.5, 1)),
            "polarization_group": group((75.5, 1)),
            "select_azimuth": False,
        }
    elif nuclide in ("154Tb", "190Tl"):
        geometry = {
            "ratio_group_a": group((geometry["theta_a_deg"], 1)),
            "ratio_group_b": group((geometry["theta_b_deg"], 1)),
            "polarization_group": group((geometry["theta_p_deg"], 1)),
            "ratio_azimuth_average": True,
            "select_azimuth": False,
        }
    job["geometry"] = geometry
    job["grid"] = replay_grid(job)
    return job


def reported_delta(text, center, minus, plus, locator):
    return {"reported_delta": text, "center": center, "minus": minus, "plus": plus,
            "locator": locator}


def comparison(job, candidates):
    label = job["label"]
    candidate = candidates.get(label)
    nuclide, energy, _ = label.split()
    branches = deepcopy(candidate["selection_only"]) if candidate else []
    for branch in branches:
        branch["locator"] = candidate["source_locator"]
    if label == "154Tb 229.7 keV":
        branches.append(reported_delta("2.86 +2.31/-1.10", 2.86, 1.10, 2.31, "PDF p. 8 Table 1"))
    if label == "190Tl 272.1 keV":
        branches.append(reported_delta("0.078(18)", 0.078, 0.018, 0.018,
                                       "PDF p. 6 Sec. 4, weighted average"))
    angle = None
    if label == "164Yb 490 keV" and len(job["target"]["multipoles"]) == 2:
        angle = {"center_deg": -21, "approximate": True, "locator": "Sec. 6, Tables 2-3"}
        branch = reported_delta("arctan(delta) approximately -21 deg",
                                math.tan(math.radians(-21)), None, None, angle["locator"])
        branch["coordinate"] = "tangent of approximate reported angle"
        branches.append(branch)
    source_sigma = {
        "80Se": {"value": 0.35, "kind": "fixed_setting", "source_coordinate": "sigma/j",
                 "locator": "Publisher supplement p. 3, DCO calculations"},
        "164Yb": {"value": 0.26, "err_minus": 0.05, "err_plus": 0.05,
                  "kind": "647 keV alignment calibration", "source_coordinate": "sigma/I",
                  "locator": "Fig. 4, 647 keV pure-E1 calibration"},
    }.get(nuclide)
    for branch in branches:
        if branch["minus"] is None or branch["plus"] is None:
            branch["error_type"] = "unreported"
        else:
            branch["error_type"] = (
                "quoted_symmetric" if branch["minus"] == branch["plus"] else "quoted_asymmetric"
            )
    return {
        "nuclide": nuclide, "energy_keV": float(energy),
        "nuclear_class": candidate["nuclear_class"] if candidate else {
            "154Tb": "odd-odd", "190Tl": "odd-odd", "164Yb": "even-even",
        }[nuclide],
        "delta_branches": branches, "arctan_delta_reference": angle,
        "sigma_over_i_reference": source_sigma,
    }


def freeze_row(originals, declaration, filename, file_hash, candidates, role):
    number, original = originals[0]
    source_value = {key: value for key, value in original.items() if key != "geometry"}
    if any({key: value for key, value in row.items() if key != "geometry"} != source_value
           for _, row in originals):
        raise ValueError(f"{filename}: attempted to combine distinct observations or cascade scopes")
    nuclide = original["label"].split()[0]
    job = model_job(original, nuclide)
    if filename in MAIN_FILES:
        case_id = f"{job['mode'].lower()}_{number:02d}"
    else:
        case_id = f"{Path(filename).stem}_{number:02d}"
    return {
        "case_id": case_id, "role": role,
        "source_job_file": filename, "source_job_file_sha256": file_hash,
        "historical_jobs": [{"job_number": index, "job": row} for index, row in originals],
        "source_declaration": declaration,
        "literature": comparison(job, candidates),
        "job": job,
    }


def build_snapshots():
    wiki = CASES.parents[4]
    legacy_files = {}

    def read(path):
        data = path.read_bytes()
        legacy_files[path.relative_to(CASES).as_posix()] = digest(data)
        return json.loads(data)

    readiness = read(CASES / "modeling_readiness.json")
    archive = read(CASES / "empirical_manifest.json")
    candidates = {row["display"]: row for row in read(CASES / "candidates.json")["candidates"]}
    e03_path = CASES.parent / "research" / "geometry" / "results.json"
    e03_bytes = e03_path.read_bytes()
    e03 = json.loads(e03_bytes)
    for entry in e03["sources"]:
        if digest((wiki / entry["path"]).read_bytes()) != entry["sha256"]:
            raise ValueError(f"E03 source hash mismatch: {entry['path']}")
    sources = {}
    main = []
    by_label = {row["display"]: row for row in readiness["cases"]}
    for filename in MAIN_FILES:
        jobs = read(CASES / filename)["jobs"]
        file_hash = legacy_files[filename]
        if readiness["job_file_provenance"][filename] != {"sha256": file_hash, "jobs": len(jobs)}:
            raise ValueError(f"{filename}: readiness hash/count mismatch")
        for number, job in enumerate(jobs, 1):
            declared = by_label[job["label"]]
            observation_source = declared["observation_source"]
            reference = observation_source["reference"]
            sources[reference] = readiness["sources"][reference]
            model = declared["point_angle"][job["mode"]]
            method = model.get("geometry_method_reference")
            if method:
                sources[method] = readiness["sources"][method]
            row = freeze_row([(number, job)], {
                "observation_source": observation_source,
                "historical_model": {key: value for key, value in model.items() if key != "scenarios"},
            }, filename, file_hash, candidates, "declared_alternative" if
                              job["mode"] == "P_DCO" else "main")
            if job["label"].startswith("135Pr "):
                row["source_declaration"]["replay_geometry"] = {
                    "model": "effective weighted mean of intensities",
                    "geometry_research": "E03",
                    "geometry_research_sha256": digest(e03_bytes),
                    "sources": e03["sources"],
                }
            main.append(row)

    source_only = read(CASES / "followup" / "source_only_audit.json")
    scope = read(CASES / "followup" / "coverage_followup.json")
    historical_manifest = read(CASES / "followup" / "scenarios.json")
    followup = []
    for batch in historical_manifest["batches"]:
        filename = batch["file"]
        jobs = read(CASES / "followup" / filename)["jobs"]
        file_hash = legacy_files[f"followup/{filename}"]
        if file_hash != batch["sha256"]:
            raise ValueError(f"{filename}: frozen follow-up hash mismatch")
        nuclide = batch["nuclide"]
        batches = [[entry] for entry in enumerate(jobs, 1)]
        if nuclide in ("154Tb", "190Tl"):
            if len(jobs) != (6 if nuclide == "154Tb" else 8):
                raise ValueError(f"{filename}: unexpected historical scenario count")
            batches = [sum(batches[start:start + 3], []) for start in (0, 3)] + batches[6:]
        for entries in batches:
            number = entries[0][0]
            role = "declared_alternative"
            declaration = {"historical_batch": batch}
            if nuclide in ("154Tb", "190Tl"):
                role = "readout_sensitivity" if number > 6 else "main"
                declaration["replay_geometry"] = {
                    "model": "ideal uniformly weighted rings; no relative azimuth selection",
                    "scope": "Retains the sourced ratio order and the single-line P proxy.",
                    "historical_phi_role": "Exploratory point scenarios; physical azimuth unreported.",
                }
            if nuclide in ("154Tb", "185Au"):
                key = "R033" if nuclide == "154Tb" else "R034"
                declaration["observation_source"] = {"reference": key}
                sources[key] = readiness["sources"][key]
            else:
                key = "Pal2025" if nuclide == "190Tl" else "Starosta1999"
                declaration["observation_source"] = {"reference": key}
                sources[key] = source_only["sources"][key]
            followup.append(freeze_row(entries, declaration, filename, file_hash, candidates, role))

    archive_paths = {row["sha256"]: row for row in archive["files"]}
    sources["B26"] = deepcopy(sources["B26"])
    supplement = next(row for row in archive["files"]
                      if row["path"].endswith("/Biswas2026_80Se_supplement.pdf"))
    sources["B26"]["audited_files"].append({
        "role": "supplement", "bytes": supplement["size"],
        **{key: supplement[key] for key in ("path", "sha256", "archive_required")},
    })
    for key in ("Pal2025", "Starosta1999", "Palit2000", "Duchene1999"):
        sources[key] = deepcopy(source_only["sources"][key])
        entry = archive_paths.get(sources[key]["sha256"])
        if entry:
            sources[key]["archived_path"] = entry["path"]
    for source in sources.values():
        files = source.get("audited_files", ())
        if "archived_path" in source:
            files = ({"path": source["archived_path"], "sha256": source["sha256"]},)
        for entry in files:
            if digest((wiki / entry["path"]).read_bytes()) != entry["sha256"]:
                raise ValueError(f"Literature hash mismatch: {entry['path']}")

    return {
        CASES / VERSION: {"batch": "literature", "cases": main},
        CASES / "followup" / VERSION: {
            "batch": "followup", "cases": followup, "selection_policy": historical_manifest["selection_policy"],
            "source_audits": {"154Tb": scope["tb"], "164Yb": source_only["164Yb_conditional_P"],
                              "190Tl": source_only["190Tl_observation_contract"]},
        },
    }, sources, legacy_files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Require both snapshots to already exist")
    args = parser.parse_args()
    snapshots, sources, legacy_files = build_snapshots()
    payloads = {}
    for directory, snapshot in snapshots.items():
        snapshot.update(schema=VERSION, sources=sources, legacy_inputs_sha256=legacy_files)
        payload = json_bytes(snapshot)
        payloads[directory / "snapshot.json"] = payload
        payloads[directory / "manifest.json"] = json_bytes({
            "schema": VERSION, "snapshot_sha256": digest(payload),
            "jobs": len(snapshot["cases"]), "archive_required": True,
        })
    for path, payload in payloads.items():
        if path.exists() and path.read_bytes() != payload:
            raise ValueError(f"Frozen snapshot differs: {path}")
        if args.check and not path.is_file():
            raise ValueError(f"Frozen snapshot is missing: {path}")
    for path, payload in payloads.items():
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(payload)
        print(f"{path.relative_to(CASES)} {digest(payload)}")


if __name__ == "__main__":
    main()
