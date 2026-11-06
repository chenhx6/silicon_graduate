"""Assemble only the authorized standalone isomer payload; preserve originals."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path("/workspace/wiki")
OUT = ROOT / "outputs/l4/20261106-odd-ba-manuscript-revision/isomer-package"
PACKAGE = ROOT / "raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/isomer-check"
BENCHMARK = "outputs/l4/20261106-a130-next-evidence/isomer-benchmark"
OLD_CODE = "raw/writing/gpt/odd-ba-quadrupole-closure/data/code"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(json.dumps(obj, indent=2, allow_nan=False) + "\n")


def main():
    started = datetime.now(timezone.utc).isoformat()
    protocol = json.loads((ROOT / BENCHMARK / "protocol.json").read_text())
    records = []

    def copy(source, destination, role, recorded_digest=None):
        origin = ROOT / source
        target = PACKAGE / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise FileExistsError(target)
        before = digest(origin)
        if recorded_digest is not None and before != recorded_digest:
            raise ValueError(f"frozen source mismatch: {source}")
        shutil.copyfile(origin, target)
        assert digest(target) == before == digest(origin)
        records.append({
            "path": destination, "sha256": before, "size": target.stat().st_size,
            "role": role, "source": source, "copy_verified_byte_identical": True,
            "recorded_protocol_sha256": recorded_digest,
            "actual_copy_checked_at_utc": datetime.now(timezone.utc).isoformat(),
        })

    for name in (
        "protocol.json", "energy-mapping-frozen.json", "results.json",
        "predictions.csv", "decay-width-protocol.json",
        "decay-width-results.json", "decay-width-summary.csv",
    ):
        copy(f"{BENCHMARK}/{name}", f"frozen/{name}",
             "unchanged frozen protocol or reference result")
    producers = []
    for name in ("run_benchmark.py", "run_decay_widths.py"):
        copy(f"{BENCHMARK}/{name}", f"producers/{name}", "unchanged original producer")
        producers.append({"package_path": f"producers/{name}", "filename": name})
    common = []
    for path, expected in protocol["input_sha256"].items():
        name = Path(path).name
        if path.startswith("system/scripts/analysis/"):
            source = f"{OLD_CODE}/{name}"
            package_path = f"code/{name}"
            role = "numerical module; exact existing article-code copy"
        else:
            source = path
            package_path = f"inputs/{name}"
            role = ("frozen five operator roots; numerically consumed"
                    if name == "linear-calibration.json" else
                    "frozen prior-result snapshot; file-hash prerequisite only")
        copy(source, package_path, role, expected)
        common.append({"package_path": package_path, "original_relative_path": path})
    copy(f"{OLD_CODE}/LICENSE", "code/LICENSE", "unchanged existing numerical-code license")
    layout = {
        "schema": "isomer-standalone-relative-layout/1",
        "producer_directory": BENCHMARK,
        "common_inputs": common,
        "original_producers": producers,
        "stage_inputs": {
            "strength": [{"package_path": "frozen/protocol.json", "filename": "protocol.json"}],
            "width": [
                {"package_path": "frozen/protocol.json", "filename": "protocol.json"},
                {"package_path": "frozen/decay-width-protocol.json", "filename": "decay-width-protocol.json"},
                {"package_path": "frozen/results.json", "filename": "results.json"},
            ],
        },
    }
    write_new(PACKAGE / "layout.json", layout)
    by_digest = {}
    for entry in records:
        by_digest.setdefault(entry["sha256"], []).append(entry["path"])
    historical = []

    def walk(value, filename, pointer=""):
        if isinstance(value, dict):
            for key, child in value.items():
                escaped = key.replace("~", "~0").replace("/", "~1")
                walk(child, filename, pointer + "/" + escaped)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, filename, pointer + f"/{index}")
        else:
            key = pointer.rsplit("/", 1)[-1].lower()
            raw_path = isinstance(value, str) and (
                value.startswith(("raw/", "tmp/")) or ".pdf" in value.lower()
                or "ensdf" in value.lower())
            is_hash = isinstance(value, str) and re.fullmatch("[0-9a-f]{64}", value)
            is_flag = isinstance(value, bool) and any(
                word in key for word in ("verified", "audited", "checked", "unchanged"))
            is_source = isinstance(value, str) and any(
                word in key for word in ("source", "locator", "citation", "canonical_source"))
            if not (raw_path or is_hash or is_flag or is_source):
                return
            matched = by_digest.get(value, []) if is_hash else []
            historical.append({
                "snapshot": filename, "json_pointer": pointer, "declared_value": value,
                "declaration_kind": ("hash" if is_hash else "historical-status-flag"
                                     if is_flag else "raw/source/locator-declaration"),
                "packaged_artifacts_with_same_hash": matched,
                "actual_scope": (
                    "Digest matches the listed packaged bytes only; the historical "
                    "event or numerical interpretation is not independently certified."
                    if matched else
                    "Declaration preserved from the snapshot; underlying external "
                    "file, array fingerprint or historical event not reverified here."
                ),
            })

    for record in records:
        if record["path"].endswith(".json"):
            walk(json.loads((PACKAGE / record["path"]).read_text()), record["path"])
    declarations = {
        "schema": "isomer-standalone-provenance-boundary/1",
        "assembled_at_actual_utc": started,
        "archive_required": True,
        "source_reading_scope": (
            "Existing benchmark producers/protocols and exact JSON/code copies. "
            "No raw PDF, ENSDF original, publisher crop, source page, calibration "
            "contract or historical analysis producer was opened for this assembly."
        ),
        "actually_packaged_and_copy_hash_checked": records,
        "protocol_dependencies": [
            {**entry, "declared_sha256": protocol["input_sha256"][entry["original_relative_path"]],
             "actual_package_sha256": digest(PACKAGE / entry["package_path"]),
             "actual_file_present": True}
            for entry in common
        ],
        "historical_declarations": historical,
        "external_raw_originals_packaged": [],
        "external_raw_original_hashes_reverified": [],
        "historical_events_or_nested_provenance_recursively_verified": False,
        "raw_source_reading_claim": "No fresh source reading or source validation.",
        "frozen_operator_roots": (
            "Five existing roots are read verbatim. The original producers perform "
            "only their declared positive-eB normalization to frozen Bup=0.407; "
            "no fit, root search, new operator or state reselection is introduced."
        ),
    }
    write_new(PACKAGE / "source-declarations.json", declarations)
    by_path = {record["path"]: record for record in records}
    payload = []
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE).as_posix()
        assert not path.is_symlink()
        entry = by_path.get(relative, {
            "path": relative, "role": "new standalone adapter/documentation/provenance",
            "source": "locally authored for this bounded packaging task",
        }).copy()
        entry.update(sha256=digest(path), size=path.stat().st_size)
        payload.append(entry)
    inventory = {
        "schema": "isomer-standalone-payload-inventory/1",
        "recorded_at_actual_utc": datetime.now(timezone.utc).isoformat(),
        "archive_required": True,
        "path_base": "directory containing this inventory",
        "scope": "Immutable replay payload only; excludes itself and later verification records.",
        "files": payload,
    }
    write_new(PACKAGE / "inventory.json", inventory)
    target = OUT / "standalone-copy/package"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(PACKAGE, target)
    for path in PACKAGE.rglob("*"):
        if path.is_file():
            assert digest(path) == digest(target / path.relative_to(PACKAGE))
    write_new(OUT / "assembly-receipt.json", {
        "assembled_at_actual_utc": datetime.now(timezone.utc).isoformat(),
        "package": PACKAGE.relative_to(ROOT).as_posix(),
        "standalone_copy": target.relative_to(ROOT).as_posix(),
        "payload_files": len(payload), "original_exact_copies": len(records),
        "inventory_sha256": digest(PACKAGE / "inventory.json"),
        "physical_copy_all_hashes_equal": True,
        "external_raw_originals_reverified": [],
    })
    print(json.dumps({"payload_files": len(payload), "copied_originals": len(records),
                      "historical_declarations": len(historical),
                      "inventory_sha256": digest(PACKAGE / "inventory.json"),
                      "standalone_copy": str(target)}, indent=2))


if __name__ == "__main__":
    main()
