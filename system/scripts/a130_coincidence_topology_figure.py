#!/usr/bin/env python3
"""
a130_coincidence_topology_figure.py
Didactic model of coincidence gating and level scheme topology.
Generates Img/coincidence-level-scheme-model.svg and Img/coincidence-level-scheme-model.pdf.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import hashlib

def main():
    img_dir = 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
    os.makedirs(img_dir, exist_ok=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300, gridspec_kw={'width_ratios': [1, 1.2]})

    ax1.hlines([0, 200, 600], 0.1, 0.5, colors='black', lw=2)
    ax1.text(0.08, 0, r'$0^+$', fontsize=10, va='center', ha='right')
    ax1.text(0.08, 200, r'$2_1^+$', fontsize=10, va='center', ha='right')
    ax1.text(0.08, 600, r'$4_1^+$', fontsize=10, va='center', ha='right')

    ax1.hlines([850, 1100], 0.55, 0.9, colors='#1f77b4', lw=2)
    ax1.text(0.92, 850, r'$2_2^+$ (Side)', fontsize=10, va='center', ha='left', color='#1f77b4')
    ax1.text(0.92, 1100, r'$4_2^+$ (Side)', fontsize=10, va='center', ha='left', color='#1f77b4')

    ax1.annotate('', xy=(0.25, 0), xytext=(0.25, 200), arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax1.text(0.23, 100, r'$\gamma_1 (200)$', fontsize=9, ha='right', va='center')

    ax1.annotate('', xy=(0.35, 200), xytext=(0.35, 600), arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax1.text(0.33, 400, r'$\gamma_2 (400)$', fontsize=9, ha='right', va='center')

    ax1.annotate('', xy=(0.45, 600), xytext=(0.60, 1100), arrowprops=dict(arrowstyle="->", lw=1.5, color='#ff7f0e'))
    ax1.text(0.48, 800, r'$\gamma_3 (500)$', fontsize=9, ha='right', va='center', color='#ff7f0e')

    ax1.annotate('', xy=(0.48, 600), xytext=(0.65, 850), arrowprops=dict(arrowstyle="->", lw=1.2, color='#d62728', ls='--'))
    ax1.text(0.60, 710, r'$\gamma_a (250)$', fontsize=8, color='#d62728')

    ax1.annotate('', xy=(0.48, 200), xytext=(0.75, 850), arrowprops=dict(arrowstyle="->", lw=1.2, color='#2ca02c'))
    ax1.text(0.72, 500, r'$\gamma_b (650)$' '\n' r'crossover', fontsize=8, color='#2ca02c')

    ax1.annotate('', xy=(0.75, 850), xytext=(0.75, 1100), arrowprops=dict(arrowstyle="->", lw=1.2, color='#9467bd'))
    ax1.text(0.78, 980, r'$\gamma_c (250)$', fontsize=8, color='#9467bd')

    ax1.set_xlim(0.0, 1.1)
    ax1.set_ylim(-50, 1200)
    ax1.axis('off')
    ax1.set_title(r'(a) Model Level Topology & Cascade Paths', fontsize=10)

    ax2.text(0.05, 0.90, r'Coincidence Matrix Gating Rules:', fontsize=10, weight='bold')
    ax2.text(0.05, 0.78, r'$\bullet$ Gate on $\gamma_1 (200\ \mathrm{keV})$:', fontsize=9, color='black')
    ax2.text(0.10, 0.70, r'Sees coincident $\gamma_2 (400)$, $\gamma_3 (500)$, $\gamma_a (250)$, $\gamma_b (650)$, $\gamma_c (250)$', fontsize=8.5)
    ax2.text(0.05, 0.58, r'$\bullet$ Gate on $\gamma_2 (400\ \mathrm{keV})$ (Intraband):', fontsize=9, color='black')
    ax2.text(0.10, 0.50, r'Sees $\gamma_1 (200)$, $\gamma_3 (500)$, $\gamma_a (250)$, $\gamma_c (250)$;', fontsize=8.5)
    ax2.text(0.10, 0.43, r'Anti-coincident with crossover $\gamma_b (650)$ (parallel bypass)!', fontsize=8.5, color='#2ca02c')
    ax2.text(0.05, 0.31, r'$\bullet$ Gate on Crossover $\gamma_b (650\ \mathrm{keV})$:', fontsize=9, color='#2ca02c')
    ax2.text(0.10, 0.23, r'Sees $\gamma_1 (200)$ and $\gamma_c (250)$;', fontsize=8.5)
    ax2.text(0.10, 0.16, r'Anti-coincident with $\gamma_2 (400)$, $\gamma_a (250)$, and $\gamma_3 (500)$!', fontsize=8.5, color='#d62728')
    ax2.text(0.05, 0.05, r'$\bullet$ Multiplet Warning: $\gamma_a$ & $\gamma_c$ both $250\ \mathrm{keV}$ require gate differentiation.', fontsize=8, style='italic', color='#7f7f7f')

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_title(r'(b) Gated Coincidence & Anti-coincidence Logic', fontsize=10)

    fig.tight_layout()

    svg_path = os.path.join(img_dir, 'coincidence-level-scheme-model.svg')
    pdf_path = os.path.join(img_dir, 'coincidence-level-scheme-model.pdf')

    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")

if __name__ == '__main__':
    main()
