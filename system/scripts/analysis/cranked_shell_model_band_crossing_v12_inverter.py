#!/usr/bin/env python3
"""
cranked_shell_model_band_crossing_v12_inverter.py
=================================================
Cranked Shell Model (CSM) Two-Band Mixing, Avoided Crossing Routhians e'(omega),
Interaction Matrix Element |V_12| Inverter & Backbending vs Upbending Classifier.

Physics & Formulation:
----------------------
1. Cranked Shell Model (CSM) & Routhians:
   In the rotating intrinsic coordinate frame with angular frequency omega = dE / dI_x:
   The total Routhian e'(omega) is related to lab energy E and aligned angular momentum I_x:
     e'(omega) = E(I) - omega * I_x(I)
     i_x(omega) = - de' / domega = I_x(omega) - I_x_ref(omega)
   where the Harris two-parameter reference core is:
     I_x_ref(omega) = J_0 * omega + (1/3) * J_1 * omega^3

2. Two-Band Crossing Model (Bengtsson & Frauendorf 1979):
   At the crossing frequency omega_c, the ground-state band (g-band, |1>, alignment i_1 ~ 0)
   crosses the aligned Stockholm band (s-band, |2>, broken high-j pair with alignment i_2):
     Unperturbed diabatic Routhians:
       e_1'(omega) = - 0.5 * J_0 * omega^2 - 0.25 * J_1 * omega^4
       e_2'(omega) = e_20' - i_2 * omega - 0.5 * J_0 * omega^2
     Crossing frequency condition:
       e_1'(omega_c) = e_2'(omega_c)  =>  e_20' = e_1'(omega_c) + i_2 * omega_c + 0.5 * J_0 * omega_c^2

3. Two-Band Mixing Matrix & Avoided Crossing Splitting:
   The interaction matrix element V_12 couples the two diabatic configurations:
     H_CSM = [[ e_1'(omega),  V_12 ],
              [ V_12,        e_2'(omega) ]]
   The physical adiabatic Routhians are the eigenvalues:
     e_pm'(omega) = 0.5 * (e_1' + e_2') +/- sqrt[ 0.25 * (e_1' - e_2')^2 + V_12^2 ]
   At the exact crossing frequency omega = omega_c (where e_1' = e_2'):
     Delta_e'_min = e_+'(omega_c) - e_-'(omega_c) = 2.0 * |V_12|
   The interaction matrix element is thus directly inverted from the minimum splitting:
     |V_12| = 0.5 * Delta_e'_min

4. Backbending vs Upbending Classification:
   - Weak interaction (|V_12| < 35 keV):
     The Routhians avoid crossing sharply. As spin increases, domega / dI_x becomes negative,
     causing a backward loop in the omega vs I plot (**Backbending**, e.g. 156Dy, 158Er).
   - Strong interaction (|V_12| >= 60 keV):
     The mixing is smooth and gradual. domega / dI_x remains positive everywhere, resulting
     in a smooth upward inflection (**Upbending**, e.g. 164Er, 168Yb).

References:
  - R. Bengtsson and S. Frauendorf, Nucl. Phys. A 327, 139 (1979).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-3.
  - F. S. Stephens, Rev. Mod. Phys. 47, 43 (1975).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_two_band_crossing_csm(
    omega_c_MeV: float = 0.280,
    V12_keV: float = 90.0,
    i_align_hbar: float = 10.0,
    J0_hbar2_MeV: float = 30.0,
    J1_hbar4_MeV3: float = 90.0,
    omega_scan_MeV: Optional[List[float]] = None
) -> Dict[str, Any]:
    """
    Simulates the two-band crossing model, avoided crossing Routhians, configuration mixing,
    and classifies backbending vs upbending.
    """
    if omega_c_MeV <= 0.0 or i_align_hbar <= 0.0:
        raise ValueError("Crossing frequency and alignment must be positive.")
    if V12_keV <= 0.0:
        raise ValueError("Interaction matrix element V12 must be positive.")

    V12_MeV = V12_keV * 1e-3

    # Reference diabatic Routhian at crossing
    e1_c = - 0.5 * J0_hbar2_MeV * (omega_c_MeV ** 2) - 0.25 * J1_hbar4_MeV3 * (omega_c_MeV ** 4)
    e20 = e1_c + i_align_hbar * omega_c_MeV + 0.5 * J0_hbar2_MeV * (omega_c_MeV ** 2)

    if omega_scan_MeV is None:
        omega_scan_MeV = [round(omega_c_MeV + (-0.08 + i * 0.01), 3) for i in range(17)]

    points = []
    domega = 1e-3

    for w in omega_scan_MeV:
        if w <= 0.0:
            continue

        def get_yrast_yrare(omega_val):
            e1 = - 0.5 * J0_hbar2_MeV * (omega_val ** 2) - 0.25 * J1_hbar4_MeV3 * (omega_val ** 4)
            e2 = e20 - i_align_hbar * omega_val - 0.5 * J0_hbar2_MeV * (omega_val ** 2)
            mid = 0.5 * (e1 + e2)
            diff = 0.5 * (e1 - e2)
            rad = math.sqrt(diff ** 2 + V12_MeV ** 2)
            return mid - rad, mid + rad, e1, e2

        e_yr, e_yrar, e1_diab, e2_diab = get_yrast_yrare(w)
        splitting_keV = (e_yrar - e_yr) * 1000.0

        # Mixing angle: tan(2*theta) = V12 / (0.5 * (e1 - e2))
        diff_half = 0.5 * (e1_diab - e2_diab)
        theta = 0.5 * math.atan2(V12_MeV, diff_half)
        g_band_prob = (math.cos(theta)) ** 2
        s_band_prob = (math.sin(theta)) ** 2

        # Numerical derivative for alignment: i_x = - de'/domega - I_x_ref
        e_yr_plus, _, _, _ = get_yrast_yrare(w + domega)
        e_yr_minus, _, _, _ = get_yrast_yrare(w - domega)
        Ix_tot = - (e_yr_plus - e_yr_minus) / (2.0 * domega)
        Ix_ref = J0_hbar2_MeV * w + (1.0 / 3.0) * J1_hbar4_MeV3 * (w ** 3)
        ix_aligned = Ix_tot - Ix_ref

        points.append({
            "omega_MeV": round(w, 3),
            "e_yrast_keV": round(e_yr * 1000.0, 1),
            "e_yrare_keV": round(e_yrar * 1000.0, 1),
            "splitting_keV": round(splitting_keV, 1),
            "g_band_percentage": round(g_band_prob * 100.0, 1),
            "s_band_percentage": round(s_band_prob * 100.0, 1),
            "total_spin_Ix_hbar": round(Ix_tot, 2),
            "aligned_angular_momentum_ix": round(ix_aligned, 2)
        })

    # Critical V12 threshold separating sharp backbending from smooth upbending:
    # V_crit ~ 0.5 * Delta_i * Delta_omega ~ 40 - 50 keV
    V_crit_keV = 45.0
    if V12_keV < 35.0:
        crossing_type = "Sharp Backbending (Weak interaction, S-shaped frequency inflection)"
    elif V12_keV < 65.0:
        crossing_type = "Moderate Backbending / Transitional"
    else:
        crossing_type = "Smooth Upbending (Strong interaction, gradual pair alignment)"

    return {
        "crossing_frequency_omega_c_MeV": omega_c_MeV,
        "V12_interaction_keV": V12_keV,
        "minimum_splitting_Delta_e_keV": round(2.0 * V12_keV, 1),
        "aligned_pair_ix_hbar": i_align_hbar,
        "crossing_classification": crossing_type,
        "profile": points
    }


def invert_v12_from_experimental_routhians(
    omega_list: List[float],
    e_yrast_exp_keV: List[float],
    e_yrare_exp_keV: List[float]
) -> Dict[str, Any]:
    """
    Inverts the interaction matrix element |V_12| from experimental avoided crossing data:
      |V_12| = 0.5 * min( e_yrare - e_yrast ).
    """
    if len(omega_list) != len(e_yrast_exp_keV) or len(omega_list) != len(e_yrare_exp_keV):
        raise ValueError("Input lists must have identical lengths.")

    splittings = [yrar - yr for yr, yrar in zip(e_yrast_exp_keV, e_yrare_exp_keV)]
    min_split = min(splittings)
    min_idx = splittings.index(min_split)
    omega_c_inv = omega_list[min_idx]

    v12_inv_keV = 0.5 * min_split

    classification = "Sharp Backbending" if v12_inv_keV < 35.0 else ("Transitional" if v12_inv_keV < 65.0 else "Smooth Upbending")

    return {
        "inverted_crossing_frequency_omega_c_MeV": round(omega_c_inv, 3),
        "inverted_V12_keV": round(v12_inv_keV, 2),
        "minimum_observed_splitting_keV": round(min_split, 2),
        "classification": classification
    }


def format_text_report(csm_res: Dict[str, Any], inv_res: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 76,
        "   CRANKED SHELL MODEL (CSM) TWO-BAND CROSSING & |V_12| INVERTER",
        "   Based on Bengtsson & Frauendorf (1979) & Bohr & Mottelson Vol. II §4-3",
        "=" * 76,
        " BAND-CROSSING CHARACTERISTICS & INTERACTION STRENGTH:",
        f"   Crossing Frequency hbar*omega_c: {csm_res['crossing_frequency_omega_c_MeV']:.3f} MeV",
        f"   Aligned Angular Momentum Delta_i: {csm_res['aligned_pair_ix_hbar']:.1f} hbar",
        f"   Interaction Matrix Element |V12|: {csm_res['V12_interaction_keV']:.1f} keV",
        f"   Minimum Avoided Splitting     : {csm_res['minimum_splitting_Delta_e_keV']:.1f} keV  (= 2 * |V12|)",
        f"   Crossing Classification       : {csm_res['crossing_classification']}",
        "-" * 76,
    ]

    if inv_res is not None:
        lines.extend([
            " INVERSION FROM EXPERIMENTAL AVOIDED CROSSING ROUTHIANS:",
            f"   Inverted Crossing Frequency   : {inv_res['inverted_crossing_frequency_omega_c_MeV']:.3f} MeV",
            f"   Inverted |V_12| Interaction   : {inv_res['inverted_V12_keV']:.2f} keV",
            f"   Empirical Splitting           : {inv_res['minimum_observed_splitting_keV']:.2f} keV",
            "-" * 76,
        ])

    lines.extend([
        " AVOIDED CROSSING ROUTHIAN PROFILE & CONFIGURATION MIXING:",
        "   omega (MeV)    e'_yrast (keV)    e'_yrare (keV)    Splitting    g-band %    s-band %    i_x (hbar)",
    ])

    for pt in csm_res["profile"]:
        lines.append(f"     {pt['omega_MeV']:5.3f}        {pt['e_yrast_keV']:8.1f}          {pt['e_yrare_keV']:8.1f}        {pt['splitting_keV']:6.1f}      {pt['g_band_percentage']:5.1f}%      {pt['s_band_percentage']:5.1f}%       {pt['aligned_angular_momentum_ix']:5.2f}")

    lines.extend([
        "-" * 76,
        " Methodological Guidelines for High-Spin Alignment:",
        "   - Delta_e'_min = 2 * |V12| occurs at 50/50 configuration mixing (crossing bandhead).",
        "   - |V12| < 35 keV generates sharp S-shaped backbending; |V12| > 65 keV produces smooth upbending.",
        "   - In chiral doublet bands, both partner bands exhibit identical crossing frequencies and alignments.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="CSM Two-Band Crossing & |V_12| Interaction Analyzer"
    )
    parser.add_argument("--omega-c", type=float, default=0.28, help="Band-crossing frequency in MeV (default: 0.28)")
    parser.add_argument("--v12", type=float, default=90.0, help="Interaction strength V12 in keV (default: 90.0)")
    parser.add_argument("--align", type=float, default=10.0, help="Aligned angular momentum in hbar (default: 10.0)")
    parser.add_argument("--preset", type=str, default="164Er_neutron_crossing",
                        choices=["164Er_neutron_crossing", "156Dy_sharp_backbend", "134Nd_proton_crossing"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    w_c = args.omega_c
    v12_val = args.v12
    i_val = args.align
    inv_data = None

    if args.preset == "164Er_neutron_crossing":
        # Smooth upbend benchmark (164Er i13/2 neutron crossing)
        w_c, v12_val, i_val = 0.280, 90.0, 10.0
    elif args.preset == "156Dy_sharp_backbend":
        # Sharp backbend benchmark (156Dy i13/2 neutron crossing)
        w_c, v12_val, i_val = 0.290, 20.0, 10.5
    elif args.preset == "134Nd_proton_crossing":
        # A~130 region (134Nd h11/2 proton crossing)
        w_c, v12_val, i_val = 0.320, 45.0, 7.5

    res = calculate_two_band_crossing_csm(w_c, v12_val, i_val)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, inv_data))


if __name__ == "__main__":
    main()
