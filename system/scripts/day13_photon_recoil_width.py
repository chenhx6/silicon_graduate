#!/usr/bin/env python3
"""Two-body photon recoil and evaluated-level width exercises for Day13.

Mass-number masses approximate free ground-state nuclear rest masses. Source
widths are TUNL online Tables12.13/12.14 central values, not a fresh measurement.
Lattice recoil-free effects, finite resonance population profiles and actual
analysis response/covariance are absent.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


U_MEV = 931.49410242
HBAR_KEV_PS = 6.582119569e-7


def boost_z(energy, momentum, beta):
    gamma = 1 / math.sqrt(1 - beta**2)
    return gamma * (energy + beta * momentum[2]), np.array([
        momentum[0], momentum[1], gamma * (momentum[2] + beta * energy)])


def calculate():
    cases, maximum_momentum_residual, maximum_energy_inverse = [], 0., 0.
    for mass_a, excitation in ((12., 15.110), (12., 4.43982), (32., 2.23057), (52., 1.434), (130., 1.)):
        mf = mass_a * U_MEV
        mi = mf + excitation
        photon = excitation * (2 * mf + excitation) / (2 * mi)
        daughter_energy_rest = mi - photon
        assert abs(daughter_energy_rest**2 - photon**2 - mf**2) / mf**2 < 1e-12
        observations = []
        for beta in (0., .016, .07, .3, .5):
            for theta_deg in (0, 45, 90, 135, 180):
                theta = math.radians(theta_deg)
                photon_rest_p = photon * np.array([math.sin(theta), 0., math.cos(theta)])
                ep, pp = boost_z(mi, np.zeros(3), beta)
                eg, pg = boost_z(photon, photon_rest_p, beta)
                ef, pf = boost_z(daughter_energy_rest, -photon_rest_p, beta)
                conservation = max(abs(ep - eg - ef), float(np.max(np.abs(pp - pg - pf))))
                maximum_momentum_residual = max(maximum_momentum_residual, conservation)
                gamma_parent = 1 / math.sqrt(1 - beta**2)
                corrected_parent = gamma_parent * (eg - beta * pg[2])
                beta_daughter = pf / ef
                corrected_daughter = ef / mf * (eg - float(np.dot(beta_daughter, pg)))
                expected_daughter = photon * mi / mf
                maximum_energy_inverse = max(maximum_energy_inverse,
                                             abs(corrected_parent - photon),
                                             abs(corrected_daughter - expected_daughter))
                assert abs(corrected_parent - photon) < 1e-10
                assert abs(corrected_daughter - expected_daughter) < 1e-10
                if beta == .07 and theta_deg in (0, 90, 180):
                    observations.append({"parent_lab_beta": beta, "rest_emission_theta_deg": theta_deg,
                                         "photon_lab_MeV": eg, "daughter_lab_beta_vector": beta_daughter.tolist(),
                                         "parent_frame_corrected_MeV": corrected_parent,
                                         "daughter_frame_corrected_MeV": corrected_daughter})
        cases.append({"mass_number_approx": mass_a, "excitation_gap_MeV": excitation,
                      "ground_mass_approx_MeV": mf, "parent_photon_MeV": photon,
                      "photon_recoil_energy_keV": (excitation - photon) * 1000,
                      "daughter_frame_photon_MeV": photon * mi / mf,
                      "daughter_frame_minus_parent_frame_keV": photon * (mi / mf - 1) * 1000,
                      "illustrative_boost_observations": observations})
    # Total width, total gamma width, one gamma branch, and a radiative-subset
    # branching fraction have different denominators and shared source inputs.
    total_ev, total_gamma_ev, ground_gamma_ev = 43.6, 41.8, 38.5
    partials = [38.5, .96, 1.09, 1.60, .59]
    width = {"source": "TUNL2017KE05 online Tables12.13/12.14; companion manuscript revised08Oct2020",
             "level_Ex_MeV": 15.110, "total_width_eV": total_ev,
             "total_gamma_width_eV": total_gamma_ev, "ground_gamma_partial_width_eV": ground_gamma_ev,
             "mean_tau_ps_from_total_width": HBAR_KEV_PS / (total_ev / 1000),
             "mean_tau_as_from_total_width": HBAR_KEV_PS / (total_ev / 1000) * 1e6,
             "ground_branch_among_gamma_central": ground_gamma_ev / total_gamma_ev,
             "ground_branch_among_all_decay_central": ground_gamma_ev / total_ev,
             "gamma_fraction_among_all_decay_central": total_gamma_ev / total_ev,
             "printed_gamma_partial_sum_eV": sum(partials),
             "printed_partial_sum_minus_printed_total_gamma_eV": sum(partials) - total_gamma_ev,
             "wrong_tau_using_ground_partial_over_tau_total": total_ev / ground_gamma_ev,
             "boundary": "central quotients only; deduced widths/branches share inputs, covariance unknown; printed partial central closure not an error diagnosis"}
    assert abs(cases[0]["photon_recoil_energy_keV"] - 10.2) < .01
    assert maximum_momentum_residual < 1e-8
    assert maximum_energy_inverse < 1e-10
    assert width["ground_branch_among_gamma_central"] > width["ground_branch_among_all_decay_central"]
    return {"schema_version": 1, "kind": "free-nucleus four-momentum and evaluated-width arithmetic; no data refit",
            "photon_recoil_cases": cases, "evaluated_width_example": width,
            "verification": {"parent_daughter_photon_four_momentum_conserved": True,
                             "daughter_mass_shell_passed": True, "two_rest_frame_energy_inverses_passed": True,
                             "max_four_momentum_residual_MeV": maximum_momentum_residual,
                             "max_energy_inverse_error_MeV": maximum_energy_inverse, "passed": True},
            "numpy_version": np.__version__}


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
