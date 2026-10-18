#!/usr/bin/env python3
"""Separate finite CG-product design from literal UCGretina and photon traces.

The general-density convention is an explicit hypothesis. Residuals are saved
even if it fails; this program never changes upstream source, signs or axes.
"""
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
from sympy.physics.wigner import clebsch_gordan, wigner_6j

from day16_pdco_ambiguity_preview import small_d
from day16_ucgretina_stokes_audit import configure
from day16_ucgretina_stokes_oracle import cg_half


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def finite_h(rank: int, low: int, high: int, ji2: int, jf2: int) -> float:
    cg = clebsch_gordan(low, high, rank, 1, 1, 2)
    if cg == 0:
        return 0.0
    ji, jf = sp.Rational(ji2, 2), sp.Rational(jf2, 2)
    try:
        six = wigner_6j(low, high, rank, ji, ji, jf)
    except ValueError:
        return 0.0
    exponent = low-high+(ji2+jf2)//2-1
    return float((-1)**exponent*cg*six*sp.sqrt((ji2+1)*(2*low+1)*(2*high+1)))


def tensor(ji2: int, rho: np.ndarray) -> list[np.ndarray]:
    ji = sp.Rational(ji2, 2)
    projections = list(range(-ji2, ji2+1, 2))
    result = []
    for rank in range(ji2+1):
        row = np.zeros(rank+1, dtype=complex)
        for q in range(rank+1):
            for i, m in enumerate(projections):
                for j, mp in enumerate(projections):
                    if m-mp != 2*q:
                        continue
                    factor = float((-1)**int((ji2-mp)//2)
                        *sp.sqrt(sp.Rational(ji2+1, 2*rank+1))
                        *clebsch_gordan(ji, ji, rank, sp.Rational(m, 2), -sp.Rational(mp, 2), q))
                    row[q] += factor*rho[i, j]
        result.append(row)
    assert abs(result[0][0]-1) < 1e-12
    return result


def density(case: dict) -> np.ndarray:
    n = case["Ji2"]+1
    if case["id"] == "rotatedMorseE2":
        m = np.arange(-2, 3)
        jp = np.zeros((5, 5), dtype=complex)
        for col, mi in enumerate(m[:-1]):
            jp[col+1, col] = math.sqrt(6-mi*(mi+1))
        jy = (jp-jp.conj().T)/(2j)
        val, vec = np.linalg.eigh(jy)
        ry = (vec*np.exp(-1j*.63*val))@vec.conj().T
        rz = np.diag(np.exp(-1j*.47*m))
        u = rz@ry
        return u@np.diag([0, .24, .52, .24, 0])@u.conj().T
    if case["id"] == "orientedM1":
        return np.diag([.05, .15, .8]).astype(complex)
    vectors = {"coherentSpin1mixed": [1, 1j/math.sqrt(2), -.4+.2j],
               "PSDSpin2mixed": [1, .2+1j, .5, -.3j, -.4],
               "PSDSpin2electric": [1, .2+1j, .5, -.3j, -.4],
               "PSDhalfSpinMixed": [.5, 1j, -.7, .8-.4j]}
    v = np.array(vectors[case["id"]], dtype=complex)
    pure = np.outer(v, v.conj())/np.vdot(v, v).real
    return pure if case["id"] == "coherentSpin1mixed" else .65*pure+.35*np.eye(n)/n


def parts(case: dict) -> list[tuple]:
    mp = case["MP"]
    if mp < 99:
        return [("M" if mp % 2 else "E", mp//2, 1.0)]
    low, high = mp//100, mp % 100
    return [("M" if low % 2 else "E", low//2, 1.0),
            ("M" if high % 2 else "E", high//2, case["delta"])]


def photon_trace(case: dict, rho: np.ndarray, theta: float, phi: float) -> dict:
    ji2, jf2 = case["Ji2"], case["Jf2"]
    components = parts(case)
    norm = math.sqrt(sum(a*a for _, _, a in components))
    helicities = {}
    for h in [-1, 1]:
        op = np.zeros((jf2+1, ji2+1), dtype=complex)
        for i, mf in enumerate(range(-jf2, jf2+1, 2)):
            for j, mi in enumerate(range(-ji2, ji2+1, 2)):
                mu = (mi-mf)//2
                for kind, ell, amp in components:
                    if abs(mu) <= ell:
                        op[i, j] += ((-1)**ell*amp/norm*math.sqrt((2*ell+1)/(8*math.pi))
                                     *cg_half(jf2, mf, ell, mu, ji2, mi)
                                     *np.exp(1j*mu*phi)*small_d(ell, mu, h, theta)
                                     *(h if kind == "M" else 1))
        helicities[h] = op
    ax = (-helicities[1]+helicities[-1])/math.sqrt(2)
    ay = -1j*(helicities[1]+helicities[-1])/math.sqrt(2)
    jones = np.array([[np.trace(a@rho@b.conj().T) for b in [ax, ay]] for a in [ax, ay]])
    assert np.max(abs(jones-jones.conj().T)) < 1e-12
    v = [float(jones.trace().real), float((jones[0, 0]-jones[1, 1]).real),
         float(2*jones[0, 1].real), float(2*jones[0, 1].imag)]
    assert v[0] >= -1e-14
    assert sum(x*x for x in v[1:]) <= v[0]*v[0]+1e-14
    return {"IQUV": [4*math.pi*x for x in v],
            "normalized": [x/v[0] for x in v[1:]] if v[0] > 1e-14 else None}


def finite_stokes(case: dict, pol: list[np.ndarray], theta: float, phi: float, lib: ct.CDLL) -> dict:
    ji2, jf2, mp, delta = case["Ji2"], case["Jf2"], case["MP"], case["delta"]
    ell = mp//2 if mp < 99 else mp//200
    mixed = mp > 99
    p1 = p2 = p3 = norm = 0.0
    for rank, rho in enumerate(pol):
        pn = pl1 = pl2 = 0.0
        for q, component in enumerate(rho):
            factor = 1 if q == 0 else 2
            z = component*np.exp(1j*q*phi)
            pn += factor*(z*lib.d_sdk(2*rank, 0, 2*q, math.cos(theta))).real
            if rank % 2 == 0:
                plus = lib.d_sdk(2*rank, 4, 2*q, math.cos(theta))
                minus = lib.d_sdk(2*rank, -4, 2*q, math.cos(theta))
                pl1 += factor*(z*(plus+minus)).real
                pl2 += factor*(z*(plus-minus)).imag
        f = lib.f_sdk(rank, ell, ell, jf2, ji2)
        h = finite_h(rank, ell, ell, ji2, jf2)
        if mixed:
            f += 2*delta*lib.f_sdk(rank, ell, ell+1, jf2, ji2)
            f += delta*delta*lib.f_sdk(rank, ell+1, ell+1, jf2, ji2)
            h -= 2*delta*finite_h(rank, ell, ell+1, ji2, jf2)
            h -= delta*delta*finite_h(rank, ell+1, ell+1, ji2, jf2)
        if rank % 2:
            p3 += 2*math.sqrt(2*rank+1)*pn*f
        else:
            norm += 2*math.sqrt(2*rank+1)*pn*f
            p1 += math.sqrt(2*rank+1)*pl1*h
            p2 += math.sqrt(2*rank+1)*pl2*h
    sign = 1 if (mp//100 if mixed else mp) % 2 else -1
    amplitude_norm = 1+delta*delta if mixed else 1
    iquv = [norm/(2*amplitude_norm), p1/sign/(2*amplitude_norm),
            p2/sign/(2*amplitude_norm), p3/(2*amplitude_norm)]
    return {"IQUV": iquv, "normalized": [x/iquv[0] for x in iquv[1:]] if iquv[0] > 1e-14 else None}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--binary", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "UCGRETINA-FINITE-CG-PRODUCT-AND-PSD-01"
    assert sha(a.input.parent/cfg["base_input"]) == cfg["base_sha256"]
    lib = ct.CDLL(str(a.binary.resolve()))
    configure(lib, "sdk")
    configure(lib, "old")
    coefficient_errors, zeros = [], []
    for ji2, jf2 in [(2, 0), (2, 2), (4, 2), (9, 9)]:
        for rank in range(ji2+1):
            if rank % 2:
                continue
            for low in [1, 2]:
                for high in [1, 2]:
                    den = lib.cg_sdk(2*low, 2, 2*high, -2, 2*rank)
                    h = finite_h(rank, low, high, ji2, jf2)
                    if den != 0:
                        original = lib.cg_sdk(2*low, 2, 2*high, 2, 2*rank)/den*lib.f_sdk(rank, low, high, jf2, ji2)
                        coefficient_errors.append(abs(h-original))
                    else:
                        zeros.append({"Ji2": ji2, "Jf2": jf2, "rank": rank, "L": low, "Lp": high, "H": h})
    rows, summaries = [], {}
    for case in cfg["new_cases"]:
        rho = density(case)
        eig = np.linalg.eigvalsh(rho)
        assert np.max(abs(rho-rho.conj().T)) < 1e-12 and abs(rho.trace()-1) < 1e-12 and min(eig) >= -1e-12
        pol = tensor(case["Ji2"], rho)
        residuals = []
        for deg in cfg["angles_deg"]:
            for phi in cfg["phi_rad"]:
                source = finite_stokes(case, pol, math.radians(deg), phi, lib)
                direct = photon_trace(case, rho, math.radians(deg), phi)
                residual = np.array(source["IQUV"])-direct["IQUV"]
                residuals.append(abs(residual))
                rows.append({"case": case["id"], "theta_deg": deg, "phi_rad": phi,
                             "finite_product_model": source, "photon_trace": direct, "IQUV_residual": residual.tolist()})
        summaries[case["id"]] = {"minimum_rho_eigenvalue": float(min(eig)), "max_abs_IQUV_residual": np.max(residuals, axis=0).tolist()}
    poles = [{"helper": name, "rank": rank, "d_k00_at_cos_minus1": getattr(lib, "d_"+name)(2*rank, 0, 0, -1.0)}
             for name in ["old", "sdk"] for rank in [0, 2, 4]]
    zero = photon_trace({"Ji2": 4, "Jf2": 0, "MP": 4, "delta": 0}, np.diag([0, 0, 1, 0, 0]), 0, 0)
    assert zero["normalized"] is None
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input), "script_sha256": sha(Path(__file__)),
              "binary_sha256": sha(a.binary), "max_finite_coefficient_residual": max(coefficient_errors),
              "zero_denominator_terms": zeros, "general_density_summary": summaries,
              "pole_littleD_controls": [{**v, "d_k00_at_cos_minus1": v["d_k00_at_cos_minus1"] if math.isfinite(v["d_k00_at_cos_minus1"]) else None} for v in poles],
              "true_zero_intensity_photon_control": zero, "rows": rows,
              "general_density_convention_is_hypothesis": True, "upstream_source_modified": False,
              "experimental_refit_or_full_geometry_response": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ["rows", "zero_denominator_terms"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
