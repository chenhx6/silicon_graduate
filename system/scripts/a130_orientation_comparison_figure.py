#!/usr/bin/env python3
"""Producer for thesis figure: orientation-comparison-modes (SVG + PDF).

Author: G87
Section: 4.4 A~130、稀土与重区的取向对照
Generates:
  raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.svg
  raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.pdf
Data sources:
  A. Görgen et al., Phys. Rev. C 69, 031301(R) (2004), Tables I & II (163Lu TSD1 & TSD2).
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set standard publication style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 8.5,
    'axes.labelsize': 9.2,
    'axes.titlesize': 9.8,
    'legend.fontsize': 7.8,
    'xtick.labelsize': 8.0,
    'ytick.labelsize': 8.0,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05
})

fig = plt.figure(figsize=(10.6, 8.2))
grid = fig.add_gridspec(2, 2, height_ratios=[1.2, 1.0])
axes = [fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1]),
        fig.add_subplot(grid[1, :])]

# -------------------------------------------------------------------------
# Panel (a): 163Lu In-band Transition Quadrupole Moments Qt (Görgen 2004 Table I)
# -------------------------------------------------------------------------
ax = axes[0]

# TSD1: I_i = 41/2, 45/2, 49/2, 53/2, 57/2, 61/2, 65/2, 69/2
I_tsd1 = np.array([20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5])
Qt_tsd1 = np.array([9.93, 9.34, 8.32, 8.93, 8.37, 7.45, 7.37, 7.63])
err_plus_tsd1 = np.array([1.14, 0.72, 0.47, 0.38, 0.54, 0.49, 0.82, 1.46])
err_minus_tsd1 = np.array([0.99, 0.65, 0.42, 0.35, 0.49, 0.43, 0.57, 0.88])

# TSD2: I_i = 47/2, 51/2, 55/2, 59/2, 63/2, 67/2, 71/2
I_tsd2 = np.array([23.5, 25.5, 27.5, 29.5, 31.5, 33.5, 35.5])
Qt_tsd2 = np.array([8.51, 8.67, 8.88, 7.82, 7.91, 6.66, 6.68])
err_plus_tsd2 = np.array([0.95, 0.66, 0.83, 1.66, 1.32, 1.09, 1.70])
err_minus_tsd2 = np.array([0.73, 0.53, 0.64, 1.15, 0.84, 0.76, 1.02])

ax.errorbar(I_tsd1, Qt_tsd1, yerr=[err_minus_tsd1, err_plus_tsd1],
            fmt='s', color='#1565c0', ecolor='#1565c0', elinewidth=1.2, capsize=3,
            label=r'$^{163}\mathrm{Lu}$ TSD1 ($n_w=0$)', markersize=5)
ax.errorbar(I_tsd2, Qt_tsd2, yerr=[err_minus_tsd2, err_plus_tsd2],
            fmt='o', color='#c62828', ecolor='#c62828', elinewidth=1.2, capsize=3,
            label=r'$^{163}\mathrm{Lu}$ TSD2 ($n_w=1$)', markersize=5)

ax.set_xlabel(r'Initial Spin $I_i$ [$\hbar$]')
ax.set_ylabel(r'Transition Quadrupole Moment $Q_t$ [b]')
ax.set_title(r'(a) $^{163}\mathrm{Lu}$ In-Band $Q_t$ (Görgen 2004 Table I)', fontweight='bold')
ax.set_ylim(4.5, 12.0)
ax.set_xlim(19.0, 37.0)
ax.text(0.04, 0.96, r'Observed range $\approx 6.7$--$9.9\ \mathrm{b}$',
        transform=ax.transAxes, va='top', fontsize=8)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='lower left', framealpha=0.9)

# -------------------------------------------------------------------------
# Panel (b): 163Lu Interband Connecting Transitions (Görgen 2004 Table II)
# -------------------------------------------------------------------------
ax = axes[1]

# TSD2 -> TSD1: I_i = 47/2, 51/2, 55/2, 59/2, 63/2
I_inter = np.array([23.5, 25.5, 27.5, 29.5, 31.5])
Be2_inter = np.array([0.54, 0.54, 0.70, 0.65, 0.66])
err_plus_be2 = np.array([0.13, 0.09, 0.18, 0.34, 0.29])
err_minus_be2 = np.array([0.11, 0.08, 0.15, 0.26, 0.24])

ax.errorbar(I_inter, Be2_inter, yerr=[err_minus_be2, err_plus_be2],
            fmt='D', color='#2e7d32', ecolor='#2e7d32', elinewidth=1.4, capsize=3.5,
            label=r'$B(E2; \mathrm{TSD2} \to \mathrm{TSD1})$', markersize=5.5)

ax.set_xlabel(r'Initial Spin $I_i$ [$\hbar$]')
ax.set_ylabel(r'Interband $B(E2)$ [$e^2\mathrm{b}^2$]')
ax.set_title(r'(b) $^{163}\mathrm{Lu}$ Interband $B(E2)$ (Görgen Table II)', fontweight='bold')
ax.set_ylim(0.0, 1.2)
ax.set_xlim(21.5, 33.5)
# Correct Weisskopf unit for A=163: B_W(E2) = 0.05940 * A^(4/3) e^2 fm^4 ≈ 53.0 e^2 fm^4 = 0.0053 e^2 b^2
ax.axhline(0.0053, color='#8d6e63', linestyle='--', label=r'Single-particle $B_{\mathrm{W}}(E2) \approx 0.0053\ e^2\mathrm{b}^2$')
ax.text(27.5, 0.88, r'Collective $E2$ Enhancement' + '\n' + r'$B(E2)_{\mathrm{out}} \approx 100$--$130\ \mathrm{W.u.}$',
        ha='center', fontsize=7.8, color='#1b5e20', bbox=dict(boxstyle='round,pad=0.3', fc='#e8f5e9', ec='#2e7d32', lw=1.0))
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='lower right', framealpha=0.9)
ax.text(0.04, 0.96, r'$E2/M1$ separation adopts historical $\delta=-3.10$',
        transform=ax.transAxes, va='top', fontsize=8)

# -------------------------------------------------------------------------
# Panel (c): Schematic Geometry of Orientation Modes
# -------------------------------------------------------------------------
ax = axes[2]
ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-0.4, 5.8)
ax.axis('off')
ax.set_title(r'(c) Orientation Modes & Alignment Geometry', fontweight='bold', pad=10)

# Mode 1: Transverse Wobbling (TW)
rect_tw = patches.FancyBboxPatch((0.1, 4.1), 4.8, 1.45, boxstyle="round,pad=0.08",
                                 ec="#1565c0", fc="#e3f2fd", lw=1.3)
ax.add_patch(rect_tw)
ax.text(0.3, 5.25, r'Transverse Wobbling (TW): $^{163}\mathrm{Lu}$, $^{165,167}\mathrm{Lu}$ TSD', fontsize=8.0, fontweight='bold', color="#0d47a1")
ax.text(0.3, 4.8, r'Model geometry: $\mathbf{j}$ mainly on $s$; maximum inertia on $m$; $\mathbf{R}$ need not be exactly on $m$', fontsize=8.5, color="#1565c0")
ax.text(0.3, 4.35, r'High core spin $R \sim 15$--$30\hbar \gg 1$; Strong collective $\Delta I = 1$ $E2$ linking transitions', fontsize=7.0, color="#424242")

# Mode 2: High-K Precession (Shimizu 2005)
rect_prec = patches.FancyBboxPatch((0.1, 2.3), 4.8, 1.45, boxstyle="round,pad=0.08",
                                   ec="#e65100", fc="#fff3e0", lw=1.3)
ax.add_patch(rect_prec)
ax.text(0.3, 3.45, r'High-$K$ Precession: $^{178}\mathrm{W}$, $^{178,179}\mathrm{Hf}$ (Axial Limit)', fontsize=8.0, fontweight='bold', color="#bf360c")
ax.text(0.3, 3.0, r'Axially symmetric limit ($\gamma \to 0$); Single-particle alignments build $K$ on symmetry axis', fontsize=7.2, color="#d84315")
ax.text(0.3, 2.55, r'Axial shape constraint $R_3=0$; fixed-$K$ rotational band remains; first gap $\hbar^2(K+1)/\mathcal{J}_\perp$', fontsize=8.5, color="#424242")

# Mode 3: Planar Rotation / Re-alignment (135Pr & 187Au re-analysis)
rect_pr = patches.FancyBboxPatch((0.1, 0.5), 4.8, 1.45, boxstyle="round,pad=0.08",
                                 ec="#4a148c", fc="#f3e5f5", lw=1.3)
ax.add_patch(rect_pr)
ax.text(0.3, 1.65, r'Competing interpretations: $^{135}\mathrm{Pr}$ (Lv 2022), $^{187}\mathrm{Au}$ (Guo 2022)', fontsize=8.5, fontweight='bold', color="#4a148c")
ax.text(0.3, 1.2, r'Small-$|\delta|$ solutions (747 keV: $R_{\mathrm{ac}}=0.37$, $\delta=-0.47$); $M1$ fractions derived from $\delta$', fontsize=8.5, color="#6a1b9a")
ax.text(0.3, 0.75, r'Single-particle re-alignment towards rotation axis / $\gamma$-soft IBFM / shape coexistence', fontsize=7.0, color="#424242")

plt.tight_layout()
os.makedirs("raw/writing/gpt/A130/these_2023_template/these_template/Img", exist_ok=True)
plt.savefig("raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.pdf")
plt.savefig("raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.svg")
print("orientation-comparison-modes figure updated successfully.")
