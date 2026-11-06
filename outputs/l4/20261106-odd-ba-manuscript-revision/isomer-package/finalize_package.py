"""Collect the single completed standalone replay, without rerunning a model."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path("/workspace/wiki")
OUT = ROOT / "outputs/l4/20261106-odd-ba-manuscript-revision/isomer-package"
PACKAGE = ROOT / "raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/isomer-check"
RUN = OUT / "standalone-copy/run-01"
COPY = OUT / "standalone-copy/package"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(json.dumps(value, indent=2, allow_nan=False) + "\n")


def write_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(value)


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    shutil.copyfile(source, target)
    assert sha(source) == sha(target)


def main():
    stamp = datetime.now(timezone.utc).isoformat()
    comparison = load(RUN / "comparison.json")
    receipt = load(RUN / "receipt.json")
    inventory = load(PACKAGE / "inventory.json")
    assert comparison["pass"] and receipt["pass"]
    assert sha(PACKAGE / "inventory.json") == receipt["payload_inventory_sha256"]
    for item in inventory["files"]:
        assert sha(PACKAGE / item["path"]) == item["sha256"]
        assert sha(COPY / item["path"]) == item["sha256"]

    baseline = load(OUT / "preservation-baseline.json")
    checks = []
    for path, expected in baseline["protected_sha256"].items():
        actual = sha(ROOT / path)
        checks.append({
            "path": path, "baseline_sha256": expected, "actual_sha256": actual,
            "unchanged": expected == actual,
        })
    old_data = "raw/writing/gpt/odd-ba-quadrupole-closure/data/"
    assert sum(x["path"].startswith(old_data) for x in checks) == 46
    assert all(x["unchanged"] for x in checks if x["path"].startswith(old_data))
    benchmark = "outputs/l4/20261106-a130-next-evidence/isomer-benchmark/"
    assert all(x["unchanged"] for x in checks if x["path"].startswith(benchmark))
    changed = [x for x in checks if not x["unchanged"]]
    preservation = {
        "checked_at_actual_utc": stamp,
        "original_data_manifest_entry_count": 45,
        "original45_and_shared_data_manifest_unchanged": True,
        "frozen_benchmark_inputs_and_producers_unchanged": True,
        "protected_count": len(checks),
        "unchanged_count": sum(x["unchanged"] for x in checks),
        "changed_outside_owned_scope": changed,
        "interpretation": (
            "Shared manuscript files may be concurrently edited by the parent. "
            "Changed files outside the two owned directories were neither written "
            "nor reverted by this task; only their hashes were checked."
        ),
        "checks": checks,
    }
    write_json(OUT / "preservation-check.json", preservation)

    verify = PACKAGE / "verification"
    names = [
        "comparison.json", "receipt.json", "strength-read-boundary.json",
        "width-read-boundary.json", "strength.stdout.log", "strength.stderr.log",
        "width.stdout.log", "width.stderr.log",
    ]
    for name in names:
        copy(RUN / name, verify / name)
    for source in sorted((RUN / "reproduced").iterdir()):
        copy(source, verify / "reproduced" / source.name)

    strengths = load(RUN / "reproduced/results.json")
    widths = load(RUN / "reproduced/decay-width-results.json")
    mapping = load(RUN / "reproduced/energy-mapping-frozen.json")
    csv_equal = {
        name: sha(PACKAGE / "frozen" / name) == sha(RUN / "reproduced" / name)
        for name in ("predictions.csv", "decay-width-summary.csv")
    }
    scope_counts = {}
    for stage in ("strength", "width"):
        boundary = load(RUN / f"{stage}-read-boundary.json")
        assert boundary["status"] == "passed"
        assert boundary["intentional_forbidden_read_probe_blocked"]
        assert not boundary["unexpected_denied_accesses"]
        assert not boundary["network_or_subprocess_attempts"]
        scope_counts[stage] = dict(Counter(
            item["scope"] for item in boundary["allowed_file_reads"]))
    numeric_comparisons = sum(
        item["comparisons"] for group in (
            "strength", "energy_mapping", "width_and_branches", "strength_csv", "width_csv"
        ) for item in comparison[group]["numeric_maxima"].values())
    maxima = {
        group: comparison[group]["numeric_maxima"]
        for group in ("strength", "energy_mapping", "width_and_branches",
                      "strength_csv", "width_csv")
    }
    notes = f"""# Recorded standalone replay

The unchanged strength producer and unchanged width producer each ran once
from a physical copy of this payload. Both completed successfully. No model,
operator root, state ordinal or comparison tolerance was fitted in this run.

| Comparison | Records | Maximum absolute difference |
| --- | ---: | ---: |
| Energy-first mapping | 4 pairs | 0 |
| Strength results, including signed RMEs and interference | 28 | 0 |
| E2 radiative width sums and half-life bounds | 14 | 0 |
| Open E2 branch records | 84 | 0 |
| Strength and width CSV tables | 28 + 14 | 0 |

All {numeric_comparisons} compared floating fields agree exactly after parsing.
The state-basis byte hash agrees as well. Both CSV files are byte-identical
to their frozen references. JSON files have fresh run timestamps; the exact
metadata exclusions and comparison tolerances are in `comparison.json`.
All other fields, including original protocol/producer hashes, are compared.

The tested payload inventory SHA-256 is
`{receipt["payload_inventory_sha256"]}`.
The `receipt.json` in this directory identifies the actual run from
{receipt["started_at_actual_utc"]} to {receipt["finished_at_actual_utc"]}.
Its paths record the physical execution location; these historical paths
are not runtime dependencies after this package is moved.

The run used Python 3.12.3, NumPy {receipt["runtime"]["numpy"]} and
SciPy {receipt["runtime"]["scipy"]}. Only that runtime was tested.
Each modeled first 19/2 parent has three open E2 branches, and each modeled
second 19/2 parent has nine; seven operators give 7*(3+9)=84 branch records.

The energy diagnostic again chose `{mapping["energy_nearest_in_declared_four_pairs"]}`.
It uses squared residuals of both levels relative to the lowest 11/2 anchor.
It is an internal frozen mapping rule, not a certified experimental assignment.

The two workers blocked their deliberate forbidden-file probes. They recorded
no unexpected denied access and no network/nested-subprocess attempt.
Every allowed scientific-file access event was within the staged run tree.
`allowed_file_reads` records Python audit events before the operating system
completes the operation: it therefore includes attempts to read absent `.pyc`
cache files and directory enumeration. It is not a count of successful file
opens or a complete native/OS-level trace. Runtime libraries are allowed
under the exact interpreter roots recorded in the boundary reports.

The width layout uses the real packaged frozen strength result to satisfy its
unchanged historical file-hash prerequisite. The width calculation is newly
executed; newly computed strengths are compared separately. No hash checker
was patched and no missing scientific file was simulated.

The 23 payload files are checked by `../inventory.json`. This directory has
its own relative `inventory.json` for the 14 verification artifacts. The
top-level `../manifest.json` is a repository archive envelope whose paths
are repository-relative; it is not a standalone runtime dependency.

No external PDF, ENSDF file, publisher crop, historical source page or prior
calibration run was bundled or reverified. Historical source declarations
remain in `../source-declarations.json` and the exact input snapshots.
This is numerical reproduction of the frozen model family. The decay sums
remain conditional model-scheme E2-radiative upper half-life bounds, with
no physical assignment, complete-lifetime or source-author validation claim.
"""
    write_text(verify / "README.md", notes)
    verification_files = []
    for path in sorted(verify.rglob("*")):
        if path.is_file():
            verification_files.append({
                "path": path.relative_to(verify).as_posix(),
                "sha256": sha(path), "size": path.stat().st_size,
                "source": (
                    "Documentation of the completed replay" if path.name == "README.md"
                    else "Byte-identical copy from the single standalone run"
                ),
            })
    assert len(verification_files) == 14
    write_json(verify / "inventory.json", {
        "schema": "isomer-verification-inventory/1",
        "recorded_at_actual_utc": stamp,
        "path_base": "this verification directory",
        "tested_payload_inventory_sha256": sha(PACKAGE / "inventory.json"),
        "files": verification_files,
    })

    payload_sources = {item["path"]: item["source"] for item in inventory["files"]}
    manifest_files = []
    for path in sorted(PACKAGE.rglob("*")):
        if path.is_file():
            relative = path.relative_to(PACKAGE).as_posix()
            manifest_files.append({
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha(path), "size": path.stat().st_size,
                "source": payload_sources.get(
                    relative, "Locally generated standalone replay inventory or verification record"),
                "access_scope": "local numerical manuscript supplement; no publisher full text",
            })
    write_json(PACKAGE / "manifest.json", {
        "archive_type": "research-archive-v1",
        "retrieved_at": stamp, "archive_required": True,
        "acquisition_context": "user-authorized manuscript numerical supplement assembly",
        "operation": "local exact-copy packaging and frozen-input numerical reproduction; no download",
        "external_raw_sources_verified": [],
        "files": manifest_files,
    })
    # Add verification records to the physical copy after the run. Its tested
    # immutable payload and inventory remain byte-identical throughout.
    for source in sorted(PACKAGE.rglob("*")):
        if source.is_file():
            destination = COPY / source.relative_to(PACKAGE)
            if destination.exists():
                assert sha(destination) == sha(source)
            else:
                copy(source, destination)

    write_json(OUT / "package-review.json", {
        "reviewed_at_actual_utc": stamp,
        "pass": True, "numerical_producer_executions": {"strength": 1, "width": 1},
        "scientific_counts": comparison["counts"],
        "compared_floating_fields": numeric_comparisons,
        "numeric_maxima": maxima,
        "CSV_byte_equality": csv_equal,
        "state_basis_sha256_equal": comparison["strength"]["state_basis_sha256_equal"],
        "allowed_access_event_scope_counts": scope_counts,
        "file_access_event_boundary": "Audit events include failed cache-open attempts.",
        "no_unbundled_Wiki_scientific_reads_allowed": True,
        "external_raw_originals_reverified": [],
        "payload_inventory_sha256": sha(PACKAGE / "inventory.json"),
        "verification_inventory_sha256": sha(verify / "inventory.json"),
        "archive_manifest_sha256": sha(PACKAGE / "manifest.json"),
        "archive_manifest_entries": len(manifest_files),
        "package_files_including_manifest": len(manifest_files) + 1,
        "original45_and_shared_data_manifest_unchanged": True,
        "concurrent_changes_outside_owned_scope": [x["path"] for x in changed],
        "no_commit_performed": True,
    })
    package_relative = PACKAGE.relative_to(ROOT).as_posix()
    summary = f"""# Standalone isomer package: completed numerical check

The independent bundle is `{package_relative}/`.
Its original producers each ran once from `standalone-copy/package/`;
the full generated layouts and logs are retained in `standalone-copy/run-01/`.
The numerical comparison passed: four energy mappings, 28 strengths, 14
width sums and all 84 branches agree exactly with the frozen references.
All {numeric_comparisons} compared floating fields have zero difference.
Both CSV files and the eigenvector-basis hash also agree exactly.

The runnable entry point is `reproduce.py`; from a copy of the bundle, run:

```bash
python3 -B reproduce.py --output /absolute/path/to/a-new-isomer-run
```

The output must be new and outside the package. The tested environment is
Python 3.12.3, NumPy 2.5.4 and SciPy 1.18.1. The bundle's English README
documents the frozen inputs, the two-layout design, scientific limits and
standalone use. No new fit, operator, source search or scientific input was
introduced. The original positive-eB normalization to frozen Bup=0.407
is retained in both original producers.

For manuscript integration, the recorded energy-nearest alternative remains
19/2_1 to 15/2_2, chosen by the two anchored level energies before E2
evaluation. The primary pair retains B=22.46884935273523 W.u. and a
1173.6101707745688-keV model photon energy. The energy-nearest primary-
operator branch retains 2.1776211421936043 W.u. and 48.32504893857603 keV.
The conditional Q136=+0.07 root gives 0.42002440210282804 W.u. on that
alternative branch. These are preserved model results, not a state
assignment or validation of the decay network. All 14 summed model-scheme
upper half-life bounds remain at or below 0.0002810411363297495 ns.

`source-declarations.json` distinguishes 16 exact copied originals from 101
embedded historical source/hash/locator declarations. All six original
protocol dependencies are real staged files with matching hashes. The
width protocol's frozen historical `results.json` prerequisite is provided
as an actual file in a separate width layout; no hash checker is replaced.
Unbundled PDFs, ENSDF files, publisher crops and prior source-audit events
are not reverified. The replay is not certification of source-author code,
the original electromagnetic figures, physical state assignments or paper
readiness.

Both deliberate forbidden-read probes were blocked; no unexpected denied
access or network/nested-process attempt occurred. Allowed scientific-file
events stayed in the staged trees. The logs are Python audit events, including
failed cache-read attempts, not an exhaustive OS/native trace.

The original 45 data-manifest files, shared data manifest and frozen benchmark
files match the preservation baseline. A concurrent change to shared
`main.tex` was observed by hash; this task neither wrote nor reverted it.
See `preservation-check.json` for the exact snapshot. All task writes are
within the two assigned directories, and no commit was made.

`package-review.json` reports numerical checks and payload hashes.
`archive-gate.json` and `receipt.json` record final archive verification.
The package carries its own `inventory.json`, `verification/inventory.json`,
`verification/receipt.json` and repository-relative `manifest.json`; the
shared manuscript manifest has not been edited.
"""
    write_text(OUT / "README.md", summary)
    print(json.dumps({
        "package_files": len(manifest_files) + 1,
        "numeric_comparisons": numeric_comparisons,
        "preservation": f'{preservation["unchanged_count"]}/{len(checks)}',
        "concurrent_changes": [x["path"] for x in changed],
        "payload_inventory_sha256": sha(PACKAGE / "inventory.json"),
        "archive_manifest_sha256": sha(PACKAGE / "manifest.json"),
    }, indent=2))


if __name__ == "__main__":
    main()
