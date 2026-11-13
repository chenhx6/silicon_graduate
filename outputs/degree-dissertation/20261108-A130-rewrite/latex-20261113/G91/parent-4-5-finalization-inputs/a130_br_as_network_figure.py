# system/scripts/a130_br_as_network_figure.py
# Generates actual observed parity-link network topology for 78Br and 74As
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2))

# Panel (a): 78Br Observed Network
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title(r'(a) $^{78}$Br Observed Bands & Links' + '\n' + r'(Liu et al. PRL 2016 / Liu Thesis 2016)', fontsize=11, fontweight='bold', color='#1A237E')

b1 = patches.FancyBboxPatch((0.8, 5.5), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#1565C0', facecolor='#E3F2FD', lw=1.5)
b2 = patches.FancyBboxPatch((0.8, 1.0), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#1565C0', facecolor='#E3F2FD', lw=1.5, ls='--')
ax1.add_patch(b1)
ax1.add_patch(b2)
ax1.text(2.4, 8.2, r"Band 1 ($\pi=+$)", ha='center', fontsize=10, fontweight='bold', color='#0D47A1')
ax1.text(2.4, 7.5, r"$\pi g_{9/2} \otimes \nu g_{9/2}$" + "\n" + r"$I^\pi = 8^+ \to 16^+$", ha='center', fontsize=8.5)

ax1.text(2.4, 3.7, r"Band 2 ($\pi=+$)", ha='center', fontsize=10, fontweight='bold', color='#0D47A1')
ax1.text(2.4, 3.0, r"Chiral Partner of B1" + "\n" + r"Lowest state $9^+$" + "\n" + r"$\Delta I=1$ links to B1", ha='center', fontsize=8.5)

b3 = patches.FancyBboxPatch((5.8, 5.5), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#C62828', facecolor='#FFEBEE', lw=1.5)
b4 = patches.FancyBboxPatch((5.8, 1.0), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#C62828', facecolor='#FFEBEE', lw=1.5, ls='--')
ax1.add_patch(b3)
ax1.add_patch(b4)
ax1.text(7.4, 8.2, r"Band 3 ($\pi=-$)", ha='center', fontsize=10, fontweight='bold', color='#B71C1C')
ax1.text(7.4, 7.5, r"$\pi f_{5/2}(p_{3/2}) \otimes \nu g_{9/2}$" + "\n" + r"$I^\pi = 6^- \to 15^-$", ha='center', fontsize=8.5)

ax1.text(7.4, 3.7, r"Band 4 ($\pi=-$)", ha='center', fontsize=10, fontweight='bold', color='#B71C1C')
ax1.text(7.4, 3.0, r"Chiral Partner of B3" + "\n" + r"Lowest state $7^-$" + "\n" + r"$404.3$ keV link to B3", ha='center', fontsize=8.5)

ax1.annotate('', xy=(5.8, 7.1), xytext=(4.0, 7.1), arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=2.5))
ax1.text(4.9, 7.5, "8 Observed\nE1 Transitions", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#2E7D32')

ax1.annotate('', xy=(5.8, 2.6), xytext=(4.0, 2.6), arrowprops=dict(arrowstyle='<->', color='gray', lw=1.2, ls=':'))
ax1.text(4.9, 2.8, "NO E1 Links\nObserved", ha='center', va='bottom', fontsize=8, color='gray')

ax1.annotate('', xy=(2.4, 5.5), xytext=(2.4, 4.2), arrowprops=dict(arrowstyle='<->', color='#1565C0', lw=1.5))
ax1.text(2.9, 4.8, r"M1/E2", fontsize=8, color='#1565C0')
ax1.annotate('', xy=(7.4, 5.5), xytext=(7.4, 4.2), arrowprops=dict(arrowstyle='<->', color='#C62828', lw=1.5))
ax1.text(7.9, 4.8, r"M1/E2", fontsize=8, color='#C62828')

# Panel (b): 74As Observed Network
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title(r'(b) $^{74}$As Observed Bands & Links' + '\n' + r'(Xiao et al. PRC 2022 / Xiao Thesis 2019)', fontsize=11, fontweight='bold', color='#1A237E')

b1_as = patches.FancyBboxPatch((0.8, 5.5), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#1565C0', facecolor='#E3F2FD', lw=1.5)
b2_as = patches.FancyBboxPatch((0.8, 1.0), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#1565C0', facecolor='#E3F2FD', lw=1.5, ls='--')
ax2.add_patch(b1_as)
ax2.add_patch(b2_as)
ax2.text(2.4, 8.2, r"Band 1 ($\pi=+$)", ha='center', fontsize=10, fontweight='bold', color='#0D47A1')
ax2.text(2.4, 7.5, r"$\pi g_{9/2} \otimes \nu g_{9/2}$" + "\n" + r"$I^\pi = 6^+ \to 15^+$", ha='center', fontsize=8.5)

ax2.text(2.4, 3.7, r"Band 2 ($\pi=+$)", ha='center', fontsize=10, fontweight='bold', color='#0D47A1')
ax2.text(2.4, 3.0, r"Chiral Partner of B1" + "\n" + r"$I^\pi = 7^+ \to 14^+$" + "\n" + r"$\Delta I=1$ links to B1", ha='center', fontsize=8.5)

b3_as = patches.FancyBboxPatch((5.8, 5.5), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#C62828', facecolor='#FFEBEE', lw=1.5)
b4_as = patches.FancyBboxPatch((5.8, 1.0), 3.2, 3.2, boxstyle="round,pad=0.2", edgecolor='#757575', facecolor='#FAFAFA', lw=1.2, ls=':')
ax2.add_patch(b3_as)
ax2.add_patch(b4_as)
ax2.text(7.4, 8.2, r"Band 3 ($\pi=-$)", ha='center', fontsize=10, fontweight='bold', color='#B71C1C')
ax2.text(7.4, 7.5, r"$\pi(f_{5/2}/p_{3/2}) \otimes \nu g_{9/2}$" + "\n" + r"$I^\pi = 7^- \to 14^-$", ha='center', fontsize=8.5)

ax2.text(7.4, 3.0, r"Band 4 ($\pi=-$)" + "\n" + r"2019 thesis candidate" + "\n" + r"(pseudospin, not chiral)" + "\n" + r"Not focused in 2022 paper", ha='center', fontsize=7.8, color='#616161')

ax2.annotate('', xy=(5.8, 7.1), xytext=(4.0, 7.1), arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=2.0))
ax2.text(4.9, 7.5, "3 Observed\nE1 Transitions\n(372, 919, 1293 keV)", ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='#2E7D32')

ax2.annotate('', xy=(2.4, 5.5), xytext=(2.4, 4.2), arrowprops=dict(arrowstyle='<->', color='#1565C0', lw=1.5))
ax2.text(2.9, 4.8, r"M1/E2", fontsize=8, color='#1565C0')

plt.tight_layout()
os.makedirs('raw/writing/gpt/A130/these_2023_template/these_template/Img', exist_ok=True)
pdf_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/br-as-network-topology.pdf'
svg_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Img/br-as-network-topology.svg'
plt.savefig(pdf_path)
plt.savefig(svg_path)
plt.close()
print("Saved br_as_network_figure.py successfully.")
