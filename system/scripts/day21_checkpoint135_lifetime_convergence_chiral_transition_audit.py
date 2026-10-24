#!/usr/bin/env python3
"""Quantitative audit of lifetime ratio convergence from vibrational asymmetry (tau_B/tau_A ~ 2) to tunneling symmetry (tau_B/tau_A ~ 1.09) in 135Nd."""
from fractions import Fraction as F
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # Mukhopadhyay 2007 Table I: Lifetimes in ps
    spins = ["31/2-", "33/2-", "35/2-", "37/2-", "39/2-"]

    tau_a = [0.75, 0.44, 0.28, 0.23, 0.22]
    tau_a_err = [0.04, 0.03, 0.03, 0.03, 0.03]

    tau_b = [1.46, 0.87, 0.64, 0.48, 0.24]
    tau_b_err = [0.02, 0.06, 0.05, 0.03, 0.03]

    # 1. Lifetime ratio tau_B / tau_A
    r_tau = []
    r_tau_err = []
    for i in range(len(spins)):
        r = tau_b[i] / tau_a[i]
        # Standard propagation assuming uncorrelated
        rel_err = math.sqrt((tau_b_err[i]/tau_b[i])**2 + (tau_a_err[i]/tau_a[i])**2)
        r_tau.append(r)
        r_tau_err.append(r * rel_err)

    mean_vibrational_r_tau = sum(r_tau[:4]) / 4.0
    tunneling_r_tau = r_tau[4]

    # Ratio drop factor from vibrational plateau to tunneling point
    drop_factor = mean_vibrational_r_tau / tunneling_r_tau

    # 2. Total decay widths Gamma = hbar / tau (hbar = 0.6582119569 ps*meV = 6.582e-4 ps*keV = 6.58212e-13 meV*s)
    hbar_ps_keV = 0.6582119569e-3  # keV * ps
    gamma_a_keV = [hbar_ps_keV / t for t in tau_a]
    gamma_b_keV = [hbar_ps_keV / t for t in tau_b]

    # Width difference Gamma_A - Gamma_B
    gamma_diff = [gamma_a_keV[i] - gamma_b_keV[i] for i in range(len(spins))]

    res = {
        "source": {
            "doi": "10.1103/PhysRevLett.99.172501",
            "locator": "PRL 99, 172501 Table I",
            "nucleus": "135Nd"
        },
        "spins": spins,
        "tau_BandA_ps": tau_a,
        "tau_BandB_ps": tau_b,
        "lifetime_ratios_tauB_over_tauA": r_tau,
        "lifetime_ratio_uncertainties": r_tau_err,
        "regime_characterization": {
            "vibrational_regime_spins": spins[:4],
            "vibrational_mean_tau_ratio": mean_vibrational_r_tau,
            "vibrational_dispersion": [min(r_tau[:4]), max(r_tau[:4])],
            "tunneling_regime_spin": spins[4],
            "tunneling_tau_ratio": tunneling_r_tau,
            "convergence_drop_factor": drop_factor
        },
        "total_decay_widths_keV": {
            "BandA": gamma_a_keV,
            "BandB": gamma_b_keV,
            "difference_GammaA_minus_GammaB_keV": gamma_diff
        },
        "physical_interpretation": {
            "vibrational_regime": "At low spin (31/2- to 37/2-), Band A is the 0-phonon state and Band B is the 1-phonon state. The 1-phonon excitation introduces asymmetric phase-space and decay paths, yielding tau_B / tau_A ~ 2.0 while in-band core deformation remains symmetric.",
            "tunneling_regime": "At spin 39/2-, the chiral barrier separates left- and right-handed configurations. The physical states become the parity-doublet tunneling states (|L> +- |R>)/sqrt(2), which possess strictly symmetric intrinsic decay channels to lower states, causing tau_B / tau_A to converge sharply to 1.09 +- 0.19 (~ 1.0).",
            "resolution_of_paradox": "This proves that the factor-of-2 lifetime difference at low spin and the sudden restoration of lifetime equality at 39/2- are two complementary faces of the same physical transition from chiral vibration to static chiral tunneling."
        }
    }

    out = RUN / 'lifetime-convergence-scope-135.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "vibrational_mean_ratio": mean_vibrational_r_tau,
        "tunneling_ratio": tunneling_r_tau,
        "drop_factor": drop_factor
    }))

if __name__ == '__main__':
    main()
