#!/usr/bin/env python3
"""G24 printed-input arithmetic and analytic normalization/readiness checks.

There are no fabricated event histograms or experimental response templates.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

import sympy as sp


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "GO24-CALIBRATION-NORMALIZATION-AUDIT-01"
    assert sha(Path(cfg["raw"])) == cfg["raw_sha256"]
    q = cfg["quoted"]
    energy = q["E_keV"]
    u = energy/q["electron_rest_keV"]
    kn = (1+u)/(1+u+u*u)
    curves = {name: {"Q": kn*(v["a_per_keV"]*energy+v["b"]),
        "Q_printed": v["Q_847_printed"], "parameter_source": v["source"]}
        for name, v in cfg["reference_curves"].items()}
    assert abs(curves["Morse2022_GRETINA"]["Q"]-.200) < .001
    assert abs(curves["Kojima2021_Clover"]["Q"]-.229) < .001
    covariance_bounds = []
    for key in ["Qprime_sigma_text", "Qprime_sigma_Fig6"]:
        # First-order component bounds using quoted marginal errors only.
        a = q[key]/q["P"]
        b = q["Qprime"]*q["P_sigma_reported_dominated_systematic"]/q["P"]**2
        independent = math.hypot(a, b)
        covariance_bounds.append({"marginal_case": key, "sigma_Q_if_independent": independent,
            "sigma_Q_possible_interval_for_any_Cov": [abs(a-b), a+b],
            "not_recovered": "The actual Qprime-P covariance and shared selection systematics"})
    # Work symbolically; do not choose a made-up histogram to replay P=.57.
    nu = sp.symbols("nu", positive=True)
    ss = sp.symbols("s1:4", positive=True)
    nn = sp.symbols("n1:4", positive=True)
    bb = sp.symbols("b1:4", real=True)  # s_i'(P), not background.
    total_s, total_n = sum(ss), sum(nn)
    ell = sum(n*sp.log(nu*s)-nu*s for n, s in zip(nn, ss))
    nu_hat = total_n/total_s
    assert sp.simplify(sp.diff(ell, nu).subs(nu, nu_hat)) == 0
    profiled = ell.subs(nu, nu_hat)
    conditional = sum(n*sp.log(s/total_s) for n, s in zip(nn, ss)) + total_n*sp.log(total_n)-total_n
    assert sp.simplify(sp.expand_log(profiled-conditional, force=True)) == 0
    fixed_info = nu*sum(b*b/s for b, s in zip(bb, ss))
    schur = fixed_info-nu*sum(bb)**2/total_s
    pairwise = nu/total_s*sum(ss[i]*ss[j]*(bb[i]/ss[i]-bb[j]/ss[j])**2
                             for i in range(3) for j in range(i+1, 3))
    assert sp.factor(schur-pairwise) == 0
    k = sp.symbols("k", real=True)
    assert sp.simplify(schur.subs(dict(zip(bb, [k*s for s in ss])))) == 0
    assert sp.simplify((schur-fixed_info).subs(bb[2], -bb[0]-bb[1])) == 0
    # The alternate half-factor definition changes both Q and epsilon Q^2.
    qm, p, eps = sp.symbols("Qm P epsilon", positive=True)
    qg = qm/2
    assert sp.simplify(qg*p-qm*p/2) == 0
    assert sp.simplify(eps*qg*qg/(eps*qm*qm)) == sp.Rational(1, 4)
    output = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "source_sha256": cfg["raw_sha256"], "point_KN_Q0_847": kn,
        "printed_curve_replays": curves,
        "Table1_b_c_mapping_matches_p6_text": False,
        "rounded_Qprime_over_P": q["Qprime"]/q["P"],
        "Q_ratio_uncertainty_component_bounds": covariance_bounds,
        "F_selected_from_rounded_centrals": q["epsilon_selected_approx"]*q["Q_reported"]**2,
        "selected_over_uncut_F_using_reported_relative_changes": q["selection_efficiency_retention"]*q["selection_gain_Q"]**2,
        "narrow_over_selected_F_if_same_efficiency_baseline": q["narrow_efficiency_retention_if_same_baseline"]*(q["narrow_Q"]/q["Q_reported"])**2,
        "efficiency_after_36percentloss_from_MC_central": q["epsilon_coin_MC_before_cut"]*q["selection_efficiency_retention"],
        "pure_signal_profile": {"nu_hat": str(nu_hat), "loglikelihood_matches_conditional_shape_plus_constant": True,
            "Fisher_Schur_identity": "nu*(sum(sprime_i^2/s_i)-(sum(sprime_i))^2/S) = nu/S * sum_i<j s_i*s_j*(sprime_i/s_i-sprime_j/s_j)^2",
            "zero_information_for_pure_scale_change_control": True,
            "fixed_scale_and_profile_information_equal_if_Sprime0": True,
            "actual_G24_nuisance_profile_or_confidence_interval_recovered": False},
        "same_event_marginal_boundary": "If underlying independent Poisson energy-phi cells have means mu_ephi, Cov(E_e,D_phi)=mu_ephi. Full event/partition ledger is required; two marginal histograms are not automatically independent.",
        "normalization_conversion_same_harmonic_and_P_only": {"Q_Go_equals_Q_Morse_over2": True,
            "F_Go_equals_F_Morse_over4_if_same_epsilon": True,
            "certifies_detector_response_transfer_or_rewrites_reported_table": False},
        "actual_counts_templates_or_Cov_downloaded": False,
        "new_experimental_fit": False}
    args.output.write_text(json.dumps(output, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: output[key] for key in ["point_KN_Q0_847", "printed_curve_replays", "rounded_Qprime_over_P",
        "Q_ratio_uncertainty_component_bounds", "F_selected_from_rounded_centrals",
        "selected_over_uncut_F_using_reported_relative_changes", "narrow_over_selected_F_if_same_efficiency_baseline",
        "pure_signal_profile"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
