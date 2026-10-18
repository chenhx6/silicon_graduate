#!/usr/bin/env python3
"""Independent photon trace and zero-CG diagnosis for the literal-core audit."""
from __future__ import annotations

import argparse
import ctypes as ct
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan

from day16_pdco_ambiguity_preview import small_d
from day16_gretina_convention_audit import gaussian
from day16_ucgretina_stokes_audit import configure, tensor


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def cg_half(jf2: int, mf2: int, ell: int, mu: int, ji2: int, mi2: int) -> float:
    return float(clebsch_gordan(sp.Rational(jf2, 2), ell, sp.Rational(ji2, 2),
                               sp.Rational(mf2, 2), mu, sp.Rational(mi2, 2)))


def physical(case: dict, delta: float, theta: float, phi: float, pop: np.ndarray) -> dict:
    ji2, jf2, mp = case["Ji2"], case["Jf2"], case["MP"]
    if mp < 99:
        parts = [("M" if mp % 2 else "E", mp//2, 1.0)]
    else:
        low, high = mp//100, mp % 100
        parts = [("M" if low % 2 else "E", low//2, 1.0),
                 ("M" if high % 2 else "E", high//2, delta)]
    denom = math.sqrt(sum(a*a for _, _, a in parts))
    helicity = {}
    for h in [-1, 1]:
        matrix = np.zeros((jf2+1, ji2+1), dtype=complex)
        for row, mf in enumerate(range(-jf2, jf2+1, 2)):
            for col, mi in enumerate(range(-ji2, ji2+1, 2)):
                mu = (mi-mf)//2
                for kind, ell, amp in parts:
                    if abs(mu) <= ell:
                        matrix[row, col] += ((-1)**ell*amp/denom
                            *math.sqrt((2*ell+1)/(8*math.pi))
                            *cg_half(jf2, mf, ell, mu, ji2, mi)
                            *np.exp(1j*mu*phi)*small_d(ell, mu, h, theta)
                            *(h if kind == "M" else 1))
        helicity[h] = matrix
    def rate(psi: float) -> float:
        amp = (-np.exp(1j*psi)*helicity[1]+np.exp(-1j*psi)*helicity[-1])/math.sqrt(2)
        return float(np.sum(abs(amp)**2*pop[None, :]))
    para, perp = rate(0), rate(math.pi/2)
    total = para+perp
    assert total > 0
    s1 = (para-perp)/total
    s2 = (rate(math.pi/4)-rate(3*math.pi/4))/total
    s3 = float(np.sum((abs(helicity[1])**2-abs(helicity[-1])**2)*pop[None, :]))/total
    assert s1*s1+s2*s2+s3*s3 <= 1+1e-12
    return {"W": 4*math.pi*total, "Stokes": [s1, s2, s3]}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    contract = json.loads(a.input.read_text())
    assert contract["identity"] == "UCGRETINA-STOKES-PHYSICAL-ORACLE-01"
    for key in ["core_input", "core_result"]:
        q = a.input.parent/contract[key]
        assert sha(q) == contract[key+"_sha256"]
    cfg = json.loads((a.input.parent/contract["core_input"]).read_text())
    original = json.loads((a.input.parent/contract["core_result"]).read_text())
    binary = Path(contract["binary"])
    assert sha(binary) == contract["binary_sha256"]
    lib = ct.CDLL(str(binary.resolve()))
    for label in ["old", "sdk"]:
        configure(lib, label)
    cases = {c["id"]: c for c in cfg["cases"]}
    rows, finite_errors, norm_errors = [], [], []
    for measured in original["rows"]:
        case = cases[measured["case"]]
        pop = np.array(case["population"], dtype=float) if "population" in case else gaussian(case["Ji2"], .56)
        predicted = physical(case, measured["delta"], math.radians(measured["theta_deg"]), measured["phi_rad"], pop)
        # The source code's norm includes the sum of both helicity components
        # and the unnormalised squared multipole amplitudes.
        amplitude_norm = 1+measured["delta"]**2 if case["MP"] > 99 else 1
        norm_errors.append(abs(measured["norm"]/(2*amplitude_norm)-predicted["W"]))
        error = None
        if not measured["nonfinite_components"]:
            error = max(abs(x-y) for x, y in zip(measured["Stokes"], predicted["Stokes"]))
            finite_errors.append(error)
        rows.append({"case": measured["case"], "helper": measured["helper"],
                     "delta": measured["delta"], "theta_deg": measured["theta_deg"],
                     "phi_rad": measured["phi_rad"], "photon_trace": predicted,
                     "literal_nonfinite": measured["nonfinite_components"],
                     "finite_Stokes_max_error": error})
    zeros = []
    for label in ["old", "sdk"]:
        cg, fc = getattr(lib, "cg_"+label), getattr(lib, "f_"+label)
        for rank, low, high, ji2, jf2 in [(0, 1, 2, 2, 2), (4, 1, 1, 4, 2)]:
            z = {"helper": label, "rank": rank, "L": low, "Lp": high,
                 "numerator": cg(2*low, 2, 2*high, 2, 2*rank),
                 "denominator": cg(2*low, 2, 2*high, -2, 2*rank),
                 "F": fc(rank, low, high, jf2, ji2)}
            assert z["numerator"] == z["denominator"] == z["F"] == 0.0
            zeros.append(z)
    dp = ct.POINTER(ct.c_double)
    limit_controls = []
    for label in ["old", "sdk"]:
        pop = np.array([.1, .8, .1])
        rho = tensor(lib, label, 2, pop)
        imag = np.zeros_like(rho)
        values = {}
        for mp in [3, 304]:
            out = np.empty(4)
            getattr(lib, "emit_"+label)(2, 2, mp, 0.0, math.pi/2, .37,
                rho.ctypes.data_as(dp), imag.ctypes.data_as(dp), 3, out.ctypes.data_as(dp))
            values[str(mp)] = {"finite": bool(np.isfinite(out[:3]).all()),
                              "Stokes": [float(x) if math.isfinite(x) else None for x in out[:3]],
                              "norm": float(out[3])}
        assert values["3"]["finite"] and not values["304"]["finite"]
        assert abs(values["3"]["norm"]-values["304"]["norm"]) < 1e-12
        limit_controls.append({"helper": label, "same_Ji2": 2, "same_Jf2": 2, "delta": 0,
                               "pure_vs_mixed_label": values})
    assert max(finite_errors) < 1e-12
    assert max(norm_errors) < 1e-12
    result = {"identity": contract["identity"], "input_sha256": sha(a.input),
              "script_sha256": sha(Path(__file__)),
              "max_finite_pure_control_Stokes_error": max(finite_errors),
              "max_all_case_intensity_norm_error": max(norm_errors),
              "all_photon_trace_Stokes_physical": True, "actual_zero_ratio_factors": zeros,
              "same_path_pure_limit_controls": limit_controls, "rows": rows,
              "core_nans_are_not_zero_intensity_boundaries": True,
              "original_source_modified_or_patched": False,
              "full_event_geometry_response_validated": False,
              "experimental_paper_claim_falsified": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
