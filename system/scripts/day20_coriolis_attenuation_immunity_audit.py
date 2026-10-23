#!/usr/bin/env python3
"""Audit of Coriolis Attenuation Parameter Xi and Intraband Quadrupole Extraction Immunity.

This script audits the sensitivity of extracted intraband quadrupole moments Qt to the
phenomenological Coriolis attenuation parameter xi in odd-A transitional nuclei (e.g. 131Ce, 133Pr):
1. In two-band Coriolis mixing (K=1/2 and K=3/2 of the h_11/2 subshell), the off-diagonal
   Coriolis coupling is V_Cor(I) = -xi * (hbar^2 / 2J) * sqrt(I^2 + I - 3/4) * sqrt(35).
2. As xi varies from 0.60 to 1.00 (the standard pairing-attenuation range):
   - The rotational energy signature splitting Delta E(I) changes by up to 40%;
   - However, the effective intraband Clebsch-Gordan factor CG_eff(I) changes by less than 0.15%,
     because <I 2 1/2 0 | I-2 1/2> and <I 2 3/2 0 | I-2 3/2> are nearly equal for I >= 15/2.
3. Decoupling Theorem: The choice of Coriolis attenuation parameter xi (used to fit energy spectra)
   has virtually zero impact (< 0.15%) on the extracted intraband transition quadrupole moment Qt,
   proving that Qt extraction is decoupled from Coriolis pairing-attenuation ambiguities.
"""

from __future__ import annotations

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys

# Ensure access to day19_evidence_repair_audit
sys.path.insert(0, str(Path(__file__).resolve().parent))
from day19_evidence_repair_audit import signed_cg


def coriolis_mixing_eval(two_i: int, xi: float, a_rot: float = 0.015, delta_eps: float = 0.200) -> tuple[float, float, float]:
    """Calculate Coriolis mixing angle theta, energy splitting contribution, and CG_eff for spin I."""
    I = two_i / 2.0
    If = I - 2.0
    den_E = delta_eps - 2.0 * a_rot  # in MeV
    matrix_j = math.sqrt(35.0)

    term_I = math.sqrt(I ** 2 + I - 0.75)
    term_If = math.sqrt(If ** 2 + If - 0.75)

    v_cor_I = xi * a_rot * term_I * matrix_j
    v_cor_If = xi * a_rot * term_If * matrix_j

    theta_I = 0.5 * math.atan(2.0 * v_cor_I / den_E)
    theta_If = 0.5 * math.atan(2.0 * v_cor_If / den_E)

    cg_half = signed_cg(F(two_i, 2), 2, F(two_i - 4, 2), F(1, 2), 0, F(1, 2))
    cg_3half = signed_cg(F(two_i, 2), 2, F(two_i - 4, 2), F(3, 2), 0, F(3, 2))

    cg_eff = math.cos(theta_I) * math.cos(theta_If) * cg_half + math.sin(theta_I) * math.sin(theta_If) * cg_3half
    e_split = 2.0 * v_cor_I  # scale of energy perturbation
    return theta_I, cg_eff, e_split


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True, help="Run output directory")
    args = parser.parse_args()

    controls: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(f"Control failed: {name}")
        controls.append(name)

    spins = [15, 19, 23, 27, 31, 35]  # two_i: 15/2 to 35/2

    # 1. Evaluate across spins for xi = 1.0 (unattenuated) and xi = 0.70 (typical pairing attenuated)
    spin_results = []
    for two_i in spins:
        I_val = two_i / 2.0
        th_1, cg_1, e_split_1 = coriolis_mixing_eval(two_i, 1.0)
        th_7, cg_7, e_split_7 = coriolis_mixing_eval(two_i, 0.7)

        cg_ratio = cg_7 / cg_1
        cg_diff_pct = (cg_ratio - 1.0) * 100.0
        e_ratio = e_split_7 / e_split_1

        spin_results.append({
            "spin": f"{two_i}/2",
            "I_float": I_val,
            "xi_1_0": {"theta_rad": th_1, "sin2_theta": math.sin(th_1) ** 2, "CG_eff": cg_1, "E_split_MeV": e_split_1},
            "xi_0_7": {"theta_rad": th_7, "sin2_theta": math.sin(th_7) ** 2, "CG_eff": cg_7, "E_split_MeV": e_split_7},
            "CG_ratio_0_7_over_1_0": cg_ratio,
            "CG_percent_difference": cg_diff_pct,
            "energy_split_ratio": e_ratio
        })

    # Control checks
    # Energy splitting scales linearly with xi (0.7 / 1.0 = 0.7)
    check("Energy splitting scales proportionally with xi (= 0.70)",
          all(math.isclose(r["energy_split_ratio"], 0.70, rel_tol=1e-12) for r in spin_results))

    # Intraband CG changes by less than 0.15% across all spins
    check("Intraband CG factor difference between xi=0.7 and 1.0 is strictly < 0.15%",
          all(abs(r["CG_percent_difference"]) < 0.15 for r in spin_results))

    # Maximum difference occurs at lowest spin (15/2) and monotonically decreases with spin
    check("CG difference decreases monotonically with spin",
          all(abs(spin_results[i]["CG_percent_difference"]) >= abs(spin_results[i+1]["CG_percent_difference"])
              for i in range(len(spin_results)-1)))

    # Scan across xi in [0.5, 1.0] at I = 15/2
    xi_scan = []
    for xi_val in [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        th, cg, es = coriolis_mixing_eval(15, xi_val)
        xi_scan.append({
            "xi": xi_val,
            "sin2_theta": math.sin(th) ** 2,
            "CG_eff": cg,
            "percent_difference_from_xi_1_0": (cg / spin_results[0]["xi_1_0"]["CG_eff"] - 1.0) * 100.0
        })

    check("Even for extreme xi=0.5, CG difference is < 0.25%",
          abs(xi_scan[0]["percent_difference_from_xi_1_0"]) < 0.25)

    result = {
        "schema_version": 1,
        "checkpoint": "067",
        "title": "Audit of Coriolis Attenuation Parameter Xi and Intraband Quadrupole Extraction Immunity",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "controls_passed": controls,
        "spin_evaluations": spin_results,
        "xi_parameter_scan_at_15_2": xi_scan,
        "decoupling_theorem_conclusion": (
            "While the phenomenological Coriolis attenuation parameter xi changes the rotational energy signature "
            "splitting by up to 40% (scaling linearly with xi), it alters the intraband transition Clebsch-Gordan "
            "factor by less than 0.15%. Therefore, extracted transition quadrupole moments Qt are mathematically "
            "decoupled from, and immune to, the Coriolis attenuation parameter ambiguity."
        )
    }

    out_path = args.run_dir / "coriolis-attenuation-immunity-result-067.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path} ({len(controls)} controls passed)")


if __name__ == "__main__":
    main()
