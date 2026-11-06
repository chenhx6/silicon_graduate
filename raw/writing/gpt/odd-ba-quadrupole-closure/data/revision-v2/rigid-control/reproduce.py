#!/usr/bin/env python3
"""Replay the unchanged rigid-core producer using this package alone.

This adapter stages bytes, launches the original producer once, and compares
its outputs. It contains no Hamiltonian, E2, invariant, or proxy calculation.
"""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ATOL = 1e-10
RTOL = 1e-10
THREAD_KEYS = (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
)
SCIENTIFIC_KEYS = (
    "schema", "protocol_sha256", "driver_sha256", "frozen_input_sha256",
    "model", "finite_window", "preflight_blocks", "Euler_integral_checks",
    "geometric_operator_identity", "spectator_R0_checks", "high_I_boundary_check",
    "multiplet_rephasing_check", "adjacent_state_overlaps", "thread_environment",
    "boundary",
)


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_file(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError(f"Expected a safe relative file path: {relative!r}")
    path = (root / rel).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("File resolves outside its declared root")
    return path


def copy_exact(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as handle:
        handle.write(source.read_bytes())
    if digest(source) != digest(destination):
        raise RuntimeError(f"Copy digest mismatch: {destination.name}")


def write_json(path, data):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write("\n")


class Comparison:
    def __init__(self):
        self.numeric_values_checked = 0
        self.exact_values_checked = 0
        self.max_absolute_difference = 0.0
        self.max_difference_locator = None
        self.failures = []

    def compare(self, expected, actual, locator):
        if isinstance(expected, dict):
            if not isinstance(actual, dict) or set(expected) != set(actual):
                self.failures.append({"locator": locator, "reason": "Dictionary keys differ"})
                return
            for key in expected:
                self.compare(expected[key], actual[key], locator + "/" + str(key))
        elif isinstance(expected, list):
            if not isinstance(actual, list) or len(expected) != len(actual):
                self.failures.append({"locator": locator, "reason": "List length/type differs"})
                return
            for index, (left, right) in enumerate(zip(expected, actual)):
                self.compare(left, right, locator + "/" + str(index))
        elif isinstance(expected, bool) or expected is None or isinstance(expected, str):
            self.exact_values_checked += 1
            if type(actual) is not type(expected) or actual != expected:
                self.failures.append({"locator": locator, "expected": expected, "actual": actual})
        elif isinstance(expected, int):
            self.exact_values_checked += 1
            if type(actual) is not int or actual != expected:
                self.failures.append({"locator": locator, "expected": expected, "actual": actual})
        elif isinstance(expected, float):
            self.numeric_values_checked += 1
            if not isinstance(actual, (int, float)) or not math.isfinite(actual):
                self.failures.append({"locator": locator, "reason": "Nonfinite/non-numeric output"})
                return
            difference = abs(actual - expected)
            if difference > self.max_absolute_difference:
                self.max_absolute_difference = difference
                self.max_difference_locator = locator
            if difference > ATOL + RTOL * abs(expected):
                self.failures.append({
                    "locator": locator, "expected": expected, "actual": actual,
                    "absolute_difference": difference,
                })
        else:
            raise TypeError(f"Unhandled JSON type at {locator}")

    def record(self):
        return {
            "passed": not self.failures,
            "absolute_tolerance": ATOL, "relative_tolerance": RTOL,
            "numeric_values_checked": self.numeric_values_checked,
            "exact_values_checked": self.exact_values_checked,
            "max_absolute_difference": self.max_absolute_difference,
            "max_difference_locator": self.max_difference_locator,
            "failure_count": len(self.failures), "failures": self.failures,
        }


def scientific_payload(result):
    payload = {key: result[key] for key in SCIENTIFIC_KEYS}
    payload["cases"] = [
        {key: value for key, value in case.items() if key != "elapsed_seconds"}
        for case in result["cases"]
    ]
    return payload


def csv_records(path):
    def value(cell):
        if cell == "":
            return None
        try:
            return float(cell)
        except ValueError:
            return cell
    with path.open(newline="", encoding="utf-8") as handle:
        return [{key: value(cell) for key, cell in row.items()}
                for row in csv.DictReader(handle)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="New directory for the receipt, comparisons, and replayed outputs")
    parser.add_argument("--work-dir", type=Path,
                        help="New isolated virtual-root directory; default: a new system temp directory")
    args = parser.parse_args()
    package = Path(__file__).resolve().parent
    output = args.output_dir.resolve()
    if output.exists() or output.is_relative_to(package):
        parser.error("--output-dir must be a new directory outside the package")
    if args.work_dir:
        work = args.work_dir.resolve()
        if work.exists() or work.is_relative_to(package):
            parser.error("--work-dir must be a new directory outside the package")
        if work == output or work.is_relative_to(output) or output.is_relative_to(work):
            parser.error("Work and output directories must be disjoint")
    inventory_path = package / "inventory.json"
    inventory = json.loads(inventory_path.read_text())
    checked = []
    for entry in inventory["files"]:
        path = relative_file(package, entry["path"])
        actual = digest(path)
        if actual != entry["sha256"] or path.stat().st_size != entry["size"]:
            raise RuntimeError(f"Package integrity failed: {entry['path']}")
        checked.append({"path": entry["path"], "sha256": actual, "size": entry["size"]})
    output.mkdir(parents=True, exist_ok=False)
    if args.work_dir:
        work.mkdir(parents=True, exist_ok=False)
    else:
        work = Path(tempfile.mkdtemp(prefix="rigid-core-replay-")).resolve()
    copy_exact(inventory_path, output / "inventory-at-replay.json")
    stage_entries = [entry for entry in inventory["files"] if "virtual_root_relative_path" in entry]
    if len(stage_entries) != 5:
        raise RuntimeError("Expected exactly one protocol, one original producer, and three dependencies")
    producer = None
    staged = []
    for entry in stage_entries:
        source = relative_file(package, entry["path"])
        destination = relative_file(work, entry["virtual_root_relative_path"])
        copy_exact(source, destination)
        staged.append({
            "package_file": entry["path"], "virtual_root_relative_path": entry["virtual_root_relative_path"],
            "sha256": digest(destination), "role": entry["role"],
        })
        if entry["role"] == "original-producer":
            producer = destination
    if producer is None:
        raise RuntimeError("No original producer declared")
    files_before = sorted(str(path.relative_to(work)) for path in work.rglob("*") if path.is_file())
    protocol = json.loads((producer.parent / "protocol.json").read_text())
    for relative, expected in protocol["input_sha256"].items():
        if digest(relative_file(work, relative)) != expected:
            raise RuntimeError(f"Original protocol input hash mismatch: {relative}")
    environment = dict(os.environ)
    for key in THREAD_KEYS:
        environment[key] = "1"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment.pop("PYTHONPATH", None)
    command = [sys.executable, "-I", "-B", "-u", str(producer)]
    started = now()
    begun = time.perf_counter()
    with (output / "execution.log").open("x", encoding="utf-8") as log:
        process = subprocess.Popen(
            command, cwd=work, env=environment, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True,
        )
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        returncode = process.wait()
    process_seconds = time.perf_counter() - begun
    receipt = {
        "schema": "rigid-core-independent-packaged-replay-v1",
        "started_at_utc": started, "producer_finished_at_utc": now(),
        "producer_invocation_count": 1, "producer_returncode": returncode,
        "process_wall_seconds_including_import_startup": process_seconds,
        "package_inventory_snapshot": {
            "path": "inventory-at-replay.json", "sha256": digest(output / "inventory-at-replay.json"),
        },
        "adapter_sha256": digest(Path(__file__)),
        "original_producer_sha256": digest(producer),
        "checked_package_files": checked, "staged_runtime_inputs": staged,
        "execution": {
            "python_isolated_mode": True, "bytecode_writes_disabled": True,
            "producer_working_directory": str(work),
            "pre_execution_virtual_root_files": files_before,
            "command": command,
            "external_scientific_inputs_read": [],
            "data_source": "Package-local files only; source repository paths in metadata are not opened.",
            "thread_environment": {key: environment[key] for key in THREAD_KEYS},
            "python_version": sys.version.split()[0],
            "numpy_version": importlib.metadata.version("numpy"),
            "scipy_version": importlib.metadata.version("scipy"),
        },
        "comparison_exclusions": [
            "UTC timestamps", "wall/preflight/per-case elapsed times",
            "platform-specific loaded BLAS library names and availability of introspection",
        ],
        "replay_scope": "Original five C values and twenty proxy/count combinations only; no new grid or adjustment.",
    }
    if returncode:
        receipt.update(status="producer-failed", passed=False)
        write_json(output / "replay-receipt.json", receipt)
        return 1
    replay_dir = output / "replayed"
    replay_dir.mkdir()
    for name in ("results.json", "summary.csv", "cubic-spin-sectors.csv"):
        copy_exact(producer.parent / name, replay_dir / name)
    expected = json.loads((package / "frozen/results.json").read_text())
    actual = json.loads((replay_dir / "results.json").read_text())
    comparison = Comparison()
    comparison.compare(scientific_payload(expected), scientific_payload(actual), "results.json")
    comparison.compare(csv_records(package / "summary.csv"),
                       csv_records(replay_dir / "summary.csv"), "summary.csv")
    comparison.compare(csv_records(package / "frozen/cubic-spin-sectors.csv"),
                       csv_records(replay_dir / "cubic-spin-sectors.csv"), "cubic-spin-sectors.csv")
    reference_cases = expected["cases"]
    replay_cases = actual["cases"]
    proxy_rows, moment_rows = [], []
    for reference, replay in zip(reference_cases, replay_cases):
        moment_rows.append({
            "C_MeV": reference["C_MeV"],
            "q2_reference": reference["full_6j"]["q2"], "q2_replayed": replay["full_6j"]["q2"],
            "q3_reference": reference["full_6j"]["q3"], "q3_replayed": replay["full_6j"]["q3"],
            "q2_difference": replay["full_6j"]["q2"] - reference["full_6j"]["q2"],
            "q3_difference": replay["full_6j"]["q3"] - reference["full_6j"]["q3"],
        })
        for before, after in zip(reference["proxies"], replay["proxies"]):
            proxy_rows.append({
                "C_MeV": reference["C_MeV"], "n": before["n"] if before["n"] is not None else "all",
                "reference_raw_ratio": before["raw_ratio"], "replayed_raw_ratio": after["raw_ratio"],
                "raw_difference": after["raw_ratio"] - before["raw_ratio"],
                "reference_angle_deg": before["angle_deg"], "replayed_angle_deg": after["angle_deg"],
                "reference_domain": before["angle_status"], "replayed_domain": after["angle_status"],
            })
    with (output / "comparison-proxies.csv").open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(proxy_rows[0]))
        writer.writeheader()
        writer.writerows(proxy_rows)
    threads = actual["actual_loaded_BLAS_threads"]
    actual_thread_counts = [item["num_threads"] for item in threads if "num_threads" in item]
    invariants_ok = (
        [c["C_MeV"] for c in actual["cases"]] == [0, 1, 2, 4, 8]
        and len(proxy_rows) == 20
        and all(abs(c["full_6j"]["q2"] - 1) < 1e-9
                and abs(c["full_6j"]["q3"] - protocol["closure_scope"]["expected_q3"]) < 1e-9
                for c in actual["cases"])
        and all(count == 1 for count in actual_thread_counts)
    )
    unchanged_after_run = all(
        digest(relative_file(package, item["path"])) == item["sha256"] for item in checked
    )
    passed = comparison.record()["passed"] and invariants_ok and unchanged_after_run
    receipt.update({
        "status": "passed" if passed else "comparison-failed", "passed": passed,
        "comparison": comparison.record(),
        "all_twenty_proxy_comparisons": proxy_rows, "five_full_moment_comparisons": moment_rows,
        "key_validation_values": {
            "geometric_operator_identity": actual["geometric_operator_identity"],
            "Euler_integral_checks": actual["Euler_integral_checks"],
            "spectator_R0_checks": actual["spectator_R0_checks"],
            "high_I_boundary_check": actual["high_I_boundary_check"],
            "multiplet_rephasing_check": actual["multiplet_rephasing_check"],
            "adjacent_state_overlaps": actual["adjacent_state_overlaps"],
            "actual_loaded_BLAS_threads": threads,
        },
        "hard_model_checks_passed": invariants_ok,
        "package_bytes_unchanged_after_run": unchanged_after_run,
        "replay_output_files": {
            str(path.relative_to(output)): {"sha256": digest(path), "size": path.stat().st_size}
            for path in sorted(replay_dir.iterdir())
        },
        "frozen_reference_summary_byte_equal": (
            digest(package / "summary.csv") == digest(replay_dir / "summary.csv")
        ),
        "comparison_completed_at_utc": now(),
    })
    write_json(output / "replay-receipt.json", receipt)
    print("PACKAGED_REPLAY", json.dumps({
        "passed": passed, "proxy_comparisons": len(proxy_rows),
        "full_moment_cases": len(moment_rows),
        "max_absolute_numeric_difference": comparison.max_absolute_difference,
        "process_wall_seconds": process_seconds, "actual_BLAS_threads": actual_thread_counts,
    }), flush=True)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
