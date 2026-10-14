#!/usr/bin/env python3
"""Synthetic DAY13 event-overlap covariance and deterministic spectrum replays.

One photon/event is drawn from the declared lifetime kernel. Gate overlap and
alternative correction references reuse the same events. Poisson and fixed
total event counts have different covariance. Replayed coarse histograms can
refine a partition but are not independent acquisitions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

import day13_finite_bin_lineshape as bins


ANGLE = 150.0


def probability(low, high, tau=bins.TRUE_TAU_PS, e0=bins.TRUE_E_KEV):
    if high <= low:
        return 0.0
    return float(bins.raw_bin_probabilities(np.array([low, high]), e0, tau, ANGLE)[0])


def point_angle_fisher(edges):
    p, _ = bins.conditional(bins.raw_bin_probabilities(
        edges, bins.TRUE_E_KEV, bins.TRUE_TAU_PS, ANGLE))
    derivatives = []
    step = 1e-4
    for coordinate in (0, 1):
        values = []
        for sign in (-1, 1):
            tau = bins.TRUE_TAU_PS*math.exp(sign*step) if coordinate == 0 else bins.TRUE_TAU_PS
            e0 = bins.TRUE_E_KEV+sign*step if coordinate == 1 else bins.TRUE_E_KEV
            values.append(bins.conditional(bins.raw_bin_probabilities(edges, e0, tau, ANGLE))[0])
        derivatives.append((values[1]-values[0])/(2*step))
    derivative = np.column_stack(derivatives)
    keep = p > 1e-14
    return derivative[keep].T @ (derivative[keep]/p[keep, None])


def local_errors(matrix, count=10000):
    covariance = np.linalg.inv(count*matrix)
    return dict(tau_SE_fs=1000*bins.TRUE_TAU_PS*math.sqrt(covariance[0, 0]),
                energy_SE_keV=math.sqrt(covariance[1, 1]))


def calculate():
    e0 = bins.TRUE_E_KEV
    gate_a = [e0-70.0, e0-20.0]
    gate_b = [e0-50.0, e0-5.0]
    pa = probability(*gate_a)
    pb = probability(*gate_b)
    pab = probability(max(gate_a[0], gate_b[0]), min(gate_a[1], gate_b[1]))
    exclusive = np.array([pa-pab, pb-pab, pab, 1-pa-pb+pab])
    assert exclusive.min() >= 0 and abs(exclusive.sum()-1) < 1e-12
    event_count = 10000
    poisson_cov = event_count*np.array([[pa, pab], [pab, pb]])
    fixed_cov = event_count*(np.array([[pa, pab], [pab, pb]])
                              - np.outer([pa, pb], [pa, pb]))
    rng = np.random.default_rng(131430)
    repeats = 150000
    poisson_parts = rng.poisson(event_count*exclusive, (repeats, 4))
    fixed_parts = rng.multinomial(event_count, exclusive, repeats)
    poisson_views = np.column_stack((poisson_parts[:, 0]+poisson_parts[:, 2],
                                    poisson_parts[:, 1]+poisson_parts[:, 2]))
    fixed_views = np.column_stack((fixed_parts[:, 0]+fixed_parts[:, 2],
                                  fixed_parts[:, 1]+fixed_parts[:, 2]))
    empirical_poisson = np.cov(poisson_views, rowvar=False)
    empirical_fixed = np.cov(fixed_views, rowvar=False)
    poisson_error = float(np.linalg.norm(empirical_poisson-poisson_cov)/np.linalg.norm(poisson_cov))
    fixed_error = float(np.linalg.norm(empirical_fixed-fixed_cov)/np.linalg.norm(fixed_cov))
    assert poisson_error < 0.025 and fixed_error < 0.025

    # Disjoint single-photon bins: Poisson thinning versus fixed-N anticorrelation.
    disjoint_probabilities = np.array([0.25, 0.35, 0.40])
    poisson_disjoint = np.diag(event_count*disjoint_probabilities[:2])
    fixed_disjoint = event_count*(np.diag(disjoint_probabilities[:2])
                                   - np.outer(disjoint_probabilities[:2], disjoint_probabilities[:2]))
    assert poisson_disjoint[0, 1] == 0 and fixed_disjoint[0, 1] < 0

    # Same photon corrected against two fixed exit/reference speeds. Their
    # energies differ by a deterministic factor at this point angle.
    beta_reference_a, beta_reference_b = bins.history.BETA_EXIT, 0.10
    cosine = math.cos(math.radians(ANGLE))
    d_a = (1-beta_reference_a*cosine)/math.sqrt(1-beta_reference_a**2)
    d_b = (1-beta_reference_b*cosine)/math.sqrt(1-beta_reference_b**2)
    factor = d_b/d_a
    edges_a = bins.make_edges(5.0)
    edges_b = bins.make_edges(5.0)+60.0
    mapped_b = edges_b/factor
    joint = np.zeros((len(edges_a)-1, len(edges_b)-1))
    for i in range(len(edges_a)-1):
        for j in range(len(edges_b)-1):
            joint[i, j] = probability(max(edges_a[i], mapped_b[j]),
                                       min(edges_a[i+1], mapped_b[j+1]))
    joint_mass = float(joint.sum())
    assert abs(joint_mass-1) < 1e-10
    # Fixed accepted sample: restrict all partitions to their common ROI.
    low, high = max(edges_a[0], mapped_b[0]), min(edges_a[-1], mapped_b[-1])
    def clipped(edges):
        return np.r_[low, edges[(edges > low) & (edges < high)], high]
    partition_a = clipped(edges_a)
    partition_b = clipped(mapped_b)
    union = np.unique(np.r_[partition_a, partition_b])
    fa = point_angle_fisher(partition_a)
    fb = point_angle_fisher(partition_b)
    fu = point_angle_fisher(union)
    assert np.linalg.eigvalsh(fu-fa).min() > -1e-7
    assert np.linalg.eigvalsh(fu-fb).min() > -1e-7
    # Replays may improve the coarse partition; counting them independently
    # still overstates information in this example.
    assert np.linalg.eigvalsh(fa+fb-fu).min() > 0
    p_a, p_b = joint.sum(axis=1), joint.sum(axis=0)
    cross = event_count*joint
    replay_covariance = np.block([[np.diag(event_count*p_a), cross],
                                  [cross.T, np.diag(event_count*p_b)]])
    count_difference = np.r_[np.ones(len(p_a)), -np.ones(len(p_b))]
    count_sum = np.ones(len(p_a)+len(p_b))
    difference_variance = float(count_difference @ replay_covariance @ count_difference)
    sum_variance = float(count_sum @ replay_covariance @ count_sum)
    independent_sum_variance = 2*event_count*joint_mass
    assert abs(difference_variance) < 1e-8
    assert abs(sum_variance-4*event_count*joint_mass) < 1e-8
    assert np.linalg.eigvalsh(replay_covariance).min() > -1e-8

    return dict(schema_version=1, kind="synthetic shared-event covariance and replay information",
                source_inspiration="BC84 fixedN/Poisson observation distinction; event-mark formulas are our inference",
                chosen_parameters=dict(mean_or_fixed_event_count=event_count,
                                       one_photon_per_event=True, gate_a_keV=gate_a,
                                       gate_b_keV=gate_b, angle_deg=ANGLE,
                                       repeats=repeats, seed=131430),
                overlapping_gate_controls=dict(gate_probabilities=[pa, pb], overlap_probability=pab,
                                               Poisson_expected_covariance=poisson_cov.tolist(),
                                               fixedN_expected_covariance=fixed_cov.tolist(),
                                               Poisson_MC_covariance=empirical_poisson.tolist(),
                                               fixedN_MC_covariance=empirical_fixed.tolist()),
                disjoint_control=dict(Poisson_cross_covariance=float(poisson_disjoint[0, 1]),
                                      fixedN_cross_covariance=float(fixed_disjoint[0, 1])),
                reference_replays=dict(reference_betas=[beta_reference_a, beta_reference_b],
                                       deterministic_energy_factor=factor,
                                       joint_probability_mass=joint_mass,
                                       common_raw_energy_ROI_keV=[float(low), float(high)],
                                       partition_bins=[len(partition_a)-1, len(partition_b)-1, len(union)-1],
                                       local_A_errors=local_errors(fa),
                                       local_B_errors=local_errors(fb),
                                       refined_union_errors=local_errors(fu),
                                       incorrectly_independent_A_plus_B_errors=local_errors(fa+fb),
                                       replay_total_difference_variance=difference_variance,
                                       replay_total_sum_variance=sum_variance,
                                       incorrectly_independent_sum_variance=independent_sum_variance),
                verification=dict(Poisson_MC_covariance_relative_error=poisson_error,
                                  fixedN_MC_covariance_relative_error=fixed_error,
                                  disjoint_thinning_vs_fixedN_passed=True,
                                  deterministic_replay_cross_covariance_passed=True,
                                  union_partition_information_refinement_passed=True,
                                  independent_replay_information_overcount_control_passed=True,
                                  all_passed=True),
                dependencies=dict(binning_script_sha256=hashlib.sha256(
                    Path(bins.__file__).read_bytes()).hexdigest()),
                boundaries=["One photon/event, known kernel/point angle and fixed selection/reference choices are chosen.",
                            "Multiphoton cascades, weighted events, background subtraction and real gate selection need their event marks.",
                            "Fisher errors are local design values at known response/feeding, not observed lifetime intervals.",
                            "Joint deterministic partitions can recover information lost in one coarse view; they add no new raw events.",
                            "The union result assumes common sample and monotone energy mappings with known paired event identity.",
                            "This does not identify an independence error in any source's actual spectrum processing."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"verification": result["verification"],
                      "gates": result["overlapping_gate_controls"],
                      "replays": result["reference_replays"]}))


if __name__ == "__main__":
    main()
