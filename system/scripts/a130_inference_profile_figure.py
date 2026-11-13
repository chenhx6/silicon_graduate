#!/usr/bin/env python3
"""
a130_inference_profile_figure.py
Figure producer for Section 5.10: Statistical inference, multi-root profile likelihood,
and physical boundary constraints.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

    # Panel (a): Dual-root likelihood profile in bounded arctan(delta) space
    theta_delta = np.unique(np.r_[np.linspace(-85, 85, 500), -40.0, 20.0])
    # Declared synthetic profile, not fitted angular-correlation data. The
    # smooth-step offset preserves both stationary minima at -40 and +20 deg.
    barrier_scale, second_minimum = 80.0, 0.9
    u = (theta_delta + 40.0) / 60.0
    profile_delta = (
        barrier_scale * u**2 * (1.0 - u)**2
        + second_minimum * (1.0 - 3.0 * u**2 + 2.0 * u**3)
    )

    # Local parabolic approximation around root 1 (theta ~ 20 deg)
    curv1 = (barrier_scale + 3.0 * second_minimum) / 60.0**2
    parabola = curv1 * (theta_delta - 20)**2

    ax1.plot(theta_delta, profile_delta, color='#1f77b4', lw=2.0, label=r'Global Profile Likelihood $-2\Delta\ln\lambda$')
    ax1.plot(theta_delta, parabola, color='#d62728', ls='--', lw=1.5, label=r'Local Parabolic (Hessian) Approx.')

    ax1.axhline(1.0, color='gray', ls=':', lw=1.0)
    ax1.text(-80, 1.2, r'Gaussian benchmark: $\Delta\chi^2 = 1$', fontsize=8.0, color='gray')
    ax1.axhline(3.84, color='gray', ls=':', lw=1.0)
    ax1.text(-80, 4.04, r'Gaussian benchmark: $\Delta\chi^2 = 3.84$', fontsize=8.0, color='gray')

    ax1.set_xlabel(r'Bounded Parameter $\arctan\delta$ (degrees)', fontsize=10)
    ax1.set_ylabel(r'$-2\Delta\ln\mathcal{L}$ (Test Statistic)', fontsize=10)
    ax1.set_xlim(-85, 85)
    ax1.set_ylim(-0.2, 10.0)
    ax1.set_title(r'(a) Multi-Root Degeneracy & Global Profile', fontsize=10.5)
    ax1.grid(True, ls=':', color='gray', alpha=0.5)
    ax1.legend(loc='upper center', fontsize=8.0)

    # Panel (b): Physical boundary constraint (mu >= 0)
    mu_signal = np.linspace(-2.5, 4.5, 500)
    mu_hat = -0.6  # Downward background fluctuation (unphysical unconstrained MLE)
    chi2_unconstrained = (mu_signal - mu_hat)**2 / 1.0

    # Constrained profile is strictly defined on physical domain mu >= 0 with constrained MLE mu_hat_phys = 0
    mu_phys = np.r_[0.0, mu_signal[mu_signal > 0]]
    mu_hat_phys = max(0.0, mu_hat)
    # Preserve the observed Gaussian mean mu_hat; only the reference
    # likelihood changes to the physical maximum. Recentring the quadratic
    # on mu_hat_phys would describe different data.
    chi2_constrained = (
        (mu_phys - mu_hat)**2 - (mu_hat_phys - mu_hat)**2
    ) / 1.0

    ax2.plot(mu_signal, chi2_unconstrained, color='#d62728', ls='--', lw=1.5, label=r'Unconstrained Parabola ($\widehat{\mu} < 0$)')
    ax2.plot(mu_phys, chi2_constrained, color='#2ca02c', lw=2.2, label=r'Physical Boundary Profile ($\mu \geq 0$)')

    ax2.axvline(0, color='black', lw=1.2, ls='-')
    ax2.text(0.08, 8.5, r'Physical Boundary ($\mu = 0$)', fontsize=8.5, rotation=90, va='top')
    ax2.axhline(1.0, color='gray', ls=':', lw=1.0)
    ax2.axhline(2.71, color='gray', ls=':', lw=1.0)
    ax2.text(1.2, 2.9, r'Gaussian benchmark: $\Delta\chi^2 = 2.71$', fontsize=8.0, color='gray')

    ax2.set_xlabel(r'Signal Parameter $\mu \propto B(XL)$ (Arbitrary Units)', fontsize=10)
    ax2.set_ylabel(r'$-2\Delta\ln\mathcal{L}$ (Test Statistic)', fontsize=10)
    ax2.set_xlim(-2.5, 4.5)
    ax2.set_ylim(-0.2, 10.0)
    ax2.set_title(r'(b) Physical Boundary & Likelihood Truncation', fontsize=10.5)
    ax2.grid(True, ls=':', color='gray', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=8.0)

    plt.tight_layout()

    img_dir = 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
    os.makedirs(img_dir, exist_ok=True)
    svg_path = os.path.join(img_dir, 'inference-profile-likelihood-boundary.svg')
    pdf_path = os.path.join(img_dir, 'inference-profile-likelihood-boundary.pdf')

    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    # Normalize trailing whitespace in SVG
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_lines = [line.rstrip() for line in f]
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines) + "\n")

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")

if __name__ == '__main__':
    main()
