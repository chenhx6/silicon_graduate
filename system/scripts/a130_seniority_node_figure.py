#!/usr/bin/env python3
"""
Pedagogical illustration of quasi-spin seniority node accessibility.
Single-j identical fermions, fixed seniority v = 2, one-body E2 operator.
"""
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def generate_figure():
    out_dir = 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
    os.makedirs(out_dir, exist_ok=True)

    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['mathtext.fontset'] = 'cm'

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.5), dpi=300)

    # Panel 1: Omega = 5 (j = 9/2), v = 2
    # Allowed physical states: n = 2, 4, 6, 8 (all even)
    # Algebraic zero is at n = 5 (odd, physically inaccessible in v=2)
    Omega1 = 5
    v1 = 2
    n_cont1 = np.linspace(2, 8, 200)
    ratio_cont1 = ((Omega1 - n_cont1) / (Omega1 - v1))**2

    n_phys1 = np.array([2, 4, 6, 8])
    ratio_phys1 = ((Omega1 - n_phys1) / (Omega1 - v1))**2

    ax1.plot(n_cont1, ratio_cont1, color='#1f77b4', ls='--', lw=1.8, label=r'Continuous parabola $\left(\frac{\Omega_j - n}{\Omega_j - v}\right)^2$ (Guide to eye)')
    ax1.scatter(n_phys1, ratio_phys1, color='#1f77b4', s=70, zorder=5, label=r'Physical states ($n=v, v+2, \dots$)')
    ax1.scatter([5], [0], facecolors='none', edgecolors='#d62728', s=90, lw=2.0, zorder=6, label=r'Algebraic node $n=\Omega_j=5$ (Unreachable: odd $n$)')
    ax1.axvline(5, color='#d62728', ls=':', lw=1.2, alpha=0.7)

    ax1.set_title(r'(a) $\Omega_j = 5$ ($j = 9/2$), Seniority $v = 2$', fontsize=11, fontweight='bold')
    ax1.set_xlabel(r'Particle number $n$ (even-even: $n \equiv v \ \mathrm{mod}\ 2$)', fontsize=10)
    ax1.set_ylabel(r'Normalized $B(E2; n, v) / B(E2; v, v)$', fontsize=10)
    ax1.set_xticks([2, 3, 4, 5, 6, 7, 8])
    ax1.set_ylim(-0.08, 1.15)
    ax1.grid(True, ls=':', alpha=0.5)
    ax1.legend(loc='upper center', fontsize=8.2, framealpha=0.9)

    ax1.text(5, 0.22, r'Node $n=5$ not in multiplet' + '\n' + r'$B(E2, n=4, 6) = 1/9 \ne 0$',
             ha='center', va='bottom', fontsize=9, color='#d62728',
             bbox=dict(boxstyle="round,pad=0.25", fc="#fff5f5", ec="#d62728", lw=0.8))

    # Panel 2: Omega = 6 (j = 11/2), v = 2
    # Allowed physical states: n = 2, 4, 6, 8, 10 (all even)
    # Algebraic zero is at n = 6 (even, physically accessible!)
    Omega2 = 6
    v2 = 2
    n_cont2 = np.linspace(2, 10, 200)
    ratio_cont2 = ((Omega2 - n_cont2) / (Omega2 - v2))**2

    n_phys2 = np.array([2, 4, 6, 8, 10])
    ratio_phys2 = ((Omega2 - n_phys2) / (Omega2 - v2))**2

    ax2.plot(n_cont2, ratio_cont2, color='#2ca02c', ls='--', lw=1.8, label=r'Continuous parabola $\left(\frac{\Omega_j - n}{\Omega_j - v}\right)^2$ (Guide to eye)')
    ax2.scatter(n_phys2, ratio_phys2, color='#2ca02c', s=70, zorder=5, label=r'Physical states ($n=v, v+2, \dots$)')
    ax2.scatter([6], [0], color='#d62728', s=80, marker='D', zorder=6, label=r'Physical node $n=\Omega_j=6$ (Accessible: even $n$)')
    ax2.axvline(6, color='#d62728', ls=':', lw=1.2, alpha=0.7)

    ax2.set_title(r'(b) $\Omega_j = 6$ ($j = 11/2$), Seniority $v = 2$', fontsize=11, fontweight='bold')
    ax2.set_xlabel(r'Particle number $n$ (even-even: $n \equiv v \ \mathrm{mod}\ 2$)', fontsize=10)
    ax2.set_ylabel(r'Normalized $B(E2; n, v) / B(E2; v, v)$', fontsize=10)
    ax2.set_xticks([2, 4, 6, 8, 10])
    ax2.set_ylim(-0.08, 1.15)
    ax2.grid(True, ls=':', alpha=0.5)
    ax2.legend(loc='upper center', fontsize=8.2, framealpha=0.9)

    ax2.text(6, 0.22, r'Node $n=6$ accessible!' + '\n' + r'$B(E2; n=6) \equiv 0$',
             ha='center', va='bottom', fontsize=9, color='#2ca02c',
             bbox=dict(boxstyle="round,pad=0.25", fc="#f5fff5", ec="#2ca02c", lw=0.8))

    fig.suptitle(r'Quasi-spin Seniority Node Accessibility (Single-$j$ Identical Fermions, Fixed One-Body $E2$ Operator)' + '\n' +
                 r'(Pedagogical algebraic deduction, not experimental data; particle-hole symmetric across $n = \Omega_j$)',
                 fontsize=11.0, y=1.03)

    plt.tight_layout()
    svg_path = os.path.join(out_dir, 'seniority-node-accessibility.svg')
    pdf_path = os.path.join(out_dir, 'seniority-node-accessibility.pdf')
    fig.savefig(svg_path, format='svg', bbox_inches='tight')
    svg_file = Path(svg_path)
    svg_file.write_text(
        "\n".join(line.rstrip() for line in svg_file.read_text().splitlines()) + "\n"
    )
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Generated {svg_path} and {pdf_path}")

if __name__ == '__main__':
    generate_figure()
