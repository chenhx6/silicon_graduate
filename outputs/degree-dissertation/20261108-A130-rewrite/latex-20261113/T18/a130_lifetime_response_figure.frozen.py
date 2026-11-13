#!/usr/bin/env python3
"""
a130_lifetime_response_figure.py
Didactic educational model of RDDS decay curves and DSAM Doppler line shape evolution.
Generates Img/lifetime-response-rdds-dsam.svg and Img/lifetime-response-rdds-dsam.pdf.
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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=300)

    v = 6.0 # um / ps (0.02 c)
    x = np.linspace(0, 150, 300) # um

    for tau, col, ls in [(2.0, '#1f77b4', '-'), (5.0, '#2ca02c', '--'), (15.0, '#d62728', '-.')]:
        Ru = np.exp(-x / (v * tau))
        Rs = 1.0 - Ru
        ax1.plot(x, Ru, color=col, ls=ls, lw=1.8, label=f'$\\tau = {tau:.0f}$ ps ($R_u$)')
        ax1.plot(x, Rs, color=col, ls=':', lw=1.0, alpha=0.7)

    ax1.set_xlabel(r'Target-to-Stopper Distance $x$ ($\mu\mathrm{m}$)', fontsize=10)
    ax1.set_ylabel(r'Normalized Intensity Fraction', fontsize=10)
    ax1.set_title(r'(a) RDDS Decay Curves ($v/c = 2.0\%$, Constant Velocity Toy)', fontsize=10.5)
    ax1.set_xlim(0, 150)
    ax1.set_ylim(-0.02, 1.05)
    ax1.grid(True, ls=':', color='gray', alpha=0.5)
    ax1.legend(loc='center right', fontsize=8.5)

    E_arr = np.linspace(990, 1030, 800)
    E0 = 1000.0
    dE_max = 20.0
    sig_det = 1.2 # keV detector resolution

    def dsam_shape(E_axis, tau_val, tau_s=0.8):
        f_stop = np.exp(-tau_s / tau_val)
        y_stop = f_stop * np.exp(-0.5 * ((E_axis - E0) / sig_det)**2) / (sig_det * np.sqrt(2*np.pi))
        y_flight = np.zeros_like(E_axis)
        mask = (E_axis >= E0) & (E_axis <= E0 + dE_max)
        t_flight = tau_s * (1.0 - (E_axis[mask] - E0) / dE_max)
        dt_dE = tau_s / dE_max
        tail = dt_dE * (np.exp(-t_flight / tau_val) / tau_val)
        kernel_x = np.linspace(-5*sig_det, 5*sig_det, 81)
        kernel = np.exp(-0.5 * (kernel_x / sig_det)**2) / (sig_det * np.sqrt(2*np.pi))
        tail_conv = np.convolve(tail, kernel, mode='same') * (kernel_x[1] - kernel_x[0])
        y_flight[mask] = tail_conv
        return y_stop + y_flight

    for tau_val, col, label in [(0.1, '#1f77b4', r'$\tau \ll \tau_{\mathrm{stop}}$ ($0.1$ ps)'),
                                (0.8, '#2ca02c', r'$\tau \approx \tau_{\mathrm{stop}}$ ($0.8$ ps)'),
                                (5.0, '#d62728', r'$\tau \gg \tau_{\mathrm{stop}}$ ($5.0$ ps)')]:
        spec = dsam_shape(E_arr, tau_val)
        ax2.plot(E_arr, spec / np.max(spec), color=col, lw=1.8, label=label)

    ax2.set_xlabel(r'Observed Energy $E_{\mathrm{obs}}$ (keV)', fontsize=10)
    ax2.set_ylabel(r'Normalized Intensity (Arbitrary Units)', fontsize=10)
    ax2.set_title(r'(b) DSAM Line Shape vs Stopping Time ($\tau_{\mathrm{stop}} = 0.8$ ps Toy)', fontsize=10.5)
    ax2.set_xlim(992, 1028)
    ax2.set_ylim(-0.02, 1.1)
    ax2.grid(True, ls=':', color='gray', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=8.5)

    fig.tight_layout()

    svg_path = os.path.join(img_dir, 'lifetime-response-rdds-dsam.svg')
    pdf_path = os.path.join(img_dir, 'lifetime-response-rdds-dsam.pdf')

    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")

if __name__ == '__main__':
    main()
