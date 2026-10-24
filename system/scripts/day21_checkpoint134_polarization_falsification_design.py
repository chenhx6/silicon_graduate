#!/usr/bin/env python3
"""Quantitative design for falsification of 135Nd chirality via 225.8 keV linear polarimetry."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # 225.8 keV transition: 31/2- (4007.8 keV) -> 29/2- (3782.0 keV)
    # Chiral partner prediction from Checkpoints 128-129:
    # delta ~ 0.0389, f_E2 ~ 0.00151 (predominantly M1)
    delta_chiral = 0.0389
    f_e2_chiral = delta_chiral**2 / (1.0 + delta_chiral**2)

    # Linear polarization at 90 deg:
    # Pure M1 gives P_M1 ~ -0.40; Pure E2 gives P_E2 ~ +0.50
    P_M1_pure = -0.40
    P_E2_pure = +0.50
    P_chiral = P_M1_pure * (1.0 - f_e2_chiral) + P_E2_pure * f_e2_chiral

    # Competing transverse wobbling / large E2 admixture prediction:
    # delta ~ 1.2, f_E2 ~ 0.59
    delta_wobbling = 1.2
    f_e2_wobbling = delta_wobbling**2 / (1.0 + delta_wobbling**2)
    P_wobbling = P_M1_pure * (1.0 - f_e2_wobbling) + P_E2_pure * f_e2_wobbling

    delta_P = abs(P_wobbling - P_chiral)

    # Compton polarimeter analyzing power at 225.8 keV
    # Klein-Nishina factor Q0 ~ 0.88, finite geometry Q_geom ~ 0.22 (typical for AGATA/CLOVER)
    Q_geom = 0.22

    # Experimental asymmetry A = Q * P
    A_chiral = Q_geom * P_chiral
    A_wobbling = Q_geom * P_wobbling
    delta_A = abs(A_wobbling - A_chiral)

    # Required Compton-scattered counts for 3-sigma and 5-sigma separation
    # delta_A >= n_sigma / sqrt(N) => N >= (n_sigma / delta_A)^2
    N_3sigma = math.ceil((3.0 / delta_A)**2)
    N_5sigma = math.ceil((5.0 / delta_A)**2)

    # Beam-time estimation on JUROGAM III / AGATA at JYFL:
    # 100Mo(40Ar, 5n)135Nd at 152 MeV
    # 2 pnA beam on 0.5 mg/cm^2 target => rxn rate ~ 1.88 kHz
    # 225.8 keV line intensity in array ~ 37.6 pps
    # Coincidence Compton polarimetry efficiency ~ 0.03% => event rate ~ 40.6 events/hour
    rate_per_hour = 40.6
    hours_3sigma = N_3sigma / rate_per_hour
    hours_5sigma = N_5sigma / rate_per_hour

    res = {
        "transition": {
            "nucleus": "135Nd",
            "initial_state": "31/2- (4007.8 keV)",
            "final_state": "29/2- (3782.0 keV)",
            "energy_keV": 225.8,
            "multipolarity": "M1 + E2"
        },
        "inferred_chiral_prediction": {
            "mixing_ratio_delta": delta_chiral,
            "f_E2_fraction": f_e2_chiral,
            "linear_polarization_P": P_chiral,
            "asymmetry_A": A_chiral
        },
        "competing_wobbling_prediction": {
            "mixing_ratio_delta": delta_wobbling,
            "f_E2_fraction": f_e2_wobbling,
            "linear_polarization_P": P_wobbling,
            "asymmetry_A": A_wobbling
        },
        "polarimeter_sensitivity": {
            "Compton_analyzing_power_Q": Q_geom,
            "asymmetry_difference_delta_A": delta_A
        },
        "exposure_and_count_budget": {
            "N_events_3sigma": N_3sigma,
            "N_events_5sigma": N_5sigma,
            "estimated_polarimeter_rate_events_per_hour": rate_per_hour,
            "beam_time_hours_3sigma": hours_3sigma,
            "beam_time_hours_5sigma": hours_5sigma,
            "feasibility_assessment": "3-sigma discrimination requires ~17 hours of beam time, and 5-sigma definitive falsification requires ~46 hours (under 2 days) on standard AGATA/JUROGAM-type arrays."
        },
        "falsification_criterion": {
            "conclusive_falsification_signal": "Observing positive linear polarization P > 0 (A > 0) in the 225.8 keV line at >3sigma significance conclusively falsifies the in-band M1-dominant chiral doublet interpretation, ruling out the entire low-spin chiral vibration manifold for Band D6."
        }
    }

    out = RUN / 'polarization-falsification-scope-134.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "delta_A": delta_A,
        "N_3sigma": N_3sigma,
        "hours_3sigma": hours_3sigma,
        "hours_5sigma": hours_5sigma
    }))

if __name__ == '__main__':
    main()
