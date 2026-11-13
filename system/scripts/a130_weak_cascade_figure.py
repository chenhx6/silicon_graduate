#!/usr/bin/env python3
"""
Pedagogical illustration of beta-delayed feeding and gamma/n statistical cascade competition.
Section 4.7, Figure 4.13.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_figure():
    fig, ax = plt.subplots(figsize=(8.4, 6.4))
    ax.set_xlim(0, 11.2)
    ax.set_ylim(-1.6, 9.6)
    ax.axis('off')

    # Title / schematic banner
    ax.text(0.3, 9.3, 'Not to scale; separate column energy zeros',
            ha='left', va='center', fontsize=9.5, fontstyle='italic', color='#555555')

    # 1. Parent nucleus (Z, N) on the left
    ax.plot([0.6, 2.6], [8.2, 8.2], color='#1f77b4', lw=3)
    ax.text(1.6, 8.5, r'Parent $(Z, N)$', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1f77b4')
    ax.text(1.6, 7.8, r'$J_i^\pi, \text{gs}$', ha='center', va='top', fontsize=9.5)

    # 2. Daughter nucleus (Z+1, N-1) in the center
    # Ground state
    ax.plot([4.0, 7.0], [1.2, 1.2], color='#2ca02c', lw=3)
    ax.text(5.5, 0.85, r'Daughter $(Z+1, N-1)$ Ground State', ha='center', va='top', fontsize=10.5, fontweight='bold', color='#2ca02c')

    # Low-lying discrete states below Sn
    for y in [1.9, 2.6, 3.3, 3.9]:
        ax.plot([4.2, 6.8], [y, y], color='#333333', lw=1.2)
    ax.text(4.0, 2.6, r'Discrete states $(E_x < S_n)$', ha='right', va='center', fontsize=8.5, color='#444444')

    # Sn threshold line
    ax.plot([3.8, 7.2], [4.5, 4.5], color='#d62728', lw=2, ls=':')
    ax.text(7.3, 4.5, r'$S_n$', ha='left', va='center', fontsize=12, color='#d62728')

    # High-lying continuum / resonance states above Sn
    rect = patches.Rectangle((4.0, 4.5), 3.0, 3.7, linewidth=0, edgecolor='none', facecolor='#fee8c8', alpha=0.45)
    ax.add_patch(rect)
    for y in [5.2, 5.8, 6.5, 7.2, 7.8]:
        ax.plot([4.2, 6.8], [y, y], color='#d95f02', lw=1.5)
    ax.plot([3.8, 7.2], [8.2, 8.2], color='#d95f02', lw=1.5, ls='--')
    ax.text(7.3, 8.2, r'$Q_\beta$ ceiling', ha='left', va='center', fontsize=9, color='#d95f02')

    ax.text(5.5, 8.55, r'Energy Window $Q_\beta - S_n$' + '\n' + r'$\Gamma_\gamma \text{ vs } \Gamma_n \text{ Incoherent Competition}$',
            ha='center', va='center', fontsize=9, color='#d95f02', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#d95f02', lw=1))

    # Beta feeding arrows from parent:
    # Arrow to continuum states in Q_beta - S_n window (y=6.5)
    ax.annotate('', xy=(4.1, 6.6), xytext=(1.6, 7.7),
                arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.8, ls='--'))
    # Arrow to low-lying discrete states (y=2.6)
    ax.annotate('', xy=(4.1, 2.6), xytext=(1.6, 7.7),
                arrowprops=dict(arrowstyle='->', color='#7f7f7f', lw=1.2, ls=':'))

    ax.text(2.6, 5.2, r'$\beta^-$ Decay Feeding' + '\n' +
            r'Branching $\sum_i I_\beta(i) = b_\beta \leq 1$' + '\n' +
            r'Parent clock: $T_{1/2}^\beta$',
            ha='center', va='center', fontsize=10, color='#1f77b4',
            bbox=dict(boxstyle='round,pad=0.3', fc='#f0f4f8', ec='#b0c4de', lw=1))

    # 3. Gamma cascade arrows inside daughter
    ax.annotate('', xy=(5.0, 3.3), xytext=(5.0, 6.5),
                arrowprops=dict(arrowstyle='->', color='#e377c2', lw=2.0))
    ax.text(4.85, 4.9, r'$\gamma$', color='#e377c2', fontsize=11, fontweight='bold', ha='right')

    ax.annotate('', xy=(5.0, 1.2), xytext=(5.0, 3.3),
                arrowprops=dict(arrowstyle='->', color='#e377c2', lw=2.0))
    ax.text(4.85, 2.2, r'$\gamma$', color='#e377c2', fontsize=11, fontweight='bold', ha='right')

    # 4. Granddaughter nucleus (Z+1, N-2) on the right
    ax.plot([8.2, 10.4], [1.5, 1.5], color='#9467bd', lw=3)
    ax.text(9.3, 1.15, r'Granddaughter $(Z+1, N-2)$' + '\n' + r'Ground State', ha='center', va='top', fontsize=10, fontweight='bold', color='#9467bd')

    # Explicit excited states in granddaughter
    for gy, glabel in [(2.4, r'$2_1^+$'), (3.3, r'$4_1^+$')]:
        ax.plot([8.4, 10.2], [gy, gy], color='#777777', lw=1.4)
        ax.text(10.3, gy, glabel, ha='left', va='center', fontsize=8.5, color='#555555')

    # Delayed neutron emission arrows: each lands strictly on an explicit granddaughter level
    # From daughter y=5.8 to granddaughter ground state y=1.5
    ax.annotate('', xy=(8.2, 1.5), xytext=(6.8, 5.8),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2.0))
    ax.text(7.5, 3.8, r'$n_0$', color='#ff7f0e', fontsize=10, fontweight='bold')

    # From daughter y=7.2 to granddaughter excited state y=2.4
    ax.annotate('', xy=(8.4, 2.4), xytext=(6.8, 7.2),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2.0))
    ax.text(7.6, 5.1, r'$n_1$', color='#ff7f0e', fontsize=10, fontweight='bold')

    # 5. Legend at top right
    ax.plot([], [], color='#e377c2', lw=2.0, label=r'$\gamma$ decay: $\Gamma_\gamma$')
    ax.plot([], [], color='#ff7f0e', lw=2.0, label=r'Neutron emission: $\Gamma_n$')
    ax.legend(loc='upper right', frameon=True, fontsize=9.0)

    # 6. Dedicated clean explanation box across bottom region
    desc_text = (
        r'$\sum_i I_\beta(i)=b_\beta,\qquad P_{xn}^{(\beta;\mathrm{parent})}=\sum_i I_\beta(i)\Pi_x(i)$' + '\n' +
        r'$\Pi_x(a)=\sum_{b,r}\frac{\Gamma_{a\to b}^{(r)}}{\Gamma_{\mathrm{tot}}(a)}\Pi_{x-r}(b),\qquad\Pi_{x<0}=0$' + '\n' +
        r'$\Pi_x(t)=\delta_{x0}$ for selected absorbing states'
    )
    ax.text(5.6, -0.65, desc_text,
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle='round,pad=0.5', fc='#f8f9fa', ec='#adb5bd', lw=1.2))

    plt.tight_layout()
    out_dir = os.path.join(os.path.dirname(__file__), '../../raw/writing/gpt/A130/these_2023_template/these_template/Img')
    os.makedirs(out_dir, exist_ok=True)
    svg_path = os.path.join(out_dir, 'weak-cascade-competition.svg')
    pdf_path = os.path.join(out_dir, 'weak-cascade-competition.pdf')
    fig.savefig(svg_path, format='svg')
    fig.savefig(pdf_path, format='pdf')
    plt.close(fig)
    print(f"Generated {svg_path} and {pdf_path}")

if __name__ == '__main__':
    generate_figure()
