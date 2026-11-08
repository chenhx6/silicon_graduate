#!/usr/bin/env python3
"""Reconstruct the declared two-branch teaching example, not measured nuclear data."""

from datetime import datetime, timezone
import hashlib
import json
from math import isclose, log
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs/l4/20261108-A130-branch-rate-controls"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    tau = 5e-12
    delta = 1.5
    a1, a2 = 100.0, 25.0
    alpha_m1, alpha_e2, alpha_second = 0.003, 0.0015, 0.005
    energy1, energy2 = 0.8, 0.5
    c_e2 = 5.498e22 / (150 * 197.33**5)
    c_m1 = 6.080e20 * (2 / 9) / 197.33**3
    f = delta**2 / (1 + delta**2)
    alpha_first = (alpha_m1 + delta**2 * alpha_e2) / (1 + delta**2)
    weight = a1 * (1 + alpha_first) + a2 * (1 + alpha_second)
    gamma1, gamma2 = a1 / (tau * weight), a2 / (tau * weight)
    b1 = tau * gamma1 * (1 + alpha_first)
    b2 = tau * gamma2 * (1 + alpha_second)
    be2_1, bm1_1 = gamma1 * f / (c_e2 * energy1**5), gamma1 * (1-f) / (c_m1 * energy1**3)
    be2_2 = gamma2 / (c_e2 * energy2**5)
    ratio_without_tau = a1 * f / a2 * (energy2 / energy1)**5
    checks = {
        "first_endpoint_allows_M1_and_E2": abs(4-3) <= 1 <= 4+3 and abs(4-3) <= 2 <= 4+3,
        "second_endpoint_forbids_M1": not abs(4-2) <= 1 <= 4+2,
        "second_endpoint_also_allows_M3_so_pure_E2_is_an_assumption": abs(4-2) <= 3 <= 4+2,
        "total_branch_probabilities_close": isclose(b1 + b2, 1, abs_tol=1e-14),
        "photon_branch_probabilities_not_forced_to_sum_one": tau * (gamma1 + gamma2) < 1,
        "rate_reconstructed_from_B": isclose(
            c_e2 * energy1**5 * be2_1 + c_m1 * energy1**3 * bm1_1, gamma1, rel_tol=1e-14
        ),
        "same_parent_ratio_eliminates_lifetime": isclose(be2_1 / be2_2, ratio_without_tau, rel_tol=1e-14),
        "missing_positive_channel_biases_known_rate_up": a1 / (tau * weight) > a1 / (tau * (weight + 5)),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    result = {
        "input_kind": "hypothetical teaching model; no experimental isotope",
        "inputs": {"tau_s": tau, "delta_first": delta, "relative_photon_strengths": [a1, a2],
                   "energies_MeV": [energy1, energy2], "alpha_first_M1_E2": [alpha_m1, alpha_e2],
                   "alpha_second_E2": alpha_second},
        "source_constants": {"electric_prefactor": 5.498e22, "magnetic_prefactor": 6.080e20,
                             "hbar_c_MeV_fm": 197.33},
        "C_E2": c_e2, "C_M1_book_SI": c_m1,
        "magnetic_unit": "B(M1) numerical value in Suhonen's (mu_N_SI/c)^2",
        "alpha_first_mixed": alpha_first, "normalizing_weight": weight,
        "photon_rates_s_inverse": [gamma1, gamma2], "total_branches": [b1, b2],
        "B_E2_e2_fm4": [be2_1, be2_2], "B_M1_book_SI": bm1_1,
        "ratio_E2": ratio_without_tau,
        "half_life_as_mean_life_rate_factor": 1/log(2),
        "mean_life_as_half_life_rate_factor": log(2), "checks": checks,
        "boundary": "Pure E2 and neglected higher multipoles are explicit model assumptions; no fit or real-nucleus inference.",
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "controls.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    source = ROOT / "raw/books/From nucleons to nucleus concepts of microscopic .pdf"
    provenance = {
        "recorded_at": datetime.now(timezone.utc).isoformat(), "python": sys.version,
        "producer": str(Path(__file__).resolve().relative_to(ROOT)), "producer_sha256": sha(Path(__file__)),
        "context_inputs": [{"path": str(source.relative_to(ROOT)), "sha256": sha(source),
                            "locator": "Printed pp.118–121; PDF pp.133–136; Eqs.6.1–6.18"}],
        "artifacts": [{"path": str(path.relative_to(ROOT)), "sha256": sha(path)}],
        "check_count": len(checks), "real_nucleus_calculation": False,
    }
    (OUT / "run-provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "all_pass": all(checks.values())}))


if __name__ == "__main__":
    main()
