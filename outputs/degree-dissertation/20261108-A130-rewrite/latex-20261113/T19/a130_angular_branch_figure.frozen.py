#!/usr/bin/env python3
"""
a130_angular_branch_figure.py
Didactic model of DCO quadratic rational inversion, dual-root branches, and polarimetry degeneracy breaking.
Generates Img/angular-branch-delta-likelihood.svg and Img/angular-branch-delta-likelihood.pdf.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import hashlib

def main():
    img_dir = 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
    os.makedirs(img_dir, exist_ok=True)

    theta_delta = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 500)
    delta = np.tan(theta_delta)

    # Self-consistent quadratic rational DCO response: N(delta) / D(delta)
    # N(delta) = n0 + n1*delta + n2*delta^2, D(delta) = d0 + d1*delta + d2*delta^2
    n0, n1, n2 = 0.65, -0.30, 1.10
    d0, d1, d2 = 1.05, 0.15, 0.95
    R_dco = (n0 + n1 * delta + n2 * delta**2) / (d0 + d1 * delta + d2 * delta**2)

    # Self-consistent linear polarization P(delta) = P_num / W
    w0, w1, w2 = 1.00, 0.10, 0.80
    p0, p1, p2 = -0.45, 0.60, 0.65
    P_pol = (p0 + p1 * delta + p2 * delta**2) / (w0 + w1 * delta + w2 * delta**2)
    P_pol = np.clip(P_pol, -1.0, 1.0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=300)

    ax1.plot(theta_delta * 180 / np.pi, R_dco, color='#1f77b4', lw=2.0, label=r'Calculated $R_{\mathrm{DCO}}(\delta)$')
    exp_val, exp_err = 0.80, 0.05
    ax1.axhline(exp_val, color='#d62728', ls='--', lw=1.2, label=r'Measured $R_{\mathrm{DCO}} = 0.80 \pm 0.05$')
    ax1.axhspan(exp_val - exp_err, exp_val + exp_err, color='#d62728', alpha=0.15)

    c2 = n2 - exp_val * d2
    c1 = n1 - exp_val * d1
    c0 = n0 - exp_val * d0
    roots = np.roots([c2, c1, c0])
    for r in roots:
        th_r = np.arctan(r) * 180 / np.pi
        ax1.plot(th_r, exp_val, 'ro', ms=6)
        ax1.annotate(f'Root $\\delta = {r:.2f}$\n($\\arctan\\delta = {th_r:.1f}^\\circ$)', xy=(th_r, exp_val),
                     xytext=(th_r - 25 if r < 0 else th_r + 10, exp_val + 0.18 if r < 0 else exp_val - 0.22),
                     arrowprops=dict(arrowstyle="->", color='#d62728', lw=1.0), fontsize=8.5)

    ax1.set_xlabel(r'$\arctan\delta$ (degrees)', fontsize=10)
    ax1.set_ylabel(r'Directional Correlation Ratio $R_{\mathrm{DCO}}$', fontsize=10)
    ax1.set_title(r'(a) Dual Roots in $R_{\mathrm{DCO}}$ Quadratic Rational Inversion', fontsize=10.5)
    ax1.set_xlim(-90, 90)
    ax1.set_ylim(0.2, 1.3)
    ax1.set_xticks([-90, -60, -30, 0, 30, 60, 90])
    ax1.grid(True, ls=':', color='gray', alpha=0.5)
    ax1.legend(loc='upper right', fontsize=8.5)

    ax2.plot(theta_delta * 180 / np.pi, P_pol, color='#2ca02c', lw=2.0, label=r'Calculated Polarization $P(\delta)$')
    ax2.axhline(0, color='gray', ls=':', lw=1.0)

    for r in roots:
        th_r = np.arctan(r) * 180 / np.pi
        p_val = (p0 + p1 * r + p2 * r**2) / (w0 + w1 * r + w2 * r**2)
        ax2.plot(th_r, p_val, 's', color='#d62728', ms=6)
        ax2.annotate(f'$P(\\delta_{{1,2}}) = {p_val:.2f}$', xy=(th_r, p_val),
                     xytext=(th_r - 35 if r < 0 else th_r + 10, p_val - 0.25 if r < 0 else p_val + 0.20),
                     arrowprops=dict(arrowstyle="->", color='#d62728', lw=1.0), fontsize=8.5)

    ax2.set_xlabel(r'$\arctan\delta$ (degrees)', fontsize=10)
    ax2.set_ylabel(r'Linear Polarization Degree $P$', fontsize=10)
    ax2.set_title(r'(b) Degeneracy Resolution via Compton Polarimetry', fontsize=10.5)
    ax2.set_xlim(-90, 90)
    ax2.set_ylim(-1.05, 1.05)
    ax2.set_xticks([-90, -60, -30, 0, 30, 60, 90])
    ax2.grid(True, ls=':', color='gray', alpha=0.5)
    ax2.legend(loc='upper left', fontsize=8.5)

    fig.tight_layout()

    svg_path = os.path.join(img_dir, 'angular-branch-delta-likelihood.svg')
    pdf_path = os.path.join(img_dir, 'angular-branch-delta-likelihood.pdf')

    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")

if __name__ == '__main__':
    main()
