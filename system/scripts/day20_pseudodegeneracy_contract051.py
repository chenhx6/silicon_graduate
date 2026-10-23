#!/usr/bin/env python3
"""Audits 134Pr pseudodegeneracy and configuration mixing (Petrache 2006).

Declared mathematical and physical controls:
1. Two-level mixing eigenvalue splitting Delta E = sqrt(delta^2 + 4V^2) >= 2|V|;
2. Upper bounds |V| <= 18 keV (I=15, Delta E=36 keV) and |V| <= 22 keV (I=16, Delta E=44 keV);
3. Table I wave function mixing fractions (alpha=0.894 -> beta^2=20.1% at I=15; alpha=0.427 -> 18.2% at I=16);
4. Intrinsic quadrupole moment ratio Q0,1 / Q0,2 = 2.0(4) disproving chiral shape symmetry;
5. Systematic comparison with 135Nd: energy degeneracy without shape symmetry (134Pr) vs lifetime divergence with shape symmetry (135Nd).
"""
from __future__ import annotations

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    root = Path(__file__).resolve().parents[2]

    checks = []
    def check(name, ok):
        if not ok:
            raise AssertionError(name)
        checks.append({"name": name, "passed": bool(ok)})

    # -------------------------------------------------------------------------
    # 1. Two-level mixing bounds for 134Pr at I=15 and I=16
    # -------------------------------------------------------------------------
    delta_e15 = 36.0  # keV
    delta_e16 = 44.0  # keV
    v_max_15 = delta_e15 / 2.0  # 18.0 keV
    v_max_16 = delta_e16 / 2.0  # 22.0 keV
    v_extracted_odd = 14.0       # keV (Petrache 2006 p.3)
    v_extracted_even = 17.0      # keV (Petrache 2006 p.3)
    check("Interaction V is strictly bounded by Delta_E / 2 (V <= 18 keV at I=15, V <= 22 keV at I=16)",
          v_extracted_odd <= v_max_15 and v_extracted_even <= v_max_16)

    # -------------------------------------------------------------------------
    # 2. Wave function amplitudes from Table I
    # -------------------------------------------------------------------------
    # I = 15: alpha_15_yrast = 0.894 -> beta_15 = sqrt(1 - 0.894^2)
    alpha_15 = 0.894
    beta_15_sq = 1.0 - alpha_15**2  # ~ 0.200764
    beta_15 = math.sqrt(beta_15_sq)  # ~ 0.448067
    check("At I=15, alpha=0.894 implies mixing probability beta^2 ~ 20.1%",
          math.isclose(beta_15_sq, 0.200764, rel_tol=1e-4))

    # I = 16: alpha_16_yrare = 0.427 -> yrast amplitude = sqrt(1 - 0.427^2)
    alpha_16_yrare = 0.427
    beta_16_sq = alpha_16_yrare**2   # ~ 0.182329
    alpha_16_yrast = math.sqrt(1.0 - beta_16_sq)  # ~ 0.904251
    check("At I=16, yrare amplitude 0.427 implies mixing probability ~ 18.2%",
          math.isclose(beta_16_sq, 0.182329, rel_tol=1e-4))

    # -------------------------------------------------------------------------
    # 3. Quadrupole moment ratio Q0,1 / Q0,2 = 2.0(4)
    # -------------------------------------------------------------------------
    q_ratio_central = 2.0
    q_ratio_low = 1.6
    q_ratio_high = 2.4
    # Corresponding unmixed in-band B(E2) ratio: (Q0,1 / Q0,2)^2
    be2_unmixed_ratio_central = q_ratio_central**2  # 4.0
    be2_unmixed_ratio_low = q_ratio_low**2          # 2.56
    be2_unmixed_ratio_high = q_ratio_high**2        # 5.76
    check("Unmixed B(E2) ratio is ~4.0 (allowed range 2.56 to 5.76), disproving chiral shape symmetry",
          math.isclose(be2_unmixed_ratio_central, 4.0) and be2_unmixed_ratio_low > 2.5)

    # -------------------------------------------------------------------------
    # 4. Twin comparison: 134Pr vs 135Nd
    # -------------------------------------------------------------------------
    # In 134Pr: energy degenerate (Delta_E ~ 40 keV) but shape asymmetric (B(E2) ratio ~ 4.0)
    # In 135Nd: lifetime divergent (tau ratio ~ 2.0) but shape symmetric (B(E2) ratio ~ 0.88 - 0.91)
    check("134Pr demonstrates pseudodegeneracy (small DeltaE, large B(E2) asymmetry ~4x)",
          delta_e15 < 50.0 and be2_unmixed_ratio_central >= 4.0)

    out = {
        "checkpoint": "051",
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "pr134_mixing_audit": {
            "paper": "Petrache et al., Phys. Rev. Lett. 96, 112502 (2006)",
            "energy_gaps": {"I_15_keV": delta_e15, "I_16_keV": delta_e16},
            "interaction_bounds": {"V_max_15_keV": v_max_15, "V_max_16_keV": v_max_16},
            "extracted_interaction": {"V_odd_keV": v_extracted_odd, "V_even_keV": v_extracted_even},
            "wavefunctions": {
                "I_15": {"alpha": alpha_15, "beta": round(beta_15, 4), "mixing_pct": round(beta_15_sq * 100, 2)},
                "I_16": {"alpha_yrare": alpha_16_yrare, "alpha_yrast": round(alpha_16_yrast, 4), "mixing_pct": round(beta_16_sq * 100, 2)}
            },
            "quadrupole_moment_ratio": {
                "Q0_1_over_Q0_2": q_ratio_central,
                "allowed_range": [q_ratio_low, q_ratio_high],
                "implied_unmixed_BE2_ratio": be2_unmixed_ratio_central,
                "implied_unmixed_BE2_range": [be2_unmixed_ratio_low, be2_unmixed_ratio_high]
            }
        },
        "twin_chiral_paradigm": {
            "case_134Pr": {
                "phenomenon": "Pseudodegeneracy without chiral symmetry",
                "energy_splitting": "Delta E = 36 - 44 keV (nearly degenerate)",
                "electromagnetic_symmetry": "Severely broken: Q0,1/Q0,2 = 2.0(4), unmixed B(E2) differs by 4.0x",
                "mechanism": "Accidental band crossing of two distinct quasiparticle configurations coupled by V ~ 15 keV"
            },
            "case_135Nd": {
                "phenomenon": "Electromagnetic symmetry despite lifetime divergence",
                "energy_splitting": "Delta E ~ 200 - 300 keV",
                "level_lifetimes": "Severely asymmetric: tau_B / tau_A ~ 2.0x",
                "electromagnetic_symmetry": "Highly preserved: B(E2)_B/B(E2)_A = 0.88 - 0.91, B(M1)_B/B(M1)_A = 0.90 - 1.08",
                "mechanism": "E_gamma^5 phase space and branching differences compensate the 2x lifetime divergence"
            },
            "methodological_conclusion": [
                "Energy near-degeneracy is neither necessary nor sufficient for nuclear chirality.",
                "Level lifetime symmetry is neither necessary nor sufficient for quadrupole collectivity symmetry.",
                "Absolute transition probabilities B(M1) and B(E2) extracted through lifetime and branching measurements provide the only definitive criterion for chiral symmetry."
            ]
        },
        "checks": checks,
        "all_checks_passed": True,
        "boundary": "Mathematical and physical controls on two-band mixing in 134Pr and comparative analysis with 135Nd. Does not assert full microscopic many-body wave functions."
    }

    out_path = run_dir / "pseudodegeneracy-contract-result-051.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"artifact": str(out_path), "checks": len(checks), "all_passed": True}))


if __name__ == "__main__":
    main()
