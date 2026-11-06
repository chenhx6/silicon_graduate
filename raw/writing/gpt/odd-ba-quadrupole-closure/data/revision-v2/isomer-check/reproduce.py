"""Portable replay of the frozen isomer benchmark and E2-width addendum.

Both original producers and both protocols remain byte-identical.
The strength and width jobs use separate relative-path layouts because
the frozen width protocol hashes the ORIGINAL strength result, whose
timestamps cannot equal those of a newly generated strength result.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess

PACKAGE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def within(path, root):
    return path == root or root in path.parents


def relative_path(root, name):
    path = (root / name).resolve()
    if Path(name).is_absolute() or not within(path, root.resolve()):
        raise ValueError(f"nonlocal package/layout path: {name}")
    return path


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(json.dumps(value, indent=2, allow_nan=False) + "\n")


def copy_exact(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    shutil.copyfile(source, target)
    if sha(source) != sha(target):
        raise RuntimeError(f"copy hash mismatch: {source}")


def compare(expected, actual, policy, path="", omissions=frozenset()):
    """Recursively compare every field except explicitly listed root metadata."""
    discrepancies, maxima = [], {}

    def walk(a, b, where, key):
        if isinstance(a, dict):
            if not isinstance(b, dict):
                discrepancies.append({"path": where, "reason": "type"})
                return
            ak = set(a) - (set(omissions) if where == path else set())
            bk = set(b) - (set(omissions) if where == path else set())
            if ak != bk:
                discrepancies.append({"path": where, "reason": "keys",
                                      "expected": sorted(ak), "actual": sorted(bk)})
            for k in sorted(ak & bk):
                walk(a[k], b[k], where + "/" + k, k)
        elif isinstance(a, list):
            if not isinstance(b, list) or len(a) != len(b):
                discrepancies.append({"path": where, "reason": "list-length"})
                return
            for i, (x, y) in enumerate(zip(a, b)):
                walk(x, y, where + f"/{i}", key)
        elif isinstance(a, bool) or a is None or isinstance(a, str):
            if type(a) is not type(b) or a != b:
                discrepancies.append({"path": where, "reason": "exact-value",
                                      "expected": a, "actual": b})
        elif isinstance(a, int):
            if isinstance(b, bool) or not isinstance(b, int) or a != b:
                discrepancies.append({"path": where, "reason": "integer",
                                      "expected": a, "actual": b})
        elif isinstance(a, float):
            if not isinstance(b, (float, int)) or not math.isfinite(b):
                discrepancies.append({"path": where, "reason": "nonfinite-or-type"})
                return
            if "rate_s_inverse" in key:
                kind = "rates"
            elif "half_life_upper_bound_ns" in key:
                kind = "half_life_bounds"
            elif key.endswith("_MeV") or key.endswith("_MeV2") or key.endswith("_keV"):
                kind = "energies"
            else:
                kind = "other_floats"
            limit = policy[kind]
            absolute = abs(a - b)
            relative = absolute / max(abs(a), abs(b), 1e-300)
            maximum = maxima.setdefault(kind, {"maximum_absolute": 0.,
                                                "maximum_relative": 0.,
                                                "comparisons": 0})
            maximum["maximum_absolute"] = max(maximum["maximum_absolute"], absolute)
            maximum["maximum_relative"] = max(maximum["maximum_relative"], relative)
            maximum["comparisons"] += 1
            if absolute > limit["atol"] + limit["rtol"] * abs(a):
                discrepancies.append({"path": where, "reason": "numeric-tolerance",
                                      "expected": a, "actual": b, "absolute": absolute,
                                      "relative": relative, "policy": limit})
        elif a != b:
            discrepancies.append({"path": where, "reason": "unhandled-value"})

    walk(expected, actual, path, "")
    return {"pass": not discrepancies, "discrepancies": discrepancies,
            "numeric_maxima": maxima, "omitted_root_metadata": sorted(omissions)}


def typed_csv(path, templates):
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        records = list(reader)
        header = reader.fieldnames
    if len(records) != len(templates) or header != list(templates[0]):
        raise ValueError(f"CSV schema/row-count mismatch: {path}")
    converted = []
    for record, template in zip(records, templates):
        row = {}
        for key, reference in template.items():
            value = record[key]
            if isinstance(reference, bool):
                if value not in ("True", "False"):
                    raise ValueError("invalid CSV boolean")
                row[key] = value == "True"
            elif isinstance(reference, int):
                row[key] = int(value)
            elif isinstance(reference, float):
                row[key] = float(value)
            elif reference is None:
                if value:
                    raise ValueError("nonempty CSV null")
                row[key] = None
            else:
                row[key] = value
        converted.append(row)
    return converted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New independent run directory; never reuse one.")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(output)
    # Keep immutable package bytes separate from all generated products.
    if within(output, PACKAGE):
        raise ValueError("--output must be outside the package directory")
    output.mkdir(parents=True)
    started = datetime.now(timezone.utc).isoformat()
    inventory_path = PACKAGE / "inventory.json"
    inventory = json.loads(inventory_path.read_text())
    for item in inventory["files"]:
        p = relative_path(PACKAGE, item["path"])
        if p.is_symlink() or not p.is_file() or sha(p) != item["sha256"]:
            raise RuntimeError(f"payload verification failed: {item['path']}")
        if p.stat().st_size != item["size"]:
            raise RuntimeError(f"payload size mismatch: {item['path']}")
    layout = json.loads((PACKAGE / "layout.json").read_text())
    policy = json.loads((PACKAGE / "comparison-policy.json").read_text())
    worker_receipts = []
    stage_outputs = {}
    for stage in ("strength", "width"):
        stage_root = output / f"{stage}-layout"
        producer_dir = relative_path(stage_root, layout["producer_directory"])
        producer_dir.mkdir(parents=True)
        for item in layout["common_inputs"]:
            copy_exact(relative_path(PACKAGE, item["package_path"]),
                       relative_path(stage_root, item["original_relative_path"]))
        for item in layout["original_producers"]:
            copy_exact(relative_path(PACKAGE, item["package_path"]),
                       producer_dir / item["filename"])
        for item in layout["stage_inputs"][stage]:
            copy_exact(relative_path(PACKAGE, item["package_path"]),
                       producer_dir / item["filename"])
        # ROOT=parents[4] in the original producer must resolve to this root.
        assert (producer_dir / "run_benchmark.py").resolve().parents[4] == stage_root
        assert not (stage_root / "raw").exists()
        script = producer_dir / ("run_benchmark.py" if stage == "strength"
                                 else "run_decay_widths.py")
        worker_receipt = output / f"{stage}-read-boundary.json"
        env = os.environ.copy()
        env.update({
            "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1",
            "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1", "PYTHONPATH": "",
        })
        command = [
            sys.executable, "-I", "-B", str(PACKAGE / "guarded_worker.py"),
            "--script", str(script), "--package", str(PACKAGE),
            "--run-root", str(output), "--receipt", str(worker_receipt),
        ]
        print(f"Running unchanged {stage} producer", flush=True)
        with (output / f"{stage}.stdout.log").open("x") as stdout, (
            output / f"{stage}.stderr.log").open("x") as stderr:
            done = subprocess.run(command, cwd=stage_root, env=env,
                                  stdout=stdout, stderr=stderr, check=False)
        worker = json.loads(worker_receipt.read_text())
        worker_receipts.append(worker)
        if done.returncode or worker["status"] != "passed":
            raise RuntimeError(f"{stage} producer failed; see {worker_receipt}")
        stage_outputs[stage] = producer_dir

    def load(path):
        return json.loads(path.read_text())

    expected_strength = load(PACKAGE / "frozen/results.json")
    actual_strength = load(stage_outputs["strength"] / "results.json")
    expected_mapping = load(PACKAGE / "frozen/energy-mapping-frozen.json")
    actual_mapping = load(stage_outputs["strength"] / "energy-mapping-frozen.json")
    expected_width = load(PACKAGE / "frozen/decay-width-results.json")
    actual_width = load(stage_outputs["width"] / "decay-width-results.json")
    strength = compare(
        expected_strength, actual_strength, policy, "strength",
        frozenset({"started_at_utc", "finished_at_utc", "elapsed_seconds",
                   "energy_mapping_record_sha256", "state_basis_sha256"}),
    )
    strength["state_basis_sha256_equal"] = (
        expected_strength["state_basis_sha256"] == actual_strength["state_basis_sha256"])
    strength["basis_hash_boundary"] = (
        "Exact eigenvector bytes are reported separately; physical-field comparisons "
        "include the stored signed RMEs, energies, interference and all strengths.")
    mapping = compare(expected_mapping, actual_mapping, policy, "mapping",
                      frozenset({"at_utc"}))
    width = compare(expected_width, actual_width, policy, "width",
                    frozenset({"started_at_utc", "finished_at_utc"}))
    strength_csv = compare(
        typed_csv(PACKAGE / "frozen/predictions.csv", expected_strength["rows"]),
        typed_csv(stage_outputs["strength"] / "predictions.csv", actual_strength["rows"]),
        policy, "strength_csv",
    )
    width_csv = compare(
        typed_csv(PACKAGE / "frozen/decay-width-summary.csv", expected_width["rows"]),
        typed_csv(stage_outputs["width"] / "decay-width-summary.csv", actual_width["rows"]),
        policy, "width_csv",
    )
    count_check = {
        "strength_rows": len(actual_strength["rows"]),
        "width_sums": len(actual_width["rows"]),
        "open_branches": len(actual_width["branches"]),
        "energy_mapping_pairs": len(actual_mapping["pairs"]),
    }
    assert count_check == {"strength_rows": 28, "width_sums": 14,
                           "open_branches": 84, "energy_mapping_pairs": 4}
    compare_report = {
        "policy": policy, "strength": strength, "energy_mapping": mapping,
        "width_and_branches": width, "counts": count_check,
        "strength_csv": strength_csv, "width_csv": width_csv,
        "pass": all(x["pass"] for x in (strength, mapping, width, strength_csv, width_csv)),
    }
    write_new(output / "comparison.json", compare_report)
    generated = {}
    for stage, names in {
        "strength": ["energy-mapping-frozen.json", "results.json", "predictions.csv"],
        "width": ["decay-width-results.json", "decay-width-summary.csv"],
    }.items():
        for name in names:
            source = stage_outputs[stage] / name
            target = output / "reproduced" / name
            copy_exact(source, target)
            generated[str(target.relative_to(output))] = {
                "sha256": sha(target), "size": target.stat().st_size}
    unchanged = all(sha(relative_path(PACKAGE, x["path"])) == x["sha256"]
                    for x in inventory["files"])
    assert unchanged
    receipt = {
        "schema": "137Ba-isomer-standalone-reproduction/1",
        "started_at_actual_utc": started,
        "finished_at_actual_utc": datetime.now(timezone.utc).isoformat(),
        "pass": compare_report["pass"],
        "payload_inventory_sha256": sha(inventory_path),
        "verified_payload_files": len(inventory["files"]),
        "original_producer_and_protocol_bytes_unchanged": True,
        "staged_protocol_sha_checks": (
            "Both producers executed their original real-file hash checks. "
            "No sha verifier was replaced and no protocol field was rewritten."),
        "width_base_results_scope": (
            "The width layout supplies the packaged ORIGINAL results.json as "
            "the original width protocol's hash prerequisite. Regenerated "
            "strengths are independently compared in the strength layout; "
            "they are not falsely claimed to have the historical file hash."),
        "scientific_counts": count_check,
        "comparison_sha256": sha(output / "comparison.json"),
        "generated_products": generated,
        "worker_boundary_reports": {
            f"{stage}-read-boundary.json": sha(output / f"{stage}-read-boundary.json")
            for stage in ("strength", "width")},
        "runtime": worker_receipts[0]["versions"],
        "read_boundary": {
            "forbidden_read_probe_blocked_in_both_workers":
                all(x["intentional_forbidden_read_probe_blocked"] for x in worker_receipts),
            "unexpected_denied_accesses":
                [x for w in worker_receipts for x in w["unexpected_denied_accesses"]],
            "network_or_nested_process_attempts":
                [x for w in worker_receipts for x in w["network_or_subprocess_attempts"]],
            "staged_raw_source_directories_present": False,
            "external_raw_source_hashes_reverified": [],
            "scope": "Python-level file audit plus isolated relative layout; not an OS security sandbox",
        },
        "payload_unchanged_after_run": unchanged,
        "interpretation_boundary": (
            "Reproduces frozen mathematical results only. Experimental source "
            "claims inside input snapshots are historical declarations, not "
            "fresh verification of unbundled PDFs, ENSDF files, pages or prior runs."),
    }
    write_new(output / "receipt.json", receipt)
    print(json.dumps({"pass": receipt["pass"], "counts": count_check,
                      "runtime": receipt["runtime"]}, indent=2), flush=True)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
