#!/usr/bin/env python3
"""Compare per-crystal, event-wide and literal cumulative back selections."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import struct


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flags(rows: list[dict]) -> dict:
    prefix = False
    result = {}
    for row in rows:
        prefix |= row["has_back_IP"]
        result[row["crystal"]] = prefix
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert sha(Path(cfg["source"])) == cfg["source_sha256"]
    summaries = []
    for item in cfg["inputs"]:
        path = Path(item["data"])
        assert sha(path) == item["sha256"]
        events = defaultdict(list)
        excluded = set()
        with path.open("rb") as stream:
            while header := stream.read(16):
                assert len(header) == 16
                kind, size, ts = struct.unpack("<iiq", header)
                payload = stream.read(size)
                assert len(payload) == size
                if kind != 1:
                    continue
                assert size == 464
                magic, crystal, count, energy = struct.unpack_from("<Iiif", payload)
                assert magic == 0xABCD5678 and 0 < count <= 16
                segments = [struct.unpack_from("<i", payload, 80+24*i+16)[0] for i in range(count)]
                assert all(0 <= value < 36 for value in segments)
                if count == 16:
                    excluded.add(ts)
                events[ts].append({"crystal": crystal, "core_energy_keV": energy,
                    "segments": segments, "has_back_IP": any(value//6 == 5 for value in segments)})
        total = per_crystal = cumulative = event_wide = changed = extra = 0
        witnesses = []
        for ts, rows in events.items():
            if ts in excluded:
                continue
            forward, reverse = flags(rows), flags(list(reversed(rows)))
            actual = {row["crystal"]: row["has_back_IP"] for row in rows}
            assert len(actual) == len(rows)
            total += len(rows)
            per_crystal += sum(actual.values())
            cumulative += sum(forward.values())
            event_wide += len(rows)*any(actual.values())
            n_extra = sum(forward[k] and not actual[k] for k in actual)
            extra += n_extra
            differing = [k for k in actual if forward[k] != reverse[k]]
            changed += bool(differing)
            if differing and len(witnesses) < 4:
                witnesses.append({"timestamp": ts, "rows_in_native_bank_order": rows,
                    "forward_cumulative": forward, "reversed_cumulative": reverse,
                    "per_crystal": actual, "changed_crystals": differing})
        summaries.append({"mode": item["mode"], "input_sha256": sha(path),
            "histories_with_crystals": len(events), "excluded_possible_IP_truncation_histories": len(excluded),
            "analyzed_crystal_records": total, "per_crystal_back_records": per_crystal,
            "bank_order_cumulative_back_records": cumulative, "event_wide_back_class_records": event_wide,
            "prefix_extra_over_per_crystal": extra,
            "histories_with_order_dependent_labels": changed, "actual_history_witnesses": witnesses,
            "input_after_read_unchanged": sha(path) == item["sha256"]})
    result = {"contract_sha256": sha(args.contract), "script_sha256": sha(Path(__file__)),
        "summaries": summaries,
        "scope": "native bank-order control of a public-code selection; original experimental producer/order/FEP denominator not identified",
        "not_new_experimental_backfraction_or_efficiency": True}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps([{k: v for k, v in row.items() if k != "actual_history_witnesses"}
                      for row in summaries], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
