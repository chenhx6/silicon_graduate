from pathlib import Path
import sys,math,json
import numpy as np
ROOT=Path('/workspace/wiki');sys.path.insert(0,str(ROOT/'system/scripts'))
from day23_prm_basis_rotor import spin_matrices,transformation,direct_rotor

def calculate(ti,field_sign=1,qp_sign=1):
 tj=11;j=tj/2;A=129;beta=.24;gamma=np.deg2rad(21.0);gap=1.
 kappa=206/A**(1/3);rotconst=204/(beta**2*A**(7/3));j0=1/(2*rotconst)
 inertias=[4/3*j0*np.sin(gamma-2*np.pi*k/3)**2 for k in [1,2,3]]
 axes=spin_matrices(tj);Y20=-np.sqrt(5/(4*np.pi))/(4*j*(j+1))*(3*axes[2]@axes[2]-j*(j+1)*np.eye(tj+1))
 Y22s=-np.sqrt(5/(4*np.pi))/(4*j*(j+1))*np.sqrt(3)*(axes[0]@axes[0]-axes[1]@axes[1])
 hsp=field_sign*kappa*beta*(np.cos(gamma)*Y20+np.sin(gamma)*Y22s)
 eps,U=np.linalg.eigh(hsp);unique=eps[::2];lam=unique[-1]+1.5*(unique[-2]-unique[-1]);e=np.hypot(eps-lam,gap);u=np.sqrt((1+(eps-lam)/e)/2);v=np.sqrt(1-u*u)
 Um=(U*u)@U.conj().T;Vm=(U*v)@U.conj().T;Em=(U*e)@U.conj().T
 Iops=spin_matrices(ti);Iops[1]*=-1
 hrot=np.zeros(((ti+1)*(tj+1),)*2,complex)
 for ii,jj,J in zip(Iops,axes,inertias):
  r=np.kron(ii,np.eye(tj+1))-np.kron(np.eye(ti+1),jj);hrot+=r@r/(2*J)
 ut=np.kron(np.eye(ti+1),Um);vt=np.kron(np.eye(ti+1),Vm)
 h=ut@hrot@ut+vt@hrot@vt+qp_sign*np.kron(np.eye(ti+1),Em)
 strong,weak,_=transformation(ti,tj);_,embed=direct_rotor(ti,tj,strong,inertias);hd=embed.T@h@embed
 err=np.max(np.abs(h@embed-embed@hd));assert err<1e-10
 return np.linalg.eigvalsh(hd),dict(eps=unique.tolist(),lam=float(lam),J0=float(j0),inertias=inertias,sector_leakage=float(err))

allout=[]
for fsign in [1,-1]:
 for qsign in [1,-1]:
  results={ti:calculate(ti,fsign,qsign) for ti in [7,9,11,13,15,17,19,23]};e0=results[11][0][0]
  rows={str(ti):((out[0][:4]-e0)*1000).tolist() for ti,out in results.items()}
  out={'field_sign':fsign,'quasiparticle_energy_sign':qsign,'spin_twice_rows_keV_relative_to_lowest_11_2':rows,'params':results[11][1]};allout.append(out);print(json.dumps(out),flush=True)
(ROOT/'tmp/ba129-model-readiness/model-probe.json').write_text(json.dumps(allout,indent=2)+'\n')
