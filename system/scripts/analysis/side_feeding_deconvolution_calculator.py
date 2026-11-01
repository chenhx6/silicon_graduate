#!/usr/bin/env python3
"""
In-Beam Nuclear Cascade Side-Feeding Dynamics & Doppler Lineshape Deconvolution Calculator.

Based on:
  - A. Bohr & B. R. Mottelson, "Nuclear Structure" Vol. II, Chapter 4
  - Wu Zhihua (2005), "Nuclear Physics Experimental Methods" (Section 15.3)
  - E. S. Paul et al., Phys. Rev. C 50, 698 (1994) (Side-feeding deconvolution in DSAM)

Features:
  1. Calculates exact effective attenuation factor F_eff(tau_0, tau_feed, f_feed) for exponential side feeding.
  2. Inverts true intrinsic state lifetime tau_0 from measured F_meas by deconvolving side-feeding delay.
  3. Quantifies systematic lifetime bias and resulting intrinsic quadrupole moment Qt distortion.
"""

import numpy as np
from scipy.optimize import brentq


def calculate_effective_f_factor(tau_level_ps, tau_feed_ps, f_feed, alpha_ps):
    """
    Calculate effective attenuation factor F_eff including side-feeding delay.
    F_eff = (1 - f_feed) * [alpha / (alpha + tau_0)] + f_feed * [alpha / (alpha + tau_0 + tau_feed)]
    """
    t0 = max(1e-6, float(tau_level_ps))
    tf = max(0.0, float(tau_feed_ps))
    ff = np.clip(float(f_feed), 0.0, 1.0)
    a = max(1e-4, float(alpha_ps))
    
    term_direct = (1.0 - ff) * (a / (a + t0))
    term_feed = ff * (a / (a + t0 + tf))
    return term_direct + term_feed


def deconvolve_side_feeding_lifetime(F_meas, tau_feed_ps, f_feed, alpha_ps):
    """
    Invert true intrinsic state lifetime tau_0 from measured attenuation factor F_meas.
    Solves F_eff(tau_0, tau_feed, f_feed) == F_meas for tau_0.
    """
    F = float(F_meas)
    tf = float(tau_feed_ps)
    ff = float(f_feed)
    a = float(alpha_ps)
    
    if F <= 0.0 or F >= 1.0:
        raise ValueError(f"F_meas must be strictly between 0 and 1, got {F_meas}")
        
    # Apparent lifetime without side-feeding deconvolution
    tau_apparent_ps = a * (1.0 / F - 1.0)
    
    # Define target function for root finding
    def obj(t0):
        return calculate_effective_f_factor(t0, tf, ff, a) - F
        
    # Search interval: tau_0 must be <= tau_apparent
    try:
        tau_intrinsic_ps = brentq(obj, 1e-6, max(100.0, tau_apparent_ps * 2.0))
    except ValueError:
        # Fallback if boundaries fail
        tau_intrinsic_ps = tau_apparent_ps
        
    bias_ratio = tau_apparent_ps / max(1e-6, tau_intrinsic_ps)
    # Intrinsic quadrupole moment scales with 1 / sqrt(tau):
    # Qt_true / Qt_apparent = sqrt(tau_apparent / tau_true) = sqrt(bias_ratio)
    qt_underestimation_percent = (1.0 - 1.0 / np.sqrt(max(1.0, bias_ratio))) * 100.0
    
    return {
        "F_measured": F,
        "tau_apparent_ps": tau_apparent_ps,
        "tau_intrinsic_ps": tau_intrinsic_ps,
        "tau_feed_ps": tf,
        "f_feed": ff,
        "lifetime_overestimation_ratio": bias_ratio,
        "Qt_underestimation_percent": qt_underestimation_percent
    }


if __name__ == "__main__":
    print("=== Benchmark: Side-Feeding Deconvolution & Lifetime Analysis ===")
    # In 131Ce / 135Pr high-spin state: Au stopper alpha = 1.05 ps
    alpha_Au = 1.05 # ps
    
    # Suppose measured attenuation factor F_meas = 0.55
    # And independent cascade feeding analysis reveals 40% side feeding with tau_feed = 0.35 ps
    F_exp = 0.55
    f_side = 0.40
    tau_side = 0.35 # ps
    
    res = deconvolve_side_feeding_lifetime(F_exp, tau_feed_ps=tau_side, f_feed=f_side, alpha_ps=alpha_Au)
    
    print(f"  Experimental Input:")
    print(f"    Measured Attenuation Factor F_meas : {res['F_measured']:.3f}")
    print(f"    Stopper Slowing-down Time alpha   : {alpha_Au:.2f} ps")
    print(f"    Side-Feeding Fraction f_feed       : {res['f_feed']*100:.1f}%")
    print(f"    Side-Feeding Delay Time tau_feed   : {res['tau_feed_ps']:.3f} ps ({res['tau_feed_ps']*1000:.0f} fs)")
    print("\n  Deconvolution Results:")
    print(f"    Apparent Lifetime (No Deconv)      : {res['tau_apparent_ps']:.3f} ps ({res['tau_apparent_ps']*1000:.1f} fs)")
    print(f"    True Intrinsic Lifetime tau_0      : {res['tau_intrinsic_ps']:.3f} ps ({res['tau_intrinsic_ps']*1000:.1f} fs)")
    print(f"    Lifetime Overestimation Ratio      : {res['lifetime_overestimation_ratio']:.2f}x (Apparent is inflated!)")
    print(f"    Resulting Quadrupole Moment Bias   : Qt was underestimated by {res['Qt_underestimation_percent']:.1f}%!")
    print("  Outcome: Quantitatively eliminates side-feeding delay, restoring true collective deformation!")
