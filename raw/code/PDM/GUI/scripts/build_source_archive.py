"""Bundle GUI and analysis for offline use, with a per-file checksum manifest."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


EXCLUDED = {
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".git",
    "build",
    "dist",
    ".ipynb_checkpoints",
    "pdm-results",
    "generated_figures",
}
SUFFIXES = {
    ".py",
    ".md",
    ".toml",
    ".json",
    ".csv",
    ".npz",
    ".ipynb",
    ".png",
    ".pdf",
    ".svg",
    ".txt",
    ".log",
    ".rst",
    ".yaml",
    ".yml",
}
TOKEN = re.compile(rb"pypi-[A-Za-z0-9_-]{30,}")


def build(root, output):
    entries, payloads = [], []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(
            part in EXCLUDED or part.endswith(".egg-info") for part in relative.parts
        ):
            continue
        if path.is_symlink():
            raise ValueError(f"Unexpected source-tree symlink: {relative}")
        if (
            path.name.startswith(".env")
            or path.suffix not in SUFFIXES
            and path.name not in {"LICENSE", ".gitignore"}
        ):
            continue
        data = path.read_bytes()
        if TOKEN.search(data):
            raise ValueError(
                f"Token-shaped content found in {relative}; archive refused."
            )
        name = relative.as_posix()
        entries.append(
            {
                "path": name,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
        payloads.append((name, data))
    if not any(
        entry["path"] == "analysis/01_results_and_intervals.ipynb" for entry in entries
    ):
        raise ValueError("The source archive must include the analysis notebooks.")
    manifest = {
        "schema": "multipolepdm-public-source-v1",
        "files": entries,
        "scope": "GUI, shared core, examples, tests, analysis notebooks and validation data; no private workbook or external paper originals.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise FileExistsError(f"Refusing to replace an existing archive: {output}")
    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, data in payloads + [
            ("SOURCE_MANIFEST.json", (json.dumps(manifest, indent=2) + "\n").encode())
        ]:
            info = zipfile.ZipInfo("PDM/" + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    print(
        json.dumps(
            {
                "archive": str(output),
                "files": len(entries),
                "size": output.stat().st_size,
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    build(Path(__file__).resolve().parents[2], parser.parse_args().output)
