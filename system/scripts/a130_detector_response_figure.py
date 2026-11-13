#!/usr/bin/env python3
"""
a130_detector_response_figure.py
Didactic educational simulation of HPGe gamma-ray detector response.
Generates Img/detector-response-simulation.svg and Img/detector-response-simulation.pdf.
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

    np.random.seed(42)
    E = np.linspace(50, 1650, 1600)

    E0 = 1500.0 # keV
    m_e = 511.0 # keV
    E_c = E0 * (2 * E0 / m_e) / (1 + 2 * E0 / m_e) # 1281.686... keV
    E_bs = E0 - E_c # 218.314... keV
    E_sep = E0 - m_e # 989 keV
    E_dep = E0 - 2 * m_e # 478 keV
    sigma = 1.5 # keV (FWHM ~ 3.5 keV)

    def gaussian(x, mu, sig, amp):
        return amp * np.exp(-0.5 * ((x - mu) / sig)**2)

    fep = gaussian(E, E0, sigma, 10000.0)
    sep = gaussian(E, E_sep, sigma, 600.0)
    dep = gaussian(E, E_dep, sigma, 1200.0)
    ann = gaussian(E, m_e, sigma * 1.2, 1500.0)
    bs = gaussian(E, E_bs, sigma * 6.0, 1800.0)

    compton = np.zeros_like(E)
    mask = (E > 50) & (E <= E_c)
    compton[mask] = 800.0 * (1.0 + 0.3 * (E[mask] / E_c)**2 + 1.2 * np.exp(-((E[mask] - E_c) / 40.0)**2))
    compton[(E > E_c) & (E < E0)] = 200.0 * np.exp(-((E[(E > E_c) & (E < E0)] - E_c) / 50.0))

    raw_spectrum = fep + sep + dep + ann + bs + compton + np.random.normal(0, 15, size=len(E))
    raw_spectrum = np.clip(raw_spectrum, 1, None)

    bgo_suppressed = fep * 0.98 + sep * 0.35 + dep * 0.2 + ann * 0.4 + bs * 0.25 + compton * 0.22 + np.random.normal(0, 8, size=len(E))
    bgo_suppressed = np.clip(bgo_suppressed, 1, None)

    clover_addback = fep * 1.45 + sep * 0.5 + dep * 0.3 + ann * 0.5 + bs * 0.35 + compton * 0.65 + np.random.normal(0, 12, size=len(E))
    clover_addback = np.clip(clover_addback, 1, None)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.plot(E, raw_spectrum, label=r'Raw HPGe Response (Single Crystal)', color='black', alpha=0.7, lw=1.0)
    ax.plot(E, clover_addback, label=r'Clover Add-back Mode (Inter-crystal Summing)', color='#1f77b4', lw=1.2)
    ax.plot(E, bgo_suppressed, label=r'BGO Anti-Compton Veto (Active Shielded)', color='#d62728', lw=1.2)

    ax.set_yscale('log')
    ax.set_ylim(5, 30000)
    ax.set_xlim(80, 1600)

    ax.set_xlabel(r'Observed Energy $E_{\mathrm{obs}}$ (keV)', fontsize=11)
    ax.set_ylabel(r'Counts / Channel (Arbitrary Units)', fontsize=11)
    ax.set_title(r'Educational $\gamma$-Ray Response Model ($E_\gamma = 1500$ keV, Synthetic Data)', fontsize=12)

    ax.annotate(r'Full Energy Peak (FEP)' '\n' r'$E_0 = 1500$ keV', xy=(E0, 11000), xytext=(E0 - 320, 18000),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)
    ax.annotate(r'Compton Edge' '\n' r'$E_c \approx 1281.7$ keV', xy=(E_c, 1800), xytext=(E_c - 200, 4500),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)
    ax.annotate(r'Single Escape (SEP)' '\n' r'$E_0 - 511 = 989$ keV', xy=(E_sep, 900), xytext=(E_sep - 220, 2200),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)
    ax.annotate(r'Double Escape (DEP)' '\n' r'$E_0 - 1022 = 478$ keV', xy=(E_dep, 1400), xytext=(E_dep - 200, 3500),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)
    ax.annotate(r'511 keV' '\n' r'Annihilation', xy=(m_e, 1600), xytext=(m_e + 40, 5000),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)
    ax.annotate(r'Backscatter' '\n' r'$E_{\mathrm{bs}} \approx 218.3$ keV', xy=(E_bs, 1900), xytext=(E_bs + 40, 7000),
                arrowprops=dict(arrowstyle="->", color='black', lw=0.8), fontsize=9)

    ax.legend(frameon=True, loc='lower left', fontsize=9)
    ax.grid(True, which='both', ls=':', color='gray', alpha=0.4)

    fig.tight_layout()

    svg_path = os.path.join(img_dir, 'detector-response-simulation.svg')
    pdf_path = os.path.join(img_dir, 'detector-response-simulation.pdf')

    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")

if __name__ == '__main__':
    main()
