#!/usr/bin/env python3
"""Replay unchanged control producers in a new isolated directory.

This adapter materializes the relative paths named in the frozen protocols.
It requires only this paper's data directory. No original repository, network,
raw PDFs, or credentials are used. Nothing in the paper package is overwritten.
The original operator producer explicitly checks Linux/OpenBLAS thread counts.
"""
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys

DATA = Path(__file__).resolve().parents[1]
NATIVE = Path("outputs/l4/20261105-ba129-controlled-pairing")


def copy_file(source, root, relative):
    destination = root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(destination)
    shutil.copy2(DATA / source, destination)


def compare(expected, actual, location="root"):
    if isinstance(expected, dict):
        keys = set(expected) - {"elapsed_seconds"}
        if keys != set(actual) - {"elapsed_seconds"}:
            raise AssertionError(f"{location}: keys differ")
        for key in sorted(keys):
            compare(expected[key], actual[key], f"{location}.{key}")
    elif isinstance(expected, list):
        if len(expected) != len(actual):
            raise AssertionError(f"{location}: length differs")
        for i, (x, y) in enumerate(zip(expected, actual)):
            compare(x, y, f"{location}[{i}]")
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if not isinstance(actual, (int, float)) or not math.isclose(
            expected, actual, rel_tol=1e-9, abs_tol=1e-10
        ):
            raise AssertionError(f"{location}: {expected} != {actual}")
    elif expected != actual:
        raise AssertionError(f"{location}: {expected!r} != {actual!r}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=["operator", "coupling", "quadrupole-path", "moment-match"])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    common = {
        "chain-contract.json": NATIVE / "spin-invariant-chain-contract.json",
        "core-E2-calibration.json": NATIVE / "core-E2-calibration/ba-core-E2.json",
        "results/calibrated-chain.json": NATIVE / "shape-closure-v1/study.json",
        "reproduction-prerequisites/chain-core-only-v1.json": NATIVE / "spin-invariant-probe/chain-core-only-v1.json",
        "reproduction-prerequisites/run_probe.py": NATIVE / "spin-invariant-probe/run_probe.py",
        "reproduction-prerequisites/precedent-audit.md": NATIVE / "spin-invariant-precedent-review/audit.md",
        "reproduction-prerequisites/pilot-assessment.md": NATIVE / "spin-invariant-precedent-review/pilot-assessment.md",
        "static-moment-constraints.json": NATIVE / "spin-invariant-moment-benchmark/source-constraints.json",
    }
    for name in ["single_j_ibfm.py", "quadrupole_scalar_invariants.py",
                 "paired_single_j_em.py", "paired_single_j_rotor.py"]:
        common["code/" + name] = Path("system/scripts/analysis") / name
    for source, relative in common.items():
        copy_file(source, root, relative)
    if args.kind == "operator":
        directory = NATIVE / "spin-invariant-operator-control"
        copy_file("operator-sensitivity-contract.json", root, directory / "operator-sensitivity-contract.json")
        copy_file("code/operator_controls_original.py", root, directory / "driver.py")
        script = directory / "driver.py"
        expected = DATA / "results/operator-sensitivity.json"
        result = root / directory / "results.json"
        keys = ["rows"]
    else:
        directory = NATIVE / "spin-invariant-coupling-control"
        copy_file("coupling-protocol.json", root, directory / "protocol.json")
        copy_file("code/coupling_controls_original.py", root, directory / "run_controls.py")
        if args.kind == "coupling":
            script = directory / "run_controls.py"
            expected = DATA / "results/coupling-controls.json"
            result = root / directory / "controls.json"
            keys = ["cases", "adjacent_grid_overlaps"]
        elif args.kind == "quadrupole-path":
            copy_file("quadrupole-path-protocol.json", root, directory / "gamma-path-protocol.json")
            copy_file("results/coupling-controls.json", root, directory / "controls.json")
            copy_file("code/quadrupole_path_original.py", root, directory / "run_gamma_path.py")
            script = directory / "run_gamma_path.py"
            expected = DATA / "results/quadrupole-path.json"
            result = root / directory / "gamma-path.json"
            keys = ["points", "new_point_details", "adjacent_overlaps",
                    "continuity", "endpoint_eigenvector_replay_checks"]
        else:
            copy_file("quadrupole-path-protocol.json", root, directory / "gamma-path-protocol.json")
            copy_file("results/coupling-controls.json", root, directory / "controls.json")
            copy_file("results/quadrupole-path.json", root, directory / "gamma-path.json")
            copy_file("code/quadrupole_path_original.py", root, directory / "run_gamma_path.py")
            copy_file("moment-match-protocol.json", root, directory / "moment-match-protocol.json")
            copy_file("code/moment_match_original.py", root, directory / "moment-match-run.py")
            script = directory / "moment-match-run.py"
            expected = DATA / "results/moment-matched.json"
            result = root / directory / "moment-match-results.json"
            keys = ["cases", "combined_known_and_matched_adjacent_overlaps"]
    environment = dict(os.environ)
    environment.update({
        "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
        "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
    })
    with (root / "execution.log").open("x") as log:
        phases = [["roots"], ["diagnostics"]] if args.kind == "moment-match" else [[]]
        for extra in phases:
            run = subprocess.run(
                [sys.executable, "-B", str(root / script), *extra], cwd=root,
                env=environment, stdout=log, stderr=subprocess.STDOUT)
            if run.returncode:
                raise RuntimeError(f"Producer exited {run.returncode}; see {root / 'execution.log'}")
    old, new = (json.loads(p.read_text()) for p in (expected, result))
    for key in keys:
        compare(old[key], new[key], key)
    receipt = {
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "kind": args.kind, "status": "passed", "producer_exit_code": run.returncode,
        "compared_fields": keys, "relative_tolerance": 1e-9, "absolute_tolerance": 1e-10,
        "result": str(result.relative_to(root)),
        "boundary": "Numerical reproducibility, not empirical validation or journal readiness.",
    }
    (root / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
