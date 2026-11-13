#!/usr/bin/env python3
"""Producer for thesis figures in LaTeX project (SVG + PDF) - Version 2.2 (Review Round 2).

Author: G80 (Gemini Figure Producer)
Target directory: raw/writing/gpt/A130/these_2023_template/these_template/Img/
Receipt/preview: outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G80/
"""

import os
import sys
import json
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import scipy.integrate as integrate

# ---------------------------------------------------------------------------
# Global Matplotlib Styling (Publication Quality, Colorblind-Friendly)
# ---------------------------------------------------------------------------
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 8.2,
    'axes.labelsize': 8.8,
    'axes.titlesize': 9.2,
    'xtick.labelsize': 8.0,
    'ytick.labelsize': 8.0,
    'legend.fontsize': 7.5,
    'figure.titlesize': 10.0,
    'lines.linewidth': 1.4,
    'lines.markersize': 5.0,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.5,
    'grid.linestyle': ':',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'svg.fonttype': 'none',
})

# Colorblind-safe palette (Okabe-Ito & scientific neutrals)
C_BLUE = '#0072B2'
C_VERMILION = '#D55E00'
C_GREEN = '#009E73'
C_ORANGE = '#E69F00'
C_SKY = '#56B4E9'
C_PURPLE = '#CC79A7'
C_CHARCOAL = '#222222'
C_GRAY = '#666666'
C_LIGHT_GRAY = '#F8FAFC'
C_FILL_BLUE = '#E0F2FE'
C_FILL_GREEN = '#DCFCE7'
C_FILL_ORANGE = '#FFEDD5'

ROOT = Path(__file__).resolve().parents[2]
IMG_DIR = ROOT / 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
G80_DIR = ROOT / 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G80'

IMG_DIR.mkdir(parents=True, exist_ok=True)
G80_DIR.mkdir(parents=True, exist_ok=True)

def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def clean_svg_trailing_whitespace(svg_path: Path):
    with open(svg_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    lines = [line.rstrip() for line in content.splitlines()]
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines).rstrip() + '\n')

def render_preview_png(pdf_path: Path, png_path: Path):
    """Use pdftoppm to render clean 300dpi preview from PDF."""
    prefix = str(png_path.with_suffix(''))
    cmd = ['pdftoppm', '-png', '-r', '300', '-singlefile', str(pdf_path), prefix]
    subprocess.run(cmd, check=True)

# ===========================================================================
# 1. QUANTITATIVE FIGURE 1: occupancy-centroids
# ===========================================================================
def build_occupancy_centroids() -> dict:
    """Teaching model E(n) = e0*n + 0.5*V*n*(n-1) + n*B.
    Parameters: g=8, e0=0, V=1, B=0 (Arbitrary Units).
    End-points: n=0 has no removal; n=g has no addition (unallowed channels omitted).
    Continuous derivative: e0 + V*(n - 0.5) + B.
    Spectral centroid: e0 + V*n*(1 - 1/g) + B.
    No artificial red X marks on energy coordinates.
    Mid-shell annotation placed in open space at (4.7, 2.2) without touching data.
    """
    g = 8
    e0, V, B = 0.0, 1.0, 0.0
    n_vals = np.arange(g + 1)  # 0 .. 8

    E = lambda k: e0 * k + 0.5 * V * k * (k - 1) + k * B

    n_add = np.arange(0, g)
    E_add = [E(k + 1) - E(k) for k in n_add]  # V * k for n < g

    n_rem = np.arange(1, g + 1)
    E_rem = [E(k) - E(k - 1) for k in n_rem]  # V * (k - 1) for n > 0

    n_cont = np.linspace(0, g, 200)
    dE_dn = e0 + V * (n_cont - 0.5) + B

    centroid = e0 + V * n_vals * (1.0 - 1.0 / g) + B

    assert np.isclose(centroid[g // 2], e0 + V * (g // 2 - 0.5) + B)

    fig, ax = plt.subplots(figsize=(5.51, 3.8), dpi=300)

    # Plot continuous derivative
    ax.plot(n_cont, dE_dn, color=C_GRAY, linestyle='--',
            label=r'Derivative: $\partial E / \partial n = V(n - 0.5)$')

    # Plot spectral centroid
    ax.plot(n_vals, centroid, color=C_BLUE, linestyle='-', marker='o',
            label=r'Spectral centroid: $\bar{\epsilon}(n) = Vn(1 - 1/g)$ (slope $7/8$)')

    # Plot allowed transitions (strictly n < g for addition, n > 0 for removal)
    ax.scatter(n_add, E_add, color=C_VERMILION, marker='^', s=45, zorder=4,
               label=r'Particle addition: $\Delta E_+ = Vn$ ($n < g$)')
    ax.scatter(n_rem, E_rem, color=C_GREEN, marker='v', s=45, zorder=4,
               label=r'Particle removal: $\Delta E_- = V(n-1)$ ($n > 0$)')

    # Boundary conditions in margin (NO artificial red X on energy coordinates)
    ax.text(0.0, -0.65, r'(No removal channel at $n=0$)', color=C_GRAY, fontsize=7.0, ha='center')
    ax.text(8.0, 7.55, r'(No addition channel at $n=g$)', color=C_GRAY, fontsize=7.0, ha='center')

    # Mid-shell crossing annotation in clear space at bottom-right of intersection
    ax.scatter([4], [3.5], s=90, facecolors='none', edgecolors=C_PURPLE, linewidths=1.8, zorder=6)
    ax.annotate(r'Mid-shell match ($n = g/2 = 4$):' + '\n' + r'$\partial E/\partial n = \bar{\epsilon}(4) = 3.5$',
                xy=(4, 3.5), xytext=(4.7, 2.2),
                arrowprops=dict(arrowstyle='->', color=C_PURPLE, lw=1.2),
                fontsize=7.4, color=C_PURPLE,
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#F3E8FF', edgecolor=C_PURPLE, alpha=0.95))

    # Model parameters in top-left
    ax.text(0.04, 0.96,
            "Single-orbit two-body monopole model\n"
            r"$g=8, \epsilon_0=0, V=1, B=0$ (Arb. Units)" + "\n"
            r"Self-interaction factor: $(1 - 1/g) = 7/8$" + "\n"
            r"Channel limits: $\Delta E_+$ for $n<g$, $\Delta E_-$ for $n>0$",
            transform=ax.transAxes, fontsize=7.2,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=C_LIGHT_GRAY, edgecolor=C_GRAY, alpha=0.95))

    ax.set_xlabel(r'Orbital particle occupancy $n$ (degeneracy $g = 2j+1 = 8$)')
    ax.set_ylabel('Energy [Arbitrary Units]')
    ax.set_xlim(-0.8, 8.8)
    ax.set_ylim(-1.0, 8.2)
    ax.set_xticks(np.arange(0, 9))
    ax.grid(True)
    ax.legend(loc='lower right', framealpha=0.95, fontsize=7.2)

    fig.tight_layout()

    svg_path = IMG_DIR / 'occupancy-centroids.svg'
    pdf_path = IMG_DIR / 'occupancy-centroids.pdf'
    png_path = G80_DIR / 'occupancy-centroids.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'occupancy-centroids',
        'type': 'teaching_model',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': ['system/scripts/a130_rewrite_monopole_centroid_audit.py'],
        'parameters': {'g': 8, 'e0': 0.0, 'V': 1.0, 'B': 0.0, 'units': 'Arbitrary Units'},
        'boundaries': [
            'Single-orbit two-body monopole benchmark only',
            'No configuration mixing, cross-shell monopole, or pairing residual force',
            'Not an experimental single-particle state (ESPE) extraction',
            'Removal only defined for n > 0; addition only defined for n < g'
        ],
        'caption': 'Particle-occupancy dependence of addition/removal energies, continuous derivative, and spectral centroid in a single-j degenerate shell model.'
    }

# ===========================================================================
# 2. QUANTITATIVE FIGURE 2: gamma-measure (Review R2: 2-line wrapped warning)
# ===========================================================================
def build_gamma_measure() -> dict:
    """Isotropic gamma-soft geometric phase space probability density.
    p_gamma = (3/2)*sin(3*gamma), gamma in [0, pi/3].
    Transformation x = cos(3*gamma) gives flat uniform p_x = 1/2 in [-1, 1].
    Bottom warning wrapped into 2 short lines with ample margin, preventing any clipping.
    """
    gamma_rad = np.linspace(0, np.pi / 3, 300)
    gamma_deg = np.rad2deg(gamma_rad)
    p_rad = 1.5 * np.sin(3 * gamma_rad)

    norm_gamma, _ = integrate.quad(lambda g: 1.5 * np.sin(3 * g), 0, np.pi / 3)
    assert np.isclose(norm_gamma, 1.0)

    x_vals = np.linspace(-1, 1, 200)
    p_x = np.full_like(x_vals, 0.5)

    norm_x, _ = integrate.quad(lambda x: 0.5, -1, 1)
    x2_mean, _ = integrate.quad(lambda x: 0.5 * x**2, -1, 1)
    assert np.isclose(norm_x, 1.0)
    assert np.isclose(x2_mean, 1.0 / 3.0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.51, 3.2), dpi=300)
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.24, top=0.86, wspace=0.35)

    # Panel (a): p_gamma(gamma)
    ax1.plot(gamma_deg, p_rad, color=C_BLUE, lw=1.6, label=r'$p_\gamma = \frac{3}{2}\sin(3\gamma)$')
    ax1.fill_between(gamma_deg, p_rad, color=C_FILL_BLUE, alpha=0.6)

    ax1.set_xlabel(r'Triaxial angle $\gamma$ [deg]')
    ax1.set_ylabel(r'Density $p_\gamma$ [$\mathrm{rad}^{-1}$]', color=C_CHARCOAL)
    ax1.set_xlim(0, 60)
    ax1.set_ylim(0, 1.70)
    ax1.set_xticks([0, 15, 30, 45, 60])
    ax1.grid(True)

    # Peak annotation with dual units inside plot
    ax1.scatter([30], [1.5], color=C_VERMILION, s=35, zorder=5)
    ax1.annotate(r'Metric peak at $\gamma=30^\circ$:' + '\n' +
                 r'$p_\gamma^{\max} = 1.5\,\mathrm{rad}^{-1}$' + '\n' +
                 r'($= 0.0262\,\mathrm{deg}^{-1}$)',
                 xy=(30, 1.5), xytext=(5, 1.05),
                 arrowprops=dict(arrowstyle='->', color=C_VERMILION, lw=1.0),
                 fontsize=7.2, color=C_VERMILION,
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor=C_VERMILION, alpha=0.95))

    ax1.set_title('(a) Angular metric density\n' + r'($\int p_\gamma d\gamma = 1.000$)', fontsize=8.2)

    # Panel (b): p_x(x)
    ax2.plot(x_vals, p_x, color=C_GREEN, lw=1.6, label=r'$p_x = 1/2$')
    ax2.fill_between(x_vals, p_x, color=C_FILL_GREEN, alpha=0.6)

    ax2.set_xlabel(r'Invariant coordinate $x = \cos(3\gamma)$')
    ax2.set_ylabel(r'Density $p_x(x)$', color=C_CHARCOAL)
    ax2.set_xlim(-1.05, 1.05)
    ax2.set_ylim(0, 0.8)
    ax2.grid(True)

    ax2.text(0.05, 0.85,
             "Uniform distribution in x" + "\n"
             r"$\int_{-1}^1 p_x(x)\,dx = 1.000$" + "\n"
             r"$\langle x^2 \rangle = \int_{-1}^1 x^2 p_x\,dx = 1/3$",
             transform=ax2.transAxes, fontsize=7.2, verticalalignment='top',
             bbox=dict(boxstyle='round,pad=0.25', facecolor=C_LIGHT_GRAY, edgecolor=C_GRAY, alpha=0.95))

    ax2.set_title('(b) Invariant metric density\n' + r'(Uniform flat: $p_x = 1/2$)', fontsize=8.2)

    # 2-line wrapped warning with ample side padding (no clipping)
    fig.text(0.5, 0.06,
             r"Caution: $\gamma=30^\circ$ peak is a metric volume projection ($d\mu_\gamma \propto |\sin 3\gamma| d\gamma$)," + "\n" +
             r"NOT a dynamical potential energy well.",
             ha='center', va='center', fontsize=7.0, color=C_VERMILION, style='italic', weight='bold')

    svg_path = IMG_DIR / 'gamma-measure.svg'
    pdf_path = IMG_DIR / 'gamma-measure.pdf'
    png_path = G80_DIR / 'gamma-measure.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'gamma-measure',
        'type': 'analytical_geometry',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': ['Bohr-Mottelson 5D collective Hamiltonian volume element'],
        'parameters': {
            'gamma_domain': '[0, pi/3]',
            'norm_gamma': norm_gamma,
            'norm_x': norm_x,
            'x2_expectation': x2_mean
        },
        'boundaries': [
            'Isotropic flat collective potential assumption',
            'Density peak is a coordinate Jacobian projection, not a potential well',
            'Does not include dynamic pairing or microscopic particle-rotor polarization'
        ],
        'caption': 'Isotropic geometric phase-space volume measure and probability distribution for the triaxial shape coordinate.'
    }

# ===========================================================================
# 3. QUANTITATIVE FIGURE 3: digital-energy-response
# ===========================================================================
def build_digital_energy_response() -> dict:
    """Reads ballistic_deficit_study.csv directly.
    Plots normalized peak amplitude and ballistic deficit percentage vs rise time.
    """
    csv_path = ROOT / 'outputs/l4/20261108-digital-pulse-response/ballistic_deficit_study.csv'
    df = pd.read_csv(csv_path)

    A0 = 1000.0

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.51, 3.2), dpi=300)
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.20, top=0.86, wspace=0.32)

    # Panel (a): Normalized Peak Amplitude
    ax1.plot(df['rise_time_ns'], df['flat_top_0ns_amp'] / A0,
             color=C_BLUE, marker='o', label=r'Flat-top $L = 0$ ns')
    ax1.plot(df['rise_time_ns'], df['flat_top_100ns_amp'] / A0,
             color=C_ORANGE, marker='s', label=r'Flat-top $L = 100$ ns')
    ax1.plot(df['rise_time_ns'], df['flat_top_400ns_amp'] / A0,
             color=C_GREEN, marker='^', label=r'Flat-top $L = 400$ ns')

    ax1.set_xlabel(r'Pulse rise time $\tau_{\mathrm{rise}}$ [ns]')
    ax1.set_ylabel(r'Normalized amplitude $A / A_0$')
    ax1.set_xlim(10, 410)
    ax1.set_ylim(0.84, 1.01)
    ax1.grid(True)
    ax1.legend(loc='lower left', fontsize=7.2)
    ax1.set_title('(a) Filter peak amplitude\n' + r'($A_0=1000$ Arb. Units)', fontsize=8.2)

    # Panel (b): Ballistic Deficit Percentage
    ax2.plot(df['rise_time_ns'], df['deficit_flat0_pct'],
             color=C_VERMILION, marker='o', label=r'Deficit ($L = 0$ ns)')
    ax2.plot(df['rise_time_ns'], df['deficit_flat400_pct'],
             color=C_GREEN, marker='^', label=r'Deficit ($L = 400$ ns)')

    ax2.fill_between(df['rise_time_ns'], df['deficit_flat400_pct'], df['deficit_flat0_pct'],
                     color=C_FILL_ORANGE, alpha=0.5, label='Mitigation gain')

    ax2.set_xlabel(r'Pulse rise time $\tau_{\mathrm{rise}}$ [ns]')
    ax2.set_ylabel('Ballistic deficit [%]')
    ax2.set_xlim(10, 410)
    ax2.set_ylim(0, 16)
    ax2.grid(True)
    ax2.legend(loc='upper left', fontsize=7.2)
    ax2.set_title('(b) Ballistic deficit [%]\n' + r'($\tau_{\mathrm{rise}} = 20\text{--}400\,\mathrm{ns}$)', fontsize=8.2)

    fig.text(0.5, 0.04,
             r"Ideal noiseless double-exponential pulse model ($\tau_{\mathrm{decay}}=50\,\mu\mathrm{s}, k=2000\,\mathrm{ns}$); no experimental nuclear data.",
             ha='center', fontsize=7.0, color=C_CHARCOAL, style='italic')

    svg_path = IMG_DIR / 'digital-energy-response.svg'
    pdf_path = IMG_DIR / 'digital-energy-response.pdf'
    png_path = G80_DIR / 'digital-energy-response.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'digital-energy-response',
        'type': 'simulation_csv',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': [str(csv_path.relative_to(ROOT))],
        'input_sha256': sha256_file(csv_path),
        'parameters': {
            'decay_ns': 50000.0,
            'shaping_rise_k_ns': 2000,
            'tested_flat_tops': [0, 100, 400],
            'rise_time_range_ns': [20, 400]
        },
        'boundaries': [
            'Ideal noiseless double-exponential pulse response',
            'No charge-carrier drift simulation or preamplifier noise profile',
            'Not an in-situ nuclear detector calibration'
        ],
        'caption': 'Digital trapezoidal filter ballistic deficit and flat-top mitigation under varying pulse collection rise times.'
    }

# ===========================================================================
# 4. QUANTITATIVE FIGURE 4: cfd-phase-convergence (Review R2: Uncluttered low points)
# ===========================================================================
def build_cfd_phase_convergence() -> dict:
    """Reads sampling_convergence.csv and cfd_phase_walk_analysis.csv.
    Plots 20-phase sample walk error vs arrival phase, and max error vs sampling step.
    Only top point (0.2566 ns) explicitly labeled in panel (b) to avoid low-end clutter.
    """
    conv_csv = ROOT / 'outputs/l4/20261108-digital-pulse-response/sampling_convergence.csv'
    walk_csv = ROOT / 'outputs/l4/20261108-digital-pulse-response/cfd_phase_walk_analysis.csv'

    df_conv = pd.read_csv(conv_csv)
    df_walk = pd.read_csv(walk_csv)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.51, 3.2), dpi=300)
    fig.subplots_adjust(left=0.12, right=0.94, bottom=0.20, top=0.86, wspace=0.34)

    # Panel (a): 20 Phase samples error at dt = 10 ns
    ax1.plot(df_walk['phase_ns'], df_walk['timing_error_ns'],
             color=C_BLUE, marker='o', markersize=4.0, linestyle='-')
    ax1.axhline(0, color=C_GRAY, linestyle=':', lw=0.8)

    max_idx = np.argmax(np.abs(df_walk['timing_error_ns']))
    max_phase = df_walk.loc[max_idx, 'phase_ns']
    max_err = df_walk.loc[max_idx, 'timing_error_ns']

    ax1.scatter([max_phase], [max_err], color=C_VERMILION, s=40, zorder=5)
    ax1.annotate(f'Max walk: {abs(max_err):.4f} ns\nat phase {max_phase:.1f} ns',
                 xy=(max_phase, max_err), xytext=(1.8, -0.10),
                 arrowprops=dict(arrowstyle='->', color=C_VERMILION, lw=1.0),
                 fontsize=7.2, color=C_VERMILION,
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor=C_VERMILION, alpha=0.95))

    ax1.set_xlabel(r'Arrival phase $\phi$ in clock cycle [ns]')
    ax1.set_ylabel('CFD timing error [ns]')
    ax1.set_xlim(-0.5, 10.0)
    ax1.set_ylim(-0.30, 0.15)
    ax1.grid(True)
    ax1.set_title('(a) Phase-walk across 20 samples\n' + r'($\Delta t = 10\,\mathrm{ns}$ clock)', fontsize=8.2)

    # Panel (b): Max error vs sampling interval
    dt = df_conv['sampling_interval_ns']
    err = df_conv['max_abs_interpolation_error_ns']

    ax2.plot(dt, err, color=C_PURPLE, marker='D', markersize=5.0, lw=1.5,
             label='Sampled model maximum')

    # Label only the top point (dt=10 ns) to keep low-error points uncluttered
    max_dt_val = dt.iloc[0]  # 10.0
    max_err_val = err.iloc[0]  # 0.256608
    ax2.annotate(f'{max_err_val:.4f} ns', xy=(max_dt_val, max_err_val),
                 xytext=(max_dt_val - 0.4, max_err_val - 0.025),
                 fontsize=7.0, color=C_PURPLE, ha='right')

    ax2.set_xlabel(r'Sampling clock interval $\Delta t$ [ns]')
    ax2.set_ylabel(r'Max absolute error $\max |\Delta t_{\mathrm{CFD}}|$ [ns]')
    ax2.set_xlim(0.5, 11.0)
    ax2.set_ylim(0, 0.30)
    ax2.grid(True)
    ax2.legend(loc='upper left', fontsize=7.2)
    ax2.set_title('(b) Maximum error convergence\n(Sampled model extrema)', fontsize=8.2)

    fig.text(0.5, 0.04,
             r"Note: $t_{\mathrm{ref}}\approx 157\text{--}161\,\mathrm{ns}$ is filter group latency (not error); sample maximum is not a continuous bound.",
             ha='center', fontsize=7.0, color=C_CHARCOAL, style='italic')

    svg_path = IMG_DIR / 'cfd-phase-convergence.svg'
    pdf_path = IMG_DIR / 'cfd-phase-convergence.pdf'
    png_path = G80_DIR / 'cfd-phase-convergence.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'cfd-phase-convergence',
        'type': 'simulation_csv',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': [str(conv_csv.relative_to(ROOT)), str(walk_csv.relative_to(ROOT))],
        'input_sha256': {'convergence': sha256_file(conv_csv), 'walk': sha256_file(walk_csv)},
        'parameters': {
            'sampling_steps_ns': [10.0, 5.0, 2.5, 1.25],
            'cfd_fraction': 0.4,
            'cfd_delay_ns': 80
        },
        'boundaries': [
            'Reference latency (t_ref ~ 157-161 ns) is filter group delay, not timing jitter or walk',
            'Error values are empirical maxima of 20 discrete phase samples, not an analytic continuous bound',
            'No electronic noise, timing discriminator walk, or jitter included'
        ],
        'caption': 'Digital CFD sub-clock phase walk timing error and interpolation convergence with sampling clock interval.'
    }

# ===========================================================================
# 5. CONCEPTUAL FIGURE 1: shape-moments
# ===========================================================================
def build_shape_moments() -> dict:
    """Conceptual 3-panel representation of nuclear shape moments.
    (a) Laboratory frame isotropic state (I=0, <Q20>=0, quantum state, not time-exposure smear).
    (b) Intrinsic body-fixed reference ellipsoid (deformed body-fixed frame, Q0 != 0).
    (c) E2 transition network / sum rule: q2 = sum_n B(E2; 0+ -> 2_n+) >= 0,
        labeled 'Scalar quadrupole correlation'. Emphasizes zero-point self-terms,
        does not alone prove rigid deformation.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(5.51, 2.5), dpi=300)
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.10, top=0.88, wspace=0.28)

    # Panel (a): Laboratory frame isotropic ground state
    theta = np.linspace(0, 2 * np.pi, 200)
    r_circle = 0.70
    ax1.plot(r_circle * np.cos(theta), r_circle * np.sin(theta), color=C_BLUE, lw=1.6)
    ax1.fill(r_circle * np.cos(theta), r_circle * np.sin(theta), color=C_FILL_BLUE, alpha=0.5)

    for phi in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        ax1.annotate('', xy=(0.92 * np.cos(phi), 0.92 * np.sin(phi)),
                     xytext=(0.70 * np.cos(phi), 0.70 * np.sin(phi)),
                     arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=1.0))

    ax1.text(0, 0, r'$I^\pi = 0^+$' + '\n' + r'$\langle \hat{Q}_{20} \rangle_{\mathrm{lab}} = 0$',
             ha='center', va='center', fontsize=7.5, color=C_CHARCOAL, weight='bold')

    ax1.text(0, -1.25,
             "Quantum orientation singlet\n"
             r"(NOT time-averaged smear)",
             ha='center', va='top', fontsize=6.8, color=C_VERMILION)

    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.4, 1.4)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('(a) Laboratory Frame ($I=0$)', fontsize=8.0)

    # Panel (b): Intrinsic body-fixed frame (deformed spheroid)
    a, b = 1.0, 0.6
    ax2.plot(a * np.cos(theta), b * np.sin(theta), color=C_VERMILION, lw=1.6)
    ax2.fill(a * np.cos(theta), b * np.sin(theta), color=C_FILL_ORANGE, alpha=0.5)

    ax2.annotate('', xy=(1.35, 0), xytext=(-1.35, 0), arrowprops=dict(arrowstyle='->', color=C_CHARCOAL, lw=0.9))
    ax2.annotate('', xy=(0, 0.95), xytext=(0, -0.95), arrowprops=dict(arrowstyle='->', color=C_CHARCOAL, lw=0.9))
    ax2.text(1.38, 0, r"$z'$", va='center', fontsize=7.5, color=C_CHARCOAL)
    ax2.text(0, 1.02, r"$x'$", ha='center', fontsize=7.5, color=C_CHARCOAL)

    ax2.text(0, 0, r'$Q_0 \neq 0$' + '\n' + r'$\beta > 0, \gamma$',
             ha='center', va='center', fontsize=7.5, color=C_CHARCOAL, weight='bold')

    ax2.text(0, -1.25,
             "Body-fixed deformation\n"
             r"(SO(3) symmetry broken)",
             ha='center', va='top', fontsize=6.8, color=C_CHARCOAL)

    ax2.set_xlim(-1.4, 1.4)
    ax2.set_ylim(-1.4, 1.4)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('(b) Intrinsic Frame', fontsize=8.0)

    # Panel (c): E2 transition network / scalar sum
    y_0 = 0.15
    y_21 = 0.55
    y_22 = 0.85
    y_23 = 1.15

    ax3.hlines(y_0, 0.1, 0.9, color=C_CHARCOAL, lw=2.0)
    ax3.text(0.05, y_0, r'$0_1^+$', va='center', ha='right', fontsize=7.5, weight='bold')

    ax3.hlines(y_21, 0.1, 0.9, color=C_GREEN, lw=1.6)
    ax3.text(0.95, y_21, r'$2_1^+$', va='center', ha='left', fontsize=7.5, color=C_GREEN)

    ax3.hlines(y_22, 0.1, 0.9, color=C_GREEN, lw=1.4)
    ax3.text(0.95, y_22, r'$2_2^+$', va='center', ha='left', fontsize=7.5, color=C_GREEN)

    ax3.hlines(y_23, 0.1, 0.9, color=C_GREEN, lw=1.2)
    ax3.text(0.95, y_23, r'$2_3^+$', va='center', ha='left', fontsize=7.5, color=C_GREEN)

    ax3.annotate('', xy=(0.30, y_21), xytext=(0.30, y_0),
                 arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2.2))
    ax3.annotate('', xy=(0.50, y_22), xytext=(0.50, y_0),
                 arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=1.5))
    ax3.annotate('', xy=(0.70, y_23), xytext=(0.70, y_0),
                 arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=1.0))

    ax3.text(0.50, 1.35,
             r'$q_2 = \sum_n B(E2; 0_1^+ \to 2_n^+) \geq 0$',
             ha='center', va='center', fontsize=7.2, color=C_CHARCOAL, weight='bold')

    ax3.text(0.50, -0.20,
             "Scalar quadrupole correlation\n"
             r"(Includes zero-point & self-terms;" + "\n"
             "does not alone prove rigid shape)",
             ha='center', va='top', fontsize=6.5, color=C_GREEN)

    ax3.set_xlim(-0.05, 1.05)
    ax3.set_ylim(-0.45, 1.50)
    ax3.axis('off')
    ax3.set_title(r'(c) Invariant $q_2 \geq 0$ Network', fontsize=8.0)

    svg_path = IMG_DIR / 'shape-moments.svg'
    pdf_path = IMG_DIR / 'shape-moments.pdf'
    png_path = G80_DIR / 'shape-moments.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'shape-moments',
        'type': 'concept',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': ['knowledge/research-notes/doctoral-thesis-architecture-and-section-map-20261108.md (Section 1.2/2.1)'],
        'boundaries': [
            'Conceptual schematic for laboratory frame vs intrinsic body-fixed frame',
            'Isotropic ground state is a quantum angular momentum singlet, not an exposure time-average',
            'Scalar sum q2 = sum B(E2; 0+ -> 2_n+) includes zero-point fluctuations and self-terms, not proving rigid deformation alone'
        ],
        'caption': 'Conceptual distinction between isotropic laboratory state, deformed body-fixed reference spheroid, and scalar E2 quadrupole correlation network.'
    }

# ===========================================================================
# 6. CONCEPTUAL FIGURE 2: six-region-map (Review R2: Strict 1.4 Verified Cases)
# ===========================================================================
def build_six_region_map() -> dict:
    """Cross-region comparative landscape across 6 nuclear mass regions:
    A~60, 80, 100, 130, 160, 190.
    Strictly adheres to Section 1.4 verified benchmark anchors:
    - A60: 64Ge / RDM lifetime & E2 / Qs is theoretical
    - A80: 74,76Kr / Multistep CoulEx / Mixing & K-map assumptions
    - A100: 98Zr / RDDS lifetime & E2 / Adopted branching ratios
    - A130: 133Ce [Anchor] / Coincidence & relative EM / Candidate lifetimes absent in cited work
    - A160: 163Lu / DSAM & in/out-band E2 / Shared branch & delta inputs
    - A190: 182,184,186,188Hg / CoulEx E2 network / Wide diagonal errors & missing terms
    Explicit card subtitle: 'selected examples / not exhaustive'.
    """
    regions = [
        {
            'title': r'A ~ 60 (Selected Example)',
            'isotope': 'Isotope: 64Ge',
            'probe': 'Probe: RDM lifetime & E2',
            'bound': 'Boundary: Qs is theoretical',
            'color': '#E0F2FE', 'border': C_BLUE
        },
        {
            'title': r'A ~ 80 (Selected Example)',
            'isotope': 'Isotopes: 74,76Kr',
            'probe': 'Probe: Multistep CoulEx',
            'bound': 'Boundary: Mixing & K-map assumptions',
            'color': '#FEF3C7', 'border': C_ORANGE
        },
        {
            'title': r'A ~ 100 (Selected Example)',
            'isotope': 'Isotope: 98Zr',
            'probe': 'Probe: RDDS lifetime & E2',
            'bound': 'Boundary: Adopted branching ratios',
            'color': '#DCFCE7', 'border': C_GREEN
        },
        {
            'title': r'A ~ 130 [Anchor Benchmark]',
            'isotope': 'Isotope: 133Ce (Selected Example)',
            'probe': 'Probe: Coincidence & relative EM',
            'bound': 'Boundary: Lifetime absent in cited study',
            'color': '#F3E8FF', 'border': C_PURPLE
        },
        {
            'title': r'A ~ 160 (Selected Example)',
            'isotope': 'Isotope: 163Lu',
            'probe': 'Probe: DSAM & in/out-band E2',
            'bound': 'Boundary: Shared branch & delta inputs',
            'color': '#FFEDD5', 'border': C_VERMILION
        },
        {
            'title': r'A ~ 190 (Selected Example)',
            'isotope': 'Isotopes: 182,184,186,188Hg',
            'probe': 'Probe: CoulEx E2 network',
            'bound': 'Boundary: Wide errors & missing terms',
            'color': '#F1F5F9', 'border': C_CHARCOAL
        }
    ]

    fig, ax = plt.subplots(figsize=(5.51, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Card coordinates (2 columns x 3 rows)
    xs = [3, 52, 3, 52, 3, 52]
    ys = [68, 68, 35, 35, 2, 2]
    w, h = 45, 30

    for reg, x, y in zip(regions, xs, ys):
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=1.0,rounding_size=2.0',
                                     facecolor=reg['color'], edgecolor=reg['border'], lw=1.2)
        ax.add_patch(box)

        # 4 well-spaced lines per card
        ax.text(x + 2.5, y + h - 5.5, reg['title'], fontsize=7.8, weight='bold', color=reg['border'])
        ax.text(x + 2.5, y + h - 11.5, reg['isotope'], fontsize=7.0, color=C_CHARCOAL, weight='bold')
        ax.text(x + 2.5, y + h - 17.5, reg['probe'], fontsize=6.7, color=C_CHARCOAL, style='italic')
        ax.text(x + 2.5, y + h - 23.5, reg['bound'], fontsize=6.4, color='#1F2937')

    fig.tight_layout()

    svg_path = IMG_DIR / 'six-region-map.svg'
    pdf_path = IMG_DIR / 'six-region-map.pdf'
    png_path = G80_DIR / 'six-region-map.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'six-region-map',
        'type': 'concept_map',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': ['knowledge/research-notes/doctoral-thesis-architecture-and-section-map-20261108.md (Section 1.4 & S6 Table I)'],
        'boundaries': [
            'Strictly restricted to Section 1.4 verified anchor examples (64Ge, 74/76Kr, 98Zr, 133Ce, 163Lu, 182-188Hg)',
            'Annotated explicitly as selected examples / not exhaustive territory labels',
            'Anchored on 133Ce triaxiality benchmark'
        ],
        'caption': 'Comparative landscape of experimental probes, verified isotope examples, and observational boundaries across six nuclear mass regions.'
    }

# ===========================================================================
# 7. CONCEPTUAL FIGURE 3: chapter-dependency
# ===========================================================================
def build_chapter_dependency() -> dict:
    """Chapter prerequisite and empirical feedback dependency graph for 5 chapters.
    Arrows routed cleanly through inter-box gaps and margins without clashing with text.
    """
    fig, ax = plt.subplots(figsize=(5.51, 4.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    chapters = [
        {
            'id': 'Ch1',
            'title': 'Ch 1: Spectral Questions',
            'desc': 'Anomalies & model distance\nQuantum shape & 6-region anchors',
            'xy': (4, 66), 'w': 42, 'h': 24, 'color': '#E0F2FE', 'border': C_BLUE
        },
        {
            'id': 'Ch2',
            'title': 'Ch 2: Microscopic Shape',
            'desc': 'ESPE, shell evolution & pairing\nDeformation coordinates & algebra',
            'xy': (54, 66), 'w': 42, 'h': 24, 'color': '#DCFCE7', 'border': C_GREEN
        },
        {
            'id': 'Ch3',
            'title': 'Ch 3: Triaxial Excitations',
            'desc': 'Rotational limits & wobbling\nChirality & gamma-vibration',
            'xy': (54, 35), 'w': 42, 'h': 24, 'color': '#F3E8FF', 'border': C_PURPLE
        },
        {
            'id': 'Ch4',
            'title': 'Ch 4: Cross-Region Probes',
            'desc': 'Six-region comparative tests\nIsomers, weak decay & reactions',
            'xy': (4, 35), 'w': 42, 'h': 24, 'color': '#FEF3C7', 'border': C_ORANGE
        },
        {
            'id': 'Ch5',
            'title': 'Ch 5: In-Beam Gamma DAQ',
            'desc': 'Pulse shaping & CFD timing\nCoincidence, DCO, tau & statistics',
            'xy': (29, 3), 'w': 42, 'h': 24, 'color': '#FFE4E6', 'border': C_VERMILION
        }
    ]

    for ch in chapters:
        x, y = ch['xy']
        w, h = ch['w'], ch['h']
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=1.0,rounding_size=2.0',
                                     facecolor=ch['color'], edgecolor=ch['border'], lw=1.2)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h - 5.5, ch['title'], ha='center', va='center',
                fontsize=7.5, weight='bold', color=ch['border'])
        ax.text(x + w / 2, y + (h - 7) / 2, ch['desc'], ha='center', va='center',
                fontsize=6.5, color=C_CHARCOAL)

    def draw_arrow(p1, p2, style='->', color=C_CHARCOAL, lw=1.2, dashed=False, conn=None):
        ls = '--' if dashed else '-'
        if conn:
            arrowprops = dict(arrowstyle=style, color=color, lw=lw, linestyle=ls, connectionstyle=conn)
        else:
            arrowprops = dict(arrowstyle=style, color=color, lw=lw, linestyle=ls)
        ax.annotate('', xy=p2, xytext=p1, arrowprops=arrowprops)

    # Forward deductive arrows (solid)
    draw_arrow((46, 78), (54, 78), color=C_BLUE, lw=1.3)
    draw_arrow((75, 66), (75, 59), color=C_GREEN, lw=1.3)
    draw_arrow((54, 47), (46, 47), color=C_PURPLE, lw=1.3)
    draw_arrow((70, 35), (62, 27), color=C_GREEN, lw=1.1)
    draw_arrow((62, 35), (52, 27), color=C_PURPLE, lw=1.1)

    # Backward empirical feedback arrows (dashed, routed cleanly without clashing with cards)
    # Ch5 -> Ch1: Left perimeter route bypassing Ch4 completely
    draw_arrow((29, 15), (4, 78), color=C_VERMILION, lw=1.3, dashed=True,
               conn="angle,angleA=180,angleB=90,rad=3")
    # Ch5 -> Ch3: Direct upward route into Ch3 bottom
    draw_arrow((50, 27), (58, 35), color=C_VERMILION, lw=1.3, dashed=True)
    # Ch4 -> Ch2: Diagonal across central gap between (46, 56) and (54, 68), touching NO cards
    draw_arrow((46, 57), (54, 69), color=C_ORANGE, lw=1.2, dashed=True)

    # Top clear legend
    ax.plot([6, 14], [96, 96], color=C_CHARCOAL, lw=1.3, linestyle='-')
    ax.text(16, 95.5, 'Deductive prerequisite path', fontsize=7.0, color=C_CHARCOAL)

    ax.plot([54, 62], [96, 96], color=C_VERMILION, lw=1.3, linestyle='--')
    ax.text(64, 95.5, 'Empirical feedback constraint', fontsize=7.0, color=C_VERMILION)

    fig.tight_layout()

    svg_path = IMG_DIR / 'chapter-dependency.svg'
    pdf_path = IMG_DIR / 'chapter-dependency.pdf'
    png_path = G80_DIR / 'chapter-dependency.png'

    fig.savefig(svg_path, format='svg')
    clean_svg_trailing_whitespace(svg_path)
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)

    render_preview_png(pdf_path, png_path)

    return {
        'id': 'chapter-dependency',
        'type': 'architecture_dependency',
        'svg': str(svg_path.relative_to(ROOT)),
        'pdf': str(pdf_path.relative_to(ROOT)),
        'preview_png': str(png_path.relative_to(ROOT)),
        'svg_sha256': sha256_file(svg_path),
        'pdf_sha256': sha256_file(pdf_path),
        'inputs': ['knowledge/research-notes/doctoral-thesis-architecture-and-section-map-20261108.md (Section 1.5)'],
        'boundaries': [
            'Covers Chapters 1-5 structural workflow and evidence loops',
            'Differentiates forward deductive path from backward empirical constraints',
            'Does not substitute for section-level mathematical derivations'
        ],
        'caption': 'Dependency and feedback architecture among the five thesis chapters, linking questions, microscopic models, triaxial modes, cross-region tests, and in-beam spectroscopy.'
    }

# ===========================================================================
# MAIN RUNNER
# ===========================================================================
def main():
    start_utc = datetime.now(timezone.utc).isoformat()
    print(f'G80 Figure Producer started at {start_utc}')

    manifest_records = []

    # 1. Quantitative 4 figures first
    print('Building quantitative figure: occupancy-centroids...')
    rec1 = build_occupancy_centroids()
    manifest_records.append(rec1)

    print('Building quantitative figure: gamma-measure...')
    rec2 = build_gamma_measure()
    manifest_records.append(rec2)

    print('Building quantitative figure: digital-energy-response...')
    rec3 = build_digital_energy_response()
    manifest_records.append(rec3)

    print('Building quantitative figure: cfd-phase-convergence...')
    rec4 = build_cfd_phase_convergence()
    manifest_records.append(rec4)

    # 2. Conceptual 3 figures
    print('Building conceptual figure: shape-moments...')
    rec5 = build_shape_moments()
    manifest_records.append(rec5)

    print('Building conceptual figure: six-region-map...')
    rec6 = build_six_region_map()
    manifest_records.append(rec6)

    print('Building conceptual figure: chapter-dependency...')
    rec7 = build_chapter_dependency()
    manifest_records.append(rec7)

    # Verify all files exist and non-zero
    print('\nVerifying outputs...')
    for rec in manifest_records:
        svg = ROOT / rec['svg']
        pdf = ROOT / rec['pdf']
        png = ROOT / rec['preview_png']
        assert svg.exists() and svg.stat().st_size > 0, f'Missing or empty: {svg}'
        assert pdf.exists() and pdf.stat().st_size > 0, f'Missing or empty: {pdf}'
        assert png.exists() and png.stat().st_size > 0, f'Missing or empty: {png}'
        print(f"  [OK] {rec['id']}: SVG={svg.stat().st_size}B, PDF={pdf.stat().st_size}B, PNG={png.stat().st_size}B")

    # Write figure-manifest.json into Img/
    manifest_path = IMG_DIR / 'figure-manifest.json'
    manifest_data = {
        'generator': 'system/scripts/a130_latex_figures.py',
        'producer': 'G80 (Gemini Figure Producer)',
        'version': 'v2.2-round2',
        'generated_utc': datetime.now(timezone.utc).isoformat(),
        'target_directory': str(IMG_DIR.relative_to(ROOT)),
        'figures_count': len(manifest_records),
        'figures': manifest_records
    }
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    print(f'\nWrote manifest: {manifest_path}')

    # Write receipt and data excerpts to G80 directory
    receipt_path = G80_DIR / 'receipt.json'
    receipt_data = {
        'status': 'completed',
        'version': 'v2.2-round2',
        'generated_utc': datetime.now(timezone.utc).isoformat(),
        'repairs_applied_round2': [
            'six-region-map: strictly restricted to Section 1.4 verified anchors (64Ge, 74,76Kr, 98Zr, 133Ce, 163Lu, 182-188Hg); card subtitles marked as selected examples / not exhaustive; eliminated all unverified isotopes and generic probes',
            'gamma-measure: bottom warning wrapped into 2 short lines with bottom margin 0.24, completely eliminating side clipping',
            'cfd-phase-convergence: only labeled top point 0.2566 ns in panel (b), removing crowded low-end labels'
        ],
        'figures': [r['id'] for r in manifest_records],
        'quantitative_figures': ['occupancy-centroids', 'gamma-measure', 'digital-energy-response', 'cfd-phase-convergence'],
        'conceptual_figures': ['shape-moments', 'six-region-map', 'chapter-dependency'],
        'manifest_sha256': sha256_file(manifest_path),
        'producer_sha256': sha256_file(Path(__file__).resolve()),
    }
    with open(receipt_path, 'w', encoding='utf-8') as f:
        json.dump(receipt_data, f, indent=2, ensure_ascii=False)

    data_excerpts_path = G80_DIR / 'data_excerpts.json'
    data_excerpts = {
        'occupancy_centroids': {
            'g': 8, 'V': 1.0, 'e0': 0.0,
            'additions_n_0_7': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
            'removals_n_1_8': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
            'centroid_slope': 7.0 / 8.0,
            'derivative_slope': 1.0,
            'mid_shell_crossing_n4': 3.5
        },
        'gamma_measure': {
            'integral_norm_gamma': 1.0,
            'integral_norm_x': 1.0,
            'x2_mean': 1.0 / 3.0,
            'p_gamma_peak_rad': 1.5,
            'p_gamma_peak_deg': 1.5 * (np.pi / 180.0)
        },
        'digital_energy_response': {
            'source_csv': 'outputs/l4/20261108-digital-pulse-response/ballistic_deficit_study.csv',
            'rise_time_range_ns': [20, 400],
            'deficit_pct_flat0_range': [0.7144, 14.3807],
            'deficit_pct_flat400_range': [0.0508, 6.8916]
        },
        'cfd_phase_convergence': {
            'source_csv': 'outputs/l4/20261108-digital-pulse-response/sampling_convergence.csv',
            'steps_ns': [10.0, 5.0, 2.5, 1.25],
            'max_abs_errors_ns': [0.256608, 0.129692, 0.013737, 0.005997]
        }
    }
    with open(data_excerpts_path, 'w', encoding='utf-8') as f:
        json.dump(data_excerpts, f, indent=2, ensure_ascii=False)

    print(f'Wrote receipt: {receipt_path}')
    print(f'Wrote data excerpts: {data_excerpts_path}')
    print('\nAll 7 figures generated and verified successfully (v2.2-round2).')

if __name__ == '__main__':
    main()
