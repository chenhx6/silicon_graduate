# a130_mode_mixing_figure.py
# Generates schematic avoided crossing and mode mixing diagram for Section 3.6
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

os.makedirs('raw/writing/gpt/A130/these_2023_template/these_template/Img', exist_ok=True)

delta = np.linspace(-4.0, 4.0, 200)
V = 0.8
E_center = 5.0

E1_0 = E_center + 0.5 * delta
E2_0 = E_center - 0.5 * delta

E_plus = E_center + 0.5 * np.sqrt(delta**2 + 4 * V**2)
E_minus = E_center - 0.5 * np.sqrt(delta**2 + 4 * V**2)

theta = 0.5 * np.arctan2(2 * V, delta)
prob_1_plus = np.cos(theta)**2
prob_2_plus = np.sin(theta)**2

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 6.0), sharex=True)

ax1.plot(delta, E1_0, 'k--', alpha=0.5, label=r'Uncoupled $\varepsilon_1^{(0)}(\Delta)$')
ax1.plot(delta, E2_0, 'b--', alpha=0.5, label=r'Uncoupled $\varepsilon_2^{(0)}(\Delta)$')
ax1.plot(delta, E_plus, 'r-', lw=2.0, label=r'Coupled $E_+(\Delta)$ (Upper)')
ax1.plot(delta, E_minus, 'g-', lw=2.0, label=r'Coupled $E_-(\Delta)$ (Lower)')

ax1.annotate('', xy=(0, E_center + V), xytext=(0, E_center - V),
             arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))
ax1.text(0.18, E_center, r'$2|V|$', va='center', fontsize=11, color='purple')
ax1.vlines(0, E_center - V, E_center + V, colors='purple', linestyles='dotted', lw=1.2)

ax1.set_ylabel(r'Energy / arb. units', fontsize=11)
ax1.set_title(r'Schematic Avoided Crossing and Mode Mixing (Declared Toy Model)', fontsize=12)
ax1.legend(loc='upper left', frameon=True, fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.6)

ax2.plot(delta, prob_1_plus, 'm-', lw=2.0, label=r'$|c_1|^2$ (Fraction of Mode 1 in $|+\rangle$)')
ax2.plot(delta, prob_2_plus, 'c--', lw=2.0, label=r'$|c_2|^2$ (Fraction of Mode 2 in $|+\rangle$)')
ax2.axvline(0, color='gray', linestyle=':', alpha=0.7)
ax2.axhline(0.5, color='gray', linestyle=':', alpha=0.7)

ax2.set_xlabel(r'Detuning parameter $\Delta = \varepsilon_1^{(0)} - \varepsilon_2^{(0)}$ / arb. units', fontsize=11)
ax2.set_ylabel(r'Basis-state probability in $|+\rangle$', fontsize=11)
ax2.set_ylim(-0.05, 1.05)
ax2.legend(loc='center right', frameon=True, fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

pdf_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/mode-mixing-avoided-crossing.pdf'
svg_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/mode-mixing-avoided-crossing.svg'
plt.savefig(pdf_path)
plt.savefig(svg_path)
svg_file = Path(svg_path)
svg_file.write_text(
    "\n".join(line.rstrip() for line in svg_file.read_text().splitlines()) + "\n"
)
plt.close()
print("Saved figure script to system/scripts/a130_mode_mixing_figure.py")
