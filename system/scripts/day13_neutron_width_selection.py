#!/usr/bin/env python3
"""Natural-width scales, neutron TOF, and source gate/denominator checks.

Senyi2014 source values are central printed numbers, not event data. The
truth-table comparison labels competing readings of the prose; it does not
select the production mgt predicate or infer a data rejection fraction.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


HBAR_KEV_PS = 6.582119569e-7
M_NEUTRON_MEV = 939.56542052
C_MM_PER_NS = 299.792458


def calculate():
    width_cases = []
    for label, initial_tau, final_tau, observed in (
        ("Klemme134Nd6g-to4g", 1.63, 4.94, None),
        ("Senyi27Al2211keV-level-context", .0266, None, 15.)):
        gi = HBAR_KEV_PS / initial_tau
        gf = HBAR_KEV_PS / final_tau if final_tau else 0.
        width_cases.append({"source_input_label": label, "initial_mean_tau_ps": initial_tau,
                            "final_mean_tau_ps": final_tau, "Gamma_initial_keV": gi,
                            "Gamma_final_keV": gf, "ideal_transition_Lorentz_width_keV": gi + gf,
                            "source_observed_FWHM_keV_if_listed": observed,
                            "observed_over_natural_if_ground_final": observed / gi if observed else None,
                            "boundary": "ideal Markov Lorentz widths; source lifetimes/observed width remain reported inputs, no refit"})
    tof = []
    for neutron_e in (.5, 1., 2., 10.):
        gamma = 1 + neutron_e / M_NEUTRON_MEV
        beta = math.sqrt(1 - gamma**-2)
        for length in (235., 500.):
            tg = length / C_MM_PER_NS
            tn = length / (C_MM_PER_NS * beta)
            tof.append({"neutron_kinetic_MeV": neutron_e, "beta_neutron": beta,
                        "path_length_mm": length, "gamma_TOF_ns": tg, "neutron_TOF_ns": tn,
                        "separation_ns": tn - tg,
                        "boundary": "monoenergetic straight paths; source actual distributions, finite thickness, timing response absent"})
    central = [
        ("1040peak", .57, .28, .69), ("1040peak+bump", .52, .42, .72),
        ("total0-4095keV", .7373, .3368, .8258), ("Co1173", .117, .18, .276),
        ("Co1332", .09, .185, .258),
    ]
    denominators = []
    for label, first, conditional, reported in central:
        product = 1 - (1 - first) * (1 - conditional)
        assert abs(product - reported) < .003
        denominators.append({"source_label": label, "core_to_standard_reduction": first,
                             "standard_to_neutron_reject_reduction": conditional,
                             "calculated_core_to_final_reduction": product,
                             "source_reported_core_to_final_reduction": reported,
                             "central_rounding_difference": product - reported,
                             "boundary": "Table4 central count-ratio arithmetic; no joint covariance or binomial reconstruction"})
    truth = []
    for good in itertools.product((False, True), repeat=4):
        body_accept = any(good)
        # Hypothesis: conclusion's OR of bad conditions is a rejection rule.
        conclusion_reject = any(not x for x in good)
        alternative_accept = not conclusion_reject
        truth.append({"good_E1_E2_angle_FM": list(good), "body_accept_OR_good": body_accept,
                      "body_complement_reject_AND_bad": not body_accept,
                      "hypothesis_conclusion_reject_OR_bad": conclusion_reject,
                      "hypothesis_conclusion_accept_AND_good": alternative_accept,
                      "predicates_differ": body_accept != alternative_accept})
    differ = sum(x["predicates_differ"] for x in truth)
    assert differ == 14
    assert width_cases[0]["ideal_transition_Lorentz_width_keV"] < 1e-6
    assert width_cases[1]["Gamma_initial_keV"] < 1e-4
    ge_bound = 2. * 4 * 74 / (1 + 74)**2 * 1000
    monotonicity = {
        "assumptions": "same fixed standard clusters, same energies/line identity and peak-count normalization; plain acceptance post-filter; E1>45 is subset of E1>30",
        "source_single_E1_gt45_Co1332_loss_percent": 3.9,
        "source_combined_OR_gt30_Co1332_loss_percent": 18.5,
        "max_loss_for_literal_acceptance_OR_under_assumptions_percent": 3.9,
        "reported_combined_minus_bound_percent": 18.5 - 3.9,
        "literal_acceptance_OR_cannot_reproduce_under_assumptions": True,
        "boundary": "does not prove actual code uses a wrong predicate: retracking, cluster reassembly, line fitting, or different stage definitions can break post-filter assumptions; no significance/covariance inferred",
    }
    assert monotonicity["source_combined_OR_gt30_Co1332_loss_percent"] > monotonicity["max_loss_for_literal_acceptance_OR_under_assumptions_percent"]
    return {"schema_version": 1, "kind": "source-input arithmetic and gate-logic hypotheses; no event replay",
            "natural_width_cases": width_cases, "neutron_TOF_rows": tof,
            "elastic_recoil_toy": {"E_neutron_MeV": 2., "mass_ratio_A": 74,
                                   "max_recoil_keV_nonrel": ge_bound,
                                   "source_context_max_keV": 100., "source_context_visible_keV": 35.,
                                   "boundary": "mass-number elastic bound; pulse-height defect is source context, no quenching law inferred"},
            "nested_denominator_rows": denominators,
            "gate_truth_table": truth, "differing_boolean_assignments_out_of_16": differ,
            "gate_monotonicity": monotonicity,
            "gate_boundary": "not a14/16datafraction; thresholds away from equality and no production predicate selected; strict complement also changes < to <=",
            "verification": {"central_nested_ratios_match_rounding": True,
                             "DeMorgan_truth_table_checked": True,
                             "natural_width_orders_checked": True, "passed": True}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    r = calculate()
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(a.output), "verification": r["verification"]}))


if __name__ == "__main__":
    main()
