#!/usr/bin/env python3
"""Roy Table 1 printed inputs, with explicit finite-difference spin centers.

This is rounded-input arithmetic, not a new DSAM fit. No covariance or gamma
energy errors are supplied here; no confidence intervals are generated.
"""
import json
from pathlib import Path


def main():
    spins = [16, 18, 20, 22, 24]
    gamma_keV = [1075, 1224, 1323, 1314, 1358]
    tau_ps = [0.36, 0.23, 0.17, 0.21, 0.27]
    be2 = [0.14, 0.12, 0.11, 0.09, 0.06]
    be2_errors = [0.01, 0.02, 0.02, 0.03, 0.02]
    transitions = []
    for i, spin in enumerate(spins):
        # For a single pure E2 branch of unit branching and negligible conversion:
        # B(E2)[e2 b2] = 0.0816 / (E_gamma[MeV]^5 tau[ps]).
        pure = 0.0816 / ((gamma_keV[i] / 1000) ** 5 * tau_ps[i])
        transitions.append({
            "I_initial": spin, "E_gamma_keV": gamma_keV[i],
            "tau_mean_ps": tau_ps[i], "BE2_reported_e2b2": be2[i],
            "BE2_reported_error_e2b2": be2_errors[i],
            "BE2_unit_branch_negligible_conversion_e2b2": pure,
            "assumption": "No conversion/branch correction; printed rounded lifetime."
        })
    intervals = []
    for i in range(len(spins) - 1):
        difference = (gamma_keV[i + 1] - gamma_keV[i]) / 1000
        j2 = 4 / difference
        mean_be2 = (be2[i] + be2[i + 1]) / 2
        intervals.append({
            "transition_initial_spins": spins[i:i + 2],
            "I_center": (spins[i] + spins[i + 1]) / 2 - 1,
            "hbar_omega_center_MeV": (gamma_keV[i] + gamma_keV[i + 1]) / 4000,
            "delta_Egamma_keV": gamma_keV[i + 1] - gamma_keV[i],
            "J2_hbar2_per_MeV": j2,
            "BE2_arithmetic_mean_e2b2": mean_be2,
            "J2_over_mean_BE2": j2 / mean_be2,
            "interpretation": "Negative finite difference retained; smooth rotor approximation fails here."
                if difference < 0 else "Finite difference of rounded energies; no uncertainty propagation."
        })
    data = {
        "evidence_status": "direct-table-input-plus-conditional-arithmetic",
        "source": "Roy et al., Phys. Lett. B 694 (2011) 322-326, Table 1 p324",
        "raw_sha256": "2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a",
        "transitions": transitions,
        "finite_difference_intervals": intervals,
        "spin_convention": "hbar omega(I-1)=Egamma(I->I-2)/2; derivative centers lie between those I-1 values.",
        "ratio_convention": "Mean of adjacent transition B(E2), explicitly interpolated; not a separately measured B(E2) at I_center.",
        "limitations": "Quoted Table 1 errors omit stopping-power systematic uncertainty up to 20%. No universal AMR threshold or mode certification."
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
