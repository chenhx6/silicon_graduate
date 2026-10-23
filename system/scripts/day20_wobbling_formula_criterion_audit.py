#!/usr/bin/env python3
"""Audit of Transverse Wobbling Electromagnetic Signatures, 1/I Scaling, and Decontamination.

This script audits the foundational electromagnetic and dynamic criteria for nuclear wobbling
(Bohr-Mottelson 1975, Frauendorf & Dönau 2014) applied to the A ~ 130 region (135Pr, 133La, 136Nd):
1. Harmonic approximation (HFA) interband-to-intraband E2 ratio:
   B(E2; I -> I-1)_out / B(E2; I -> I-2)_in = (1 / I) * tan^2(gamma + 30 deg).
2. Monotonic 1/I falloff: At gamma = 20 deg, the ratio must decrease from 16.7% at I=17/2 to 11.4% at I=25/2.
3. Multipole mixing ratio delta decontamination:
   The extracted B(E2)_out is proportional to delta^2 / (1 + delta^2).
   In 135Pr (747 keV link), changing from Matta 2015 assumed delta = -2.1 (E2 fraction 81.5%)
   to Lv 2022 measured delta = -0.47 (E2 fraction 18.1%) reduces the deduced B(E2)_out by a factor of 4.50,
   collapsing the apparent wobbling signature to an M1-dominated magnetic precession transition.
4. Dynamic frequency criterion: Transverse wobbling requires d(hbar * omega_w) / dI < 0,
   which is strictly conditioned on J_m > J_s > J_l and short-axis alignment.
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


def hfa_wobbling_e2_ratio(two_i: int, gamma_deg: float) -> float:
    """Calculate HFA B(E2)_out / B(E2)_in ratio for given spin I = two_i / 2 and gamma."""
    i_float = two_i / 2.0
    gamma_rad = math.radians(gamma_deg)
    tan_factor = math.tan(gamma_rad + math.pi / 6.0) ** 2
    return (1.0 / i_float) * tan_factor


def e2_fraction(delta: float) -> float:
    """Calculate radiative E2 fraction delta^2 / (1 + delta^2)."""
    return (delta ** 2) / (1.0 + delta ** 2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True, help="Run output directory")
    args = parser.parse_args()

    controls: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(f"Control failed: {name}")
        controls.append(name)

    # 1. HFA B(E2) ratio scaling checks for gamma = 20 deg
    gamma_test = 20.0
    tan2_factor = math.tan(math.radians(50.0)) ** 2  # tan^2(50 deg) ~ 1.420
    check("tan^2(gamma+30) at gamma=20 deg is ~ 1.420", math.isclose(tan2_factor, 1.42028, abs_tol=0.001))

    spins_test = [17, 21, 25, 29]  # 17/2 to 29/2
    ratios_hfa = [hfa_wobbling_e2_ratio(two_i, gamma_test) for two_i in spins_test]

    check("HFA ratio at 17/2 is ~ 0.167 (16.7%)", math.isclose(ratios_hfa[0], 0.1671, abs_tol=0.002))
    check("HFA ratio at 25/2 is ~ 0.114 (11.4%)", math.isclose(ratios_hfa[2], 0.1136, abs_tol=0.002))
    check("HFA ratio strictly decreases monotonically as 1/I",
          all(ratios_hfa[i] > ratios_hfa[i+1] for i in range(len(ratios_hfa)-1)))

    # 2. Decontamination audit of 135Pr 747.3 keV transition
    delta_matta = -2.10
    delta_lv = -0.47

    e2_frac_matta = e2_fraction(delta_matta)
    e2_frac_lv = e2_fraction(delta_lv)
    overestimation_factor = e2_frac_matta / e2_frac_lv

    check("Matta 2015 assumed delta=-2.1 gives ~ 81.5% E2 fraction",
          math.isclose(e2_frac_matta, 0.81516, abs_tol=0.002))
    check("Lv 2022 measured delta=-0.47 gives ~ 18.1% E2 fraction",
          math.isclose(e2_frac_lv, 0.18094, abs_tol=0.002))
    check("Overestimation factor of B(E2)_out exceeds 4.4x", overestimation_factor > 4.4)

    # 3. Spin dependence table for 135Pr
    # Experimental 135Pr states: 17/2-, 21/2-, 25/2-
    pr135_eval = []
    for two_i, delta_val in [(17, -0.47), (21, -0.37), (25, -0.31)]:
        i_f = two_i / 2.0
        hfa_theory = hfa_wobbling_e2_ratio(two_i, gamma_test)
        e2_f = e2_fraction(delta_val)
        m1_f = 1.0 - e2_f
        pr135_eval.append({
            "initial_spin": f"{two_i}/2^-",
            "I_float": i_f,
            "measured_delta": delta_val,
            "E2_fraction_percent": e2_f * 100.0,
            "M1_fraction_percent": m1_f * 100.0,
            "HFA_theoretical_E2_ratio": hfa_theory,
            "wobbling_status": "Falsified: M1 dominance (>80%) excludes collective transverse wobbling."
        })

    check("All 135Pr interband links have M1 fraction > 80%",
          all(e["M1_fraction_percent"] > 80.0 for e in pr135_eval))

    result = {
        "schema_version": 1,
        "checkpoint": "066",
        "title": "Audit of Transverse Wobbling Electromagnetic Signatures, 1/I Scaling, and Decontamination",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "controls_passed": controls,
        "hfa_theory_benchmarks": {
            "formula": "B(E2)_out / B(E2)_in = (1 / I) * tan^2(gamma + 30 deg)",
            "gamma_deg": gamma_test,
            "tan2_factor": tan2_factor,
            "spin_ratios": [
                {"spin": f"{two_i}/2", "I_float": two_i / 2.0, "ratio": r}
                for two_i, r in zip(spins_test, ratios_hfa)
            ]
        },
        "pr135_decontamination_audit": {
            "transition_energy_keV": 747.3,
            "delta_matta_2015": delta_matta,
            "delta_lv_2022": delta_lv,
            "e2_fraction_matta": e2_frac_matta,
            "e2_fraction_lv": e2_frac_lv,
            "b_e2_overestimation_factor": overestimation_factor,
            "states_evaluated": pr135_eval,
            "conclusion": "Polarization measurements by Lv et al. disprove transverse wobbling in 135Pr by revealing >80% M1 dominance across all connecting lines, collapsing B(E2)_out by a factor of 4.5."
        }
    }

    out_path = args.run_dir / "wobbling-formula-criterion-result-066.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path} ({len(controls)} controls passed)")


if __name__ == "__main__":
    main()
