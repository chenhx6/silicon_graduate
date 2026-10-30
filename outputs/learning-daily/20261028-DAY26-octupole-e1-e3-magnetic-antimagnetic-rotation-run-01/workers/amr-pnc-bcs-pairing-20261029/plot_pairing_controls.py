#!/usr/bin/env python3
"""Three distinct finite-model controls; all curves analytic and schematic."""
from pathlib import Path
import csv,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).parent
r=list(csv.DictReader((BASE/'bcs_exact_shellgap_control.csv').open()))
a=list(csv.DictReader((BASE/'effective_avoided_crossing.csv').open()))
fig,axs=plt.subplots(1,3,figsize=(14.2,4.3))
x=[float(t['two_epsilon_over_G']) for t in r]
axs[0].plot(x,[float(t['Delta_BCS_MeV'])/0.8 for t in r],label='BCS anomalous gap / G',lw=2)
axs[0].plot(x,[float(t['pair_transfer_coherence_exact']) for t in r],label='Exact pair transfer coherence',lw=2)
axs[0].axvline(1,color='gray',ls=':',lw=1)
axs[0].set(xlabel=r'Shell-gap control $2\epsilon/G$',ylabel='Different dimensionless diagnostics',title='(a) Mean-field collapse vs finite-N coherence')
axs[0].set_xlim(0,3);axs[0].legend(fontsize=8)
for w,col in [(0,'black'),(.02,'tab:orange'),(.10,'tab:blue')]:
 om=[.3+i*.001 for i in range(201)]
 ys=[]
 for o in om:
  d=-6*(o-.4);rr=math.sqrt(d*d+4*w*w)
  ys.append(float('nan') if rr==0 else 6*(1-d/rr)/2)
 axs[1].plot(om,ys,label=f'W = {w:g} MeV',color=col)
axs[1].axvline(.4,color='gray',ls=':',lw=1)
axs[1].set(xlabel=r'$\omega$ (MeV/$\hbar$)',ylabel=r'Alignment ($\hbar$)',title='(b) Mixing broadens; center stays fixed')
axs[1].legend(fontsize=8)
wc=math.sqrt(4*.2*.2+.8*.8)
axs[2].plot([0,wc],[0,0],lw=2,color='tab:green')
axs[2].plot([wc,1.6],[1,1],lw=2,color='tab:green')
axs[2].plot([wc,wc],[0,1],ls=':',lw=1,color='tab:green')
axs[2].scatter([wc,wc],[0,1],facecolors='white',edgecolors='tab:green',zorder=3)
axs[2].set(xlabel=r'$\omega$ (MeV/$\hbar$)',ylabel=r'Ground-state $J$ ($\hbar$)',title='(c) Exact-N genuine symmetry-sector crossing')
axs[2].set_ylim(-.1,1.1);axs[2].set_xlim(0,1.6)
for ax in axs:
 ax.spines[['right','top']].set_visible(False)
 ax.grid(alpha=.15)
fig.text(.5,.015,'Analytic finite-model demonstrations; no Cd/Pd fit. Panel (a) compares different diagnostics, not two measured gaps.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.055,1,1])
fig.savefig(BASE/'pairing_finite_number_controls.png',dpi=180)
fig.savefig(BASE/'pairing_finite_number_controls.pdf')
