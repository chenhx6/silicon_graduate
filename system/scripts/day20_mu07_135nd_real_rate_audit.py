#!/usr/bin/env python3
"""Audit of Mukhopadhyay 2007 Table I: literal lifetimes and transition strengths in 135Nd.

Audits the true Table I published lifetimes and transition probabilities in 135Nd.
Proves that Band B level lifetimes are a factor of ~2 longer than Band A at 31/2- to 37/2-,
retracting the fabricated tau_band_a = [1.34, 0.81, ...] numbers in day19_nd_chiral_evolution_audit.py.
Quantifies how branch fractions p_gamma and gamma energies compensate so that in-band B(E2)
and B(M1) remain nearly symmetric (~0.88 and ~0.97 ratios) despite the 2x lifetime divergence.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    raw = root / "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"
    mu07_sha = "9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425"
    checks = []

    def check(name, cond):
        checks.append({"name": name, "passed": bool(cond)})
        if not cond:
            raise AssertionError(name)

    check("Mukhopadhyay 2007 raw SHA256 verified", hashlib.sha256(raw.read_bytes()).hexdigest() == mu07_sha)

    # Table I exact literal values from PRL 99, 172501 page 2:
    # Band A:
    # 29/2-: tau = 1.00(5), B(M1) = 3.2(2), B(E2) = 0.32(2)
    # 31/2-: tau = 0.75(8), B(M1) = 2.5(3), B(E2) = 0.32(3)
    # 33/2-: tau = 0.44(2), B(M1) = 2.2(2), B(E2) = 0.32(3)
    # 35/2-: tau = 0.28(2), B(M1) = 2.4(3), B(E2) = 0.32(3)
    # 37/2-: tau = 0.23(2), B(M1) = 1.7(3), B(E2) = 0.32(4)
    # 39/2-: tau = 0.22(2), B(M1) = 2.1(3), B(E2) = 0.13(3)
    # 41/2-: tau = 0.18(2), B(M1) = 2.1(3), B(E2) = 0.19(3)
    # 43/2-: tau = 0.16(2), B(M1) = 2.0(3), B(E2) = 0.21(4)
    # Band B:
    # 31/2-: tau = 1.46(2), B(M1) = 2.7(3), B(E2) = 0.28(3)
    # 33/2-: tau = 0.87(6), B(M1) = 2.1(2), B(E2) = 0.28(3)
    # 35/2-: tau = 0.64(5), B(M1) = 2.2(2), B(E2) = 0.28(4)
    # 37/2-: tau = 0.48(3), B(M1) = 1.7(2), B(E2) = 0.29(4)
    # 39/2-: tau = 0.24(4), B(M1) = 1.9(3), B(E2) = 0.11(3)
    table1_matched = [
        {"spin": "31/2", "tau_A": 0.75, "tau_A_err": 0.08, "tau_B": 1.46, "tau_B_err": 0.02,
         "bm1_A": 2.5, "bm1_A_err": 0.3, "bm1_B": 2.7, "bm1_B_err": 0.3,
         "be2_A": 0.32, "be2_A_err": 0.03, "be2_B": 0.28, "be2_B_err": 0.03},
        {"spin": "33/2", "tau_A": 0.44, "tau_A_err": 0.02, "tau_B": 0.87, "tau_B_err": 0.06,
         "bm1_A": 2.2, "bm1_A_err": 0.2, "bm1_B": 2.1, "bm1_B_err": 0.2,
         "be2_A": 0.32, "be2_A_err": 0.03, "be2_B": 0.28, "be2_B_err": 0.03},
        {"spin": "35/2", "tau_A": 0.28, "tau_A_err": 0.02, "tau_B": 0.64, "tau_B_err": 0.05,
         "bm1_A": 2.4, "bm1_A_err": 0.3, "bm1_B": 2.2, "bm1_B_err": 0.2,
         "be2_A": 0.32, "be2_A_err": 0.03, "be2_B": 0.28, "be2_B_err": 0.04},
        {"spin": "37/2", "tau_A": 0.23, "tau_A_err": 0.02, "tau_B": 0.48, "tau_B_err": 0.03,
         "bm1_A": 1.7, "bm1_A_err": 0.3, "bm1_B": 1.7, "bm1_B_err": 0.2,
         "be2_A": 0.32, "be2_A_err": 0.04, "be2_B": 0.29, "be2_B_err": 0.04},
        {"spin": "39/2", "tau_A": 0.22, "tau_A_err": 0.02, "tau_B": 0.24, "tau_B_err": 0.04,
         "bm1_A": 2.1, "bm1_A_err": 0.3, "bm1_B": 1.9, "bm1_B_err": 0.3,
         "be2_A": 0.13, "be2_A_err": 0.03, "be2_B": 0.11, "be2_B_err": 0.03},
    ]

    # 1. Lifetime ratios Band B / Band A
    tau_ratios = [row["tau_B"] / row["tau_A"] for row in table1_matched]
    # Ratios are ~1.95, 1.98, 2.29, 2.09, 1.09
    check("Band B lifetimes are ~2x longer than Band A at 31/2- to 37/2-",
          all(1.90 <= r <= 2.35 for r in tau_ratios[:4]))
    check("Band B / Band A lifetime ratio drops to ~1.09 at 39/2-",
          math.isclose(tau_ratios[4], 1.091, abs_tol=0.01))

    # 2. B(E2) and B(M1) ratios Band B / Band A
    be2_ratios = [row["be2_B"] / row["be2_A"] for row in table1_matched]
    bm1_ratios = [row["bm1_B"] / row["bm1_A"] for row in table1_matched]
    check("Band B / Band A in-band B(E2) ratio is exactly 0.875 for 31/2- to 35/2-",
          all(math.isclose(r, 0.875, abs_tol=1e-4) for r in be2_ratios[:3]))
    check("Band B / Band A in-band B(M1) ratio averages ~0.97 across 5 states",
          math.isclose(sum(bm1_ratios)/5.0, 0.971, abs_tol=0.01))

    # 3. Branching / energy compensation factor
    # Since B(E2) = C * p_gamma / (tau * E_gamma^5),
    # [p_gamma(B) / E_gamma^5(B)] / [p_gamma(A) / E_gamma^5(A)] = [tau(B) / tau(A)] * [B(E2_B) / B(E2_A)]
    comp_factors_e2 = [tau_r * be2_r for tau_r, be2_r in zip(tau_ratios, be2_ratios)]
    check("Compensation factor for B(E2) is 1.70 - 2.00 at 31/2- to 37/2-",
          all(1.65 <= c <= 2.05 for c in comp_factors_e2[:4]))

    result = {
        "kind": "literal audit of Mukhopadhyay 2007 Table I lifetimes and electromagnetic strengths",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_raw_sha256": mu07_sha,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "table1_matched": table1_matched,
        "ratios": {
            "tau_B_over_tau_A": tau_ratios,
            "be2_B_over_be2_A": be2_ratios,
            "bm1_B_over_bm1_A": bm1_ratios,
            "branching_energy_compensation_factor_E2": comp_factors_e2,
        },
        "checks": checks,
        "all_checks_passed": all(c["passed"] for c in checks),
        "scientific_conclusion": (
            "Table I of Mukhopadhyay 2007 proves that Band B level lifetimes are twice as long as Band A "
            "at spins 31/2- to 37/2- (tau_B / tau_A = 1.95 - 2.29), dropping to 1.09 at 39/2-. "
            "The old assertion of tau_B / tau_A ~ 1.08 +- 0.02 in checkpoint 042 was a numerical fabrication "
            "using fake tau_band_a inputs and is formally retracted. "
            "Despite the 2x lifetime difference, in-band B(E2) and B(M1) are nearly identical (B(E2)_B/B(E2)_A = 0.875) "
            "because the partial rate factors p_gamma / E_gamma^(2L+1) in Band B are 1.7 - 2.0 times larger, "
            "illustrating the crucial decoupling between total level lifetime and reduced electromagnetic transition strength."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "all_passed": result["all_checks_passed"]}))


if __name__ == "__main__":
    main()
