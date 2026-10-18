#!/usr/bin/env python3
"""Compare initialised CRYS fields; exclude trig_time and unused IP tail."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import struct


def records(path: Path) -> dict:
    rows = {}
    with path.open("rb") as stream:
        while header := stream.read(16):
            if len(header) != 16:
                raise ValueError("Truncated GEB header")
            kind, size, ts = struct.unpack("<iiq", header)
            if not 0 <= size <= 1_000_000:
                raise ValueError("Invalid payload size")
            payload = stream.read(size)
            if len(payload) != size:
                raise ValueError("Truncated payload")
            if kind != 1:
                continue
            if size != 464:
                raise ValueError("Contract requires native 464-byte CRYS_IPS")
            magic, crystal, count = struct.unpack_from("<Iii", payload)
            if magic != 0xABCD5678 or not 0 < count <= 16:
                raise ValueError("Invalid CRYS magic or IP count")
            key = (ts, crystal)
            if key in rows:
                raise ValueError("Duplicate timestamp/crystal pair")
            rows[key] = payload[:40] + payload[48:80] + payload[80:80+24*count]
    return rows


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    old, new = records(args.old), records(args.new)
    mismatches = [list(k) for k in sorted(old.keys() & new.keys()) if old[k] != new[k]]
    ok = bool(old) and old.keys() == new.keys() and not mismatches
    result = {
        "at": datetime.now(timezone.utc).isoformat(),
        "script_sha256": sha(Path(__file__)),
        "old": str(args.old), "new": str(args.new),
        "old_sha256": sha(args.old), "new_sha256": sha(args.new),
        "old_CRYS_records": len(old), "new_CRYS_records": len(new),
        "same_timestamp_crystal_keys": old.keys() == new.keys(),
        "mismatch_timestamp_crystals": mismatches,
        "all_known_CRYS_fields_bitwise_equal": ok,
        "excluded_fields": ["trig_time bytes40:48", "unused IP tail", "type11 capacity/padding/beta"],
        "scope": "chosen same-seed source histories only; not full geometry/response proof",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
