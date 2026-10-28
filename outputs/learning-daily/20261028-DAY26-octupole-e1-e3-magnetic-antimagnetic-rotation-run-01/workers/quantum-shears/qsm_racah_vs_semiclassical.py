#!/usr/bin/env python3
"""Finite-j quantum shears benchmark.

This dependency-free script evaluates the Racah factorial sum for
    { jp  I-1  jn }
    { I   jp    1  }
and compares the exact fixed-(jp, jn) M1 rate with the semiclassical
Macchiavelli shears expression.  It deliberately keeps the j-length
prescription in the user supplied formula separate from the
sqrt(j(j+1)) prescription quoted as Clark--Macchiavelli Eq. (5).

The code is a model benchmark, not an extraction of an experimental rate.
"""

from __future__ import annotations

import csv
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "qsm_racah_vs_semiclassical.csv"
JSON_PATH = ROOT / "qsm_racah_vs_semiclassical.json"


def _integer(x: Fraction) -> int:
    if x.denominator != 1:
        raise ValueError(f"Racah factorial argument is not integral: {x}")
    return x.numerator


def _fact(x: Fraction) -> int:
    n = _integer(x)
    if n < 0:
        raise ValueError(f"negative factorial argument: {x}")
    return math.factorial(n)


def _delta_squared(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """Triangle coefficient Delta(a,b,c)^2."""
    return Fraction(
        _fact(a + b - c) * _fact(a - b + c) * _fact(-a + b + c),
        _fact(a + b + c + 1),
    )


def sixj_squared(a: Fraction, b: Fraction, c: Fraction,
                 d: Fraction, e: Fraction, f: Fraction) -> Fraction:
    """Return the exact square of a Wigner 6j symbol via Racah's sum.

    The usual Racah convention is used:
      {a b c; d e f} = product(Delta) * sum_z (-1)^z (z+1)! / (...) .
    Since only the square is needed for B(M1), the positive triangle
    prefactor is multiplied by the exact rational square of the sum.
    """
    tri = (
        _delta_squared(a, b, c)
        * _delta_squared(a, e, f)
        * _delta_squared(d, b, f)
        * _delta_squared(d, e, c)
    )
    z_min = max(a + b + c, a + e + f, d + b + f, d + e + c)
    z_max = min(a + b + d + e, a + c + d + f, b + c + e + f)
    z0, z1 = _integer(z_min), _integer(z_max)
    racah_sum = Fraction(0, 1)
    for z in range(z0, z1 + 1):
        denominator = (
            _fact(Fraction(z) - a - b - c)
            * _fact(Fraction(z) - a - e - f)
            * _fact(Fraction(z) - d - b - f)
            * _fact(Fraction(z) - d - e - c)
            * _fact(a + b + d + e - z)
            * _fact(a + c + d + f - z)
            * _fact(b + c + e + f - z)
        )
        term = Fraction(_fact(Fraction(z + 1)), denominator)
        racah_sum += term if z % 2 == 0 else -term
    return tri * racah_sum * racah_sum


def sixj_value(a: Fraction, b: Fraction, c: Fraction,
               d: Fraction, e: Fraction, f: Fraction) -> float:
    """Numerical 6j value, retaining the Racah-sum sign."""
    tri = math.sqrt(float(
        _delta_squared(a, b, c)
        * _delta_squared(a, e, f)
        * _delta_squared(d, b, f)
        * _delta_squared(d, e, c)
    ))
    z_min = max(a + b + c, a + e + f, d + b + f, d + e + c)
    z_max = min(a + b + d + e, a + c + d + f, b + c + e + f)
    racah_sum = 0.0
    for z in range(_integer(z_min), _integer(z_max) + 1):
        denominator = (
            math.factorial(_integer(Fraction(z) - a - b - c))
            * math.factorial(_integer(Fraction(z) - a - e - f))
            * math.factorial(_integer(Fraction(z) - d - b - f))
            * math.factorial(_integer(Fraction(z) - d - e - c))
            * math.factorial(_integer(a + b + d + e - z))
            * math.factorial(_integer(a + c + d + f - z))
            * math.factorial(_integer(b + c + e + f - z))
        )
        term = math.factorial(z + 1) / denominator
        racah_sum += term if z % 2 == 0 else -term
    return tri * racah_sum


def allowed_total_spins(jp: Fraction, jn: Fraction) -> list[Fraction]:
    lo, hi = abs(jp - jn), jp + jn
    n = _integer(hi - lo)
    return [lo + k for k in range(n + 1)]


def reduced_square(jp: Fraction, jn: Fraction, I: Fraction) -> tuple[Fraction, Fraction]:
    """Return 6j form and closed Racah form of |<I-1||jp||I>|^2."""
    sj2 = sixj_squared(jp, I - 1, jn, I, jp, Fraction(1))
    sixj_form = (2 * I - 1) * (2 * I + 1) * jp * (jp + 1) * (2 * jp + 1) * sj2
    J, D = jp + jn, jp - jn
    closed = ((J + 1) ** 2 - I**2) * (I**2 - D**2) / (4 * I)
    return sixj_form, closed


def bm1_quantum(jp: Fraction, jn: Fraction, I: Fraction, dg: float) -> float:
    """B(M1; I -> I-1) in mu_N^2 with M1=sqrt(3/4pi)*(gp jp+gn jn)."""
    sixj_form, _ = reduced_square(jp, jn, I)
    return (3.0 / (4.0 * math.pi)) * dg**2 * float(sixj_form) / float(2 * I + 1)


def bm1_classical_j(jp: Fraction, jn: Fraction, I: Fraction, dg: float) -> tuple[float, float]:
    """User supplied formula, using blade lengths jp and jn."""
    cosine = (float(I**2 - jp**2 - jn**2) / float(2 * jp * jn))
    if abs(cosine) > 1.0:
        return 0.0, float("nan")
    sin2 = max(0.0, 1.0 - cosine * cosine)
    value = (3.0 / (8.0 * math.pi)) * dg**2 * (float(jp * jn / I) ** 2) * sin2
    return value, math.degrees(math.acos(cosine))


def bm1_classical_sqrtjj(jp: Fraction, jn: Fraction, I: Fraction, dg: float) -> float:
    """Clark--Macchiavelli Eq. (5) angle prescription, for audit only."""
    jp2, jn2 = float(jp * (jp + 1)), float(jn * (jn + 1))
    cosine = (float(I * (I + 1)) - jp2 - jn2) / (2.0 * math.sqrt(jp2 * jn2))
    if abs(cosine) > 1.0:
        return 0.0
    return (3.0 / (8.0 * math.pi)) * dg**2 * (
        math.sqrt(jp2 * jn2) / math.sqrt(float(I * (I + 1)))
    ) ** 2 * (1.0 - cosine * cosine)


def row(label: str, jp: Fraction, jn: Fraction, I: Fraction, dg: float) -> dict:
    sixj_form, closed = reduced_square(jp, jn, I)
    q = bm1_quantum(jp, jn, I, dg)
    c, theta = bm1_classical_j(jp, jn, I, dg)
    c_sqrt = bm1_classical_sqrtjj(jp, jn, I, dg)
    ratio = q / c if c > 0.0 else None
    return {
        "scenario": label,
        "jp": float(jp),
        "jn": float(jn),
        "I": float(I),
        "spin_2I": int(2 * I),
        "sixj": sixj_value(jp, I - 1, jn, I, jp, Fraction(1)),
        "reduced_sq_6j": float(sixj_form),
        "reduced_sq_closed": float(closed),
        "reduced_identity_abs_error": abs(float(sixj_form - closed)),
        "BM1_quantum_muN2": q,
        "BM1_classical_j_muN2": c,
        "theta_classical_j_deg": theta,
        "quantum_over_classical_j": ratio,
        "relative_difference_percent": None if ratio is None else 100.0 * (ratio - 1.0),
        "BM1_classical_sqrtjj_muN2": c_sqrt,
    }


def main() -> None:
    dg = 1.42
    rows: list[dict] = []

    # Symmetric j_p=j_n=11/2 track.  The allowed coupled spins are integer;
    # a half-integer I=11/2..23/2 window is forbidden by angular-momentum
    # addition and is recorded explicitly in the JSON boundary.
    jp_sym = jn_sym = Fraction(11, 2)
    for I in [Fraction(k) for k in range(5, 12)]:
        rows.append(row("symmetric_j11over2_allowed_integer_I", jp_sym, jn_sym, I, dg))

    # Half-integer requested window, using a particle-hole-like j_n=10 input.
    jp_half, jn_half = Fraction(11, 2), Fraction(10)
    for k in range(11, 24, 2):
        rows.append(row("half_integer_window_jp11over2_jn10", jp_half, jn_half, Fraction(k, 2), dg))
    rows.append(row("half_integer_window_endpoint_control", jp_half, jn_half, Fraction(31, 2), dg))

    # Interior asymptotic check at I=0.8 I_max for equal integer j.
    asymptotic = []
    for j in [5, 10, 20, 40, 80]:
        jj = Fraction(j)
        I = Fraction(4 * j, 5)
        r = row("equal_j_interior_asymptotic", jj, jj, I, dg)
        asymptotic.append({"j": j, "I": float(I), "ratio": r["quantum_over_classical_j"]})

    identity_max = max(r["reduced_identity_abs_error"] for r in rows)
    endpoint = rows[-1]
    payload = {
        "schema": "qsm-racah-vs-semiclassical/v1",
        "description": "Exact finite-j Wigner-6j/Racah M1 benchmark against the user-supplied Macchiavelli shears formula.",
        "source_conventions": {
            "operator": "M(M1,mu)=sqrt(3/(4*pi))*(g_p*j_p+g_n*j_n)",
            "reduced_matrix_element": "(-1)^(jp+jn+I)*sqrt((2I+1)(2I-1))*Delta_g*sqrt(jp(jp+1)(2jp+1))*{jp,I-1,jn;I,jp,1}",
            "B_definition": "B(M1;I->I-1)=|<I-1||M1||I>|^2/(2I+1)",
            "classical_formula": "3/(8*pi)*Delta_g^2*(jp*jn/I)^2*sin(theta)^2",
            "classical_angle": "cos(theta)=(I^2-jp^2-jn^2)/(2*jp*jn)",
            "closed_racah_identity": "|<(jp jn) I-1 || jp || (jp jn) I>|^2 = [((jp+jn+1)^2-I^2)(I^2-(jp-jn)^2)]/(4I)",
            "interior_ratio_identity": "B_quantum/B_classical = [2I/(2I+1)]*{[(jp+jn+1)^2-I^2]/[(jp+jn)^2-I^2]}",
        },
        "literature_locators": [
            "Clark and Macchiavelli, Annu. Rev. Nucl. Part. Sci. 50, 1-36 (2000), PDF p.15, Sec.4.4, Eqs.(5)-(7): finite-j angle prescription and semiclassical B(M1) geometry.",
            "Frauendorf, Rev. Mod. Phys. 73, 463-514 (2001), PDF pp.487-488, Sec.IV.A: magnetic rotation as high-j current-loop/shears motion and transverse magnetic moment.",
            "Frauendorf, Rev. Mod. Phys. 73, 463-514 (2001), PDF pp.499-502, Sec.VIII: laboratory-frame quantization/projection and beyond-mean-field limits of TAC.",
        ],
        "parameter_delta_g_muN": dg,
        "angular_momentum_boundary": "Two half-integer blades (11/2,11/2) couple only to integer I. Therefore I=11/2..23/2 cannot be evaluated for jp=jn=11/2; the requested half-integer window is supplied with jn=10 as a particle-hole-like control.",
        "max_reduced_identity_abs_error": identity_max,
        "asymptotic_interior_equal_j": asymptotic,
        "rows": rows,
        "endpoint_control": {
            "description": "At I=jp+jn the classical j-length formula is zero, while the finite-j Racah rate remains nonzero when Delta_g != 0.",
            "row": endpoint,
        },
        "evidence_boundary": [
            "All numerical rows are fixed-j model calculations; none is an experimental B(M1) extraction.",
            "The 6j algebra is exact within the two-body coupled basis. Effective-g quenching, core rotation, configuration mixing, pairing and band crossings are outside this benchmark.",
            "The term operator renormalization is used here only as finite-j recoupling/renormalization of the semiclassical strength; no field-theoretic renormalization is claimed.",
        ],
    }

    fieldnames = list(rows[0].keys())
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {JSON_PATH}")
    print(f"max reduced-matrix identity error = {identity_max:.3e}")


if __name__ == "__main__":
    main()
