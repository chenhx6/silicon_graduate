#!/usr/bin/env python3
"""Literal rate/geometry checks and conditional inverse examples, not a refit.

The scalar p=τ Tγ audit assumes the printed Eq1, K=1/2 and pairing of the
printed central lifetime and Qt. Its failures do not identify the producer,
true K, branch fractions, or an experimental inconsistency significance.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import scipy
from scipy.constants import alpha, c, electron_volt, hbar

from day19_evidence_repair_audit import cg_squared, rotor_cg_squared


def beta_from_moment(q_eb, z=58, a=131, r0=1.2, quadratic=.36):
    pref = 3 / math.sqrt(5 * math.pi) * z * (r0 * a ** (1 / 3)) ** 2 / 100
    u = q_eb / pref
    # Rationalized root is stable as u approaches zero.
    return 2 * u / (1 + math.sqrt(1 + 4 * quadratic * u))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ledger = json.loads(args.input.read_text())
    checks = []

    def check(name, value):
        checks.append({"name": name, "passed": bool(value)})
        if not value:
            raise AssertionError(name)

    root = Path(__file__).resolve().parents[2]
    raw = root / "raw/papers/2016_Singh et al_Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr.pdf"
    check("raw identity", hashlib.sha256(raw.read_bytes()).hexdigest() == ledger["raw_sha256"])
    # General radiation formula, e²/(4πε0)=alpha hbar c. b² ->fm⁴ =10⁴.
    hs = hbar / (electron_volt * 1e6)
    hc = hs * c * 1e15
    ke2 = (4 * math.pi / 75) * alpha * 1e4 / (hs * hc ** 4)
    check("E2 B units: e2b2 coefficient is about12.25 perps", 12.24 < ke2 * 1e-12 < 12.26)
    legacy_rate_perps = 1.2252
    check("old1p2252 perps coefficient misses factor10", 9.99 < (ke2 * 1e-12) / legacy_rate_perps < 10.01)
    diagnostics = []
    for name in ("case_Ce131", "case_Pr133"):
        for row in ledger[name]["rows"]:
            i = F(str(row["spin"]))
            g = rotor_cg_squared(i, F(1, 2))
            check(name + str(i) + " closedCG/exact factorial agreement", g == cg_squared(i, 2, i - 2, F(1, 2), 0, F(1, 2)))
            if row["tau"]["kind"] != "finite" or row["Qt"]["kind"] != "finite":
                continue
            energy, tau, qt = row["E_gamma_keV"], row["tau"]["value"], row["Qt"]["value"]
            def product(t, q, e):
                return t * 1.224 * (e / 1000) ** 5 * float(g) * q ** 2
            p = product(tau, qt, energy)
            # Half last printed digit: an explicit rounding convention, NOT a CI.
            tau_step = 1 if (name == "case_Pr133" and i == F(15, 2)) else (.1 if (tau in [9.6, 3.9]) else .01)
            low = product(tau - tau_step / 2, qt - .005, energy - .5)
            high = product(tau + tau_step / 2, qt + .005, energy + .5)
            diagnostics.append({
                "case": name, "I": str(i), "E_keV": energy,
                "tau_ps_literal": tau, "Qt_eb_literal": qt, "K_control": "1/2",
                "CG_squared_exact": str(g), "p_implied_Eq1": p,
                "scalar_Eq1_tau_for_p1_ps": tau / p,
                "declared_half_last_digit_rounding_product_range": [low, high],
                "rounding_only_contains_p1": low <= 1 <= high,
                "central_p_exceeds_one_under_this_contract": p > 1,
                "interpretation": "Literal scalar central-product audit only. Physical photon branch <=1 under the stated formula/role contract; do not infer an actual branch, true K, producer, error probability or corrected measured value.",
            })
    i, k = F(27, 2), F(11, 2)
    ratio = math.sqrt(float(rotor_cg_squared(i, F(1, 2)) / rotor_cg_squared(i, k)))
    check("fixedK candidate ratio is sqrt169over114", math.isclose(ratio, math.sqrt(169 / 114)))
    check("printed2p72over2p28 is not fixedK ratio", not math.isclose(ratio, 2.72 / 2.28, rel_tol=.01))
    # Eq5 explicitly permits two gamma choices around -30deg with equal factor.
    def geom(gamma):
        return math.cos(math.radians(gamma + 30)) / math.cos(math.radians(30))
    q20 = 2.5 / geom(-80)
    check("gamma-80 and+20 give identical Eq5 geometry", math.isclose(geom(-80), geom(20)))
    examples = [{"declared_Qt_eb": 2.5, "gamma_deg": gamma,
                 "Q20_eb": 2.5 / geom(gamma),
                 "beta2_if_Eq4_applied_to_Q20": beta_from_moment(2.5 / geom(gamma))}
                for gamma in (-80, 20, 0)]
    # Nonzero E2 strength at exactly zero static spectroscopic moment.
    # I3,K2 ->I2,K2 is allowed; I3 ->I1 at K2 is NOT an allowed control.
    gs = cg_squared(3, 2, 2, 2, 0, 2)
    qs_factor = F(3 * 2 ** 2 - 3 * (3 + 1), (3 + 1) * (2 * 3 + 3))
    b = 5 / (16 * math.pi) * 4 ** 2 * float(gs)
    check("zeroQs with allowed nonzero E2 branch", qs_factor == 0 and gs == F(5, 14) and b > 0)
    result = {
        "kind": "printed scalar-rate closure and declared geometry counterexamples",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "CG_dependency_sha256": hashlib.sha256((root / "system/scripts/day19_evidence_repair_audit.py").read_bytes()).hexdigest(),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "source_sha256": ledger["raw_sha256"],
        "modern_unit_reconstruction": {"scipy_version": scipy.__version__, "alpha": alpha,
            "hbar_MeV_s": hs, "hbarc_MeV_fm": hc,
            "K_E2_per_s_per_MeV5_per_e2b2": ke2,
            "K_E2_per_ps": ke2 * 1e-12,
            "rotor_Qt_coefficient_from_modern_units_per_s": ke2 * 5 / (16 * math.pi),
            "Singh_printed_Eq1_Qt_coefficient_per_s": 1.224e12,
            "role": "Independent units reconstruction from scipy.constants; do not replace historical printed coefficients or claim digits as experimental precision."},
        "literal_scalar_closure": diagnostics,
        "fixedK_candidates_not_actualK": {"I": "27/2", "hypothetical_ratio": ratio, "printed_ratio": 2.72 / 2.28},
        "Eq5_inverse_examples_not_measured_shapes": examples,
        "zero_Qs_control_not_Ce131": {"I": 3, "K": 2, "Q0_eb": 4,
            "allowed_E2_final_I": 2, "CG_squared": str(gs), "Qs_eb": 0,
            "B_E2_e2b2": b},
        "checks": checks, "all_mathematical_controls_passed": all(c["passed"] for c in checks),
        "boundaries": ["No original likelihood, joint covariance, branch/ICC ledger or exact producer",
            "Rounding intervals are not error bars or confidence intervals",
            "A central scalar closure residual does not assign experimental significance or infer true K",
            "Eq4 applied to Q20 is the author's mapping convention, not a general triaxial invariant",
            "No actual nuclear shape, feeding direction or collective mode identified"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks),
        "literal_p": [{"case": r["case"], "I": r["I"], "p": r["p_implied_Eq1"]} for r in diagnostics],
        "inverse_examples": examples}, ensure_ascii=False))


if __name__ == "__main__":
    main()
