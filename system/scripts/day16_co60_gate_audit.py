#!/usr/bin/env python3
"""Audit emitted gamma pairs and a named unsmeared detector-angle recipe.

The recipe reconstructs native producer coordinates with its own crmat.
It does not run GRUTinizer, simulate polarized EM, or infer an experimental Q.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import struct

import numpy as np


def sha(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def direction(phi: float, theta: float) -> np.ndarray:
    assert math.isfinite(phi) and math.isfinite(theta) and 0 <= theta <= math.pi+1e-6
    return np.array([math.sin(theta)*math.cos(phi), math.sin(theta)*math.sin(phi), math.cos(theta)])


def moments(values: list[float]) -> dict:
    x = np.asarray(values)
    n = len(x)
    assert n > 1
    vectors = np.column_stack([5*(3*x*x-1)/2, 9*(35*x**4-30*x*x+3)/8])
    cov = np.cov(vectors, rowvar=False, ddof=1)/n
    assert np.linalg.eigvalsh(cov).min() >= -1e-12
    return {"selected_histories": n, "a2_a4_moment_estimate": vectors.mean(axis=0).tolist(),
            "a2_a4_cov_mean": cov.tolist(), "a2_a4_stat_SE": np.sqrt(cov.diagonal()).tolist(),
            "scope": "conditional on one complete emitted pair/history; no detector unfolding"}


def analyze(row: dict, matrix: np.ndarray, bins: int) -> dict:
    path = Path(row["data"])
    assert sha(path) == row["data_sha256"]
    audit_path = Path(row["native_audit"])
    assert sha(audit_path) == row["native_audit_sha256"]
    audit = json.loads(audit_path.read_text())
    assert audit["all_declared_bookkeeping_controls_passed"]
    assert audit["max_num_IP_records"] == 0, "Possible IP truncation blocks this angle recipe"
    assert audit["ABI_sizes_header_crys_IP_offset_sim_EG_offset_maxIP_maxGamma"] == [16, 464, 24, 80, 1132, 28, 12, 16, 40]
    assert audit["binary_data_sha256"] == row["data_sha256"]
    n = audit["sim_events"]
    simulated, crystals = {}, defaultdict(list)
    orthogonal, roundtrip, radii = [], [], []
    tied_maxima = 0
    with path.open("rb") as stream:
        while header := stream.read(16):
            assert len(header) == 16
            kind, size, ts = struct.unpack("<iiq", header)
            assert 0 <= size <= 1_000_000 and ts % 10000 == 0 and 0 <= ts//10000 < n
            payload = stream.read(size)
            assert len(payload) == size
            if kind == 11:
                assert size == 1132 and ts not in simulated
                magic, count, _ = struct.unpack_from("<Iii", payload)
                assert magic == 0xABCD1234 and 0 <= count <= 40
                photons = []
                for i in range(count):
                    energy, x, y, z, phi, theta = struct.unpack_from("<ffffff", payload, 12+28*i)
                    assert energy > 0 and all(math.isfinite(v) for v in [energy, x, y, z, phi, theta])
                    photons.append((energy, direction(phi, theta)))
                simulated[ts] = photons
            elif kind == 1:
                assert size == 464
                magic, cid, count, energy = struct.unpack_from("<Iiif", payload)
                assert magic == 0xABCD5678 and 0 < count <= 16
                points = [struct.unpack_from("<ffffif", payload, 80+24*i) for i in range(count)]
                assert all(math.isfinite(v) for p in points for v in p)
                order = max(range(count), key=lambda i: points[i][3])
                tied_maxima += sum(p[3] == points[order][3] for p in points) > 1
                local = np.asarray(points[order][:3])
                transform = matrix[cid//4, cid % 4]
                rotation, translation = transform[:3, :3], transform[:3, 3]*10
                orthogonal.append(float(np.max(np.abs(rotation.T@rotation-np.eye(3)))))
                world = rotation@local+translation
                roundtrip.append(float(np.linalg.norm(rotation.T@(world-translation)-local)))
                assert 100 < np.linalg.norm(world) < 500
                radii.append(float(np.linalg.norm(world)))
                crystals[ts].append((cid, energy, world/np.linalg.norm(world)))
            else:
                raise ValueError(f"Unexpected source record type {kind}")
    assert set(simulated) == set(range(0, n*10000, 10000))
    assert max(orthogonal, default=0) < 1e-4 and max(roundtrip, default=0) < .02
    emitted, measured = [], []
    missing, ambiguous = [], []
    literal_missing_cosines = []
    detector_gate_classes = Counter()
    for ts, photons in simulated.items():
        high = [v for e, v in photons if 1331 < e < 1334]
        low = [v for e, v in photons if 1171 < e < 1175]
        if len(high) == len(low) == 1:
            cosine = float(high[0]@low[0])
            assert -1-1e-12 <= cosine <= 1+1e-12
            emitted.append(cosine)
        else:
            target = missing if not high or not low else ambiguous
            target.append({"timestamp": ts, "num_high": len(high), "num_low": len(low)})
            # Preserve the literal fallback path as an explicitly invalid control.
            a = high[-1] if high else np.full(3, -1.)
            b = low[-1] if low else np.full(3, -1.)
            literal_missing_cosines.append(float(a@b/(a@a)/(b@b)))
        high_hits = [h for h in crystals[ts] if 1328 < h[1] < 1337]
        low_hits = [h for h in crystals[ts] if 1168 < h[1] < 1178]
        detector_gate_classes[(len(low_hits), len(high_hits))] += 1
        if len(high_hits) == len(low_hits) == 1:
            assert high_hits[0][0] != low_hits[0][0]
            measured.append(float(high_hits[0][2]@low_hits[0][2]))
    emitted_hist = np.histogram(emitted, bins=100, range=(-1, 1))[0]
    detector_hist = np.histogram(measured, bins=bins, range=(-1, 1))[0]
    assert int(emitted_hist.sum()) == len(emitted) and int(detector_hist.sum()) == len(measured)
    # At most one named detector pair per complete decay history.
    count = detector_hist.astype(float)
    cov = n/(n-1)*(np.diag(count)-np.outer(count, count)/n)
    assert np.linalg.eigvalsh(cov).min() > -1e-9
    return {"mode": row["mode"], "data_sha256": sha(path), "histories": n,
        "emitted_complete_unique_pairs": len(emitted), "missing_pair_histories": missing,
        "ambiguous_pair_histories": ambiguous, "literal_invalid_fallback_cosines": literal_missing_cosines,
        "emitted_moments": moments(emitted), "emitted_100bin_histogram": emitted_hist.tolist(),
        "detector_unique_unsmeared_pairs": len(measured),
        "detector_gate_multiplicity_classes": {str(k): v for k, v in sorted(detector_gate_classes.items())},
        "detector_coarse_histogram": detector_hist.tolist(), "detector_count_cov_fixedN": cov.tolist(),
        "max_crmat_rotation_orthogonality_error": max(orthogonal, default=0),
        "max_crmat_roundtrip_error_mm": max(roundtrip, default=0), "max_IP_energy_tie_records": tied_maxima,
        "highest_IP_global_radius_min_max_mm": [min(radii, default=0), max(radii, default=0)],
        "input_after_analysis_unchanged": sha(path) == row["data_sha256"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "CO60-GATE-ROLE-NATIVE-ANALYSIS-01"
    crmat = Path(cfg["crmat"])
    assert sha(crmat) == cfg["crmat_sha256"] and crmat.stat().st_size == 7936
    matrix = np.frombuffer(crmat.read_bytes(), dtype="<f4").reshape(31, 4, 4, 4).astype(float)
    rows = [analyze(row, matrix, cfg["detector_cos_bins"]) for row in cfg["inputs"]]
    corr, iso = (next(r for r in rows if r["mode"] == mode) for mode in ["corr", "iso"])
    c, i = (np.array(r["detector_coarse_histogram"], dtype=float) for r in [corr, iso])
    ok = i > 0
    scale = iso["histories"]/corr["histories"]
    ratio = np.full_like(c, np.nan)
    ratio[ok] = scale*c[ok]/i[ok]
    jc, ji = np.diag(scale/i[ok]), np.diag(-scale*c[ok]/i[ok]**2)
    cc, ci = (np.array(r["detector_count_cov_fixedN"])[np.ix_(ok, ok)] for r in [corr, iso])
    cov = jc@cc@jc.T+ji@ci@ji.T
    eigenvalues = np.linalg.eigvalsh(cov)
    assert eigenvalues.min(initial=0) > -1e-9
    result = {"identity": cfg["identity"], "script_sha256": sha(Path(__file__)),
        "contract_sha256": sha(args.contract), "crmat_sha256": sha(crmat), "rows": rows,
        "detector_ratio_corr_per_history_over_iso_per_history": [float(x) if math.isfinite(x) else None for x in ratio],
        "undefined_denominator_zero_bins": np.where(~ok)[0].tolist(),
        "ratio_cov_valid_bins_fixedN_independent_MC": cov.tolist(),
        "ratio_cov_valid_bins_eigenvalues": eigenvalues.tolist(),
        "ratio_covariance_approximation": "first-order delta method; no exact confidence interval or zero-count upper bound",
        "minimum_reference_count_valid_bins": int(i[ok].min()) if np.any(ok) else None,
        "GRUT_runtime_crmat_dat_verified": False,
        "scope": "named unsmeared native-source recipe; independent finite-MC controls, not experiments or original GRUT response",
        "GRUTinizer_executed_or_Q_inferred": False}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"counts": [{k: r[k] for k in ["mode", "histories", "emitted_complete_unique_pairs", "detector_unique_unsmeared_pairs", "emitted_moments", "max_crmat_rotation_orthogonality_error", "max_crmat_roundtrip_error_mm"]} for r in rows],
        "missing_pairs": {r["mode"]: len(r["missing_pair_histories"]) for r in rows},
        "undefined_ratio_bins": result["undefined_denominator_zero_bins"], "no_Q": True}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
