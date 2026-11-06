#!/usr/bin/env python3
"""Numerical replay of all calibration branches with an explicit verifier adapter.

The original scientific producer and its numerical contract are unchanged.
This bundle verifies their bytes and every runtime module. Historical source
page/raw-file hashes are recorded, not presented as files verified in this
bundle. In particular, one mutable historical knowledge-page version is absent.
"""
import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path

from reproduce_controls import compare

DATA = Path(__file__).resolve().parents[1]
ORIGINAL = DATA / "code/calibrated_operator_original.py"
CONTRACT = DATA / "calibrated-operator-contract.json"
CONTRACT_SHA = "5d49a9ceda150dea250e80eceb1389fdc6b96f6af4307ca2c6c8c2aabb75b6ff"
ORIGINAL_SHA = "f206481c5abef00e261029de8c790bb32182a7562bfd0ac7b60e898365f955cd"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    contract = json.loads(CONTRACT.read_text())
    if sha(CONTRACT) != CONTRACT_SHA:
        raise ValueError("Frozen numerical contract has changed")
    if sha(ORIGINAL) != ORIGINAL_SHA:
        raise ValueError("Original producer differs from its recorded research run")
    spec = importlib.util.spec_from_file_location("calibrated_operator_original", ORIGINAL)
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    producer.OUT = output
    producer.CONTRACT = CONTRACT
    producer.CONTRACT_SHA = CONTRACT_SHA
    original_sha = sha(ORIGINAL)
    verification = {
        "adapter": "paper-numerical-verifier-v1",
        "adapter_sha256": sha(__file__),
        "original_driver_sha256": original_sha,
        "frozen_numerical_contract_sha256": CONTRACT_SHA,
        "runtime_modules": [],
        "historical_source_identities": contract["input_files"],
        "historical_sources_status": "hashes recorded; original source bytes not reverified in this bundle",
        "missing_historical_page": (
            "The source-page hash 24075979e4ff1e11ee03215dfcd77b751dc1003d03b34c801a9a73df5fd6c02c "
            "belongs to an earlier mutable Wiki note; no reconstructed replacement is asserted."),
        "algorithm_change": False,
        "parameter_or_target_change": False,
        "native_thread_check_changed": False,
    }

    def verify_numerical_inputs(c):
        if sha(CONTRACT) != CONTRACT_SHA or sha(ORIGINAL) != original_sha:
            raise ValueError("Numerical contract or original producer changed during replay")
        checked = []
        for item in c["read_only_modules"]:
            local = DATA / "code" / Path(item["path"]).name
            observed = sha(local)
            if observed != item["sha256"]:
                raise ValueError(f"Runtime module mismatch: {local.name}")
            checked.append({"path": str(local.relative_to(DATA)), "sha256": observed,
                            "status": "present_and_verified"})
        verification["runtime_modules"] = checked

    original_write = producer.write_new

    def write_with_verification_scope(name, value):
        value = dict(value)
        changed = False
        for key in ("inputs_and_modules_unchanged", "input_and_module_hashes_unchanged"):
            if key in value:
                del value[key]
                changed = True
        if changed:
            value["numerical_contract_and_runtime_modules_unchanged"] = True
            value["historical_source_files_reverified_in_this_bundle"] = False
            value["verification_adapter"] = "paper-numerical-verifier-v1"
        original_write(name, value)

    producer.verify_inputs = verify_numerical_inputs
    producer.write_new = write_with_verification_scope
    verify_numerical_inputs(contract)
    with (output / "execution.log").open("x") as log, contextlib.redirect_stdout(log):
        producer.calibration_stage(contract)
        producer.prediction_stage(contract)
    verify_numerical_inputs(contract)
    expected = json.loads((DATA / "results/calibrated-operator-predictions.json").read_text())
    actual = json.loads((output / "predictions.json").read_text())
    compare(expected["rows"], actual["rows"], "prediction_rows")
    # Every valid branch is preserved; no selection based on the unused target.
    if not actual["all_finite_roots_evaluated_without_holdout_selection"]:
        raise AssertionError("Incomplete calibration branch coverage")
    verification.update({
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed", "compared_prediction_rows": len(actual["rows"]),
        "all_finite_branches_preserved": True,
        "relative_tolerance": 1e-9, "absolute_tolerance": 1e-10,
        "boundary": "Numerical replay of a conditional calibration, not independent experimental validation.",
    })
    (output / "verification.json").write_text(json.dumps(verification, indent=2) + "\n")
    print(json.dumps({
        "status": verification["status"],
        "rows": verification["compared_prediction_rows"],
        "historical_sources_reverified": False,
        "runtime_modules_verified": len(verification["runtime_modules"]),
        "record": str(output / "verification.json"),
    }, indent=2))


if __name__ == "__main__":
    main()
