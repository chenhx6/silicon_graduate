#!/usr/bin/env python3
"""Synthetic Day13 recoil-stage exercise with exact four-vector conservation.

Case A: one isotropic neutron precedes the target gamma. Correction by the
compound-nucleus velocity retains a calculable recoil box distribution;
using the actual post-neutron gamma-emitter velocity removes it.
Case B: a gamma precedes an unobserved neutron. The same observed photon and
terminal residue plus a known initial invariant mass still permit different
initial velocities if the intermediate level is unspecified.
This is not a simulation/refit of Al-Adili, Crespi, VAMOS or A~130 experiments.
Ground masses A*u are illustrative free-nucleus approximations. No material
energy loss, evaporation-temperature distribution, alignment or response.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


U_MEV = 931.49410242
NEUTRON_MEV = 939.56542052


def boost(p4: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """Active boost from rest coordinates; p4 may be a batch of rows."""
    beta = np.asarray(beta, dtype=float)
    b2 = float(beta @ beta)
    if b2 == 0:
        return p4.copy()
    gamma = 1 / math.sqrt(1 - b2)
    bp = p4[..., 1:] @ beta
    energy = gamma * (p4[..., 0] + bp)
    momentum = p4[..., 1:] + (((gamma - 1) * bp / b2 + gamma * p4[..., 0])[..., None] * beta)
    return np.concatenate((energy[..., None], momentum), axis=-1)


def invariant2(p4: np.ndarray) -> np.ndarray:
    return p4[..., 0]**2 - np.sum(p4[..., 1:]**2, axis=-1)


def directions(rng: np.random.Generator, size: int) -> np.ndarray:
    u = rng.uniform(-1, 1, size)
    phi = rng.uniform(0, 2*math.pi, size)
    return np.column_stack((np.sqrt(1-u*u)*np.cos(phi), np.sqrt(1-u*u)*np.sin(phi), u))


def calculate() -> dict:
    rng = np.random.default_rng(131014)
    samples = 250000
    neutron_t = 2.
    neutron_e = NEUTRON_MEV + neutron_t
    neutron_p = math.sqrt(neutron_t * (2*NEUTRON_MEV + neutron_t))
    cases = []
    max_conservation, max_inverse, max_sigma_difference = 0., 0., 0.
    for a in (12., 52., 130.):
        ground = a * U_MEV
        emitter_mass = ground + 1.
        emitter_e_cn = math.hypot(emitter_mass, neutron_p)
        compound_mass = neutron_e + emitter_e_cn
        recoil_beta = neutron_p / emitter_e_cn
        recoil_gamma = emitter_e_cn / emitter_mass
        photon_rest = (2*ground + 1.) / (2*emitter_mass)
        # Fix neutron +z in CN frame. Isotropic photons in the recoiling
        # emitter frame make the relative angle isotropic; an arbitrary
        # neutron orientation gives the same CN-corrected distribution.
        gamma_direction = directions(rng, samples)
        photon4_rest = np.column_stack((np.full(samples, photon_rest), photon_rest * gamma_direction))
        photon4_cn = boost(photon4_rest, np.array([0., 0., -recoil_beta]))
        mean_analytic = recoil_gamma * photon_rest
        sigma_analytic = photon_rest * neutron_p / (math.sqrt(3) * emitter_mass)
        sigma_mc = float(np.std(photon4_cn[:, 0]))
        rel = abs(sigma_mc / sigma_analytic - 1)
        max_sigma_difference = max(max_sigma_difference, rel)
        observations = []
        # Four-vector-conserving replay uses a handful of angles; Monte Carlo
        # above is an independent check of the exact recoil distribution.
        for cn_beta in (0., .016, .07, .3):
            lab_boost = np.array([0., 0., cn_beta])
            compound4 = boost(np.array([compound_mass, 0., 0., 0.]), lab_boost)
            neutron4 = boost(np.array([neutron_e, 0., 0., neutron_p]), lab_boost)
            emitter4 = boost(np.array([emitter_e_cn, 0., 0., -neutron_p]), lab_boost)
            for cosine in (-1., 0., 1.):
                photon4 = np.array([photon_rest, photon_rest*math.sqrt(1-cosine*cosine), 0., photon_rest*cosine])
                photon_cn = boost(photon4, np.array([0., 0., -recoil_beta]))
                photon_lab = boost(photon_cn, lab_boost)
                daughter_lab = emitter4 - photon_lab
                residual = float(np.max(np.abs(compound4-neutron4-emitter4)))
                residual = max(residual, abs(float(invariant2(daughter_lab))/ground**2-1)*ground)
                max_conservation = max(max_conservation, residual)
                recovered = boost(photon_lab, -emitter4[1:]/emitter4[0])[0]
                cn_corrected = boost(photon_lab, -lab_boost)[0]
                max_inverse = max(max_inverse, abs(recovered-photon_rest), abs(cn_corrected-photon_cn[0]))
                if cn_beta == .07:
                    observations.append({"photon_emitter_rest_cos_theta": cosine,
                                         "CN_beta": cn_beta, "true_emitter_lab_beta_z": emitter4[3]/emitter4[0],
                                         "CN_corrected_keV": cn_corrected*1000,
                                         "emitter_corrected_keV": recovered*1000})
        cases.append({"approx_ground_A": a, "source_boundary": "A and Tn are illustrative, not source fit parameters",
                      "neutron_T_in_CN_MeV": neutron_t, "emitter_excitation_gap_MeV": 1.,
                      "parent_rest_photon_keV": photon_rest*1000,
                      "recoil_beta_in_CN": recoil_beta,
                      "CN_corrected_mean_bias_keV": (mean_analytic-photon_rest)*1000,
                      "CN_corrected_sigma_keV": sigma_analytic*1000,
                      "CN_corrected_sigma_MC_keV": sigma_mc*1000,
                      "relative_sigma_MC_difference": rel,
                      "CN_corrected_box_half_range_keV": photon_rest*neutron_p/emitter_mass*1000,
                      "illustrative_n4_fixed_mass_independent_isotropic_sigma_keV": 2*sigma_analytic*1000,
                      "exact_replay": observations})
    # Case B: fix observed terminal residue and photon in their joint rest
    # frame, then choose different unobserved neutron directions. Known Mi
    # fixes q's energy through (C+q)^2=Mi^2 but leaves its direction free.
    terminal_mass = 130 * U_MEV
    observed_photon4 = np.array([1., 0., 0., 1.])
    terminal4 = np.array([math.hypot(terminal_mass, 1.), 0., 0., -1.])
    visible4 = observed_photon4 + terminal4
    visible_mass = visible4[0]
    initial_mass = visible_mass + NEUTRON_MEV + 2.
    neutron_e_missing = NEUTRON_MEV + 2. + (2*NEUTRON_MEV+2.)/visible_mass
    missing_p = math.sqrt((neutron_e_missing-NEUTRON_MEV)*(neutron_e_missing+NEUTRON_MEV))
    alternatives = []
    for cosine in (-1., 0., 1.):
        missing4 = np.array([neutron_e_missing, missing_p*math.sqrt(1-cosine*cosine), 0., missing_p*cosine])
        initial4 = visible4 + missing4
        intermediate4 = initial4 - observed_photon4
        actual_initial_mass = math.sqrt(float(invariant2(initial4)))
        gamma_in_initial = boost(observed_photon4, -initial4[1:]/initial4[0])[0]
        assert abs(actual_initial_mass-initial_mass) < 1e-8
        assert math.sqrt(float(invariant2(intermediate4))) > terminal_mass + NEUTRON_MEV
        alternatives.append({"missing_neutron_cos_to_observed_gamma": cosine,
                             "known_initial_mass_MeV": initial_mass,
                             "initial_lab_beta_vector": (initial4[1:]/initial4[0]).tolist(),
                             "gamma_in_initial_rest_keV": gamma_in_initial*1000,
                             "unspecified_intermediate_mass_MeV": math.sqrt(float(invariant2(intermediate4))),
                             "boundary": "observed photon and terminal residue are identical; the intermediate level is not fixed"})
    assert max_sigma_difference < .006
    assert max_conservation < 1e-7
    assert max_inverse < 1e-10
    assert alternatives[0]["gamma_in_initial_rest_keV"] > alternatives[2]["gamma_in_initial_rest_keV"]
    return {"schema_version": 1, "kind": "synthetic recoil-stage/conservation exercise; no experimental refit",
            "neutron_before_gamma": cases, "neutron_after_gamma_same_visible_counterexample": alternatives,
            "boundaries": ["Case A applies to unmeasured recoil vectors, not a residual ion with correctly reconstructed emitter velocity.",
                           "Case B is a conditional late-particle/unknown-intermediate-level counterexample; it is not asserted for the low-lying bound lines of Klemme or VAMOS.",
                           "Fixed known intermediate levels, independent particles or kinematic constraints can reduce the Case B ambiguity.",
                           "n=4 variance is a leading fixed-mass independent-isotropic illustration, not an exact sequential evaporation calculation."],
            "verification": {"four_momentum_and_mass_shell_passed": True,
                             "max_conservation_scale_residual_MeV": max_conservation,
                             "exact_rest_energy_inverse_max_error_MeV": max_inverse,
                             "max_MC_sigma_relative_difference": max_sigma_difference,
                             "same_visible_known_initial_mass_counterexample_passed": True,
                             "passed": True}, "numpy_version": np.__version__}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verification": result["verification"],
                      "sigma_recoil_keV": [x["CN_corrected_sigma_keV"] for x in result["neutron_before_gamma"]]}))


if __name__ == "__main__":
    main()
