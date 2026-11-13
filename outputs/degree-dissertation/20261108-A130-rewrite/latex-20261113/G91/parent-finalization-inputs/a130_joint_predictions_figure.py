# system/scripts/a130_joint_predictions_figure.py
# Generates joint predictions and complementary observables workflow for Section 3.8
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8.2, 5.2), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

ax.text(5.0, 6.6, "Joint Predictions and Complementary Observables Framework",
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1A237E')

rect1 = patches.FancyBboxPatch((0.5, 4.4), 9.0, 1.8, boxstyle="round,pad=0.2",
                               edgecolor='#303F9F', facecolor='#E8EAF6', lw=1.5)
ax.add_patch(rect1)
ax.text(0.8, 5.9, "I. Theoretical Forward Model Space (Declared Inputs & Coordinates)",
        fontsize=10.5, fontweight='bold', color='#1A237E')
ax.text(1.0, 5.4, "- Coordinates & Truncations: Euler angles (orientation) vs. Bohr (beta, gamma) vs. Quasi-particles", fontsize=9)
ax.text(1.0, 5.0, "- Inputs: Phenomenological or microscopic PES, Moments of Inertia J_k(w), Pairing Delta, Effective operators", fontsize=9)
ax.text(1.0, 4.6, "- Boundaries: Model labels are NOT observables; Wavefunction trajectories belong to specific representations", fontsize=9)

rect2 = patches.FancyBboxPatch((0.5, 2.2), 9.0, 1.8, boxstyle="round,pad=0.2",
                               edgecolor='#00796B', facecolor='#E0F2F1', lw=1.5)
ax.add_patch(rect2)
ax.text(0.8, 3.7, "II. Correlated Complementary Observable Channels (Holdout Validation)",
        fontsize=10.5, fontweight='bold', color='#004D40')

box_props = dict(boxstyle='square,pad=0.3', facecolor='#B2DFDB', edgecolor='#00796B', lw=1)
ax.text(1.8, 3.0, "Energy Levels\nAvoided crossing\nRepulsion & staggering", ha='center', va='center', fontsize=8.5, bbox=box_props)
ax.text(4.0, 3.0, "Absolute Rates\nB(sigmaL) prop. to 1/tau\nBranching & ICC cov.", ha='center', va='center', fontsize=8.5, bbox=box_props)
ax.text(6.2, 3.0, "Angular & Polariz.\nDCO quadratic roots\nSI charge-type delta", ha='center', va='center', fontsize=8.5, bbox=box_props)
ax.text(8.4, 3.0, "High-Spin Response\nAligned momentum ix\nBand crossings", ha='center', va='center', fontsize=8.5, bbox=box_props)

rect3 = patches.FancyBboxPatch((0.5, 0.2), 9.0, 1.6, boxstyle="round,pad=0.2",
                               edgecolor='#D32F2F', facecolor='#FFEBEE', lw=1.5)
ax.add_patch(rect3)
ax.text(0.8, 1.5, "III. Falsifiable Empirical Candidates (Model-Specific Discriminative Paths)",
        fontsize=10.5, fontweight='bold', color='#B71C1C')
ax.text(1.0, 1.1, "1. 98Mo Octupole Candidate: Weak links (1833.3 keV 5- -> 2+, 1585.8 keV 7- -> 4+); Need mother-state lifetime via strong in-band lines", fontsize=8.0)
ax.text(1.0, 0.75, "2. 102Ru Dipole Response: NRF Gamma0^2/Gamma, 2.95 MeV isolated E1 & 4.5-5.5 MeV cluster; Two-phonon [2+ x 3-] vs quasiparticle response", fontsize=8.0)
ax.text(1.0, 0.4, "3. A~130 Low-Spin Orientation: 135Pr negative-parity 17/2- -> 15/2- dual delta roots; Frozen PRM vs Tilted QTR vs gamma-soft IBFM", fontsize=8.0)

arrow_props = dict(facecolor='#37474F', edgecolor='#37474F', width=1.5, headwidth=6, shrink=0.05)
ax.annotate('', xy=(5.0, 4.4), xytext=(5.0, 4.0), arrowprops=arrow_props)
ax.annotate('', xy=(5.0, 2.2), xytext=(5.0, 1.8), arrowprops=arrow_props)

plt.tight_layout()

pdf_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/joint-predictions-workflow.pdf'
svg_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/joint-predictions-workflow.svg'
plt.savefig(pdf_path)
plt.savefig(svg_path)
plt.close()
print("Saved figure successfully.")
