#!/usr/bin/env python3
"""Conditional branch gates and shared photon counts: declared L2 model only."""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.special import ndtr


def design() -> dict:
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)
        if not condition:
            raise AssertionError(label)

    # These probabilities are chosen for the exercise, not fitted from Table I.
    b, h = .60, .20
    e_a, e_b, e_l, e_h = .05, .07, .10, .10
    rate = 1_000_000.0
    probabilities = [h, b, e_h, e_l, e_a, e_b]
    labels = ["A_low", "A_high", "B_low", "B_high", "A_gate", "B_gate"]
    mean = np.zeros(6)
    second = np.zeros((6, 6))
    fourth = np.zeros((6, 6))
    norm = 0.0

    def event_vector(bits):
        high, cascade, det_high, det_low, det_a, det_b = bits
        gate_a = (1 - cascade) * det_a
        gate_b = cascade * det_b
        return np.array([gate_a * cascade * det_low,
                         gate_a * high * det_high,
                         gate_b * det_low,
                         gate_b * high * det_high,
                         gate_a, gate_b], dtype=float)

    for bits in itertools.product((0, 1), repeat=6):
        p = np.prod([q if bit else 1 - q for bit, q in zip(bits, probabilities)])
        vec = event_vector(bits)
        outer = np.outer(vec, vec)
        norm += p
        mean += p * vec
        second += p * outer
        fourth += p * outer ** 2
    analytic_mean = np.array([0, h*(1-b)*e_a*e_h, b*e_b*e_l,
                              h*b*e_b*e_h, (1-b)*e_a, b*e_b])
    check("probabilities_normalized", np.isclose(norm, 1))
    check("means_agree_with_direct_branch_products", np.allclose(mean, analytic_mean))
    check("low_line_excluded_by_true_direct_branch_gate", mean[0] == 0)
    covariance_poisson_flow = rate * second
    covariance_fixed_n = rate * (second - np.outer(mean, mean))
    check("shared_two_photons_positive_covariance", np.isclose(covariance_poisson_flow[2,3], rate*h*b*e_b*e_l*e_h))
    check("poisson_flow_disjoint_branches_zero_covariance", covariance_poisson_flow[1,2] == 0)
    check("fixed_n_disjoint_branches_negative_covariance", covariance_fixed_n[1,2] < 0)
    check("flow_covariance_difference_is_rank_one", np.linalg.matrix_rank(covariance_poisson_flow-covariance_fixed_n, tol=1e-8) == 1)
    check("compound_poisson_covariance_psd", np.linalg.eigvalsh(covariance_poisson_flow).min() >= -1e-9)
    check("fixed_n_covariance_psd", np.linalg.eigvalsh(covariance_fixed_n).min() >= -1e-9)
    check("gate_subset_covariance_not_independent", np.isclose(covariance_poisson_flow[1,4], rate*mean[1]))

    # Independent event generation checks the enumeration, with variance-aware tolerances.
    rng = np.random.default_rng(20261014)
    trials = 5_000_000
    total = np.zeros(6)
    total_second = np.zeros((6,6))
    for start in range(0, trials, 100_000):
        k = min(100_000, trials-start)
        flags = rng.random((k,6)) < probabilities
        hi, route, dh, dl, da, db = flags.T
        ga, gb = (~route)&da, route&db
        v = np.column_stack((ga&route&dl, ga&hi&dh, gb&dl, gb&hi&dh, ga, gb)).astype(float)
        total += v.sum(axis=0)
        total_second += v.T @ v
    mc_mean, mc_second = total/trials, total_second/trials
    mean_se = np.sqrt(np.maximum(0, np.diag(second)-mean**2)/trials)
    second_se = np.sqrt(np.maximum(0, fourth-second**2)/trials)
    z_mean = np.divide(abs(mc_mean-mean), mean_se, out=np.zeros(6), where=mean_se>0)
    z_second = np.divide(abs(mc_second-second), second_se, out=np.zeros((6,6)), where=second_se>0)
    check("mc_mean_within_declared_6sigma", z_mean.max() < 6)
    check("mc_shared_second_moments_within_declared_6sigma", z_second.max() < 6)
    check("mc_preserves_branch_exclusion", total[0] == 0)

    # Unknowns L,H are unconditional photon yields including their photon efficiency.
    q = np.array([[0, (1-b)*e_a], [e_b, b*e_b]])
    check("pure_two_gate_design_rank_two", np.linalg.matrix_rank(q) == 2)
    check("one_gate_one_total_is_rank_one", np.linalg.matrix_rank(q[1:]) == 1)
    check("no_A_efficiency_loses_rank", np.linalg.matrix_rank(np.array([[0,0],[e_b,b*e_b]])) == 1)
    check("b_one_loses_direct_gate", np.linalg.matrix_rank(np.array([[0,0],[e_b,e_b]])) == 1)
    # A known leakage can also make the two gate signatures proportional.
    collapse_leak = (1-b)/b
    polluted = np.array([[collapse_leak*e_a,(1-b)*e_a],[e_b,b*e_b]])
    check("proportional_gate_contamination_loses_rank", np.linalg.matrix_rank(polluted) == 1)

    # Bin-integrated Gaussians: template geometry, without assuming Poisson bin likelihood.
    edges = np.arange(293.2, 305.900001, .1)
    def response(center, sigma):
        return np.diff(ndtr((edges-center)/sigma))
    tl, th = response(299.2,1), response(299.8,1)
    def condition(matrix):
        norms = np.linalg.norm(matrix,axis=0)
        s = np.linalg.svd(matrix/norms, compute_uv=False)
        return float(s[0]/s[-1]) if s[-1] > 1e-14 else None
    one_spectrum = np.column_stack((tl,th))
    joint = np.vstack((np.column_stack((q[0,0]*tl,q[0,1]*th)),
                       np.column_stack((q[1,0]*tl,q[1,1]*th))))
    indistinguishable = np.column_stack((tl,tl))
    joint_indistinguishable = np.vstack((np.column_stack((q[0,0]*tl,q[0,1]*tl)),
                                        np.column_stack((q[1,0]*tl,q[1,1]*tl))))
    check("same_response_one_spectrum_rank_one", np.linalg.matrix_rank(indistinguishable) == 1)
    check("same_response_two_known_gates_rank_two", np.linalg.matrix_rank(joint_indistinguishable) == 2)
    check("two_known_gates_improve_normalized_template_condition", condition(joint) < condition(one_spectrum))

    # When b is unknown, two *total* peak yields allow a continuous physical family.
    observed_a = rate*mean[1]
    observed_b_total = rate*(mean[2]+mean[3])
    family = []
    for candidate_b in [.45,.50,.60,.70,.75]:
        candidate_H = observed_a/((1-candidate_b)*e_a)
        candidate_L = observed_b_total/e_b-candidate_b*candidate_H
        candidate_rate = candidate_L/(candidate_b*e_l)
        candidate_h = candidate_H/(candidate_rate*e_h)
        prediction = np.array([[0,(1-candidate_b)*e_a],[e_b,candidate_b*e_b]]) @ np.array([candidate_L,candidate_H])
        check("unknown_branch_family_closure_"+str(candidate_b), np.allclose(prediction,[observed_a,observed_b_total]))
        check("unknown_branch_family_physical_"+str(candidate_b), candidate_rate>0 and 0<candidate_h<1)
        family.append({"b":candidate_b,"high_fraction":candidate_h,"parent_poisson_mean":candidate_rate,
                       "predicted_A_total":prediction[0],"predicted_B_total":prediction[1]})
    # Additional pure gate singles can constrain b, under this closed two-path model.
    na, nb = rate*mean[4], rate*mean[5]
    recovered_b = (nb/e_b)/(na/e_a+nb/e_b)
    recovered_rate = na/e_a+nb/e_b
    check("gate_singles_recover_b_under_closed_model", np.isclose(recovered_b,b))
    check("gate_singles_recover_rate_under_closed_model", np.isclose(recovered_rate,rate))

    low_energy = []
    for energy, alpha in [(46,261.0),(87,12.82)]:
        efficiency = .01
        population = 5000
        photon_fraction = 1/(1+alpha)
        detect_probability = efficiency*photon_fraction
        pzero = float(np.exp(population*np.log1p(-detect_probability)))
        n95 = float(np.log(.05)/np.log1p(-detect_probability))
        check("low_energy_gamma_suppression_"+str(energy), 0<photon_fraction<1)
        check("zero_count_threshold_exact_"+str(energy), np.isclose(np.exp(n95*np.log1p(-detect_probability)),.05))
        low_energy.append({"energy_keV":energy,"source_conditional_E2_alpha":alpha,
                           "photon_fraction":photon_fraction,"chosen_efficiency":efficiency,
                           "chosen_parent_population":population,"mean_detected":population*detect_probability,
                           "conditional_probability_zero":pzero,"population_for_5percent_zero":n95})

    return {"kind":"L2 conditional design; not193Bi data or fitted branching",
            "chosen_parameters":{"cascade_probability":b,"upper299.8_fraction":h,"eps622":e_a,"eps323":e_b,"eps299.2":e_l,"eps299.8":e_h,"parent_poisson_mean":rate},
            "count_labels":labels,"expected_counts":(rate*mean).tolist(),
            "poisson_flow_covariance":covariance_poisson_flow.tolist(),"fixed_parent_N_covariance":covariance_fixed_n.tolist(),
            "enumeration_states":64,"mc_trials":trials,"mc_seed":20261014,"max_mc_mean_z":float(z_mean.max()),"max_mc_second_z":float(z_second.max()),
            "gate_design":q.tolist(),"template_geometry":{"sigma_keV":1,"separation_keV":.6,"one_spectrum_condition":condition(one_spectrum),"two_gate_condition":condition(joint),"same_response_two_gate_condition":condition(joint_indistinguishable),"not_a_likelihood_or_power_estimate":True},
            "unknown_branch_family":family,"additional_gate_singles":{"N_A":na,"N_B":nb,"recovered_b":recovered_b},
            "low_energy_nonobservation_design":low_energy,"checks":checks,"checks_passed":sum(checks.values()),
            "source_locators":[{"path":"knowledge/sources/herzan-2015-193bi-spectroscopy.md","locator":"HE15-5"},{"path":"knowledge/sources/herzan-2015-193bi-spectroscopy.md","locator":"HE15-4"},{"path":"knowledge/sources/herzan-2015-193bi-spectroscopy.md","locator":"HE15-13"}],
            "boundaries":["One nucleus, two complete photon paths, no IC for the299/622 branch toy; independent detection and no angular correlations, summing, randoms or additional feeding. These are chosen limiting assumptions, not measured JUROGAM properties.","The0.6-keV line separation is source-supported; sigma, branch probability, efficiencies, rate and high fraction are self-chosen. Source intensity ratios are not fitted.","Shared event counts require compound Poisson or fixed-N covariance as appropriate. Template condition numbers ignore likelihood/background and do not predict experimental significance.","Pure tags and known conditional coefficients are necessary for the rank argument. Unknown branch, acceptance or correlated background can restore nonidentifiability.","Low-energy E2 alpha values are the author's Ref41 assumptions, not observed46/87-keV decays. N=5000 and eps=.01 are conditional examples without x-ray background or ICC uncertainty; zero-count probabilities are not real experimental upper limits."]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.resolve().relative_to(Path(__file__).resolve().parents[2])
    result=design()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"checks_passed":result["checks_passed"],"counts":result["expected_counts"],"geometry":result["template_geometry"],"mc_max_z":[result["max_mc_mean_z"],result["max_mc_second_z"]],"low_energy":result["low_energy_nonobservation_design"]},ensure_ascii=False))


if __name__=="__main__":
    main()
