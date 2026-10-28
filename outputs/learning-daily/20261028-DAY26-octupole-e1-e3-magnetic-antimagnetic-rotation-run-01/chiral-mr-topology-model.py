"""Synthetic chiral-vibration -> static-chirality landscape.

E(phi; x)=a(x) sin^2(phi)+b sin^4(phi), b>0.
phi is an azimuthal out-of-plane coordinate; x is a dimensionless spin/frequency
control parameter. This is an illustrative Landau landscape, not a fit to a nucleus.
"""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
phi=np.linspace(-np.pi/2,np.pi/2,1001)
x=np.linspace(0,1,301); b=1.0; ac=0.42
a=ac-x
E=np.array([aa*np.sin(phi)**2+b*np.sin(phi)**4 for aa in a])
mins=[]
for xx,aa,ee in zip(x,a,E):
 i=np.argmin(ee); mins.append((xx,aa,phi[i],ee[i]))
fig,ax=plt.subplots(figsize=(8.2,5.1))
for xx in [0.0,.2,.4,.42,.6,.8,1.0]:
 aa=ac-xx;ax.plot(np.rad2deg(phi),aa*np.sin(phi)**2+b*np.sin(phi)**4,label=f'x={xx:.2f}')
ax.axvline(0,color='k',lw=.6);ax.axvline(0,color='k',lw=.6)
ax.set(xlabel='out-of-plane azimuth φ (degrees)',ylabel='E / arbitrary scale',title='Synthetic planar-to-aplanar chiral landscape')
ax.grid(alpha=.2);ax.legend(ncol=2,frameon=False,fontsize=8);fig.tight_layout();fig.savefig(out/'chiral-mr-topology-landscape.pdf');fig.savefig(out/'chiral-mr-topology-landscape.svg')
with (out/'chiral-mr-topology-landscape.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['control_x','a','phi_min_rad','energy_min']);w.writerows(mins)
meta={'model':'even azimuthal Landau landscape','formula':'E=a(x) sin^2(phi)+b sin^4(phi)','a':'0.42-x','b':b,'critical_control_x':ac,'interpretation':'a>0 single planar minimum; a=0 soft mode; a<0 two degenerate minima +/-phi0','not_a_fit':True,'observables_needed':['partner-resolved energies','intra/interband M1,E2 matrix elements','alignment and moments of inertia','configuration and triaxiality constraints'],'boundary':'a sign change is a model diagnostic, not an experimental static-chirality proof'}
(out/'chiral-mr-topology-landscape.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
