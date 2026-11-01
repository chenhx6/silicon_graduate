#!/usr/bin/env python3
"""
detector_deadtime_pileup_correction_calculator.py
=================================================
Radiation Detector Dead Time, Pulse Pile-up & Counting Loss Analysis Suite:
Reconciliation of Wu Zhihua (Experimental Methods) vs Wang Xiaolian (Particle Detection).

Physics & Formulation:
----------------------
1. The Fundamental Discrepancy & Reconciliation:
   - Wu Zhihua ("Nuclear Physics Experimental Methods", Ch 1 & Ch 10):
     Focuses on traditional multichannel analyzer (MCA) / ADC conversion where dead time
     is strictly NON-PARALYZABLE (可扩展/非麻痹型):
       m = n / (1 + n * tau)  ==>  n = m / (1 - m * tau)
     where m is measured count rate, n is true event rate, and tau is fixed dead time.

   - Wang Xiaolian ("Particle Detection Technology", Ch 4 & Ch 5):
     Focuses on physical detector processes (gas discharge space charge, PMT recovery,
     analog pulse shaping), which are inherently PARALYZABLE (不可扩展/麻痹型):
       m = n * exp(-n * tau)
     In paralyzable systems, every event extends the insensitive period. As true rate n
     increases beyond n_crit = 1/tau, the observed rate m drops toward zero!
     This generates a DANGEROUS DUAL-ROOT AMBIGUITY: for any observed rate m < m_max,
     there exist two physical rates (unsaturated branch n1 and heavily paralyzed branch n2).

2. Hybrid (Series) Dead Time Model (Lee-Gardner / Muller Model):
   Real nuclear spectroscopy chains possess both:
   - Paralyzable analog pulse shaping front-end (tau_P ~ shaping time)
   - Non-paralyzable ADC conversion back-end (tau_N ~ conversion time)
       m = [ n * exp(-n * tau_P) ] / [ 1 + n * tau_N * exp(-n * tau_P) ]

3. Peak Pile-up & Ballistic Deficit:
   For pulse shaping inspection window T_w (typically 2.0 - 2.5 * peaking time T_p):
     P_clean = exp(-2 * n * T_p)
     Fractional Pileup Loss: f_pu = 1 - exp(-2 * n * T_p) ~ 2 * n * T_p

4. Exact Lambert W Inversion for Paralyzable Systems:
   n_1 = -W_0(-m * tau) / tau     (Lower normal branch)
   n_2 = -W_{-1}(-m * tau) / tau  (Upper saturated branch)

References:
  - 吴治华, 《原子核物理实验方法》, 第3版, 原子能出版社 (2005), 第1章与第10章.
  - 汪晓莲, 李澄, 邵明, 陈宏芳, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第4章与第5章.
  - G. F. Knoll, Radiation Detection and Measurement, 4th ed., Wiley (2010), Ch 17.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def lambert_w_eval(x: float, branch: int = 0, tol: float = 1e-11, max_iter: int = 100) -> float:
    """
    Pure-Python Halley's method evaluation of the Lambert W function W(x).
    branch = 0 for principal branch (x >= -1/e, W >= -1)
    branch = -1 for secondary branch (-1/e <= x < 0, W <= -1)
    """
    inv_e = -1.0 / math.e
    if x < inv_e - 1e-12:
        raise ValueError(f"x = {x} is outside domain [-1/e, inf)")
    if abs(x - inv_e) < 1e-12:
        return -1.0

    if branch == 0:
        if x < -0.3:
            w = -1.0 + math.sqrt(2.0 * (math.e * x + 1.0))
        elif x < 1.0:
            w = x / (1.0 + x)
        else:
            w = math.log(x) - math.log(max(1.0, math.log(x)))
    elif branch == -1:
        if x >= 0.0 or x < inv_e:
            raise ValueError(f"x = {x} outside branch -1 domain [-1/e, 0)")
        if x < -0.3:
            w = -1.0 - math.sqrt(2.0 * (math.e * x + 1.0))
        else:
            w = math.log(-x) - 2.0
    else:
        raise ValueError("Only branch 0 and -1 are supported.")

    for _ in range(max_iter):
        ew = math.exp(w)
        w_ew = w * ew
        f = w_ew - x
        if abs(f) < tol:
            return w
        f_prime = ew * (w + 1.0)
        f_double_prime = ew * (w + 2.0)
        delta = f / (f_prime - (f * f_double_prime) / (2.0 * f_prime))
        w -= delta
        if abs(delta) < tol:
            break
    return w


def calculate_deadtime_models(
    true_rate: float,
    tau_nonpar: float,
    tau_par: float,
    tau_hybrid_p: float,
    tau_hybrid_n: float,
    peaking_time: float
) -> Dict[str, Any]:
    """
    Calculates observed count rates and throughput for non-paralyzable, paralyzable,
    and hybrid dead time models given a true interaction rate.
    """
    n = max(0.0, float(true_rate))

    m_np = n / (1.0 + n * tau_nonpar)
    livetime_np = 1.0 / (1.0 + n * tau_nonpar)

    m_p = n * math.exp(-n * tau_par)
    m_p_max = (1.0 / (math.e * tau_par)) if tau_par > 0 else 0.0
    n_crit_p = (1.0 / tau_par) if tau_par > 0 else 0.0
    livetime_p = math.exp(-n * tau_par)
    is_saturated_par = bool(n > n_crit_p)

    exp_p = math.exp(-n * tau_hybrid_p)
    m_hybrid = (n * exp_p) / (1.0 + n * tau_hybrid_n * exp_p)
    livetime_hybrid = m_hybrid / max(1e-12, n)

    pileup_prob = 1.0 - math.exp(-2.0 * n * peaking_time)
    clean_peak_rate = n * math.exp(-2.0 * n * peaking_time)

    return {
        "true_rate_cps": n,
        "non_paralyzable": {
            "tau_sec": tau_nonpar,
            "observed_rate_cps": m_np,
            "fractional_loss": 1.0 - (m_np / max(1e-12, n)),
            "live_time_fraction": livetime_np
        },
        "paralyzable": {
            "tau_sec": tau_par,
            "observed_rate_cps": m_p,
            "max_possible_rate_cps": m_p_max,
            "critical_true_rate_cps": n_crit_p,
            "fractional_loss": 1.0 - (m_p / max(1e-12, n)),
            "live_time_fraction": livetime_p,
            "is_in_saturated_regime": is_saturated_par
        },
        "hybrid": {
            "tau_paralyzable_sec": tau_hybrid_p,
            "tau_nonparalyzable_sec": tau_hybrid_n,
            "observed_rate_cps": m_hybrid,
            "fractional_loss": 1.0 - (m_hybrid / max(1e-12, n)),
            "live_time_fraction": livetime_hybrid
        },
        "pileup_diagnostics": {
            "peaking_time_sec": peaking_time,
            "pileup_loss_fraction": pileup_prob,
            "clean_peak_rate_cps": clean_peak_rate
        }
    }


def invert_observed_rate(
    observed_rate: float,
    tau_nonpar: float,
    tau_par: float
) -> Dict[str, Any]:
    """
    Inverts measured count rate m to find true rate n under non-paralyzable
    and paralyzable assumptions, demonstrating the critical dual-root pitfall.
    """
    m = max(0.0, float(observed_rate))

    if m * tau_nonpar >= 1.0:
        n_np = float("inf")
        np_valid = False
    else:
        n_np = m / (1.0 - m * tau_nonpar)
        np_valid = True

    m_max = 1.0 / (math.e * tau_par) if tau_par > 0 else float("inf")
    x = -m * tau_par

    if m > m_max:
        p_valid = False
        root1 = None
        root2 = None
    else:
        p_valid = True
        try:
            w0 = lambert_w_eval(x, branch=0)
            root1 = -w0 / tau_par
        except Exception:
            root1 = None

        try:
            wm1 = lambert_w_eval(x, branch=-1)
            root2 = -wm1 / tau_par
        except Exception:
            root2 = None

    return {
        "observed_rate_cps": m,
        "non_paralyzable_inversion": {
            "tau_sec": tau_nonpar,
            "true_rate_cps": n_np,
            "is_physically_admissible": np_valid
        },
        "paralyzable_dual_root_inversion": {
            "tau_sec": tau_par,
            "max_observable_rate_cps": m_max,
            "is_physically_admissible": p_valid,
            "root1_unsaturated_cps": root1,
            "root2_paralyzed_cps": root2,
            "dual_root_discrepancy_ratio": (root2 / root1) if (root1 and root2 and root1 > 0) else None
        }
    }


def format_text_report(fwd: Dict[str, Any], inv: Dict[str, Any]) -> str:
    lines = [
        "=" * 74,
        "   DETECTOR DEAD TIME, PULSE PILE-UP & COUNTING LOSS ANALYZER",
        "   Reconciliation: Wu Zhihua (Experimental) vs Wang Xiaolian (Detectors)",
        "=" * 74,
        f" FORWARD THROUGHPUT AT TRUE RATE n = {fwd['true_rate_cps']:.1f} cps:",
        f"   1. Non-Paralyzable (Wu Zhihua ADC Model, tau = {fwd['non_paralyzable']['tau_sec']*1e6:.2f} us):",
        f"      Observed Rate m_NP   : {fwd['non_paralyzable']['observed_rate_cps']:.1f} cps",
        f"      Live Time Fraction   : {fwd['non_paralyzable']['live_time_fraction']*100:.2f}%",
        f"      Counting Loss        : {fwd['non_paralyzable']['fractional_loss']*100:.2f}%",
        "",
        f"   2. Paralyzable (Wang Xiaolian Front-End Model, tau = {fwd['paralyzable']['tau_sec']*1e6:.2f} us):",
        f"      Observed Rate m_P    : {fwd['paralyzable']['observed_rate_cps']:.1f} cps",
        f"      Max Observable Rate  : {fwd['paralyzable']['max_possible_rate_cps']:.1f} cps (at n_crit = {fwd['paralyzable']['critical_true_rate_cps']:.1f})",
        f"      Live Time Fraction   : {fwd['paralyzable']['live_time_fraction']*100:.2f}%",
        f"      Regime Status        : {'PARALYZED SATURATION! (Rate decreases)' if fwd['paralyzable']['is_in_saturated_regime'] else 'Normal unsaturated operation'}",
        "",
        f"   3. Hybrid Series Model (Analog Shaper tau_P + Digital ADC tau_N):",
        f"      tau_P = {fwd['hybrid']['tau_paralyzable_sec']*1e6:.2f} us, tau_N = {fwd['hybrid']['tau_nonparalyzable_sec']*1e6:.2f} us",
        f"      Observed Rate m_Hyb  : {fwd['hybrid']['observed_rate_cps']:.1f} cps (Live Time: {fwd['hybrid']['live_time_fraction']*100:.2f}%)",
        "",
        f"   4. Pulse Pile-up in Peaking Window (T_p = {fwd['pileup_diagnostics']['peaking_time_sec']*1e6:.2f} us):",
        f"      Fractional Pile-up   : {fwd['pileup_diagnostics']['pileup_loss_fraction']*100:.2f}%",
        f"      Clean Full-Energy Rate: {fwd['pileup_diagnostics']['clean_peak_rate_cps']:.1f} cps",
        "-" * 74,
        f" EXPERIMENTAL INVERSION FROM OBSERVED RATE m = {inv['observed_rate_cps']:.1f} cps:",
        f"   Non-Paralyzable Inversion n_NP: {inv['non_paralyzable_inversion']['true_rate_cps']:.1f} cps" if inv['non_paralyzable_inversion']['is_physically_admissible'] else "   Non-Paralyzable: Over range (m * tau >= 1.0)",
        f"   Paralyzable DUAL ROOTS:",
    ]

    p_inv = inv['paralyzable_dual_root_inversion']
    if p_inv['is_physically_admissible']:
        r1 = p_inv['root1_unsaturated_cps']
        r2 = p_inv['root2_paralyzed_cps']
        ratio = p_inv['dual_root_discrepancy_ratio']
        lines.extend([
            f"      Root 1 (Unsaturated) : {r1:.1f} cps",
            f"      Root 2 (Paralyzed)   : {r2:.1f} cps",
            f"      Discrepancy Ratio    : {ratio:.2f}x (Hazardous 2nd root!)"
        ])
    else:
        lines.append(f"      EXCEEDS MAX OBSERVABLE RATE ({p_inv['max_observable_rate_cps']:.1f} cps)!")

    lines.extend([
        "-" * 74,
        " Physical & Methodological Synthesis:",
        "   - Wu Zhihua's formula applies strictly to ADC and fixed digital dead times.",
        "   - Wang Xiaolian's model governs analog shaping and detector discharge physics.",
        "   - In high-intensity in-beam reactions, paralyzable systems exhibit dual roots;",
        "     applying Wu's formula blindly leads to catastrophic rate underestimation.",
        "   - Solution: Use digital trapezoidal filters with dual-threshold pile-up rejectors.",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Detector Dead Time, Pile-up & Counting Loss Reconciler"
    )
    parser.add_argument("--true-rate", "-n", type=float, default=25000.0,
                        help="True event rate (cps)")
    parser.add_argument("--obs-rate", "-m", type=float, default=20000.0,
                        help="Observed event rate for inversion (cps)")
    parser.add_argument("--tau-np", type=float, default=10.0,
                        help="Non-paralyzable dead time in microseconds (default: 10.0 us)")
    parser.add_argument("--tau-p", type=float, default=10.0,
                        help="Paralyzable dead time in microseconds (default: 10.0 us)")
    parser.add_argument("--tp", type=float, default=4.0,
                        help="Peaking time in microseconds (default: 4.0 us)")
    parser.add_argument("--json", action="store_true",
                        help="Output pure JSON")

    args = parser.parse_args()

    tau_np_sec = args.tau_np * 1e-6
    tau_p_sec = args.tau_p * 1e-6
    tp_sec = args.tp * 1e-6

    fwd = calculate_deadtime_models(
        true_rate=args.true_rate,
        tau_nonpar=tau_np_sec,
        tau_par=tau_p_sec,
        tau_hybrid_p=tau_p_sec * 0.5,
        tau_hybrid_n=tau_np_sec * 0.5,
        peaking_time=tp_sec
    )

    inv = invert_observed_rate(
        observed_rate=args.obs_rate,
        tau_nonpar=tau_np_sec,
        tau_par=tau_p_sec
    )

    if args.json:
        print(json.dumps({"forward": fwd, "inversion": inv}, indent=2))
    else:
        print(format_text_report(fwd, inv))


if __name__ == "__main__":
    main()
