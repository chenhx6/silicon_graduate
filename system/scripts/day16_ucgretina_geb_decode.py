#!/usr/bin/env python3
"""Decode known producer fields using a compiled native GEB ABI description."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import struct
import subprocess
import sys


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--build", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert cfg["identity"] == "UCGRETINA-NATIVE-GEB-SMOKE-DECODE-01"
    assert sys.byteorder == "little"
    inc = Path(cfg["source_include"]).resolve()
    assert sha(inc/"GEB.hh") == cfg["GEB_header_sha256"]
    path = Path(cfg["binary_data"])
    assert sha(path) == cfg["binary_sha256"]
    a.build.mkdir(parents=True, exist_ok=True)
    cpp, exe = a.build/"producer-abi.cc", a.build/"producer-abi"
    cpp.write_text('''#include <cstdint>
#include <cstddef>
#include <iostream>
#include "GEB.hh"
int main(){std::cout<<sizeof(GEBDATA)<<" "<<sizeof(CRYS_IPS)<<" "<<sizeof(IP)<<" "
 <<offsetof(CRYS_IPS,ips)<<" "<<sizeof(G4SIM_EGS)<<" "<<sizeof(EG)<<" "
 <<offsetof(G4SIM_EGS,gammas)<<" "<<MAX_INTPTS<<" "<<MAX_SIM_GAMMAS<<"\\n";}
''')
    definitions = cfg.get("producer_definitions", [])
    assert set(definitions) <= {"HIGHMULT"}
    c = subprocess.run(["g++", "-std=c++17"]+["-D"+x for x in definitions]
                       +["-I"+str(inc), str(cpp), "-o", str(exe)], capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    sizes = list(map(int, subprocess.check_output([str(exe)], text=True).split()))
    header_size, crys_size, ip_size, ip_offset, sim_size, eg_size, eg_offset, max_ip, max_gamma = sizes
    assert header_size == 16 and ip_size == 24 and eg_size == 28
    types, multiplicity, ids = Counter(), Counter(), Counter()
    crystals = defaultdict(list)
    sim = {}
    issues, point_differences = [], []
    record_count = 0
    with path.open("rb") as f:
        while raw := f.read(header_size):
            if len(raw) != header_size:
                raise ValueError("Truncated GEB header")
            kind, length, timestamp = struct.unpack("<iiq", raw)
            assert 0 <= length <= 1_000_000
            payload = f.read(length)
            assert len(payload) == length
            types[kind] += 1
            record_count += 1
            if kind == 1:
                assert length == crys_size
                magic, crystal, num, energy = struct.unpack_from("<Iiif", payload)
                assert magic == 0xABCD5678 and 0 < num <= max_ip
                assert math.isfinite(energy) and energy >= 0
                ips = [struct.unpack_from("<ffffif", payload, ip_offset+i*ip_size) for i in range(num)]
                assert all(math.isfinite(v) for row in ips for v in row)
                ids[crystal] += 1
                crystals[timestamp].append({"id": crystal, "energy_keV": energy, "num_IP": num})
                point_differences.append({"timestamp": timestamp, "num_IP": num, "core_energy_keV": energy,
                    "core_minus_stored_IP_sum_keV": energy-sum(row[3] for row in ips)})
            elif kind == 11:
                assert length == sim_size
                magic, num, full = struct.unpack_from("<Iii", payload)
                assert magic == 0xABCD1234 and 0 <= num <= max_gamma
                assert timestamp not in sim
                gammas = []
                for i in range(num):
                    e, x, y, z, phi, theta = struct.unpack_from("<ffffff", payload, eg_offset+i*eg_size)
                    assert all(math.isfinite(v) for v in [e, x, y, z, phi, theta]) and e >= 0
                    gammas.append({"energy_keV": e, "source_mm": [x, y, z], "phi_rad": phi, "theta_rad": theta})
                sim[timestamp] = {"num": num, "fullEnergy_field": full, "gammas": gammas}
                multiplicity[num] += 1
    expected = set(i*cfg["timestamp_step"] for i in range(cfg["requested_events"]))
    timestamp_ok = set(sim) == expected
    if not timestamp_ok:
        issues.append("sim_timestamp_count_or_range")
    if cfg["mode"] == "gamma" and set(multiplicity) != {1}:
        issues.append("primary_gamma_not_one_per_event")
    if sim and all(row["num"] == 0 for row in sim.values()):
        issues.append("all_emitted_gamma_truth_records_empty")
    energy_excesses = []
    for timestamp, records in crystals.items():
        assert timestamp in sim
        deposited = sum(x["energy_keV"] for x in records)
        emitted = sum(x["energy_keV"] for x in sim[timestamp]["gammas"])
        if cfg["mode"] == "gamma" and deposited > emitted+.05+1e-5*emitted:
            energy_excesses.append({"timestamp": timestamp, "deposited": deposited, "emitted": emitted})
    if energy_excesses:
        issues.append("gamma_energy_excess")
    untruncated = [r for r in point_differences if r["num_IP"] < max_ip]
    inconsistent_point_sums = [r for r in untruncated
                              if abs(r["core_minus_stored_IP_sum_keV"]) > .05+1e-5*r["core_energy_keV"]]
    if inconsistent_point_sums:
        issues.append("core_IP_energy_sum_inconsistent")
    nonpositive_gamma_fields = sum(g["energy_keV"] <= 0 for event in sim.values() for g in event["gammas"])
    if nonpositive_gamma_fields:
        issues.append("nonpositive_emitted_gamma_truth_energy")
    result = {"identity": cfg["identity"], "contract_sha256": sha(a.contract), "script_sha256": sha(Path(__file__)),
        "binary_data_sha256": sha(path), "ABI_sizes_header_crys_IP_offset_sim_EG_offset_maxIP_maxGamma": sizes,
        "record_count": record_count, "record_types": dict(types), "sim_events": len(sim),
        "sim_multiplicity": dict(multiplicity), "crystal_record_count": sum(ids.values()),
        "crystal_id_counts": dict(sorted(ids.items())), "detected_event_count": len(crystals),
        "timestamp_contract_passed": timestamp_ok, "gamma_energy_excesses": energy_excesses,
        "producer_definitions": definitions, "inconsistent_point_sums": inconsistent_point_sums,
        "nonpositive_gamma_truth_records": nonpositive_gamma_fields,
        "max_abs_core_minus_untruncated_IPsum_keV": max(abs(x["core_minus_stored_IP_sum_keV"]) for x in untruncated),
        "max_num_IP_records": sum(x["num_IP"] == max_ip for x in point_differences),
        "max_emitted_gamma_keV": max((g["energy_keV"] for event in sim.values() for g in event["gammas"]), default=None),
        "issues": issues, "valid_fields_only_padding_beta_ignored": True,
        "all_declared_bookkeeping_controls_passed": not issues,
        "geometry_warning_or_full_response_resolved": False, "original_data_modified": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
