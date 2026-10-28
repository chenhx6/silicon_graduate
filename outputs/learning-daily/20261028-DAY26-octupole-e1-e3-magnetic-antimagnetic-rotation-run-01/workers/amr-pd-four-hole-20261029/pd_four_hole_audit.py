#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import sin,cos,pi
from pathlib import Path
import json,csv
OUT=Path(__file__).resolve().parent
# Four equal g9/2-hole vectors grouped in two time-reversed pairs.
def vec(j,t,phi,sign):
    return (sign*j*sin(t)*cos(phi),sign*j*sin(t)*sin(phi),j*cos(t))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def norm(a):return sum(x*x for x in a)**0.5
def rzpi(v):return (-v[0],-v[1],v[2])
def ryT(v): # T first, then Ry(pi): v -> (-vx,-vy,-vz)->(vx,-vy,vz)
    return (v[0],-v[1],v[2])
# two pairs may have different theta and azimuth, but each pair is equal-weight opposite transverse blades.
max_mu=max_q21=max_rz=max_ryt=0.0; rows=[]
for ia in range(0,91):
    ta=ia*pi/180
    for ib in range(0,91):
        tb=ib*pi/180
        vs=[vec(1,ta,0,1),vec(1,ta,0,-1),vec(1,tb,0,1),vec(1,tb,0,-1)]
        mu=(sum(v[0] for v in vs),sum(v[1] for v in vs),sum(v[2] for v in vs))
        q21=sum(v[2]*(v[0]+1j*v[1]) for v in vs)
        total=tuple(sum(v[k] for v in vs) for k in range(3))
        rz=tuple(sum(rzpi(v)[k] for v in vs) for k in range(3))
        # Q22 proportional to (x+iy)^2; pair result 2 sin^2(theta) for each unit q.
        q22=sum((v[0]+1j*v[1])**2 for v in vs)
        max_mu=max(max_mu,norm(mu[:2]));max_q21=max(max_q21,abs(q21));max_rz=max(max_rz,norm(tuple(rz[k]-total[k] for k in range(3))))
        max_ryt=max(max_ryt,norm(tuple(sum(ryT(v)[k] for v in vs)-total[k] for k in range(3))))
        if (ia,ib) in [(0,0),(30,30),(60,30),(90,90)]: rows.append(dict(theta_a=ia,theta_b=ib,mu_perp=norm(mu[:2]),q21_abs=abs(q21),q22=q22.real))
# Exact j^4 Pauli count.
j=4.5; ms=[-j+i for i in range(10)]; counts=Counter(sum(c) for c in combinations(ms,4));mult={int(J):counts[J]-counts[J+1] for J in range(0,19) if counts[J]-counts[J+1]}
# two-hole exact count for comparison
two=Counter(sum(c) for c in combinations(ms,2)); mult2={int(J):two[J]-two[J+1] for J in range(0,10) if two[J]-two[J+1]}
# geometry fixed-amplitude normalized Q22 scales: pair-pair equal theta has 4 sin2; two-hole has 2 sin2.
angles=[0,15,30,45,60,75,90]
with (OUT/'four_hole_geometry.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['theta_deg','T22_two_hole','T22_four_hole','Irel_two_hole','Irel_four_hole']);w.writeheader()
    for d in angles:
        s=sin(d*pi/180)**2;w.writerow(dict(theta_deg=d,T22_two_hole=2*s,T22_four_hole=4*s,Irel_two_hole=(2*s)**2,Irel_four_hole=(4*s)**2))
results={'scope':'ideal vector geometry and exact single-j Pauli counting; no Pd Hamiltonian or experimental fit','geometry':{'grid_points':91*91,'max_mu_perp':max_mu,'max_q21':max_q21,'max_Rz_pi_residual':max_rz,'max_Ry_pi_T_residual':max_ryt,'q22_equal_pair_formula':'2 sin(theta_a)^2 exp(2iphi_a)+2 sin(theta_b)^2 exp(2iphi_b)','equal_theta_phi0_T22_four_blades':'4 sin(theta)^2','equal_theta_phi0_relative_B_E2':'16 sin(theta)^4'},'pauli':{'single_j':'g9/2','two_hole_allowed_J_multiplicities':mult2,'two_hole_Jmax':max(mult2),'four_hole_allowed_J_multiplicities':mult,'four_hole_Jmax':max(mult),'fully_aligned_M':sum(sorted(ms,reverse=True)[:4]),'warning':'pairwise composite blades do not bypass full j^4 antisymmetry'},'symmetry':{'Rz_pi':'exchanges each opposite-transverse pair; requires equal pair weights/density','Ry_pi_T':'leaves every xz-plane vector invariant, but is not exclusive to AMR','odd_q':'pairwise cancellation applies to ideal equivalent pairs; pairing/off-diagonal terms require full density check'},'source_boundary':{'104Pd':'Rather2014 first page direct DSAM scope; Zhang2019 full arXiv theory','106Pd':'no Pd AMR entry found in Kumar2023 review scope; absence is not nonexistence proof','108Pd':'no Pd AMR entry found in Kumar2023 review scope; absence is not nonexistence proof'}}
(OUT/'pd_four_hole_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));(OUT/'sample_geometry.csv').write_text('')
print(json.dumps(results,ensure_ascii=False,indent=2))
