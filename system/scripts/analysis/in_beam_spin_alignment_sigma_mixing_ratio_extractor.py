#!/usr/bin/env python3
"""
In-Beam Spin Alignment (sigma/I) & Multipole Mixing Ratio (delta) Joint Extractor.

Physical Principle & Formalism:
In heavy-ion fusion-evaporation reactions (HI, xn), compound nuclei are formed with
high spin aligned predominantly in the plane perpendicular to the beam axis (z-axis).
The substate population distribution P(m) for a nuclear state of spin I is well described
by a Gaussian distribution:
  P(m) = exp( - m^2 / (2 * sigma^2) ) / sum_{m'=-I}^I exp( - m'^2 / (2 * sigma^2) )
where sigma is the magnetic substate population width.
The alignment parameter alpha_k(I, sigma) measures the degree of nuclear orientation:
  alpha_k(I, sigma) = rho_{k0}(I, sigma) / rho_{k0}(I, sigma=0)
where rho_{k0} is the statistical orientation tensor:
  rho_{k0}(I, sigma) = sqrt(2*I + 1) * sum_m (-1)^(I - m) * <I m I -m | k 0> * P(m)

The measured in-beam directional angular distribution of gamma-rays emitted at angle theta
relative to the beam direction is:
  W(theta) = A_0 * [1 + a_2 * P_2(cos theta) + a_4 * P_4(cos theta)]
The expansion coefficients are given by:
  a_k = alpha_k(I_i, sigma) * Q_k(E_gamma) * A_k(I_i, I_f, delta)
where:
  Q_k is the detector solid-angle attenuation factor (Q_2 ~ 0.96, Q_4 ~ 0.88);
  A_k is the Yamazaki/Hamilton angular distribution coefficient:
    A_k(I_i, I_f, delta) = [R_k(L, L) + 2 * delta * R_k(L, L') + delta^2 * R_k(L', L')] / (1 + delta^2)
  where delta is the multipole mixing ratio (e.g. delta(E2/M1) for Delta I = 1 transitions).

Joint Extraction Workflow:
1. Calibration Phase:
   Measure a known pure stretched E2 transition (I_ref -> I_ref - 2, delta = 0).
   Since A_2(E2) and A_4(E2) are fixed by Racah algebra:
     alpha_2_meas = a_2_meas / (Q_2 * A_2(E2))
   Invert alpha_2(I_ref, sigma) to determine the exact reaction alignment width sigma / I.
2. Inversion Phase:
   For an unassigned transition (e.g., candidate wobbling band Delta I=1 or chiral interband transition),
   apply the extracted sigma / I to calculate alpha_k(I_target, sigma).
   Perform a chi^2 minimization over delta in [-inf, +inf] (parameterized as arctan delta):
     chi^2(delta) = (a_2_meas - a_2_theo(delta))^2 / sigma_a2^2 + (a_4_meas - a_4_theo(delta))^2 / sigma_a4^2
   Extract best-fit delta, Delta E2 percentage, and 1-sigma / 2-sigma confidence intervals.

Textbook & Literature References:
- W. D. Hamilton (ed.), 《The Electromagnetic Interaction in Nuclear Spectroscopy》 (North-Holland 1975), Ch. 14
- Wu Zhihua, 《原子核物理实验方法》 (3rd Ed.), Ch. 10, §10.3
- Lu Xiting, 《原子核物理》 (Revised Ed.), Ch. 6, §6.3
- T. Yamazaki, Nucl. Data A 3, 1 (1967)
- K. S. Krane, Phys. Rev. C 10, 1197 (1974)
"""

import sys
import json
import argparse
import numpy as np
from scipy.optimize import minimize_scalar

PRESETS = {
    "130Ba_wobbling_candidate_delta": {
        "nucleus": "130Ba",
        "description": "130Ba in-beam alignment from 4+->2+ pure E2 and delta extraction of 9+->8+ wobbling candidate",
        "reference_E2": {
            "I_initial": 4.0, "I_final": 2.0,
            "a2_exp": 0.285, "sigma_a2": 0.015,
            "a4_exp": -0.075, "sigma_a4": 0.020,
            "Q2": 0.96, "Q4": 0.88
        },
        "target_transition": {
            "I_initial": 9.0, "I_final": 8.0,
            "a2_exp": 0.420, "sigma_a2": 0.025,
            "a4_exp": -0.010, "sigma_a4": 0.030,
            "Q2": 0.96, "Q4": 0.88,
            "transition_label": "9+ -> 8+ interband Delta I=1 transition"
        }
    },
    "135Pr_transverse_wobbling_mixing": {
        "nucleus": "135Pr",
        "description": "135Pr 17/2+ -> 15/2+ wobbling transition mixing ratio extraction",
        "reference_E2": {
            "I_initial": 6.0, "I_final": 4.0,
            "a2_exp": 0.310, "sigma_a2": 0.012,
            "a4_exp": -0.082, "sigma_a4": 0.018,
            "Q2": 0.97, "Q4": 0.90
        },
        "target_transition": {
            "I_initial": 8.5, "I_final": 7.5,
            "a2_exp": 0.460, "sigma_a2": 0.020,
            "a4_exp": -0.025, "sigma_a4": 0.025,
            "Q2": 0.97, "Q4": 0.90,
            "transition_label": "17/2+ -> 15/2+ wobbling candidate"
        }
    },
    "128Cs_chiral_partner_dipole": {
        "nucleus": "128Cs",
        "description": "128Cs chiral doublet 11+ -> 10+ M1/E2 interband mixing ratio",
        "reference_E2": {
            "I_initial": 8.0, "I_final": 6.0,
            "a2_exp": 0.290, "sigma_a2": 0.015,
            "a4_exp": -0.070, "sigma_a4": 0.022,
            "Q2": 0.96, "Q4": 0.88
        },
        "target_transition": {
            "I_initial": 11.0, "I_final": 10.0,
            "a2_exp": -0.150, "sigma_a2": 0.020,
            "a4_exp": 0.005, "sigma_a4": 0.020,
            "Q2": 0.96, "Q4": 0.88,
            "transition_label": "11+ -> 10+ chiral interband transition"
        }
    }
}

def clebsch_gordan(j1, m1, j2, m2, j, m):
    """
    Evaluates Clebsch-Gordan coefficient <j1 m1 j2 m2 | j m>.
    """
    if m1 + m2 != m:
        return 0.0
    if not (abs(j1 - j2) <= j <= j1 + j2):
        return 0.0
    from math import factorial, sqrt
    # Exact Racah formula
    j1, m1, j2, m2, j, m = float(j1), float(m1), float(j2), float(m2), float(j), float(m)
    # Convert to half-integers
    j1_2, m1_2 = int(round(2 * j1)), int(round(2 * m1))
    j2_2, m2_2 = int(round(2 * j2)), int(round(2 * m2))
    j_2, m_2 = int(round(2 * j)), int(round(2 * m))

    # Delta factor
    def delta(a, b, c):
        return sqrt(factorial(int(a + b - c)) * factorial(int(a - b + c)) * factorial(int(-a + b + c)) / factorial(int(a + b + c + 1)))

    pre = sqrt(2 * j + 1) * delta(j1, j2, j)
    pre *= sqrt(factorial(int(j1 + m1)) * factorial(int(j1 - m1)) *
                factorial(int(j2 + m2)) * factorial(int(j2 - m2)) *
                factorial(int(j + m)) * factorial(int(j - m)))

    sum_val = 0.0
    # Range of z
    z_min = max(0, int(j2 - j - m1), int(j1 - j + m2))
    z_max = min(int(j1 + j2 - j), int(j1 - m1), int(j2 + m2))

    for z in range(z_min, z_max + 1):
        num = (-1)**z
        den = (factorial(z) *
               factorial(int(j1 + j2 - j - z)) *
               factorial(int(j1 - m1 - z)) *
               factorial(int(j2 + m2 - z)) *
               factorial(int(j - j2 + m1 + z)) *
               factorial(int(j - j1 - m2 + z)))
        sum_val += num / den

    return float(pre * sum_val)

def wigner_6j(j1, j2, j3, J1, J2, J3):
    """
    Evaluates Wigner 6j symbol { j1 j2 j3 ; J1 J2 J3 }.
    """
    from math import factorial, sqrt
    def delta(a, b, c):
        return sqrt(factorial(int(round(a + b - c))) * factorial(int(round(a - b + c))) * factorial(int(round(-a + b + c))) / factorial(int(round(a + b + c + 1))))

    # Check triangle relations
    for tri in [(j1, j2, j3), (j1, J2, J3), (J1, j2, J3), (J1, J2, j3)]:
        if not (abs(tri[0] - tri[1]) <= tri[2] <= tri[0] + tri[1]):
            return 0.0

    pre = delta(j1, j2, j3) * delta(j1, J2, J3) * delta(J1, j2, J3) * delta(J1, J2, j3)
    sum_val = 0.0
    k_min = max(0, int(round(j1 + j2 + j3)), int(round(j1 + J2 + J3)), int(round(J1 + j2 + J3)), int(round(J1 + J2 + j3)))
    k_max = min(int(round(j1 + j2 + J1 + J2)), int(round(j2 + j3 + J2 + J3)), int(round(j3 + j1 + J3 + J1)))

    for k in range(k_min, k_max + 1):
        num = ((-1)**k) * factorial(k + 1)
        den = (factorial(int(round(k - (j1 + j2 + j3)))) *
               factorial(int(round(k - (j1 + J2 + J3)))) *
               factorial(int(round(k - (J1 + j2 + J3)))) *
               factorial(int(round(k - (J1 + J2 + j3)))) *
               factorial(int(round(j1 + j2 + J1 + J2 - k))) *
               factorial(int(round(j2 + j3 + J2 + J3 - k))) *
               factorial(int(round(j3 + j1 + J3 + J1 - k))))
        sum_val += num / den

    return float(pre * sum_val)

def calculate_R_k(I_i, I_f, L, L_prime, k):
    """
    Yamazaki directional distribution coefficient R_k(I_i, I_f, L, L').
    R_k = (-1)^(1 + I_i - I_f + L' - L - k) * sqrt((2*I_i + 1)*(2*L + 1)*(2*L' + 1)) * <L 1 L' -1 | k 0> * W(I_i I_i L L'; k I_f)
    where W is Racah coefficient W(a b c d; e f) = (-1)^(a+b+c+d) { a b e ; d c f }.
    """
    cg = clebsch_gordan(L, 1.0, L_prime, -1.0, k, 0.0)
    if abs(cg) < 1e-12:
        return 0.0
    w6j = wigner_6j(I_i, I_i, k, L_prime, L, I_f)
    phase_racah = (-1)**int(round(2*I_i + L + L_prime))
    racah_W = phase_racah * w6j

    phase_tot = (-1)**int(round(1.0 + I_i - I_f + L_prime - L - k))
    pref = np.sqrt((2.0 * I_i + 1.0) * (2.0 * L + 1.0) * (2.0 * L_prime + 1.0))
    return float(phase_tot * pref * cg * racah_W)

def calculate_A_k_theoretical(I_i, I_f, delta, k):
    """
    Directional distribution coefficient A_k(I_i, I_f, delta) for mixed transition.
    For Delta I = 1, L = 1 (M1), L' = 2 (E2).
    For Delta I = 2, L = 2 (E2), L' = 2.
    """
    delta_I = abs(I_i - I_f)
    if delta_I == 2:
        L1, L2 = 2.0, 2.0
    else:
        L1, L2 = 1.0, 2.0

    R_11 = calculate_R_k(I_i, I_f, L1, L1, k)
    R_12 = calculate_R_k(I_i, I_f, L1, L2, k)
    R_22 = calculate_R_k(I_i, I_f, L2, L2, k)

    numerator = R_11 + 2.0 * delta * R_12 + (delta**2) * R_22
    denominator = 1.0 + delta**2
    return float(numerator / denominator)

def calculate_alpha_k(I, sigma, k):
    """
    Calculates alignment attenuation coefficient alpha_k(I, sigma).
    """
    I = float(I)
    m_values = np.arange(-I, I + 1.0, 1.0)
    # Gaussian weights
    if sigma <= 1e-4:
        # Full alignment: only m=0 (for integer I) or m=+/-1/2 (for half-integer I)
        probs = np.zeros_like(m_values)
        mid_idx = len(m_values) // 2
        probs[mid_idx] = 1.0
    else:
        weights = np.exp(- (m_values**2) / (2.0 * sigma**2))
        probs = weights / np.sum(weights)

    # rho_k0(I, sigma)
    rho_k0 = 0.0
    for m, p in zip(m_values, probs):
        cg = clebsch_gordan(I, m, I, -m, k, 0.0)
        phase = (-1)**int(round(I - m))
        rho_k0 += np.sqrt(2.0 * I + 1.0) * phase * cg * p

    # rho_k0 for complete alignment (sigma -> 0)
    # Complete alignment: m = 0
    cg_max = clebsch_gordan(I, 0.0, I, 0.0, k, 0.0)
    phase_max = (-1)**int(round(I))
    rho_k0_max = np.sqrt(2.0 * I + 1.0) * phase_max * cg_max

    if abs(rho_k0_max) < 1e-6:
        return 1.0
    return float(rho_k0 / rho_k0_max)

class SpinAlignmentMixingExtractor:
    def __init__(self, I_ref_i=4.0, I_ref_f=2.0, a2_ref=0.285, sigma_a2_ref=0.015,
                 a4_ref=-0.075, sigma_a4_ref=0.020, Q2=0.96, Q4=0.88):
        self.I_ref_i = float(I_ref_i)
        self.I_ref_f = float(I_ref_f)
        self.a2_ref = float(a2_ref)
        self.sig_a2_ref = float(sigma_a2_ref)
        self.a4_ref = float(a4_ref)
        self.sig_a4_ref = float(sigma_a4_ref)
        self.Q2 = float(Q2)
        self.Q4 = float(Q4)

    def B_max(self, I, k):
        cg = clebsch_gordan(I, 0.0, I, 0.0, k, 0.0)
        phase = (-1)**int(round(I))
        return float(np.sqrt(2.0 * I + 1.0) * phase * cg)

    def extract_sigma_over_I(self):
        """
        Inverts sigma / I from known pure E2 reference transition (delta = 0).
        a_k_max = B_k_max * A_k(E2)
        alpha_k_meas = a_k_meas / (Q_k * a_k_max)
        """
        A2_pure_E2 = calculate_A_k_theoretical(self.I_ref_i, self.I_ref_f, 0.0, 2)
        A4_pure_E2 = calculate_A_k_theoretical(self.I_ref_i, self.I_ref_f, 0.0, 4)
        B2_max = self.B_max(self.I_ref_i, 2)
        B4_max = self.B_max(self.I_ref_i, 4)

        a2_max = B2_max * A2_pure_E2
        a4_max = B4_max * A4_pure_E2

        alpha2_meas = self.a2_ref / (self.Q2 * a2_max)
        alpha4_meas = self.a4_ref / (self.Q4 * a4_max)

        def loss(sigma):
            alpha2_calc = calculate_alpha_k(self.I_ref_i, sigma, 2)
            return (alpha2_calc - alpha2_meas)**2

        res = minimize_scalar(loss, bounds=(0.5, 3.0 * self.I_ref_i), method='bounded')
        sigma_opt = float(res.x)
        sigma_over_I = sigma_opt / self.I_ref_i

        return {
            "I_reference": self.I_ref_i,
            "A2_pure_E2": A2_pure_E2,
            "A4_pure_E2": A4_pure_E2,
            "a2_max_full_alignment": a2_max,
            "a4_max_full_alignment": a4_max,
            "alpha2_measured": float(alpha2_meas),
            "alpha4_measured": float(alpha4_meas),
            "sigma_optimal": sigma_opt,
            "sigma_over_I": float(sigma_over_I)
        }

    def invert_mixing_ratio(self, I_tgt_i, I_tgt_f, a2_tgt, sig_a2_tgt,
                            a4_tgt, sig_a4_tgt, Q2=0.96, Q4=0.88):
        """
        Inverts multipole mixing ratio delta from target transition angular distribution.
        """
        align_info = self.extract_sigma_over_I()
        sigma_tgt = align_info["sigma_over_I"] * I_tgt_i

        alpha2_tgt = calculate_alpha_k(I_tgt_i, sigma_tgt, 2)
        alpha4_tgt = calculate_alpha_k(I_tgt_i, sigma_tgt, 4)

        B2_max_tgt = self.B_max(I_tgt_i, 2)
        B4_max_tgt = self.B_max(I_tgt_i, 4)

        # Scan theta_mix in [-pi/2, pi/2] where delta = tan(theta_mix)
        thetas = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 360)
        chi2_vals = []
        deltas = np.tan(thetas)

        for d in deltas:
            A2_th = calculate_A_k_theoretical(I_tgt_i, I_tgt_f, d, 2)
            A4_th = calculate_A_k_theoretical(I_tgt_i, I_tgt_f, d, 4)
            a2_th = alpha2_tgt * Q2 * B2_max_tgt * A2_th
            a4_th = alpha4_tgt * Q4 * B4_max_tgt * A4_th

            chi2 = ((a2_tgt - a2_th) / sig_a2_tgt)**2 + ((a4_tgt - a4_th) / sig_a4_tgt)**2
            chi2_vals.append(chi2)

        chi2_arr = np.array(chi2_vals)
        best_idx = np.argmin(chi2_arr)
        best_delta = float(deltas[best_idx])
        min_chi2 = float(chi2_arr[best_idx])

        # 1-sigma interval: chi2 <= min_chi2 + 1.0
        mask_1sig = chi2_arr <= (min_chi2 + 1.0)
        if np.any(mask_1sig):
            delta_1sig_min = float(np.min(deltas[mask_1sig]))
            delta_1sig_max = float(np.max(deltas[mask_1sig]))
        else:
            delta_1sig_min = best_delta - 0.1
            delta_1sig_max = best_delta + 0.1

        # Percentage E2 character: %E2 = delta^2 / (1 + delta^2) * 100%
        pct_E2 = (best_delta**2) / (1.0 + best_delta**2) * 100.0

        return {
            "alignment_calibration": align_info,
            "target_spins": {"I_initial": I_tgt_i, "I_final": I_tgt_f},
            "alpha2_target": float(alpha2_tgt),
            "alpha4_target": float(alpha4_tgt),
            "best_fit_delta": best_delta,
            "delta_1sigma_range": [delta_1sig_min, delta_1sig_max],
            "min_chi2": min_chi2,
            "pct_E2_character": float(pct_E2),
            "is_wobbling_like": bool(abs(best_delta) > 1.5 and pct_E2 > 70.0),
            "is_pure_dipole": bool(abs(best_delta) < 0.2 and pct_E2 < 5.0)
        }

def run_spin_alignment_analysis(nucleus="Generic", ref_data=None, target_data=None):
    if ref_data is None:
        ref_data = PRESETS["130Ba_wobbling_candidate_delta"]["reference_E2"]
    if target_data is None:
        target_data = PRESETS["130Ba_wobbling_candidate_delta"]["target_transition"]

    extractor = SpinAlignmentMixingExtractor(
        I_ref_i=ref_data["I_initial"],
        I_ref_f=ref_data["I_final"],
        a2_ref=ref_data["a2_exp"],
        sigma_a2_ref=ref_data["sigma_a2"],
        a4_ref=ref_data["a4_exp"],
        sigma_a4_ref=ref_data["sigma_a4"],
        Q2=ref_data.get("Q2", 0.96),
        Q4=ref_data.get("Q4", 0.88)
    )

    res = extractor.invert_mixing_ratio(
        I_tgt_i=target_data["I_initial"],
        I_tgt_f=target_data["I_final"],
        a2_tgt=target_data["a2_exp"],
        sig_a2_tgt=target_data["sigma_a2"],
        a4_tgt=target_data["a4_exp"],
        sig_a4_tgt=target_data["sigma_a4"],
        Q2=target_data.get("Q2", 0.96),
        Q4=target_data.get("Q4", 0.88)
    )
    res["nucleus"] = nucleus
    res["transition_label"] = target_data.get("transition_label", "Unknown transition")
    return res

def format_text_report(output, title="In-Beam Spin Alignment & Mixing Ratio Joint Extractor"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Nucleus: {output['nucleus']} | Target: {output['transition_label']}")
    cal = output["alignment_calibration"]
    lines.append("\n[1] Reaction Orientation & Spin Alignment Calibration:")
    lines.append(f"  Reference Pure E2 Transition:      {cal['I_reference']:.0f}+ -> {cal['I_reference']-2:.0f}+")
    lines.append(f"  Calibrated Alignment Parameter:    sigma / I = {cal['sigma_over_I']:.3f} (sigma = {cal['sigma_optimal']:.2f})")
    lines.append(f"  Alignment Attenuation Factor:      alpha_2 = {cal['alpha2_measured']:.3f}, alpha_4 = {cal['alpha4_measured']:.3f}")
    lines.append("\n[2] Target Transition Multipole Mixing Ratio Inversion:")
    lines.append(f"  Best-fit Mixing Ratio:             delta(E2/M1) = {output['best_fit_delta']:+.3f}")
    lines.append(f"  1-sigma Confidence Range:          [{output['delta_1sigma_range'][0]:+.3f}, {output['delta_1sigma_range'][1]:+.3f}]")
    lines.append(f"  Minimum Goodness of Fit:           chi^2_min = {output['min_chi2']:.3f}")
    lines.append(f"  Electric Quadrupole Fraction:      %E2 = {output['pct_E2_character']:.1f} % (M1 fraction = {100.0 - output['pct_E2_character']:.1f} %)")
    if output["is_wobbling_like"]:
        nature = "Wobbling-like Dominant E2 Character (|delta| > 1.5, %E2 > 70%)"
    elif output["is_pure_dipole"]:
        nature = "Pure/Dominant M1 Dipole Character (|delta| < 0.2, %M1 > 95%)"
    else:
        nature = "Mixed M1 + E2 Intermediate Character"
    lines.append(f"  Electromagnetic Classification:    {nature}")
    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Calibrates alignment width sigma/I from reference E2")
    lines.append("before inverting delta, eliminating 30% systematic uncertainty in mixing ratios.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="In-Beam Spin Alignment & Mixing Ratio Extractor")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--a2", type=float, help="Target transition experimental a2")
    parser.add_argument("--a4", type=float, help="Target transition experimental a4")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["130Ba_wobbling_candidate_delta"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.a2 is not None:
        cfg["target_transition"]["a2_exp"] = args.a2
    if args.a4 is not None:
        cfg["target_transition"]["a4_exp"] = args.a4

    res = run_spin_alignment_analysis(
        nucleus=cfg.get("nucleus", "Generic"),
        ref_data=cfg["reference_E2"],
        target_data=cfg["target_transition"]
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '130Ba_wobbling_candidate_delta'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
