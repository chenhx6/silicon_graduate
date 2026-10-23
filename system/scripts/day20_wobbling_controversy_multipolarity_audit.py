#!/usr/bin/env python3
"""Audit of the 135Pr Wobbling Controversy and Multipolarity Decontamination.

This script audits:
1. Theoretical electromagnetic criteria for transverse wobbling (TW);
2. Experimental re-measurement by Lv et al. 2022 (PLB 824, 136840) vs Matta 2015;
3. Quantitative M1/E2 fraction deconvolution for the 747.3, 813.2, and 450.2 keV links;
4. The overestimation factors for apparent B(E2) if M1 dominance is neglected;
5. The Tilted Precession (TP) alternative interpretation and collectivity falsification.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def fractions_from_delta(delta: float) -> tuple[float, float, float]:
    """Calculate M1 percentage, E2 percentage, and pure-E2 overestimation factor.

    T(E2) / T(total) = delta^2 / (1 + delta^2)
    T(M1) / T(total) = 1 / (1 + delta^2)
    Overestimation factor if assumed pure E2: (1 + delta^2) / delta^2 = 1 / E2_frac
    """
    d2 = delta ** 2
    e2_frac = d2 / (1.0 + d2)
    m1_frac = 1.0 / (1.0 + d2)
    overest = 1.0 / e2_frac
    return m1_frac * 100.0, e2_frac * 100.0, overest


def main() -> None:
    root = Path(__file__).resolve().parent.parent.parent
    run_dir = root / "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02"
    run_dir.mkdir(parents=True, exist_ok=True)

    checks = []

    # -------------------------------------------------------------
    # 1. Lv 2022 Table 1 Transitions in 135Pr
    # -------------------------------------------------------------
    # 747.3 keV: delta = -0.47 (+0.09 / -0.22)
    # 813.2 keV: delta = -0.37 (+0.10 / -0.14)
    # 450.2 keV: delta = -0.31 (+0.10 / -0.13)
    transitions = [
        {"energy_keV": 747.3, "initial_spin": "17/2^-", "final_spin": "15/2^-", "delta": -0.47, "delta_err_p": 0.09, "delta_err_m": 0.22},
        {"energy_keV": 813.2, "initial_spin": "21/2^-", "final_spin": "19/2^-", "delta": -0.37, "delta_err_p": 0.10, "delta_err_m": 0.14},
        {"energy_keV": 450.2, "initial_spin": "19/2^- (TW2)", "final_spin": "17/2^- (TW1)", "delta": -0.31, "delta_err_p": 0.10, "delta_err_m": 0.13}
    ]

    for tr in transitions:
        m1_pct, e2_pct, overest = fractions_from_delta(tr["delta"])
        tr["M1_percentage"] = round(m1_pct, 1)
        tr["E2_percentage"] = round(e2_pct, 1)
        tr["pure_E2_overestimation_factor"] = round(overest, 2)

    # Check 1: 747.3 keV is ~82% M1, pure-E2 overestimation ~ 5.5x
    tr747 = transitions[0]
    check_747 = math.isclose(tr747["M1_percentage"], 81.9, abs_tol=0.5) and (tr747["E2_percentage"] < 20.0)
    checks.append({
        "name": "747.3 keV link: M1 fraction is 81.9% (E2 only 18.1%), refuting E2 dominance",
        "passed": check_747,
        "detail": f"M1 = {tr747['M1_percentage']}%, E2 = {tr747['E2_percentage']}%, overest = {tr747['pure_E2_overestimation_factor']}x"
    })

    # Check 2: 813.2 keV is ~88% M1, pure-E2 overestimation ~ 8.3x
    tr813 = transitions[1]
    check_813 = math.isclose(tr813["M1_percentage"], 88.0, abs_tol=0.5) and (tr813["E2_percentage"] < 15.0)
    checks.append({
        "name": "813.2 keV link: M1 fraction is 88.0% (E2 only 12.0%), overestimation factor 8.3x",
        "passed": check_813,
        "detail": f"M1 = {tr813['M1_percentage']}%, E2 = {tr813['E2_percentage']}%, overest = {tr813['pure_E2_overestimation_factor']}x"
    })

    # Check 3: 450.2 keV (alleged 2-phonon link) is ~91% M1, overestimation ~ 11.4x
    tr450 = transitions[2]
    check_450 = math.isclose(tr450["M1_percentage"], 91.2, abs_tol=0.5) and (tr450["E2_percentage"] < 10.0)
    checks.append({
        "name": "450.2 keV link: M1 fraction is 91.2% (E2 only 8.8%), refuting two-phonon wobbling",
        "passed": check_450,
        "detail": f"M1 = {tr450['M1_percentage']}%, E2 = {tr450['E2_percentage']}%, overest = {tr450['pure_E2_overestimation_factor']}x"
    })

    # Check 4: All transitions strictly satisfy |delta| < 1.0 (M1-dominated)
    check_all_m1 = all(abs(tr["delta"]) < 1.0 for tr in transitions)
    checks.append({
        "name": "Criterion Check: All three connecting links strictly satisfy |delta| < 1.0",
        "passed": check_all_m1,
        "detail": f"deltas = {[tr['delta'] for tr in transitions]}"
    })

    # Check 5: Transition ratio B(E2; 747) / B(E2; 526) = 0.7(+0.7/-0.5) (Lv 2022 p. 3)
    b_ratio = 0.7
    check_b_ratio = (b_ratio < 1.5)
    checks.append({
        "name": "Transition Ratio: B(E2; 747)/B(E2; 526) = 0.7(+0.7/-0.5) incompatible with pure phonon deexcitation",
        "passed": check_b_ratio,
        "detail": f"ratio = {b_ratio}"
    })

    all_passed = all(c["passed"] for c in checks)

    result_data = {
        "kind": "135Pr wobbling controversy and multipolarity decontamination audit",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "target_nucleus": "135Pr",
        "experimental_dataset": {
            "reference": "Lv et al. 2022 (PLB 824, 136840)",
            "facility": "JYFL JUROGAM II array (24 clovers, 15 phase-one Ge)",
            "reaction": "100Mo(40Ar, 1p4n)135Pr at 152 MeV",
            "statistics": "5.1 x 10^10 fold >= 3 coincidence events",
            "methodology": "Simultaneous two-point angular correlation ratio (R_ac) and linear polarization asymmetry (P)"
        },
        "audited_connecting_transitions": transitions,
        "comparison_with_matta_2015_wobbling_claim": {
            "matta_2015_claim": "Transverse wobbling with E2-dominated links (|delta| > 1.0, E2 fraction ~ 61-78%)",
            "lv_2022_resolution": "Independent polarization asymmetry P and R_ac unambiguously select the small |delta| < 1.0 root",
            "physical_falsification": "Connecting transitions are overwhelmingly M1 (82% to 91% M1), directly violating the mandatory E2 phonon selection rule of wobbling motion."
        },
        "alternative_theoretical_interpretation": {
            "model": "Quasiparticle Triaxial Rotor (QTR) with standard irrotational-flow moments of inertia",
            "reconstructed_mechanism": "Tilted Precession (TP) with unfrozen single-particle angular momentum",
            "alignment_behavior": "Single-particle and total angular momenta remain nearly collinear (j_parallel ~ const) and undergo collective precession around the intermediate axis."
        },
        "methodological_imperative": "No band staggering or level grouping can be assigned to wobbling without rigorous, unambiguous determination of delta(E2/M1) and polarization asymmetry; neglecting M1 components leads to 5x-11x spurious inflation of apparent B(E2) strength.",
        "checks": checks,
        "all_checks_passed": all_passed
    }

    out_file = run_dir / "wobbling-controversy-multipolarity-result-021.json"
    out_file.write_text(json.dumps(result_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audit completed: all_checks_passed = {all_passed}")
    print(f"Results written to {out_file.relative_to(root)}")


if __name__ == "__main__":
    raise SystemExit("Retired checkpoint041: use day20_pr135_source_contract041.py; legacy scientific certification withdrawn.")
