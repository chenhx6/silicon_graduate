#!/usr/bin/env python3
"""Arithmetic from Pai2016 TableIII plus an explicitly illustrative rotor.

No self-consistent HFB, QRPA, TAC or scissors-to-MR transformation is computed.
"""
from pathlib import Path
from math import sqrt, pi, degrees
import json

OUT=Path(__file__).resolve().parent
interference=[]
for name,total,orb,spin in [('QRPA',1.52,.60,.21),('LSSM',.826,.316,.120)]:
    cross=total-orb-spin
    interference.append({'model':name,'total_muN2':total,'orbital_only_muN2':orb,
                         'spin_only_muN2':spin,'interference_muN2':cross,
                         'interference_fraction':cross/total,
                         'fully_constructive_from_rounded_parts_muN2':(sqrt(orb)+sqrt(spin))**2,
                         'phase_cosine_from_rounded_values':cross/(2*sqrt(orb*spin)),
                         'rounding_boundary':'A cosine slightly above one reflects rounded table entries; it is not a measured phase.'})
Ip,In,Esc=10.,15.,3.
Ired=Ip*In/(Ip+In)
phi_rms=sqrt(1/(2*Ired*Esc))
res={'kind':'source-table-arithmetic-and-illustrative-rotor-not-microscopic-evolution',
     'source':'Pai et al. 2016 PRC93 014318, arXiv1601.01905v1 pp4,9 TableIII',
     'detailed_balance':{'B_up_0to1_muN2':1.113,'sigma_up_muN2':.049,
                         'B_down_1to0_muN2':1.113/3,'sigma_down_muN2':.049/3,
                         'MR_reverse_factor_at_I35over2':(2*17.5+1)/(2*17.5-1)},
     'orbital_spin_interference':interference,
     'illustrative_rotor':{'parameters_assumed_not_fitted':True,'hbar':1,'Ip_MeVinv':Ip,'In_MeVinv':In,
                          'Ired_MeVinv':Ired,'E_sc_MeV':Esc,'C_MeV':Ired*Esc**2,
                          'phi_rms_rad':phi_rms,'phi_rms_deg':degrees(phi_rms),
                          'momentum_transition_square_hbar2':Ired*Esc/2,
                          'one_cartesian_M1_operator_square_muN2':3/(4*pi)*Ired*Esc/2,
                          'normalization_boundary':'One transverse Cartesian coordinate; not a projected nuclear B(M1).'},
     'uncomputed':['No same-isotope low-spin-to-MR branch tracking.','No microscopic current reconstruction from observed data.','No historical-paper full-text reproduction.']}
(OUT/'scissors-mode-to-mr-quantitative.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    x=np.linspace(-2.5,2.5,151);z=np.linspace(-3,3,181);X,Z=np.meshgrid(x,z)
    a,c,phi=1.,1.35,.05
    rho=np.exp(-X**2/a**2-Z**2/c**2)
    tilt=2*phi*X*Z*(1/a**2-1/c**2)*rho
    fig,ax=plt.subplots(1,3,figsize=(12,3.5),gridspec_kw={'width_ratios':[1,1,1.2]})
    lim=float(abs(tilt).max())
    for k,field in enumerate([tilt,np.zeros_like(tilt)]):
        ax[k].pcolormesh(x,z,field,vmin=-lim,vmax=lim,cmap='RdBu_r',shading='auto')
        ax[k].contour(X,Z,rho,levels=[.2,.5,.8],colors='black',linewidths=.45)
        ax[k].set_aspect('equal');ax[k].set_xlabel('x (arbitrary units)');ax[k].set_ylabel('z')
    ax[0].set_title('Small tilt about transverse y: delta rho')
    ax[1].set_title('Rotation about symmetry z: delta rho = 0')
    names=[r['model'] for r in interference];bottom=np.zeros(2)
    for field,label in [('orbital_only_muN2','orbital only'),('spin_only_muN2','spin only'),('interference_muN2','interference')]:
        val=np.array([r[field] for r in interference]);ax[2].bar(names,val,bottom=bottom,label=label);bottom+=val
    ax[2].set_ylabel('B(M1) upward (mu_N squared)');ax[2].set_title('Pai2016 TableIII model strengths');ax[2].legend(fontsize=7)
    fig.suptitle('Illustrative axial-density kinematics and published-model arithmetic; no MR conversion simulated',fontsize=10)
    fig.tight_layout();fig.savefig(OUT/'scissors-axis-and-interference.svg');plt.close(fig)
except ImportError:
    pass
print(json.dumps(res,ensure_ascii=False,indent=2))
