#!/usr/bin/env python3
"""Producer for thesis figure: rotor-local-limits (SVG + PDF).

Author: G81
Generates:
  raw/writing/gpt/A130/these_2023_template/these_template/Img/rotor-local-limits.svg
  raw/writing/gpt/A130/these_2023_template/these_template/Img/rotor-local-limits.pdf
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set standard publication style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 8.5,
    'axes.labelsize': 9.2,
    'axes.titlesize': 9.5,
    'legend.fontsize': 7.8,
    'xtick.labelsize': 8.0,
    'ytick.labelsize': 8.0,
    'lines.linewidth': 1.6,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05
})

gamma_deg = np.linspace(0.5, 59.5, 300)
gamma_rad = np.radians(gamma_deg)

# 1. Irrotational flow moments of inertia (normalized to 4 B beta^2)
J_irr_1 = np.sin(gamma_rad + np.pi/3)**2   # intermediate axis (m) around 30 deg
J_irr_2 = np.sin(np.pi/3 - gamma_rad)**2   # short axis (s) around 30 deg
J_irr_3 = np.sin(gamma_rad)**2            # long axis (l) around 30 deg

# 2. Rigid body moments of inertia (approximate quadrupole expansion for beta=0.3)
beta = 0.3
c = np.sqrt(5.0 / (4.0 * np.pi)) * beta
J_rig_1 = 1.0 - c * np.cos(gamma_rad - 2.0*np.pi/3.0)  # k=1 (short axis s)
J_rig_2 = 1.0 - c * np.cos(gamma_rad - 4.0*np.pi/3.0)  # k=2 (intermediate axis m)
J_rig_3 = 1.0 - c * np.cos(gamma_rad)                  # k=3 (long axis l)

# 3. Wobbling frequency ratio for irrotational flow where J_1 is dominant (gamma in (0, 60))
num_irr = (J_irr_1 - J_irr_2) * (J_irr_1 - J_irr_3)
den_irr = J_irr_2 * J_irr_3
ratio_irr = np.sqrt(np.maximum(0.0, num_irr / np.maximum(den_irr, 1e-6)))

# For rigid body, where J_rig_1 is largest (shortest axis s):
num_rig = (J_rig_1 - J_rig_2) * (J_rig_1 - J_rig_3)
den_rig = J_rig_2 * J_rig_3
ratio_rig = np.sqrt(np.maximum(0.0, num_rig / np.maximum(den_rig, 1e-6)))

# Plotting dual panel
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.6))

# Panel (a): Moments of Inertia
ax1.plot(gamma_deg, J_irr_1, 'b-', label=r'Irrotational $\mathcal{J}_m^{\rm irr}$ (Intermediate)')
ax1.plot(gamma_deg, J_irr_2, 'b--', label=r'Irrotational $\mathcal{J}_s^{\rm irr}$ (Short)')
ax1.plot(gamma_deg, J_irr_3, 'b:', label=r'Irrotational $\mathcal{J}_l^{\rm irr}$ (Long)')

ax1.plot(gamma_deg, J_rig_1, 'r-', alpha=0.85, label=r'Rigid $\mathcal{J}_s^{\rm rig}$ (Short, Maximum)')
ax1.plot(gamma_deg, J_rig_2, 'r--', alpha=0.85, label=r'Rigid $\mathcal{J}_m^{\rm rig}$ (Intermediate)')
ax1.plot(gamma_deg, J_rig_3, 'r:', alpha=0.85, label=r'Rigid $\mathcal{J}_l^{\rm rig}$ (Long)')

ax1.set_xlabel(r'Triaxial angle $\gamma$ [deg]')
ax1.set_ylabel(r'Relative inertia $\mathcal{J}_k / \mathcal{J}_0$')
ax1.set_title('(a) Principal Moments of Inertia Hierarchy')
ax1.set_xlim(0, 60)
ax1.set_ylim(0, 1.35)
ax1.axvline(30, color='gray', linestyle='-.', alpha=0.5)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right', frameon=True, framealpha=0.9)

# Panel (b): Wobbling frequency ratio
ax2.plot(gamma_deg, ratio_irr, 'b-', label=r'Irrotational rotor ($\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$)')
ax2.plot(gamma_deg, ratio_rig, 'r-', alpha=0.85, label=r'Rigid rotor ($\mathcal{J}_s > \mathcal{J}_m > \mathcal{J}_l$)')

ax2.set_xlabel(r'Triaxial angle $\gamma$ [deg]')
ax2.set_ylabel(r'Wobbling ratio $\omega_{\rm wob} / \omega_{\rm rot}$')
ax2.set_title('(b) Pure Rotor Wobbling Frequency Limits')
ax2.set_xlim(0, 60)
ax2.set_ylim(0, 3.5)
ax2.axvline(30, color='gray', linestyle='-.', alpha=0.5)

# Annotate limits
ax2.annotate(r'Equatorial limit ($\gamma \to 0^\circ$)' + '\n' + r'$\omega_{\rm wob} \to 0$ (Free precession)',
             xy=(2, 0.15), xytext=(6, 1.8),
             arrowprops=dict(arrowstyle="->", color="black", lw=0.9),
             fontsize=8, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="gray", alpha=0.9))

ax2.annotate(r'Max triaxiality ($\gamma = 30^\circ$)' + '\n' + r'Wobbling stationary point',
             xy=(30, ratio_irr[len(ratio_irr)//2]), xytext=(31, 2.7),
             arrowprops=dict(arrowstyle="->", color="blue", lw=0.9),
             fontsize=8, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="blue", alpha=0.9))

ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper left', frameon=True, framealpha=0.9)

plt.tight_layout()

# Save paths
img_dir = "raw/writing/gpt/A130/these_2023_template/these_template/Img"
os.makedirs(img_dir, exist_ok=True)
svg_path = os.path.join(img_dir, "rotor-local-limits.svg")
pdf_path = os.path.join(img_dir, "rotor-local-limits.pdf")

plt.savefig(svg_path)
plt.savefig(pdf_path)
plt.close()

print(f"Generated {svg_path} successfully!")
print(f"Generated {pdf_path} successfully!")
