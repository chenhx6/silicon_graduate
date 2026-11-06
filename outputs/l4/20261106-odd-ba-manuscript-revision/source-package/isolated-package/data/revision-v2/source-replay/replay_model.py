#!/usr/bin/env python3
"""Replay the frozen 12 source-energy comparisons using this data package.

The unchanged original producer supplies every model/comparison operation.
This adapter changes locations, verification scope and run metadata only.
No original paper, figure, raw archive, Wiki module or PyMuPDF is required.
"""

import sys

sys.dont_write_bytecode = True

import argparse
import contextlib
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]
SOURCE = HERE / "source-points-frozen.json"
CONTRACT = HERE / "comparison-contract.json"
ORIGINAL = HERE / "producers/compare_fixed_chain.py"
SOURCE_SHA = "bc4dbed2c29f65ae8f9546cd146005efa6dbb64eb08ef23781ede6f907b91d22"
CONTRACT_SHA = "cc3b8cc2f677635593f739cd450fb1c5fdcdac54dcdbe0a94075391a63b9f940"
ORIGINAL_SHA = "1858bf76ee46392e52fe0aab9918632f49c52f4c39545d0d01e5b6a8f28eb504"
ATOL_KEV = 1e-8
RTOL = 1e-10


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_new(path, value):
    with Path(path).open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")


def compare(expected, actual, label="root", errors=None):
    if errors is None:
        errors = []
    if isinstance(expected, bool) or expected is None or isinstance(expected, str):
        assert actual == expected, (label, expected, actual)
    elif isinstance(expected, (int, float)):
        assert math.isfinite(actual), (label, actual)
        error = abs(actual - expected)
        assert error <= ATOL_KEV + RTOL * abs(expected), (label, expected, actual)
        errors.append(error)
    elif isinstance(expected, list):
        assert len(actual) == len(expected), label
        for i, (left, right) in enumerate(zip(expected, actual)):
            compare(left, right, f"{label}[{i}]", errors)
    elif isinstance(expected, dict):
        assert set(actual) == set(expected), label
        for key, value in expected.items():
            compare(value, actual[key], f"{label}.{key}", errors)
    else:
        raise TypeError(type(expected))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New result directory")
    parser.add_argument("--forbid-external-root", type=Path,
                        help="Audit mode: reject opens under this root outside this data package and output")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError("Use a fresh output directory; frozen and prior results are not overwritten.")
    output.mkdir(parents=True)

    rejected = []
    if args.forbid_external_root:
        forbidden = args.forbid_external_root.resolve()

        def guard(event, arguments):
            if event != "open" or not isinstance(arguments[0], (str, bytes, os.PathLike)):
                return
            path = Path(os.fsdecode(arguments[0])).resolve()
            if path.is_relative_to(forbidden) and not any(path.is_relative_to(p) for p in (DATA, output)):
                rejected.append(str(path))
                raise PermissionError(f"Read/write outside isolated package: {path}")

        sys.addaudithook(guard)

    index = json.loads((HERE / "package-index.json").read_text())
    contract = json.loads(CONTRACT.read_text())
    source = json.loads(SOURCE.read_text())
    freeze = json.loads((HERE / "source-freeze.json").read_text())
    expected_run = json.loads((HERE / "expected/run-original.json").read_text())
    evidence = json.loads((HERE / "source-identities.json").read_text())
    verification = {
        "adapter": "source-energy-package-verifier-v1",
        "adapter_sha256": sha(__file__),
        "original_producer_sha256": ORIGINAL_SHA,
        "frozen_source_json_sha256": SOURCE_SHA,
        "frozen_comparison_contract_sha256": CONTRACT_SHA,
        "frozen_source_freeze_sha256": sha(HERE / "source-freeze.json"),
        "algorithm_changed": False,
        "Hamiltonian_parameters_or_state_policy_changed": False,
        "historical_source_originals_reverified_in_this_model_run": False,
        "historical_sources": evidence["originals"],
        "historical_source_status": "Original hashes retained from frozen provenance; source bytes are not read by this replay.",
        "native_thread_verifier_changed": False,
        "package_files_verified": [],
    }
    # A previous packaging-time verification must not be confused with this run.
    for item in verification["historical_sources"]:
        item["verified_in_this_model_run"] = False

    def verify_package(_contract):
        assert sha(SOURCE) == SOURCE_SHA
        assert sha(CONTRACT) == CONTRACT_SHA
        assert sha(ORIGINAL) == ORIGINAL_SHA == expected_run["driver_sha256"]
        assert freeze["source_json"]["sha256"] == SOURCE_SHA
        assert sha(HERE / "source-points-frozen.csv") == freeze["source_csv"]["sha256"]
        assert sha(HERE / "producers/extract_source.py") == freeze["extractor"]["sha256"]
        assert sha(HERE / "expected/comparison.json") == expected_run["comparison_json_sha256"]
        assert sha(HERE / "expected/comparison.csv") == expected_run["comparison_csv_sha256"]
        checked = []
        for item in index["files"]:
            local = (DATA / item["path_from_data"]).resolve()
            assert local.is_relative_to(DATA), local
            assert sha(local) == item["sha256"], local
            checked.append({"path_from_data": item["path_from_data"],
                            "sha256": item["sha256"], "status": "present_and_verified"})
        verification["package_files_verified"] = checked

    verify_package(contract)
    with (HERE / "source-points-frozen.csv").open(newline="") as f:
        csv_points = list(csv.DictReader(f))
    points = source["original_figure"]["points"]
    assert len(points) == len(csv_points) == 12
    for row, point in zip(csv_points, points):
        for key, text in row.items():
            value = point[key]
            if isinstance(value, (int, float)):
                assert float(text) == value, key
            else:
                assert text == value, key
    assert {p["odd_A"] for p in points} == {135, 137}

    spec = importlib.util.spec_from_file_location("frozen_source_energy_producer", ORIGINAL)
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    producer.OUT = output
    producer.ROOT = DATA
    producer.CONTRACT = CONTRACT
    producer.SOURCE = SOURCE
    producer.verify = verify_package

    # Load only the package's existing kernel. The original producer's legacy
    # ROOT/system/scripts/analysis path is not a dependency of this replay.
    sys.path.insert(0, str(DATA / "code"))
    import single_j_ibfm
    import paired_single_j_em
    import paired_single_j_rotor
    modules = (single_j_ibfm, paired_single_j_em, paired_single_j_rotor)
    verification["runtime_modules"] = []
    for module in modules:
        path = Path(module.__file__).resolve()
        assert path == (DATA / "code" / f"{module.__name__}.py").resolve()
        verification["runtime_modules"].append({
            "path_from_data": str(path.relative_to(DATA)), "sha256": sha(path),
        })

    original_write = producer.write_new

    def write_with_scoped_metadata(name, value):
        value = dict(value)
        if name == "run.json":
            value.pop("all_locked_inputs_unchanged", None)
            value.update(
                packaged_numerical_inputs_and_runtime_modules_unchanged=True,
                historical_source_originals_reverified=False,
                verification_adapter="source-energy-package-verifier-v1",
                adapter_sha256=sha(__file__),
            )
        original_write(name, value)

    producer.write_new = write_with_scoped_metadata
    with (output / "execution.log").open("x") as log, contextlib.redirect_stdout(log):
        producer.main()
    verify_package(contract)
    actual = json.loads((output / "comparison.json").read_text())
    expected = json.loads((HERE / "expected/comparison.json").read_text())
    errors = compare(expected["rows"], actual["rows"], "rows")
    errors += compare(expected["summaries"], actual["summaries"], "summaries")
    assert len(actual["rows"]) == 12
    assert all(row["kernel_ordinal_zero_based"] == 0 for row in actual["rows"])
    assert actual["no_parameter_variants_or_fit"] and actual["no_EM_calculations"]
    assert len(actual["models"]) == 2
    for left, right in zip(expected["models"], actual["models"]):
        assert left["parameters"] == right["parameters"]
        assert left["odd_A"] == right["odd_A"]

    verification.update({
        "status": "passed",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_points_checked": 12, "comparison_rows_checked": 12,
        "absolute_numeric_tolerance": ATOL_KEV, "relative_numeric_tolerance": RTOL,
        "maximum_numeric_replay_difference": max(errors, default=0.0),
        "max_abs_kernel_minus_source_keV": {
            str(r["odd_A"]): r["max_abs_kernel_minus_source_keV"] for r in actual["summaries"]
        },
        "RMS_kernel_minus_source_keV": {
            str(r["odd_A"]): r["RMS_kernel_minus_source_keV"] for r in actual["summaries"]
        },
        "external_root_guard_enabled": bool(args.forbid_external_root),
        "rejected_external_open_attempts": rejected,
        "source_reextraction_performed": False,
        "original_source_freeze_rewritten": False,
        "boundary": "Replay of frozen source-point comparisons, not renewed extraction, author-run certification or experimental/EM validation.",
    })
    write_new(output / "verification.json", verification)
    print(json.dumps({
        "status": "passed", "source_points": 12, "compared_rows": 12,
        "max_abs_kernel_minus_source_keV": verification["max_abs_kernel_minus_source_keV"],
        "max_numeric_replay_difference": verification["maximum_numeric_replay_difference"],
        "source_originals_read": False, "record": str(output / "verification.json"),
    }, indent=2))


if __name__ == "__main__":
    main()
