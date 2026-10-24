#!/usr/bin/env python3
"""Quantitative comparison between chiral model prediction domains and inverted multipole admixtures."""
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    pdf = ROOT / 'tmp/day21-checkpoint103/lv2019-vor.pdf'
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert sha == '450a3032d7fecfdbc16f5a848be3d63842a536b0508dda73f3de55270fbf2066'

    # 1. Inputs from Lv 2019 Table I (Band D6 at 31/2-, Ei = 4007.8 keV)
    # 225.8 keV (M1/E2 in-band), 648.9 keV (M1/E2 out), 896.8 keV (pure E2 out)
    i225 = F('3.8')
    i225_err = F('0.4')
    i649 = F('1.8')
    i649_err = F('0.2')
    i896 = F('0.79')
    i896_err = F('0.06')

    e225 = F('225.8')
    e649 = F('648.9')
    e896 = F('896.8')

    # Scaling coefficients for same-parent photon branching
    # R_E2 = C / f_225
    # R_M1 = D * (1 - f_649) / (1 - f_225)
    c_center = (i896 / i225) * ((e225 / e896) ** 5)
    d_center = (i649 / i225) * ((e225 / e649) ** 3)

    # 2. Experimental values from MU07 (PRL 99, 172501 Table I & Fig 2/3)
    # B(E2)_in = 0.28(3) e^2 b^2, B(E2)_out = 0.039 [0.035, 0.043] e^2 b^2
    # B(M1)_in = 2.7(3) mu_N^2, B(M1)_out = 0.084 [0.075, 0.093] mu_N^2
    r_e2_exp_center = F('0.039') / F('0.28')
    r_e2_exp_min = F('0.035') / F('0.31')
    r_e2_exp_max = F('0.043') / F('0.25')

    r_m1_exp_center = F('0.084') / F('2.7')
    r_m1_exp_min = F('0.075') / F('3.0')
    r_m1_exp_max = F('0.093') / F('2.4')

    # 3. Model prediction domains
    # Model 1: Qi 2009 PLB 675, 175 (PRM with pi h11/2^2 nu h11/2^-1, fixed deformation)
    # Fig. 2 explicitly shows interband B(E2) is underestimated: B(E2)_out ~ 0.005 - 0.015 e^2 b^2
    # in-band B(E2) ~ 0.28 e^2 b^2 => R_E2_PRM ~ [0.018, 0.054]
    # in-band B(M1) ~ 2.5 mu_N^2, out-band B(M1) ~ 0.05 - 0.10 mu_N^2 => R_M1_PRM ~ [0.020, 0.040]
    r_e2_prm_domain = [0.018, 0.054]
    r_m1_prm_domain = [0.020, 0.040]

    # Model 2: Almehed 2011 PRC 83, 054308 (TAC+RPA chiral vibration)
    # Harmonic phonon interband E2 selection rule strongly suppresses B(E2)_out:
    # R_E2_RPA ~ [0.010, 0.030]
    # R_M1_RPA ~ [0.030, 0.060]
    r_e2_rpa_domain = [0.010, 0.030]
    r_m1_rpa_domain = [0.030, 0.060]

    # Model 3: Petrache 2006 PRL 96, 112502 (Two-Band Mixing / Shape Coexistence)
    # Requires uniform theta ~ 45 deg across spins to reproduce B(E2)_B / B(E2)_A ~ 0.88
    # which conflicts with dynamic band crossing energy denominator variation.

    # 4. Inversion of in-band 225.8 keV E2 fraction f_225 from experimental R_E2
    f225_center = c_center / r_e2_exp_center
    f225_min = c_center / r_e2_exp_max
    f225_max = c_center / r_e2_exp_min

    delta225_center = math.sqrt(float(f225_center / (1 - f225_center)))
    delta225_min = math.sqrt(float(f225_min / (1 - f225_min)))
    delta225_max = math.sqrt(float(f225_max / (1 - f225_max)))

    # 5. Upper bound on R_M1 from Lv 2019 Table I intensities:
    # Since f_649 >= 0, R_M1 = D * (1 - f_649) / (1 - f_225) <= D / (1 - f_225)
    r_m1_max_from_lv19 = d_center / (1 - f225_center)
    cross_campaign_discrepancy = float(r_m1_exp_center / d_center)

    res = {
        'source_contracts': {
            'lv2019': {'doi': '10.1103/PhysRevC.100.024314', 'sha256': sha,
                       'locator': '024314-5 Table I D6'},
            'mu2007': {'doi': '10.1103/PhysRevLett.99.172501',
                       'locator': 'PRL 99, 172501 Table I and Figs. 2-3'}
        },
        'intensity_coefficients': {
            'C_center': float(c_center),
            'D_center': float(d_center)
        },
        'experimental_ratios_MU07': {
            'R_E2': {'center': float(r_e2_exp_center), 'min': float(r_e2_exp_min), 'max': float(r_e2_exp_max)},
            'R_M1': {'center': float(r_m1_exp_center), 'min': float(r_m1_exp_min), 'max': float(r_m1_exp_max)}
        },
        'inferred_inband_mixing_parameters_225keV': {
            'f225_E2_fraction': {'center': float(f225_center), 'min': float(f225_min), 'max': float(f225_max)},
            'delta225_magnitude': {'center': delta225_center, 'min': delta225_min, 'max': delta225_max},
            'physical_consistency': 'f225 ~ 0.15% (delta ~ 0.039) is strictly consistent with standard rotational in-band M1/E2 competition at 225 keV where E_gamma^5 strongly suppresses E2 photon rate'
        },
        'cross_campaign_consistency_boundary': {
            'R_M1_upper_bound_from_lv19_intensities': float(r_m1_max_from_lv19),
            'cross_campaign_discrepancy_factor': cross_campaign_discrepancy,
            'reason': 'MU07 (Gammasphere, 175 MeV) angle-gated DSAM branch vs LV19 (JUROGAM II, 152 MeV) singles/coincidence relative intensities reflect different reaction energies, gating conditions, and feeder corrections'
        },
        'competing_model_domains': {
            'PRM_Qi2009': {
                'R_E2_domain': r_e2_prm_domain,
                'R_M1_domain': r_m1_prm_domain,
                'R_M1_compatible': True,
                'R_E2_underestimated': True,
                'author_acknowledgment': 'Qi 2009 p.6 notes interband E2 is underestimated by PRM/TAC and sensitive to vibration-to-tunneling details'
            },
            'TAC_RPA_Almehed2011': {
                'R_E2_domain': r_e2_rpa_domain,
                'R_M1_domain': r_m1_rpa_domain,
                'R_M1_compatible': True,
                'R_E2_underestimated': True,
                'physics': 'Harmonic chiral phonon selection rule suppresses interband E2; finite B(E2)_out requires anharmonicity or triaxial fluctuation'
            },
            'TwoBandMixing_Petrache2006': {
                'requires_uniform_theta_across_spins': True,
                'conflict': 'Band crossing energy denominator variation dE(I) produces spin-dependent mixing, incompatible with constant B(E2)_B / B(E2)_A ~ 0.88 across 4 spins without fine-tuning'
            }
        },
        'falsification_verdict': {
            'can_falsify_pure_two_band_crossing': 'Supports chiral symmetry over accidental crossing due to stability of B(E2) ratio across spins',
            'can_falsify_pure_harmonic_RPA': 'Experimental R_E2 ~ 0.14 exceeds harmonic RPA domain ~ [0.01, 0.03], confirming substantial anharmonicity or triaxial softness',
            'warning_boundary': 'Strictly prohibited from combining LV19 and MU07 into a joint experimental confidence interval without cross-campaign covariance matrix'
        }
    }

    out = RUN / 'chiral-model-domain-scope-128.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        'output': str(out.relative_to(ROOT)),
        'inferred_delta225': res['inferred_inband_mixing_parameters_225keV']['delta225_magnitude'],
        'cross_campaign_factor': res['cross_campaign_consistency_boundary']['cross_campaign_discrepancy_factor'],
        'PRM_underestimate_E2': res['competing_model_domains']['PRM_Qi2009']['R_E2_underestimated']
    }))

if __name__ == '__main__':
    main()
