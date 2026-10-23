#!/usr/bin/env python3
"""Exact quantitative derivation of Singh 2016 Eq. (2)-(3) K-mixing CG coefficients.

Audits:
1. Exact reduced Wigner d-matrix elements a_K = d^{11/2}_{11/2, K}(pi/2) for j=11/2;
2. Sum of probabilities sum_K a_K^2 == 1.0 (exact binomial distribution / 2^11);
3. Exact Clebsch-Gordan coefficients <I 2 K 0 | I-2 K> for K=1/2 vs mixed K;
4. Verifies Singh's literal claim on p. 6 that the difference between mixed CG
   and pure K=1/2 CG is 'at most only a few percent' (5.2% at 15/2-, dropping to 0.9% at 35/2-);
5. Quantifies the impact on extracted Qt and confirms it is dominated by experimental errors.

Requires --output PATH. Uses only Python standard library.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys

# Add script directory for rotor_cg_squared / cg_squared
sys.path.append(str(Path(__file__).resolve().parent))
from day19_evidence_repair_audit import cg_squared, rotor_cg_squared


def wigner_d_max_j_element(j_frac, k_frac):
    """Calculate d^j_{j, K}(pi/2) for state of maximum projection j along perpendicular axis."""
    two_j = int(round(float(2 * j_frac)))
    idx = int(round(float(j_frac + k_frac)))
    c = math.comb(two_j, idx)
    sign = (-1) ** int(round(float(j_frac - k_frac)))
    # d^j_{j, K}(pi/2) = (-1)^(j-K) * sqrt(binom(2j, j+K)) / 2^j
    val = sign * math.sqrt(c) / (2.0 ** float(j_frac))
    prob = c / (2.0 ** two_j)
    return val, prob


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []

    def check(name, ok):
        checks.append({"name": name, "passed": bool(ok)})
        if not ok:
            raise AssertionError(f"Check failed: {name}")

    j = F(11, 2)
    k_values = [F(-11 + 2 * step, 2) for step in range(12)]

    # 1. Verification of reduced rotation matrix elements
    expansion_table = []
    prob_sum = 0.0
    for k in k_values:
        amp, prob = wigner_d_max_j_element(j, k)
        prob_sum += prob
        expansion_table.append({
            "K": str(k),
            "amplitude_a_K": amp,
            "probability_a_K_sq": prob,
        })

    check("j=11/2 has exactly 12 K projections", len(expansion_table) == 12)
    check("Wigner d-matrix probabilities sum to exactly 1.0", math.isclose(prob_sum, 1.0, rel_tol=1e-14))
    # Check reflection symmetry a_K^2 == a_{-K}^2
    check("probabilities are symmetric under K -> -K",
          all(math.isclose(expansion_table[i]["probability_a_K_sq"],
                           expansion_table[11 - i]["probability_a_K_sq"], rel_tol=1e-14)
              for i in range(6)))

    # 2. Compute pure K=1/2 CG vs mixed CG across all yrast spins in 131Ce and 133Pr
    # Spins: 15/2-, 19/2-, 23/2-, 27/2-, 31/2-, 35/2-
    eval_spins = [F(15, 2), F(19, 2), F(23, 2), F(27, 2), F(31, 2), F(35, 2)]
    cg_comparison = []

    for i in eval_spins:
        # Pure K=1/2 CG: <I 2 1/2 0 | I-2 1/2>
        cg_pure_sq = float(rotor_cg_squared(i, F(1, 2)))
        cg_pure = math.sqrt(cg_pure_sq)

        # Mixed CG: sum_K a_K^2 * <I 2 K 0 | I-2 K>
        cg_mixed = 0.0
        details = []
        for row in expansion_table:
            k = F(row["K"])
            if abs(k) <= i - 2:
                cg_k_sq = float(rotor_cg_squared(i, k))
                cg_k = math.sqrt(cg_k_sq)
                prob = row["probability_a_K_sq"]
                cg_mixed += prob * cg_k
                details.append({"K": str(k), "CG_K": cg_k, "weight": prob, "contrib": prob * cg_k})

        diff_pct = (cg_mixed - cg_pure) / cg_pure * 100.0
        qt_scale_factor = cg_pure / cg_mixed # Qt_mixed / Qt_pure = CG_pure / CG_mixed

        cg_comparison.append({
            "I": str(i),
            "I_float": float(i),
            "CG_pure_K_half": round(cg_pure, 5),
            "CG_mixed_Eq2": round(cg_mixed, 5),
            "diff_pct": round(diff_pct, 2),
            "Qt_multiplier_if_mixed": round(qt_scale_factor, 4),
        })

    # Verifications of Singh's claim
    # At I = 15/2-, diff is ~ -5.22%
    c15 = next(c for c in cg_comparison if c["I"] == "15/2")
    check("15/2- mixed CG difference is ~ -5.2%", math.isclose(c15["diff_pct"], -5.22, abs_tol=0.1))

    # At higher spins I >= 23/2-, diff is <= 2.1%
    c27 = next(c for c in cg_comparison if c["I"] == "27/2")
    c31 = next(c for c in cg_comparison if c["I"] == "31/2")
    c35 = next(c for c in cg_comparison if c["I"] == "35/2")
    check("27/2- mixed CG difference is ~ -1.5%", math.isclose(c27["diff_pct"], -1.49, abs_tol=0.1))
    check("31/2- mixed CG difference is ~ -1.1%", math.isclose(c31["diff_pct"], -1.12, abs_tol=0.1))
    check("35/2- mixed CG difference is ~ -0.9%", math.isclose(c35["diff_pct"], -0.87, abs_tol=0.1))

    # All differences across the entire band are strictly < 6%
    check("All K-mixing CG differences across the band are <= 5.3% ('at most only a few percent')",
          all(abs(c["diff_pct"]) <= 5.3 for c in cg_comparison))

    # 3. Compare with experimental uncertainties in 131Ce Table 1
    # 131Ce experimental Qt errors:
    # 15/2-: 2.93(+0.60/-0.30) -> rel error ~ 15%
    # 27/2-: 2.26(+0.37/-0.23) -> rel error ~ 13%
    # 31/2-: 2.66(+0.13/-0.12) -> rel error ~ 4.7%
    # 35/2-: 2.43(+0.22/-0.20) -> rel error ~ 8.6%
    ce131_states = [
        {"spin": "15/2", "Qt_rep": 2.93, "err_rep": 0.45, "rel_err_pct": 15.36},
        {"spin": "27/2", "Qt_rep": 2.26, "err_rep": 0.30, "rel_err_pct": 13.27},
        {"spin": "31/2", "Qt_rep": 2.66, "err_rep": 0.125, "rel_err_pct": 4.70},
        {"spin": "35/2", "Qt_rep": 2.43, "err_rep": 0.21, "rel_err_pct": 8.64},
    ]
    for s in ce131_states:
        c = next(comp for comp in cg_comparison if comp["I"] == s["spin"])
        s["cg_shift_pct"] = abs(c["diff_pct"])
        s["shift_dominated_by_exp_error"] = s["cg_shift_pct"] < s["rel_err_pct"]
        s["Qt_mixed_eb"] = round(s["Qt_rep"] * c["Qt_multiplier_if_mixed"], 3)
        s["delta_Qt_eb"] = round(s["Qt_mixed_eb"] - s["Qt_rep"], 3)

    check("K-mixing correction is smaller than experimental error for all 131Ce states",
          all(s["shift_dominated_by_exp_error"] for s in ce131_states))

    result = {
        "kind": "Singh 2016 Eq2-Eq3 K-mixing Clebsch-Gordan quantitative derivation",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "quasiparticle_angular_momentum": "j = 11/2",
        "wigner_d_matrix_expansion_table": expansion_table,
        "cg_comparison_pure_vs_mixed": cg_comparison,
        "impact_on_131Ce_measured_Qt": ce131_states,
        "scientific_conclusion": (
            "Exact algebraic computation of Singh 2016 Eqs. (2)-(3) proves that K-mixing "
            "for a rotation-aligned j=11/2 quasiparticle modifies the pure K=1/2 Clebsch-Gordan "
            "coefficient by only -5.22% at 15/2- and less than -1.5% for spins I >= 27/2-. "
            "This quantitatively substantiates Singh et al.'s stated justification on page 6 "
            "for adopting the simpler Eq. (1) with K=1/2, as the correction (+0.02 to +0.16 eb) "
            "is strictly dominated by the experimental measurement uncertainties (4.7% to 15.4%)."
        ),
        "checks": checks,
        "all_checks_passed": all(c["passed"] for c in checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "all_passed": result["all_checks_passed"]}))


if __name__ == "__main__":
    raise SystemExit("Retired checkpoint034: use day20_kmix_shrinkage034.py; legacy scientific certification withdrawn.")
