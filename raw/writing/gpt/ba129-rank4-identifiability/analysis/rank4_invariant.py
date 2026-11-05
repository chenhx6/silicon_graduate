#!/usr/bin/env python3
"""Conditional same-parent rank-4 identifiability gate for 129Ba.

This program is deliberately self-contained.  It computes the angular
momentum coefficient ratio for the 13/2 -> 11/2 and 13/2 -> 9/2 pure-E2
channels, verifies the exact -8/3 relation, and applies it to public
summary coefficients.  It does not reconstruct the historical detector
response or perform a paper-level experimental fit.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path


def phase(n: int) -> int:
    return -1 if n % 2 else 1


def triangle(a: int, b: int, c: int) -> Fraction:
    if (a + b + c) % 2 or not abs(a - b) <= c <= a + b:
        return Fraction(0)
    return Fraction(
        factorial((a + b - c) // 2)
        * factorial((a - b + c) // 2)
        * factorial((-a + b + c) // 2),
        factorial((a + b + c) // 2 + 1),
    )


@lru_cache(maxsize=None)
def cg2(a: int, b: int, c: int, ma: int, mb: int, mc: int) -> float:
    """Clebsch--Gordan coefficient with all angular momenta doubled."""
    if (
        ma + mb != mc
        or abs(ma) > a
        or abs(mb) > b
        or abs(mc) > c
        or not abs(a - b) <= c <= a + b
        or any(x % 2 for x in (a + ma, b + mb, c + mc, a + b + c))
    ):
        return 0.0

    aa = (a + b - c) // 2
    bb = (a - ma) // 2
    cc = (b + mb) // 2
    dd = (c - b + ma) // 2
    ee = (c - a - mb) // 2
    pref = Fraction(
        (c + 1)
        * factorial(aa)
        * factorial((a - b + c) // 2)
        * factorial((-a + b + c) // 2),
        factorial((a + b + c) // 2 + 1),
    )
    for n in (
        (a + ma) // 2,
        (a - ma) // 2,
        (b + mb) // 2,
        (b - mb) // 2,
        (c + mc) // 2,
        (c - mc) // 2,
    ):
        pref *= factorial(n)

    total = Fraction(0)
    for z in range(max(0, -dd, -ee), min(aa, bb, cc) + 1):
        total += Fraction(
            phase(z),
            factorial(z)
            * factorial(aa - z)
            * factorial(bb - z)
            * factorial(cc - z)
            * factorial(dd + z)
            * factorial(ee + z),
        )
    return math.sqrt(float(pref)) * float(total)


@lru_cache(maxsize=None)
def sixj2(a: int, b: int, c: int, d: int, e: int, f: int) -> float:
    """Wigner 6-j symbol with doubled angular momenta."""
    pref = (
        triangle(a, b, c)
        * triangle(a, e, f)
        * triangle(d, b, f)
        * triangle(d, e, c)
    )
    if not pref:
        return 0.0
    lower = [
        (a + b + c) // 2,
        (a + e + f) // 2,
        (d + b + f) // 2,
        (d + e + c) // 2,
    ]
    upper = [
        (a + b + d + e) // 2,
        (a + c + d + f) // 2,
        (b + c + e + f) // 2,
    ]
    total = Fraction(0)
    for z in range(max(lower), min(upper) + 1):
        denominator = math.prod(factorial(z - n) for n in lower) * math.prod(
            factorial(n - z) for n in upper
        )
        total += Fraction(phase(z) * factorial(z + 1), denominator)
    return math.sqrt(float(pref)) * float(total)


def native_f(twice_ji: int, twice_jf: int, rank: int, ell: int, ellp: int) -> float:
    """Yamazaki/Rose-Brink coefficient used for the rank-k channel."""
    cg = cg2(2 * ell, 2 * ellp, 2 * rank, 2, -2, 0)
    if cg == 0:
        return 0.0
    racah = phase(twice_ji + ell + ellp) * sixj2(
        twice_ji, twice_ji, 2 * rank, 2 * ellp, 2 * ell, twice_jf
    )
    return phase((twice_jf - twice_ji) // 2 - 1) * math.sqrt(
        (2 * ell + 1) * (2 * ellp + 1) * (twice_ji + 1)
    ) * cg * racah


def exact_sixj_square(
    a: int, b: int, c: int, d: int, e: int, f: int
) -> tuple[Fraction, int]:
    """Exact square and sign of the doubled-argument 6-j sum."""
    pref = triangle(a, b, c) * triangle(a, e, f) * triangle(d, b, f) * triangle(
        d, e, c
    )
    lower = [
        (a + b + c) // 2,
        (a + e + f) // 2,
        (d + b + f) // 2,
        (d + e + c) // 2,
    ]
    upper = [
        (a + b + d + e) // 2,
        (a + c + d + f) // 2,
        (b + c + e + f) // 2,
    ]
    total = Fraction(0)
    for z in range(max(lower), min(upper) + 1):
        denominator = math.prod(factorial(z - n) for n in lower) * math.prod(
            factorial(n - z) for n in upper
        )
        total += Fraction(phase(z) * factorial(z + 1), denominator)
    return pref * total * total, (-1 if total < 0 else 1)


def load_rows(
    path: Path, *, require_reference_nonzero: bool = True
) -> dict[str, dict[str, float | str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 2 or {row["label"] for row in rows} != {"target_365", "reference_462"}:
        raise ValueError("input must contain exactly target_365 and reference_462")
    out = {}
    for row in rows:
        out[row["label"]] = {
            **row,
            "Ji_twice": int(row["Ji_twice"]),
            "Jf_twice": int(row["Jf_twice"]),
            "energy_keV": float(row["energy_keV"]),
            "A2": float(row["A2"]),
            "A2_sigma": float(row["A2_sigma"]),
            "A4": float(row["A4"]),
            "A4_sigma": float(row["A4_sigma"]),
        }
        for field in ("energy_keV", "A2", "A2_sigma", "A4", "A4_sigma"):
            if not math.isfinite(out[row["label"]][field]):
                raise ValueError(f"{row['label']} {field} must be finite")
        if min(out[row["label"]][field] for field in ("energy_keV", "A2_sigma", "A4_sigma")) <= 0:
            raise ValueError("energy and quoted marginal errors must be positive")
    target, reference = out["target_365"], out["reference_462"]
    if not target.get("parent_id") or target["parent_id"] != reference.get("parent_id"):
        raise ValueError("both rows require the same explicit parent_id")
    if target["Ji_twice"] != reference["Ji_twice"]:
        raise ValueError("the parent spins must agree")
    if (target["Ji_twice"], target["Jf_twice"], reference["Jf_twice"]) != (13, 11, 9):
        raise ValueError("this case study supports only the (13,11,9) doubled-spin sequence")
    if (target["multipolarity"], reference["multipolarity"]) != ("M1+E2", "E2"):
        raise ValueError("the stated target/reference multipole hypotheses must be retained")
    if require_reference_nonzero and reference["A4"] == 0:
        raise ValueError("zero reference A4 makes the central ratio undefined; use coefficient-space profiling")
    return out


def interval_image(reference_lo: float, reference_hi: float, scale: float) -> list[float]:
    """Image of scale*f*reference for f in [0,1]."""
    candidates = [0.0, scale * reference_lo, scale * reference_hi]
    return [min(candidates), max(candidates)]


def diagonal_profile(
    target: float,
    target_sigma: float,
    reference: float,
    reference_sigma: float,
    scale: float,
    points: int = 10001,
) -> dict[str, float]:
    """Literal Gaussian diagnostic for s4=1; never reported as a p-value."""
    best = None
    for i in range(points):
        f_e2 = i / (points - 1)
        c = scale * f_e2
        denom = 1 / reference_sigma**2 + c * c / target_sigma**2
        reference_true = (
            reference / reference_sigma**2 + c * target / target_sigma**2
        ) / denom
        target_true = c * reference_true
        score = (
            (reference - reference_true) ** 2 / reference_sigma**2
            + (target - target_true) ** 2 / target_sigma**2
        )
        candidate = (score, f_e2, reference_true, target_true)
        if best is None or candidate[0] < best[0]:
            best = candidate
    assert best is not None
    return {
        "minimum_diagnostic_score": best[0],
        "f_E2_at_minimum": best[1],
        "reference_true_at_minimum": best[2],
        "target_true_at_minimum": best[3],
        "interpretation": "literal independent-marginal Gaussian diagnostic only; not a formal test",
    }


def analyze(input_path: Path) -> dict:
    rows = load_rows(input_path)
    target = rows["target_365"]
    reference = rows["reference_462"]
    ji = int(target["Ji_twice"])
    target_jf = int(target["Jf_twice"])
    reference_jf = int(reference["Jf_twice"])

    f4_target = native_f(ji, target_jf, 4, 2, 2)
    f4_reference = native_f(ji, reference_jf, 4, 2, 2)
    ratio = f4_target / f4_reference
    sq_target, sign_target = exact_sixj_square(ji, ji, 8, 4, 4, target_jf)
    sq_reference, sign_reference = exact_sixj_square(
        ji, ji, 8, 4, 4, reference_jf
    )
    square_ratio = sq_target / sq_reference
    assert square_ratio == Fraction(64, 9)
    numerator = math.isqrt(square_ratio.numerator)
    denominator = math.isqrt(square_ratio.denominator)
    if numerator**2 != square_ratio.numerator or denominator**2 != square_ratio.denominator:
        raise ValueError("the squared angular-momentum ratio does not have a rational square root")
    exact_ratio = Fraction(
        phase((target_jf - reference_jf) // 2) * sign_target * sign_reference * numerator,
        denominator,
    )
    assert exact_ratio == Fraction(-8, 3)
    assert math.isclose(ratio, float(exact_ratio), rel_tol=0, abs_tol=2e-13)

    target_a4 = float(target["A4"])
    reference_a4 = float(reference["A4"])
    target_s4 = float(target["A4_sigma"])
    reference_s4 = float(reference["A4_sigma"])
    required_fs4 = -(3 / 8) * target_a4 / reference_a4
    synthetic_f = 0.65
    synthetic_s4 = 1.25
    synthetic_reference = 0.08
    synthetic_target = float(exact_ratio) * synthetic_f * synthetic_s4 * synthetic_reference
    synthetic_recovered_product = -(3 / 8) * synthetic_target / synthetic_reference
    assert math.isclose(
        synthetic_recovered_product,
        synthetic_f * synthetic_s4,
        rel_tol=0,
        abs_tol=2e-14,
    )

    interval_controls = []
    for multiplier in (1, 2):
        ref_lo = reference_a4 - multiplier * reference_s4
        ref_hi = reference_a4 + multiplier * reference_s4
        target_lo = target_a4 - multiplier * target_s4
        target_hi = target_a4 + multiplier * target_s4
        target_image_s4_one = interval_image(ref_lo, ref_hi, float(exact_ratio))
        interval_controls.append(
            {
                "quoted_marginal_multiplier": multiplier,
                "reference_A4_interval": [ref_lo, ref_hi],
                "target_A4_interval": [target_lo, target_hi],
                "both_intervals_strictly_positive": ref_lo > 0 and target_lo > 0,
                "predicted_target_image_for_s4_1_and_f_E2_0_1": target_image_s4_one,
                "overlap_with_target_interval_for_s4_1": (
                    max(target_image_s4_one[0], target_lo)
                    <= min(target_image_s4_one[1], target_hi)
                ),
                "not_joint_confidence_region": True,
            }
        )

    return {
        "identity": {
            "nucleus": "129Ba",
            "target": "643.6-keV 13/2- -> 11/2- 364.7-keV line",
            "reference": "643.6-keV 13/2- -> 9/2- 461.6-keV line",
            "source_locator": "ENSDF 129056001/013; 1977 Gi02 A2/A4 records",
        },
        "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "algebra": {
            "F4_target_pure_E2": f4_target,
            "F4_reference_pure_E2": f4_reference,
            "F4_ratio": ratio,
            "exact_F4_ratio": str(exact_ratio),
            "exact_6j_squared_ratio": str(square_ratio),
            "6j_signs": {"target": sign_target, "reference": sign_reference},
            "relation": "A4_target = -(8/3) * f_E2 * s4 * A4_reference",
            "physical_domain": "0 <= f_E2 <= 1; s4 = Q4_target/Q4_reference",
        },
        "public_summary_values": {
            "target_A2": target["A2"],
            "target_A2_sigma": target["A2_sigma"],
            "target_A4": target_a4,
            "target_A4_sigma": target_s4,
            "reference_A2": reference["A2"],
            "reference_A2_sigma": reference["A2_sigma"],
            "reference_A4": reference_a4,
            "reference_A4_sigma": reference_s4,
        },
        "central_diagnostic": {
            "target_A4_times_reference_A4": target_a4 * reference_a4,
            "target_over_reference_A4": target_a4 / reference_a4,
            "required_f_E2_times_s4": required_fs4,
            "central_physical_domain_satisfied_for_positive_s4": (
                required_fs4 >= 0
            ),
            "interpretation": (
                "The central summary values require a negative f_E2*s4 under "
                "the declared companion-line contract. This is a contract "
                "diagnostic, not an experimental error verdict."
            ),
        },
        "identification": {
            "identified_quantity_under_shared_selected_parent": "f_E2*s4",
            "s4_calibrated": False,
            "f_E2_identified": False,
            "delta_magnitude_identified": False,
            "delta_sign_identified": False,
            "zero_reference_case": "ratio undefined; coefficient-space method required",
            "different_parent_selection": "retain g4=rho4_target/rho4_reference as a distinct factor",
        },
        "synthetic_algebra_control": {
            "f_E2_true": synthetic_f,
            "s4_true": synthetic_s4,
            "reference_A4": synthetic_reference,
            "target_A4_generated": synthetic_target,
            "f_E2_times_s4_recovered": synthetic_recovered_product,
            "passed": True,
            "not_experimental_data": True,
        },
        "interval_controls": interval_controls,
        "diagonal_s4_one_control": diagonal_profile(
            target_a4,
            target_s4,
            reference_a4,
            reference_s4,
            float(exact_ratio),
        ),
        "boundary": [
            "common parent_id and spin checked; common postselection remains an assumption",
            "target is restricted to M1+E2 and reference is treated as pure E2",
            "the coefficient layer and finite-acceptance corrections must be commensurate",
            "s4 must be positive for the sign gate; this is not established by the public summary alone",
            "quoted marginal errors are not a joint covariance or a formal confidence region",
            "no event counts, detector response, feeding model, lifetime, absolute B(E2), or mode classification is inferred",
        ],
        "scientific_certification": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = analyze(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "F4_ratio": result["algebra"]["F4_ratio"],
                "exact_F4_ratio": result["algebra"]["exact_F4_ratio"],
                "required_f_E2_times_s4": result["central_diagnostic"][
                    "required_f_E2_times_s4"
                ],
                "one_sigma_sign_gate": result["interval_controls"][0][
                    "both_intervals_strictly_positive"
                ],
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
