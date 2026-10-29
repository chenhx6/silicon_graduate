#!/usr/bin/env python3
"""Direct E3 network for odd-A octupole parity-doublet bands.

The calculation is a transparent strong-coupling angular-momentum model.  It
implements the convention used in the companion research note:

  <Ii K p || M(E3) || If K -p>
    = sqrt(2 Ii + 1) C(Ii K, 3 0 | If K) m3 F(K, If, p_oct)

where m3 = sqrt(7/(16 pi)) e Q30 and, for K=1/2,
F = 1 + (-1)**(If+1/2) p_oct.  B(E3) is obtained by dividing the squared
reduced matrix element by 2 Ii+1.  The phase convention is explicit; changing
the intrinsic phase changes p_oct but not an observable when the convention is
changed consistently.

Outputs are written beside this script unless --outdir is supplied.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

def half(value: str | int | float):
    """Convert a spin written as 1/2, 3/2, ... to an exact Fraction."""
    if isinstance(value, str) and "/" in value:
        n, d = value.split("/", 1)
        return Fraction(int(n), int(d))
    return Fraction(str(value))


def spin_text(j) -> str:
    j = Fraction(j)
    return f"{j.numerator}/{j.denominator}" if j.denominator != 1 else str(j.numerator)


def _factorial(x: Fraction) -> float:
    if x.denominator != 1 or x < 0:
        return 0.0
    return math.factorial(x.numerator)


def cg(j1, m1, j2, m2, j3, m3) -> float:
    """Wigner Clebsch-Gordan coefficient from the finite factorial sum."""
    if m3 != m1 + m2 or abs(m1) > j1 or abs(m2) > j2 or abs(m3) > j3:
        return 0.0
    if j3 < abs(j1 - j2) or j3 > j1 + j2:
        return 0.0
    pref = math.sqrt(
        (2 * float(j3) + 1)
        * _factorial(j1 + j2 - j3)
        * _factorial(j1 - j2 + j3)
        * _factorial(-j1 + j2 + j3)
        / _factorial(j1 + j2 + j3 + 1)
    )
    pref *= math.sqrt(
        _factorial(j1 + m1) * _factorial(j1 - m1)
        * _factorial(j2 + m2) * _factorial(j2 - m2)
        * _factorial(j3 + m3) * _factorial(j3 - m3)
    )
    total = 0.0
    # k terms are finite because every denominator factorial must be valid.
    for k in range(0, 100):
        args = (
            Fraction(k), j1 + j2 - j3 - k, j1 - m1 - k,
            j2 + m2 - k, j3 - j2 + m1 + k,
            j3 - j1 - m2 + k,
        )
        if any(x.denominator != 1 or x < 0 for x in args):
            continue
        den = 1.0
        for x in args:
            den *= math.factorial(x.numerator)
        total += ((-1) ** k) / den
    return pref * total


def axial_cg(ii, k, lam, if_, q=0):
    return cg(ii, k, lam, q, if_, k)


def phase_exponent(if_):
    exponent = Fraction(if_) + Fraction(1, 2)
    if exponent.denominator != 1:
        raise ValueError("If must be half-integral for an odd-A band")
    return exponent.numerator


def decoupling_factor(k, if_, p_oct):
    if k != Fraction(1, 2):
        return 1
    return 1 + ((-1) ** phase_exponent(if_)) * int(p_oct)


def transitions(k, i_min, i_max, q30, p_oct, nucleus, parity_label):
    rows = []
    m3 = math.sqrt(7.0 / (16.0 * math.pi)) * q30
    i = Fraction(str(i_min))
    while i <= Fraction(str(i_max)):
        for delta in (-3, -2, -1, 0, 1, 2, 3):
            f = i + delta
            if f < k or f < 0:
                continue
            # Triangle condition for coupling Ii with lambda=3 to If.
            if abs(i - 3) > f or f > i + 3:
                continue
            c = axial_cg(i, k, 3, f)
            if abs(c) < 1e-15:
                continue
            factor = decoupling_factor(k, f, p_oct)
            reduced = math.sqrt(float(2 * i + 1)) * c * m3 * float(factor)
            b_e3 = reduced * reduced / float(2 * i + 1)
            rows.append({
                "nucleus": nucleus,
                "K": spin_text(k),
                "parity_band": parity_label,
                "p_oct": int(p_oct),
                "Ii": spin_text(i),
                "If": spin_text(f),
                "delta_I": int(delta),
                "CG": c,
                "CG2": c * c,
                "decoupling_factor": float(factor),
                "m3_e_fm3": m3,
                "reduced_matrix_element_e_fm3": reduced,
                "B_E3_e2fm6": b_e3,
                "formula": "B=CG^2*m3^2*F^2",
            })
        i += 1
    return rows


def write_csv(path: Path, rows: Iterable[dict]):
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    # Q30 is a clearly labelled illustrative intrinsic moment.  It is not an
    # experimental value for any one odd-A actinide in this work package.
    q30 = 1000.0
    nuclei = [
        ("223Ra", "1/2", 0.5, 9.5),
        ("225Ra", "1/2", 0.5, 11.5),
        ("225Ac", "3/2", 1.5, 11.5),
        ("227Ac", "3/2", 1.5, 13.5),
    ]
    network = []
    for nucleus, k_text, k_float, i_max in nuclei:
        k = half(k_text)
        # p_oct is an intrinsic phase label.  Both values are calculated so
        # that the interference and its convention dependence are visible.
        for p_oct in (-1, 1):
            network.extend(transitions(
                k, k_float, i_max, q30, p_oct, nucleus,
                f"K={k_text}, opposite-parity partner",
            ))

    cg_rows = []
    for k_text in ("1/2", "3/2"):
        k = half(k_text)
        for ii2 in range(int(2 * k), 24, 2):
            ii = Fraction(ii2, 2)
            for delta in (-3, -2, -1, 0, 1, 2, 3):
                f = ii + delta
                if f < k or abs(ii - 3) > f or f > ii + 3:
                    continue
                c = axial_cg(ii, k, 3, f)
                cg_rows.append({
                    "K": k_text,
                    "Ii": spin_text(ii),
                    "If": spin_text(f),
                    "delta_I": delta,
                    "CG": c,
                    "CG2": c * c,
                })

    curve = []
    for if2 in range(1, 40, 2):
        f = Fraction(if2, 2)
        sign = (-1) ** phase_exponent(f)
        for p_oct in (-1, 1):
            factor = decoupling_factor(Fraction(1, 2), f, p_oct)
            curve.append({
                "K": "1/2",
                "If": spin_text(f),
                "p_oct": p_oct,
                "alternating_sign": sign,
                "interference_factor": int(factor),
                "relative_strength_factor": int(factor * factor),
            })

    delta3 = []
    for k_text in ("1/2", "3/2"):
        k = half(k_text)
        i = k
        while i <= Fraction(23, 2):
            f_plus, f_minus = i + 3, i - 3
            if f_minus >= k:
                c_plus = axial_cg(i, k, 3, f_plus)
                c_minus = axial_cg(i, k, 3, f_minus)
                if abs(c_plus) > 1e-15 and abs(c_minus) > 1e-15:
                    delta3.append({
                        "K": k_text,
                        "Ii": spin_text(i),
                        "If_plus3": spin_text(f_plus),
                        "If_minus3": spin_text(f_minus),
                        "CG2_plus3": c_plus * c_plus,
                        "CG2_minus3": c_minus * c_minus,
                        "CG2_plus_over_minus": (c_plus * c_plus) / (c_minus * c_minus),
                        "Khalf_factor_cancels": k != Fraction(1, 2),
                        "interpretation": "same K=1/2 interference factor for +/-3 from a fixed Ii; ratio is CG geometry",
                    })
            i += 1

    metadata = {
        "model": "strong-coupling odd-A particle-rotor E3 angular geometry",
        "date": "2026-10-29",
        "q30_e_fm3": q30,
        "intrinsic_moment_definition": "m3=sqrt(7/(16*pi))*e*Q30",
        "reduced_matrix_element": "sqrt(2*Ii+1)*CG(Ii K,3 0|If K)*m3*F",
        "b_definition": "B(E3;Ii->If)=|reduced|^2/(2*Ii+1)",
        "decoupling_factor": "F=1+(-1)^(If+1/2)*p_oct for K=1/2; F=1 for K>1/2",
        "p_oct_note": "Intrinsic phase label +/-1; not an independently measured octupole moment sign",
        "q30_status": "illustrative input, not a target-nucleus measurement",
        "evidence_boundary": "No odd-A actinide direct E3 absolute strength is claimed here; ENSDF Ra/Ac pages provide parity and E1 benchmarks only.",
        "nuclei": [n[0] for n in nuclei],
        "network_rows": len(network),
        "cg_rows": len(cg_rows),
        "delta3_rows": len(delta3),
    }
    write_csv(args.outdir / "direct_e3_network.csv", network)
    write_csv(args.outdir / "cg_geometry_matrix.csv", cg_rows)
    write_csv(args.outdir / "khalf_interference_curve.csv", curve)
    write_csv(args.outdir / "delta3_direction_comparison.csv", delta3)
    (args.outdir / "direct_e3_results.json").write_text(
        json.dumps({"metadata": metadata, "network": network, "cg_geometry": cg_rows, "khalf_curve": curve, "delta3_comparison": delta3}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
