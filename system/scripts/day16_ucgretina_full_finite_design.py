#!/usr/bin/env python3
"""Validate a separately derived finite single-emitter IQUV design.

Implements the frozen full-q/Jones algebra, never patches upstream UCGretina.
New PSD matrices are read from a pre-execution snapshot, not tuned to results.
"""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_ucgretina_finite_product import finite_h, tensor, density, photon_trace
from day16_ucgretina_stokes_audit import configure


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_rho(rho: np.ndarray) -> np.ndarray:
    if (rho.ndim != 2 or rho.shape[0] != rho.shape[1]
            or np.max(abs(rho-rho.conj().T)) > 1e-12
            or abs(np.trace(rho)-1) > 1e-12
            or np.linalg.eigvalsh(rho).min() < -1e-12):
        raise ValueError("Density must be Hermitian, unit trace and PSD; no clipping")
    return rho


def design(case: dict, pol: list[np.ndarray], theta: float, phi: float, lib: ct.CDLL,
           coordinate: str = "native") -> dict:
    ji2, jf2, mp, delta = case["Ji2"], case["Jf2"], case["MP"], case["delta"]
    mixed = mp > 99
    low = mp//200 if mixed else mp//2
    high = (mp % 100)//2 if mixed else low
    if mixed and high != low+1:
        raise ValueError("This frozen design covers adjacent real multipoles only")
    normalization = 1+delta*delta if mixed else 1.0
    lower_em_sign = 1 if (mp//100 if mixed else mp) % 2 else -1
    if coordinate not in ["native", "RB"]:
        raise ValueError("Unknown amplitude coordinate")
    # The amplitude and both cross-coefficient families transform together.
    # This is the fixed adjacent-multipole single-emitter bridge, not a new
    # physical phase change or an arbitrary cascade rule.
    cross_phase = -1 if coordinate == "RB" else 1
    t0, t2, t3 = 0j, 0j, 0j
    for rank, row in enumerate(pol):
        f = lib.f_sdk(rank, low, low, jf2, ji2)
        h = finite_h(rank, low, low, ji2, jf2)
        if mixed:
            f += 2*delta*cross_phase*lib.f_sdk(rank, low, high, jf2, ji2)
            f += delta*delta*lib.f_sdk(rank, high, high, jf2, ji2)
            h -= 2*delta*cross_phase*finite_h(rank, low, high, ji2, jf2)
            h -= delta*delta*finite_h(rank, high, high, ji2, jf2)
        if f == 0 and (h == 0 or rank % 2):
            continue
        def s(photon_m: int) -> complex:
            total = 0j
            for q in range(-rank, rank+1):
                r = row[q] if q >= 0 else (-1)**q*row[-q].conjugate()
                total += r*np.exp(1j*q*phi)*lib.d_sdk(2*rank, 2*q, 2*photon_m, math.cos(theta))
            return total
        scalar = s(0)
        if rank % 2:
            t3 += math.sqrt(2*rank+1)*f*scalar
        else:
            t0 += math.sqrt(2*rank+1)*f*scalar
            if h != 0:
                t2 += math.sqrt(2*rank+1)*h*s(2)
    assert max(abs(t0.imag), abs(t3.imag)) < 1e-10*normalization
    iquv = np.array([t0.real/normalization, t2.real/lower_em_sign/normalization,
                     -t2.imag/lower_em_sign/normalization, t3.real/normalization])
    return {"IQUV": iquv.tolist(),
            "normalized": (iquv[1:]/iquv[0]).tolist() if iquv[0] > 1e-14 else None,
            "scalar_imaginary_residual": max(abs(t0.imag), abs(t3.imag))/normalization}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "FULL-FINITE-TENSOR-STOKES-DESIGN-01"
    for path_key, hash_key in [("derivation_contract", "derivation_contract_sha256"),
                                ("regression_input", "regression_input_sha256")]:
        assert sha(args.input.parent/cfg[path_key]) == cfg[hash_key]
    binary = Path(cfg["kernel_binary"])
    assert sha(binary) == cfg["kernel_binary_sha256"]
    lib = ct.CDLL(str(binary.resolve()))
    configure(lib, "sdk")
    old = json.loads((args.input.parent/cfg["regression_input"]).read_text())
    selected = [(c, validate_rho(density(c))) for c in old["new_cases"]]
    for case in cfg["new_cases"]:
        rho = np.array(case["rho_real"])+1j*np.array(case["rho_imag"])
        selected.append((case, validate_rho(rho)))
    rows, summaries = [], {}
    rotation_errors, coordinate_errors = [], []
    pure_limits = []
    for case, rho in selected:
        pol = tensor(case["Ji2"], rho)
        residuals, physical_margins = [], []
        for degree in cfg["angles_deg"]:
            theta = math.radians(degree)
            for phi in cfg["phi_rad"]:
                actual = design(case, pol, theta, phi, lib)
                trace = photon_trace(case, rho, theta, phi)
                error = np.array(actual["IQUV"])-trace["IQUV"]
                residuals.append(abs(error))
                iquv = actual["IQUV"]
                physical_margins.append(iquv[0]*iquv[0]-sum(x*x for x in iquv[1:]))
                rows.append({"case": case["id"], "theta_deg": degree, "phi_rad": phi,
                             "design": actual, "photon_trace": trace, "residual": error.tolist()})
        # Rz rotation co-rotates direction and the e_theta/e_phi basis.
        alpha, theta, phi = .613, .723, .284
        m = np.arange(-case["Ji2"], case["Ji2"]+1, 2)/2
        rz = np.diag(np.exp(-1j*alpha*m))
        rotated = rz@rho@rz.conj().T
        x = np.array(design(case, tensor(case["Ji2"], rotated), theta, phi+alpha, lib)["IQUV"])
        y = np.array(design(case, pol, theta, phi, lib)["IQUV"])
        rotation_errors.append(float(max(abs(x-y))))
        rb_case = {**case, "delta": -case["delta"]}
        rb = np.array(design(rb_case, pol, theta, phi, lib, coordinate="RB")["IQUV"])
        coordinate_errors.append(float(max(abs(rb-y))))
        if case["MP"] > 99:
            mp = case["MP"]
            pure = {**case, "MP": mp//100, "delta": 0.0}
            mixed0 = {**case, "delta": 0.0}
            upper = {**case, "MP": mp % 100, "delta": 0.0}
            large = {**case, "delta": 1e6}
            z0 = np.array(design(mixed0, pol, theta, phi, lib)["IQUV"])
            zp = np.array(design(pure, pol, theta, phi, lib)["IQUV"])
            zi = np.array(design(large, pol, theta, phi, lib)["IQUV"])
            zu = np.array(design(upper, pol, theta, phi, lib)["IQUV"])
            pure_limits.append({"case": case["id"], "delta0_pure_error": float(max(abs(z0-zp))),
                                "delta1e6_upper_pure_error": float(max(abs(zi-zu)))})
        summaries[case["id"]] = {"Ji2": case["Ji2"], "Jf2": case["Jf2"], "MP": case["MP"],
            "minimum_density_eigenvalue": float(np.linalg.eigvalsh(rho).min()),
            "max_abs_IQUV_error": np.max(residuals, axis=0).tolist(),
            "minimum_Stokes_PSD_margin": min(physical_margins)}
    bad = np.diag([1.1, -.1, 0]).astype(complex)
    rejected = False
    try:
        validate_rho(bad)
    except ValueError:
        rejected = True
    assert rejected
    zero_case = {"Ji2": 4, "Jf2": 0, "MP": 4, "delta": 0.0}
    zero_rho = np.diag([0, 0, 1, 0, 0]).astype(complex)
    zero = design(zero_case, tensor(4, zero_rho), 0.0, 0.0, lib)
    assert zero["normalized"] is None
    max_error = max(abs(x) for row in rows for x in row["residual"])
    passed = (max_error < 1e-10 and max(rotation_errors) < 1e-10 and max(coordinate_errors) < 1e-10
              and min(v["minimum_Stokes_PSD_margin"] for v in summaries.values()) > -1e-10
              and all(v["delta0_pure_error"] < 1e-10 for v in pure_limits)
              and all(v["delta1e6_upper_pure_error"] < 1e-5 for v in pure_limits))
    result = {"identity": cfg["identity"], "input_sha256": sha(args.input), "script_sha256": sha(Path(__file__)),
              "source_binary_sha256": sha(binary), "case_count": len(selected), "calls": len(rows),
              "new_frozen_PSD_case_count": len(cfg["new_cases"]), "all_declared_design_controls_passed": passed,
              "max_abs_IQUV_error": max_error, "max_Rz_covariance_error": max(rotation_errors),
              "max_native_RB_synchronized_IQUV_error": max(coordinate_errors),
              "case_summary": summaries, "pure_limit_controls": pure_limits,
              "nonPSD_input_rejected_not_clipped": rejected, "true_zero_intensity_control": zero,
              "rows": rows, "original_source_or_binary_modified": False,
              "full_array_response_or_original_paper_producer_validated": False,
              "new_experimental_delta_or_credit": False}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ["rows", "case_summary"]}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
