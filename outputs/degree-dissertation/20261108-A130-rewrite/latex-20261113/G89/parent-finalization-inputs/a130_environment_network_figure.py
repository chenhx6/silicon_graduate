#!/usr/bin/env python3
"""Producer for thesis figure: environment-network-pathways (SVG + PDF).

Author: G87
Section: 4.8 环境和形成路径怎样改变可见性
Generates:
  raw/writing/gpt/A130/these_2023_template/these_template/Img/environment-network-pathways.svg
  raw/writing/gpt/A130/these_2023_template/these_template/Img/environment-network-pathways.pdf
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.4))

# -------------------------------------------------------------
# Panel (a): Thermal open network with intermediate bridge state
# -------------------------------------------------------------
ax = axes[0]
ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-0.5, 6.0)
ax.axis('off')
ax.set_title(r'(a) Thermal Open Network: Bridge & Timescales', fontsize=9.8, fontweight='bold', pad=10)

# Ground cluster box
rect_g = patches.FancyBboxPatch((0.1, 0.2), 1.6, 2.8, boxstyle="round,pad=0.1",
                                ec="#2b5c8f", fc="#eaf2f8", lw=1.5)
ax.add_patch(rect_g)
ax.text(0.9, 2.7, 'Cluster g (Ground band)', ha='center', va='center', fontsize=8.8, fontweight='bold', color="#1b3b5a")
ax.text(0.9, 2.3, r'e.g. $K^\pi = 0^+$ ($^{176}$Lu: $7^-$)', ha='center', va='center', fontsize=7.5, color="#2b5c8f")
# levels in g
ax.hlines([0.5, 1.0, 1.5, 2.0], 0.3, 1.5, colors='#2b5c8f', lw=1.8)
ax.text(1.55, 0.5, r'$0^+$', fontsize=7.5, va='center')
ax.text(1.55, 1.0, r'$2^+$', fontsize=7.5, va='center')
ax.text(1.55, 1.5, r'$4^+$', fontsize=7.5, va='center')
ax.text(1.55, 2.0, r'$6^+$', fontsize=7.5, va='center')
ax.text(0.9, 0.05, r'$\tau_{\mathrm{intra}} \sim 0.1$--$1\ \mathrm{ns}$', ha='center', fontsize=7.5, color="#1b3b5a")

# Isomer cluster box
rect_m = patches.FancyBboxPatch((3.3, 0.2), 1.6, 2.8, boxstyle="round,pad=0.1",
                                ec="#8f2b2b", fc="#fdeded", lw=1.5)
ax.add_patch(rect_m)
ax.text(4.1, 2.7, 'Cluster m (Isomer band)', ha='center', va='center', fontsize=8.8, fontweight='bold', color="#5a1b1b")
ax.text(4.1, 2.3, r'e.g. High-$K$ ($^{176}$Lu: $1^-$)', ha='center', va='center', fontsize=7.5, color="#8f2b2b")
# levels in m
ax.hlines([0.8, 1.3, 1.8, 2.3], 3.5, 4.7, colors='#8f2b2b', lw=1.8)
ax.text(4.75, 0.8, r'$K^\pi$', fontsize=7.5, va='center')
ax.text(4.75, 1.3, r'$K+1$', fontsize=7.5, va='center')
ax.text(4.75, 1.8, r'$K+2$', fontsize=7.5, va='center')
ax.text(4.75, 2.3, r'$K+3$', fontsize=7.5, va='center')
ax.text(4.1, 0.05, r'$\tau_{\mathrm{intra}} \sim 0.1$--$1\ \mathrm{ns}$', ha='center', fontsize=7.5, color="#5a1b1b")

# Direct hindered transition
ax.annotate('', xy=(3.3, 0.9), xytext=(1.7, 0.6),
            arrowprops=dict(arrowstyle="<->", color="gray", lw=1.2, ls="--"))
ax.text(2.5, 0.55, r'Direct EM: $\Delta K$-hindered' + '\n' + r'$\lambda_{g \leftrightarrow m} \approx 0$',
        ha='center', va='center', fontsize=7.2, color="gray")

# Intermediate Bridge State (IMS)
rect_i = patches.FancyBboxPatch((1.7, 4.2), 1.6, 1.2, boxstyle="round,pad=0.1",
                                ec="#2e7d32", fc="#e8f5e9", lw=1.5)
ax.add_patch(rect_i)
ax.text(2.5, 5.1, 'Bridge State |i>', ha='center', va='center', fontsize=8.8, fontweight='bold', color="#1b5e20")
ax.hlines([4.5], 1.9, 3.1, colors='#2e7d32', lw=2.2)
ax.text(2.5, 4.3, r'Mixed $K$ / High $E_x$', ha='center', va='center', fontsize=7.5, color="#2e7d32")

# Thermal photon bath transitions
ax.annotate('', xy=(2.0, 4.2), xytext=(1.1, 3.0),
            arrowprops=dict(arrowstyle="<->", color="#1565c0", lw=1.6))
ax.text(1.2, 3.8, r'$\lambda_{g \leftrightarrow i}(T)$', fontsize=7.8, color="#1565c0", ha='right')

ax.annotate('', xy=(3.0, 4.2), xytext=(3.9, 3.0),
            arrowprops=dict(arrowstyle="<->", color="#c62828", lw=1.6))
ax.text(3.8, 3.8, r'$\lambda_{m \leftrightarrow i}(T)$', fontsize=7.8, color="#c62828", ha='left')

# Losses / Sinks
ax.annotate('', xy=(0.9, -0.4), xytext=(0.9, 0.2),
            arrowprops=dict(arrowstyle="->", color="#424242", lw=1.5))
ax.text(0.9, -0.45, r'Sink $D_g$ ($\beta$ / $n$ capture)', ha='center', va='top', fontsize=7.5)

ax.annotate('', xy=(4.1, -0.4), xytext=(4.1, 0.2),
            arrowprops=dict(arrowstyle="->", color="#424242", lw=1.5))
ax.text(4.1, -0.45, r'Sink $D_m$ ($\beta$ / decay)', ha='center', va='top', fontsize=7.5)


# -------------------------------------------------------------
# Panel (b): Electronic and Nuclear Channels (NEEC vs NEIES vs IC)
# -------------------------------------------------------------
ax = axes[1]
ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-0.5, 6.0)
ax.axis('off')
ax.set_title(r'(b) Nuclear & Atomic Electronic Channels', fontsize=9.8, fontweight='bold', pad=10)

# Nuclear two levels (left side of panel)
ax.hlines([1.0, 4.2], 0.2, 1.8, colors=['#37474f', '#37474f'], lw=2.5)
ax.text(0.2, 0.75, r'Initial state $|i\rangle$ (e.g. Isomer)', fontsize=7.8, color='#37474f')
ax.text(0.2, 4.45, r'Triggered state $|t\rangle$ (or G.S.)', fontsize=7.8, color='#37474f')
ax.text(1.0, 2.6, r'$\Delta E_{\mathrm{nuc}}$', ha='center', va='center', fontsize=8.5, fontweight='bold')
ax.annotate('', xy=(1.0, 4.1), xytext=(1.0, 1.1),
            arrowprops=dict(arrowstyle="<->", color="#37474f", lw=1.2, ls=":"))

# Atomic electron levels (right side of panel)
# 1. Internal Conversion (IC)
rect_ic = patches.FancyBboxPatch((2.2, 4.45), 2.8, 1.05, boxstyle="round,pad=0.06",
                                 ec="#e65100", fc="#fff3e0", lw=1.2)
ax.add_patch(rect_ic)
ax.text(2.3, 5.25, r'IC: $|t\rangle \to |i\rangle + e^-$ (Bound $\to$ Continuum)', fontsize=7.4, color="#bf360c", fontweight='bold')
ax.text(2.3, 4.90, r'$E_e = \Delta E_{\mathrm{nuc}} - E_b > 0$; needs bound $e^-$', fontsize=6.9, color="#424242")
ax.text(2.3, 4.60, r'Suppressed in stripped ions or bandgap', fontsize=6.8, color="#d84315")

# 2. NEEC (Nuclear Excitation by Electron Capture)
rect_neec = patches.FancyBboxPatch((2.2, 3.15), 2.8, 1.15, boxstyle="round,pad=0.06",
                                  ec="#1565c0", fc="#e3f2fd", lw=1.2)
ax.add_patch(rect_neec)
ax.text(2.3, 4.05, r'NEEC: Free $e^- + |i\rangle \to [e^-_b] + |t\rangle$ (Cont $\to$ Bound)', fontsize=7.4, color="#0d47a1", fontweight='bold')
ax.text(2.3, 3.70, r'Resonant: $E_e + E_b = \Delta E_{\mathrm{nuc}} \equiv E_t - E_i$', fontsize=7.0, color="#1565c0", fontweight='bold')
ax.text(2.3, 3.40, r'Time-reversal of IC; requires vacant shell', fontsize=6.8, color="#424242")

# 3. NEET (Nuclear Excitation by Electronic Transition)
rect_neet = patches.FancyBboxPatch((2.2, 1.85), 2.8, 1.15, boxstyle="round,pad=0.06",
                                  ec="#00695c", fc="#e0f2f1", lw=1.2)
ax.add_patch(rect_neet)
ax.text(2.3, 2.75, r'NEET: Bound $e^-_1 \to e^-_2$ couples to $|i\rangle \to |t\rangle$', fontsize=7.4, color="#004d40", fontweight='bold')
ax.text(2.3, 2.40, r'Bound-bound: $\Delta E_{\mathrm{el}} \approx \Delta E_{\mathrm{nuc}}$', fontsize=7.0, color="#00695c", fontweight='bold')
ax.text(2.3, 2.10, r'Virtual photon exchange with bound vacancies', fontsize=6.8, color="#424242")

# 4. NEIES (Inelastic Electron Scattering)
rect_neies = patches.FancyBboxPatch((2.2, 0.55), 2.8, 1.15, boxstyle="round,pad=0.06",
                                   ec="#6a1b9a", fc="#f3e5f5", lw=1.2)
ax.add_patch(rect_neies)
ax.text(2.3, 1.45, r'NEIES: $e^-(E_e) + |i\rangle \to e^-(E_e - \Delta E) + |t\rangle$', fontsize=7.4, color="#4a148c", fontweight='bold')
ax.text(2.3, 1.10, r'Non-resonant continuum: $E_e > \Delta E_{\mathrm{nuc}}$', fontsize=7.0, color="#6a1b9a", fontweight='bold')
ax.text(2.3, 0.80, r'Continuous threshold scattering ($\neq$ NEEC)', fontsize=6.8, color="#424242")


# -------------------------------------------------------------
# Panel (c): Heavy-Ion Complete Fusion and Evaporation Survival
# -------------------------------------------------------------
ax = axes[2]
ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-0.5, 6.0)
ax.axis('off')
ax.set_title(r'(c) Heavy-Ion Complete Fusion & De-excitation Stages', fontsize=9.8, fontweight='bold', pad=10)

# Stage 1: Capture
rect_s1 = patches.FancyBboxPatch((0.1, 4.4), 4.8, 1.1, boxstyle="round,pad=0.08",
                                 ec="#00695c", fc="#e0f2f1", lw=1.3)
ax.add_patch(rect_s1)
ax.text(0.3, 5.20, r'1. Capture: $\sigma_{\mathrm{cap}}(E, J) = \frac{\pi\hbar^2}{2\mu E} \frac{2J+1}{(2I_1+1)(2I_2+1)} \sum T_l(E, J)$', fontsize=7.4, color="#004d40", fontweight='bold')
ax.text(0.3, 4.70, r'Channel coupling, static/dynamic deformations $\beta_2, \beta_4$, multi-dimensional barrier $D(B)$', fontsize=6.7, color="#004d40")

# Arrow 1->2
ax.annotate('', xy=(2.5, 3.9), xytext=(2.5, 4.4),
            arrowprops=dict(arrowstyle="->", color="#004d40", lw=1.5))

# Stage 2: Compound Nucleus Formation
rect_s2 = patches.FancyBboxPatch((0.1, 2.8), 3.3, 1.1, boxstyle="round,pad=0.08",
                                 ec="#ef6c00", fc="#fff3e0", lw=1.3)
ax.add_patch(rect_s2)
ax.text(0.3, 3.55, r'2. Compound Nucleus: $P_{\mathrm{CN}}(E, J)$ (System-dependent)', fontsize=7.4, color="#e65100", fontweight='bold')
ax.text(0.3, 3.05, 'Dissipative shape evolution on potential energy surface', fontsize=6.7, color="#e65100")

# Competing Quasifission box
rect_qf = patches.FancyBboxPatch((3.6, 2.8), 1.3, 1.1, boxstyle="round,pad=0.08",
                                 ec="#c62828", fc="#ffebee", lw=1.2)
ax.add_patch(rect_qf)
ax.text(4.25, 3.55, 'Quasifission', ha='center', fontsize=7.8, color="#b71c1c", fontweight='bold')
ax.text(4.25, 3.05, r'$1 - P_{\mathrm{CN}}$ (Loss)', ha='center', fontsize=7.2, color="#c62828")

ax.annotate('', xy=(3.6, 3.35), xytext=(3.4, 3.35),
            arrowprops=dict(arrowstyle="->", color="#c62828", lw=1.5))

# Arrow 2->3
ax.annotate('', xy=(1.75, 2.3), xytext=(1.75, 2.8),
            arrowprops=dict(arrowstyle="->", color="#e65100", lw=1.5))

# Stage 3: Survival Probability
rect_s3 = patches.FancyBboxPatch((0.1, 0.4), 4.8, 1.9, boxstyle="round,pad=0.08",
                                 ec="#283593", fc="#e8eaf6", lw=1.3)
ax.add_patch(rect_s3)
ax.text(0.3, 1.95, r'3. Survival Cascade: $W_{\mathrm{sur}}(E^*, J) \simeq \Delta_x \prod_{k=1}^x \frac{\Gamma_n}{\Gamma_{\mathrm{tot}}}(E_k^*, J_k)$', fontsize=7.4, color="#1a237e", fontweight='bold')
ax.text(0.3, 1.60, r'Evaporation vs Fission: $\Gamma_n \propto \int T_l \rho_R d\epsilon$, $\Gamma_f \propto \int \rho_{\mathrm{saddle}} d\epsilon$, damped $B_f(E^*)$', fontsize=6.7, color="#283593")
ax.text(0.3, 1.25, r'Dynamic update: $E_k^* = E_{k-1}^* - S_n^{(k)} - \epsilon_k$, $\mathbf{J}_k = \mathbf{J}_{k-1} - \mathbf{j}_n^{(k)}$', fontsize=6.7, color="#1a237e")
ax.text(0.3, 0.90, r'Entry states $\to$ statistical $\gamma$ feeding: $\sigma_{\mathrm{isomer}} = \sum_J \sigma_{\mathrm{ER}}(E, J) b_{\mathrm{feed}}(E^*_{\mathrm{entry}}, J) \approx b_{\mathrm{eff}} \sigma_{\mathrm{ER}}$', fontsize=7.0, color="#b71c1c", fontweight='bold')
ax.text(0.3, 0.55, r'Detection windows: TOF loss ($\tau \ll \tau_{\mathrm{TOF}}$) vs long-lived correlation loss ($\tau \gg \Delta T_{\mathrm{corr}}$)', fontsize=6.7, color="#424242")

plt.tight_layout()
os.makedirs("raw/writing/gpt/A130/these_2023_template/these_template/Img", exist_ok=True)
plt.savefig("raw/writing/gpt/A130/these_2023_template/these_template/Img/environment-network-pathways.pdf")
plt.savefig("raw/writing/gpt/A130/these_2023_template/these_template/Img/environment-network-pathways.svg")
print("Figure generated successfully.")
