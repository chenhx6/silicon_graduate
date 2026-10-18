#!/usr/bin/env python3
"""Calculate source singles and covariance using complete simulated histories.

Requires a passing native ABI/data audit. No energy smearing, threshold,
addback, fit, polarization calibration, or experimental covariance is inferred.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import struct

import numpy as np


def sha(path: Path) -> str:
    with path.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "UCGRETINA-SOURCE-HISTORY-COV-01"
    audit_path = Path(cfg["native_audit"])
    assert sha(audit_path) == cfg["native_audit_sha256"]
    audit = json.loads(audit_path.read_text())
    assert audit["all_declared_bookkeeping_controls_passed"]
    assert audit["ABI_sizes_header_crys_IP_offset_sim_EG_offset_maxIP_maxGamma"] == [16, 464, 24, 80, 1132, 28, 12, 16, 40]
    path = Path(cfg["data"])
    digest_before = sha(path)
    assert digest_before == cfg["data_sha256"] == audit["binary_data_sha256"]
    n = cfg["histories"]
    assert n > 1 and n == audit["sim_events"]
    regions = cfg["regions_half_open_keV"]
    for i, (low, high) in enumerate(regions):
        assert 0 <= low < high <= 8000
        assert all(high <= lo or low >= hi for lo, hi in regions[:i])
    vectors = np.zeros((n, len(regions)), dtype=np.int64)
    spectrum = np.zeros(8000, dtype=np.int64)
    event_bin_counts = Counter()
    multiplicity = np.zeros(n, dtype=np.int64)
    seen_sim = set()
    crystals = set()
    underflow = overflow = crys_records = 0
    maximum = 0.0
    with path.open("rb") as stream:
        while header := stream.read(16):
            assert len(header) == 16
            kind, size, ts = struct.unpack("<iiq", header)
            assert 0 <= size <= 1_000_000
            assert ts % 10000 == 0 and 0 <= ts//10000 < n
            event = ts//10000
            payload = stream.read(size)
            assert len(payload) == size
            if kind == 11:
                assert size == 1132 and event not in seen_sim
                assert struct.unpack_from("<I", payload)[0] == 0xABCD1234
                seen_sim.add(event)
            elif kind == 1:
                assert size == 464
                magic, crystal, points, energy = struct.unpack_from("<Iiif", payload)
                assert magic == 0xABCD5678 and 0 < points <= 16
                assert math.isfinite(energy) and energy >= 0
                assert (event, crystal) not in crystals
                crystals.add((event, crystal))
                crys_records += 1
                multiplicity[event] += 1
                maximum = max(maximum, energy)
                if energy < 0:
                    underflow += 1
                elif energy >= 8000:
                    overflow += 1
                else:
                    index = int(energy)
                    spectrum[index] += 1
                    event_bin_counts[(event, index)] += 1
                for i, (low, high) in enumerate(regions):
                    vectors[event, i] += low <= energy < high
            else:
                raise ValueError(f"Unexpected source record type {kind}")
    assert len(seen_sim) == n
    assert crys_records == audit["crystal_record_count"]
    assert int(spectrum.sum())+underflow+overflow == crys_records
    totals = vectors.sum(axis=0)
    second = vectors.T @ vectors
    cov_fixed_n = n/(n-1) * (second - np.outer(totals.astype(float), totals)/n)
    cov_numpy = np.cov(vectors, rowvar=False, ddof=1)*n
    eig = np.linalg.eigvalsh(cov_fixed_n)
    covariance_residual = float(np.max(np.abs(cov_fixed_n-cov_numpy)))
    per_bin_hdiag = np.zeros(8000, dtype=np.int64)
    for (_, index), count in event_bin_counts.items():
        per_bin_hdiag[index] += count*count
    hist_region_totals = []
    for low, high in regions:
        assert low == int(low) and high == int(high)
        hist_region_totals.append(int(spectrum[int(low):int(high)].sum()))
    assert hist_region_totals == totals.tolist()
    hits = np.count_nonzero(vectors, axis=0)
    zero_region_upper = [float(-math.expm1(math.log(.05)/n)) if count == 0 else None for count in hits]
    result = {
        "identity": cfg["identity"], "script_sha256": sha(Path(__file__)),
        "contract_sha256": sha(args.contract), "native_audit_sha256": sha(audit_path),
        "data": str(path), "data_sha256": digest_before,
        "histories": n, "crystal_singles": crys_records,
        "detected_histories": int(np.count_nonzero(multiplicity)),
        "zero_detection_histories_included_in_N": int(np.count_nonzero(multiplicity == 0)),
        "crystal_singles_multiplicity": dict(sorted(Counter(map(int, multiplicity)).items())),
        "max_core_energy_keV": maximum,
        "spectrum_axis": {"bins": 8000, "low_keV": 0, "high_keV": 8000},
        "spectrum_1keV": spectrum.tolist(), "spectrum_Rebin4": spectrum.reshape(-1, 4).sum(axis=1).tolist(),
        "underflow": underflow, "overflow": overflow,
        "regions_half_open_keV": regions,
        "region_singles_counts": totals.tolist(), "region_histories_with_any_hit": hits.tolist(),
        "region_mean_singles_per_history": (totals/n).tolist(),
        "region_H_sum_ccT": second.tolist(),
        "region_cov_total_fixedN": cov_fixed_n.tolist(),
        "region_cov_total_compoundPoisson": second.tolist(),
        "region_cov_mean_fixedN": (cov_fixed_n/n**2).tolist(),
        "region_fixedN_cov_eigenvalues": eig.tolist(),
        "independent_numpy_covariance_max_abs_difference": covariance_residual,
        "zero_hit_region_95pct_one_sided_binomial_upper_history_probability": zero_region_upper,
        "zero_hit_upper_scope": "probability of a history with >=1 regional hit within this model; not mean counts or experimental source limit",
        "bins_with_multiple_singles_same_history": int(np.count_nonzero(per_bin_hdiag != spectrum)),
        "sum_bin_Hdiag_minus_naive_counts": int((per_bin_hdiag-spectrum).sum()),
        "all_histogram_history_sums_match": True,
        "fixedN_covariance_PSD": bool(eig.min() >= -1e-9),
        "input_data_hash_after_analysis_unchanged": sha(path) == digest_before,
        "experimental_covariance_or_Q_inferred": False,
        "no_energy_smearing_threshold_addback_or_fit": True,
    }
    assert result["fixedN_covariance_PSD"] and covariance_residual < 1e-7
    assert result["input_data_hash_after_analysis_unchanged"]
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    short = {k: v for k, v in result.items() if not k.startswith("spectrum_")}
    print(json.dumps(short, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
