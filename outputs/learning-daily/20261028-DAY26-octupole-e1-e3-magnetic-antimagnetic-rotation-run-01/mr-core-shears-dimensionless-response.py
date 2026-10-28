"""Conditional core+two-blade curves; synthetic parameters, not an isotope fit.

No statistical inference or comparison to digitized data is performed.
Angular momenta use hbar=1. V2=1 is an energy scale.
The E2 curve adopts Clark2000 Eq.8 with fixed effective quadrupole moment.
"""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
j1,j2,V2=5.0,7.0,1.0
q=j1*j2
A=j1*j1+j2*j2
J0=np.sqrt(A)
c=np.linspace(0,1,401)
fig,axes=plt.subplots(2,3,figsize=(12.6,7.4),layout='constrained')
rows=[]
for kappa in [0.0,0.25,1.0]:
 Js=np.sqrt(A+2*q*c)
 spin=Js*(1+kappa*c)
 R=spin-Js
 core_fraction=R/spin
 e_rel=1.5*c*c*(1+kappa*Js*Js/q)
 b1=(1-c*c)*A/(Js*Js)
 b2=b1*b1
 ratio=np.divide(b1,b2,out=np.full_like(b1,np.nan),where=b2>1e-12)
 x=spin/J0
 lab=rf'$\kappa={kappa:g}$'
 for ax,y in zip(axes.flat,[e_rel,np.rad2deg(np.arccos(c)),core_fraction,b1,b2,ratio]):
  ax.plot(x,y,label=lab,lw=1.8)
 for vals in zip(c,spin,Js,R,e_rel,b1,b2,ratio):
  rows.append([kappa]+[float(v) if np.isfinite(v) else '' for v in vals])
for ax,title in zip(axes.flat,['Energy above bandhead / V2','Shears angle (degrees)','Core fraction R / I','B(M1) / bandhead B(M1)','B(E2) / bandhead B(E2)','[B(M1)/B(E2)] / bandhead ratio']):
 ax.set_title(title,fontsize=10)
 ax.set_xlabel(r'$I/\sqrt{j_1^2+j_2^2}$')
 ax.grid(alpha=.2)
axes[1,2].set_yscale('log')
axes[0,0].legend(frameon=False)
fig.suptitle('Conditional two-blade + core model: synthetic j1=5, j2=7\nFixed g and Qeff; no isotope fit, no imposed band termination',fontsize=12)
fig.savefig(out/'mr-core-shears-dimensionless-response.pdf')
fig.savefig(out/'mr-core-shears-dimensionless-response.svg')
with (out/'mr-core-shears-dimensionless-response.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['kappa','cos_theta','I','J_shears','R_core','energy_above_head_over_V2','B_M1_normalized','B_E2_normalized','ratio_normalized']);w.writerows(rows)
meta={'model':'parallel core + distinguishable fixed blades; synthetic example','isotope_fit':False,'parameters':{'j1':j1,'j2':j2,'V2_energy_scale':V2,'kappa':[0,.25,1]},'assumptions':['V2>0','hbar=1','core parallel to shears resultant','constant g1-g2','constant effective blade Q as Clark2000 Eq8','classical electromagnetic response'],'formulas':{'Js':'sqrt(j1^2+j2^2+2*j1*j2*c)','kappa':'3*Jcore*V2/(j1*j2)','spin':'Js*(1+kappa*c)','core_fraction':'kappa*c/(1+kappa*c)','B_M1_norm':'(1-c^2)*(j1^2+j2^2)/Js^2','B_E2_norm':'B_M1_norm^2','energy_above_head_over_V2':'1.5*c^2*(1+kappa*Js^2/(j1*j2))'},'boundary':'c=1 ends the internal shears branch; finite core model can continue with aligned blades; classical ratio undefined at exact endpoint','data_dependence':'none; no experimental values imported'}
(out/'mr-core-shears-dimensionless-response.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
