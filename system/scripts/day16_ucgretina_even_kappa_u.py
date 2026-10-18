#!/usr/bin/env python3
"""Isolate literal Stokes U with pure M1 and only even kappa coherence."""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_ucgretina_stokes_audit import configure
from day16_ucgretina_finite_product import tensor, photon_trace


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "UCGRETINA-PURE-M1-EVEN-KAPPA-STOKES-U-CONTROL-01"
    binary = Path(cfg["original_binary"])
    assert sha(binary) == cfg["binary_sha256"]
    v = np.array([1j, 0, 1], dtype=complex)/math.sqrt(2)
    rho = np.outer(v, v.conj())
    pol = tensor(2, rho)
    assert all(abs(value) < 1e-14 for row in pol for q, value in enumerate(row) if q % 2)
    flat = np.concatenate(pol)
    real, imag = np.ascontiguousarray(flat.real), np.ascontiguousarray(flat.imag)
    lib = ct.CDLL(str(binary.resolve()))
    dp = ct.POINTER(ct.c_double)
    rows = []
    for helper in ["old", "sdk"]:
        configure(lib, helper)
        for degree in cfg["theta_deg"]:
            for phi in cfg["phi_rad"]:
                out = np.empty(4)
                theta = math.radians(degree)
                getattr(lib, "emit_"+helper)(2, 0, 3, 0, theta, phi,
                    real.ctypes.data_as(dp), imag.ctypes.data_as(dp), 3, out.ctypes.data_as(dp))
                direct = photon_trace(cfg, rho, theta, phi)
                assert np.isfinite(out).all() and out[3] > 0
                ref = direct["normalized"]
                assert ref is not None
                residual = [out[3]/2-direct["IQUV"][0], out[0]-ref[0], out[1]+ref[1], out[2]-ref[2]]
                assert max(abs(x) for x in residual) < 1e-12
                def kn_ratio(u: float) -> float:
                    # E=mc^2, scatter90deg, unpolarized electron; relative
                    # K atPhi45/135: cos2Phi=0, sin2Phi=+1/-1.
                    return (1.5-u)/(1.5+u)
                rows.append({"helper": helper, "theta_deg": degree, "phi_rad": phi,
                    "literal_Stokes": out[:3].tolist(), "photon_Jones_Stokes": ref,
                    "residual_I_Q_Uopposite_V": list(map(float, residual)),
                    "relative_K45_over_K135_literal": kn_ratio(float(out[1])),
                    "relative_K45_over_K135_Jones": kn_ratio(ref[1])})
    forward = photon_trace(cfg, rho, 0.0, 0.0)
    assert forward["normalized"] is not None and abs(forward["normalized"][1]-1) < 1e-12
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input),
        "script_sha256": sha(Path(__file__)), "binary_sha256": sha(binary),
        "rho_min_eigenvalue": float(min(np.linalg.eigvalsh(rho))),
        "odd_kappa_exactly_absent_within_tolerance": True,
        "rows": rows, "max_contract_residual": max(abs(v) for row in rows for v in row["residual_I_Q_Uopposite_V"]),
        "analytical_forward_Jones_U": forward["normalized"][1],
        "original_core_finite_and_zeroCGproblem_absent": True,
        "U_is_opposite_in_frozen_eTheta_ePhi_Jones_contract": True,
        "only_U_attribution_scope": "selected coherent state + fixed code and G4consumer convention, not the original experiment",
        "detector_response_or_real_KN_count_measurement": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, ensure_ascii=False, indent=2))
    print(json.dumps(rows[0], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
