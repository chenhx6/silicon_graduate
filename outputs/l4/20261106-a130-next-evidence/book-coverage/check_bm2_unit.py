"""Generic algebra checks for the fully read BM-II PDF 66–71 unit.

No isotope inputs, fitted parameters, legacy analyzer, or physical prediction.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
import json
import math
from pathlib import Path
import time

OUT = Path(__file__).resolve().parent


def cg2(i, k, f):
    """Exact Racah factorial sum, squared; no floating point or external package."""
    j1, j2, J, m1, m2, M = map(F, (i, 2, f, k, 0, k))
    if J < abs(j1-j2) or J > j1+j2 or abs(M) > J:
        return F(0)
    def fac(v):
        assert v.denominator == 1 and v >= 0
        return math.factorial(v.numerator)
    pref = F(2*J+1)*fac(J+j1-j2)*fac(J-j1+j2)*fac(j1+j2-J)/fac(j1+j2+J+1)
    for v in (J+M, J-M, j1-m1, j1+m1, j2-m2, j2+m2):
        pref *= fac(v)
    total = F(0)
    for z in range(int(j1+j2+J)+1):
        args = tuple(map(F, (z, j1+j2-J-z, j1-m1-z, j2+m2-z,
                            J-j2+m1+z, J-j1-m2+z)))
        if any(v < 0 for v in args):
            continue
        total += F((-1)**z, math.prod(fac(v) for v in args))
    return pref*total*total


def qratio(i, k):
    i, k = F(i), F(k)
    return (3*k*k-i*(i+1))/((i+1)*(2*i+3))


def branch_ratio(i, k):
    i, k = F(i), F(k)
    return 2*k*k*(2*i-1)/((i+1)*((i-1)**2-k*k))


def main():
    start = time.perf_counter()
    # Leading quadratic coefficients of the source's rational expression.
    fixed_k = F(-1, 2)
    bandhead_path = F(2, 2)
    assert fixed_k == -F(1, 2)
    assert bandhead_path == 1
    assert qratio(2, 0) == -F(2, 7)
    assert qratio(F(1, 2), F(1, 2)) == 0
    assert abs(qratio(10**6, 2)-fixed_k) < F(1, 10**5)
    assert abs(qratio(10**6, 10**6)-bandhead_path) < F(1, 10**5)
    b02, b20, b42 = cg2(0, 0, 2), cg2(2, 0, 0), cg2(4, 0, 2)
    assert b02/b20 == 5
    assert b42/b20 == F(10, 7)
    # Independent exact CG values check the reconstructed finite-I ratio.
    formula = "2*K^2*(2*I-1)/((I+1)*((I-1)^2-K^2))"
    cases = []
    for spin, kval in [(4, 2), (6, 2), (20, 2),
                       (F(9, 2), F(3, 2))]:
        direct = cg2(spin, kval, spin-1)/cg2(spin, kval, spin-2)
        reconstructed = branch_ratio(spin, kval)
        assert direct == reconstructed
        cases.append({"I": str(spin), "K": str(kval),
                      "exact_ratio": str(direct), "decimal_ratio": float(direct)})
    assert abs(10**12*branch_ratio(10**6, 2)-16) < F(1, 10**4)
    assert cg2(4, 0, 3) == 0
    result = {
        "review_date": "2026-11-06",
        "observed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Conditional axial fixed-K rotational algebra; no experimental prediction.",
        "source": "BM-II physical PDF 66–71 / printed 44–49, Eqs4-66–4-73 and Fig4-5 caption.",
        "arithmetic": "Python standard-library Fraction and exact integer factorial CG sum",
        "environment_attempt": "Initial SymPy attempt failed with ModuleNotFoundError; replaced by exact standard-library arithmetic. No package installed.",
        "Qstatic_over_Q0_fixed_K_high_I": str(fixed_k),
        "Qstatic_over_Q0_K_equals_I_high_I": str(bandhead_path),
        "Qstatic_over_Q0_I2_K0": "-2/7",
        "Qstatic_Ihalf_Khalf": 0,
        "Bup_over_Bdown_zero_two": str(b02/b20),
        "B42_over_B20_K0": str(b42/b20),
        "finite_spin_branch_ratio_formula": str(formula),
        "branch_ratio_cases": cases,
        "I_squared_times_branch_ratio_fixed_K_limit": "4*K^2",
        "K0_DeltaI1_selection_zero": True,
        "scratch_correction": "An initial scratch ratio used (I-1) in the final denominator; cancellation of the exact CG formulas gives (I+1), as all four direct CG checks confirm. This was a learner correction, not a source erratum.",
        "interpretation_boundary": "A vanishing spectroscopic Q for I=0 or 1/2 does not imply a vanishing intrinsic quadrupole moment; fixed-K and K=I are distinct limiting sequences.",
        "runtime_seconds": time.perf_counter()-start,
        "passed": True,
    }
    with (OUT/"bm2-unit-algebra.json").open("x", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
