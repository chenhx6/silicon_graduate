"""Execute one unchanged producer with a Python-level file-access allowlist.

This is an audit boundary, not an operating-system security sandbox.
Only the staged run tree, the copied package, and interpreter/runtime
libraries may be read. Scientific originals outside those trees are denied.
"""
import sys
sys.dont_write_bytecode = True
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import runpy
import sysconfig
import traceback


def below(path, root):
    return path == root or root in path.parents


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    script = args.script.resolve()
    package = args.package.resolve()
    run_root = args.run_root.resolve()
    receipt = args.receipt.resolve()
    assert below(script, run_root) and below(receipt, run_root)

    runtime_roots = {Path(sys.base_prefix).resolve(), Path(sys.prefix).resolve()}
    for key in ("stdlib", "platstdlib", "purelib", "platlib"):
        value = sysconfig.get_path(key)
        if value:
            runtime_roots.add(Path(value).resolve())
    exact_runtime = {Path(os.devnull).resolve()}
    reads, writes, denied = {}, set(), []
    network_attempts = []
    probe = Path(Path(sys.executable).anchor) / "__isomer_unbundled_source_probe__"
    started = datetime.now(timezone.utc).isoformat()

    def check_path(value, write=False):
        if isinstance(value, int) or value is None:
            return
        path = Path(os.fsdecode(value)).absolute().resolve()
        if write:
            allowed = below(path, run_root)
        else:
            allowed = (below(path, package) or below(path, run_root)
                       or any(below(path, root) for root in runtime_roots)
                       or path in exact_runtime)
        if not allowed:
            denied.append({"path": str(path), "write": write,
                           "intentional_probe": path == probe})
            raise PermissionError(f"standalone read/write boundary: {path}")
        if write:
            writes.add(str(path))
        else:
            kind = ("run-tree" if below(path, run_root) else
                    "package" if below(path, package) else "python-runtime")
            reads[(kind, str(path))] = reads.get((kind, str(path)), 0) + 1

    def audit(event, arguments):
        if event == "open":
            path, mode, flags = arguments
            write = (
                isinstance(mode, str) and any(ch in mode for ch in "wax+")
            ) or (isinstance(flags, int) and bool(flags & (
                os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)))
            check_path(path, bool(write))
        elif event in ("os.listdir", "os.scandir"):
            check_path(arguments[0] if arguments else os.getcwd())
        elif event == "import" and len(arguments) > 1 and arguments[1]:
            check_path(arguments[1])
        elif event in ("socket.connect", "socket.connect_ex", "socket.bind",
                       "socket.getaddrinfo", "subprocess.Popen", "os.system"):
            network_attempts.append(event)
            raise PermissionError(f"standalone worker forbids {event}")

    sys.addaudithook(audit)
    status, failure, versions = "failed", None, {}
    try:
        try:
            with probe.open("rb"):
                pass
        except PermissionError:
            pass
        else:
            raise RuntimeError("file-access negative control failed")
        # These imports are inside the same read boundary as the producer.
        import numpy
        import scipy
        versions = {"python": sys.version, "numpy": numpy.__version__,
                    "scipy": scipy.__version__}
        sys.path.insert(0, str(script.parent))
        runpy.run_path(str(script), run_name="__main__")
        status = "passed"
    except BaseException as exc:
        failure = {"type": type(exc).__name__, "message": str(exc)}
        traceback.print_exc()
    finally:
        unexpected = [item for item in denied if not item["intentional_probe"]]
        if unexpected or network_attempts:
            status = "failed"
        record = {
            "started_at_actual_utc": started,
            "finished_at_actual_utc": datetime.now(timezone.utc).isoformat(),
            "status": status, "failure": failure, "versions": versions,
            "script": str(script), "package_root": str(package),
            "run_root": str(run_root),
            "python_runtime_roots": sorted(str(x) for x in runtime_roots),
            "allowed_file_reads": [
                {"scope": scope, "path": path, "count": count}
                for (scope, path), count in sorted(reads.items())
            ],
            "writes_observed_before_receipt": sorted(writes),
            "intentional_forbidden_read_probe_blocked":
                any(item["intentional_probe"] for item in denied),
            "unexpected_denied_accesses": unexpected,
            "network_or_subprocess_attempts": network_attempts,
            "boundary_scope": (
                "Python audit events; not an OS sandbox. Native runtime/library "
                "loading is not claimed to be an exhaustive OS-level trace."
            ),
            "external_scientific_raw_sources_verified": [],
            "historical_raw_hash_claims_are_not_reverified": True,
        }
        with receipt.open("x") as handle:
            handle.write(json.dumps(record, indent=2) + "\n")
    return 0 if status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
