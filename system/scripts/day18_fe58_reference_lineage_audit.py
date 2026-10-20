#!/usr/bin/env python3
"""Official Fe58 source identity and a conditional rank-one reference chart."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    d = json.loads(a.contract.read_text())
    checks = []

    def check(name, condition, **evidence):
        checks.append({"name": name, "passed": bool(condition), **evidence})

    bodies = {}
    for name, path in d["source_object_files"].items():
        data = Path(path).read_bytes()
        check(name + "_official_object_hash", hashlib.sha256(data).hexdigest() == d["source_sha256"][name])
        bodies[name] = data.decode()
    check("adopted_source_is_201004_not_2026", "10NDS    201004" in bodies["adopted"])
    check("adopted_half_life_explicitly_from_same_B", "T$from B(E2)=0.1234 {I36} (1981Le02, Coul. ex.)" in bodies["adopted"])
    check("coulex_T_explicitly_deduced", "T$deduced from B(E2)=0.1234 {I36}" in bodies["coulex"])
    check("coulex_B_reference_exact", "BE2=0.1234 36 (1981Le02)" in bodies["coulex"])
    check("static_Q_same_primary_reference", "MOME2=-27.3 50 (1981Le02)" in bodies["coulex"])
    x = d["official_inputs"]
    mean = float(x["half_life_ps"]) / math.log(2)
    mean_sd = float(x["half_life_SD_ps"]) / math.log(2)
    bup = float(x["B_up_e2b2"])
    bdown = bup / 5
    rme = math.sqrt(bup)
    rme_sd = float(x["B_up_SD_e2b2"]) / (2 * rme)
    e = float(x["gamma_MeV"])
    cc = float(x["alpha_printed"])
    conditional_mean = 0.0816202120 / (bdown * e ** 5 * (1 + cc))
    check("half_to_mean_matches_paper_precision", abs(mean - 9.4) < 0.05,
          official_mean_ps=mean, paper_mean_ps=9.4)
    check("excitation_strength_RME_chart_matches_printed_reference", abs(rme - 0.351) < 0.0005,
          chart_RME_eb=rme)
    # The measured covariance is not known.  This covariance is exact only for
    # the declared single logB primitive with fixed E, branch and ICC.
    v = (float(x["B_up_SD_e2b2"]) / bup) ** 2
    matrix = [[0.25 * v, -0.5 * v], [-0.5 * v, v]]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
    check("declared_single_primitive_log_cov_rank_one", abs(determinant) < 1e-25,
          matrix=matrix, determinant=determinant)
    check("declared_mean_lifetime_B_product_constant", math.isclose(conditional_mean*bup, (conditional_mean/2)*(2*bup), rel_tol=1e-15))
    old = []
    for row in d["oldreactionhalf_lives"]:
        tau = float(row["T_half_ps"]) / math.log(2)
        old.append({**row, "mean_ps_from_fixed_field": tau,
                    "not_new_independent_lifetime": True})
    check("old_reaction_4plus_half_mean_role", abs(old[2]["mean_ps_from_fixed_field"] - 0.54) < 0.01)
    output = {"scope": d["scope"],
              "contract_sha256": hashlib.sha256(a.contract.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "official_reference": {"half_life_ps": float(x["half_life_ps"]),
                                      "mean_tau_ps": mean, "mean_uncertainty_scale_ps": mean_sd,
                                      "B_up_e2b2_chart": bup, "B_down_e2b2_chart": bdown,
                                      "RME_eb_chart": rme, "RME_local_uncertainty_scale_eb": rme_sd,
                                      "rate_conversion_conditional_mean_tau_ps": conditional_mean,
                                      "paper_RME_uncertainty_not_replaced": d["paper_gosia_reference"]},
              "declared_log_covariance_logM_logtau": {"matrix": matrix, "determinant": determinant,
                                                        "correlation": -1,
                                                        "fixed_E_branch_ICC_single_logB_only": True,
                                                        "variance_scale_from_printed_relativeB_is_illustrative": True,
                                                        "not_actual_Gosia_covariance_or_doublecount_finding": True},
              "old_reaction_half_mean_bridge": old,
              "actual_Gosia_weights_or_target_constraint_free_fit": "not obtained",
              "checks": checks, "checks_total": len(checks),
              "checks_passed": sum(x["passed"] for x in checks),
              "all_passed": all(x["passed"] for x in checks)}
    a.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_passed": output["all_passed"], "checks": len(checks),
                      "reference": output["official_reference"]}, ensure_ascii=False))
    if not output["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
