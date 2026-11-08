#!/usr/bin/env python3
"""Bounded seniority-zero pair-basis control; not a real-nucleus calculation."""
import json, math, sys
from pathlib import Path
p = json.loads(Path(sys.argv[1]).read_text())
O, eps, g = p['Omega'], p['epsilon'], p['G']
assert O == 2 and eps > 0 and g > 0
L = 2*O

def energy(t):
    x=(1+t)/2
    v=[math.sqrt(x)]*O+[math.sqrt(1-x)]*O
    u=[math.sqrt(1-z*z) for z in v]
    a=[]
    for s in range(1<<L):
        z=1.0
        for i in range(L): z*=v[i] if s>>i&1 else u[i]
        a.append(z)
    one=0.0
    pair=0.0
    for s, amp in enumerate(a):
        one += amp*amp*sum((-eps if i<O else eps) for i in range(L) if s>>i&1)
        for j in range(L):
            if not (s>>j&1): continue
            target=s & ~(1<<j)
            for i in range(L):
                if not (target>>i&1): pair+=a[target | (1<<i)]*amp
    return one-g*pair

def formula(t):
    q=(1-t*t)/4
    return -O*eps*t-g*(O+(4*O*O-2*O)*q)
rows=[]
for t in p['t_values']:
    direct=energy(t); analytic=formula(t)
    assert abs(direct-analytic)<1e-12
    rows.append({'t':t,'direct_pair_basis_energy':direct,'analytic_energy':analytic})
tstar=eps/(g*(2*O-1))
assert 0<tstar<1
h=1e-5
slope=(energy(tstar+h)-energy(tstar-h))/(2*h)
curvature=(energy(tstar+h)-2*energy(tstar)+energy(tstar-h))/(h*h)
assert abs(slope)<1e-9 and curvature>0
xi,d=p['matrix_xi'],p['matrix_delta']; E=math.hypot(xi,d)
u=math.sqrt((1+xi/E)/2); v=math.sqrt((1-xi/E)/2)
res_minus=math.hypot(xi*u-d*v-E*u, -d*u-xi*v-E*v)
res_plus=math.hypot(xi*u+d*v-E*u, d*u-xi*v-E*v)
assert res_minus>1 and res_plus<1e-12
s=p['binding_stagger_amplitude']; b=lambda n:100+4*n+s*(-1)**n
n=10
raw3=(-1)**n/2*(b(n-1)-2*b(n)+b(n+1))
raw4=(-1)**n/4*(b(n-2)-3*b(n-1)+3*b(n)-b(n+1))
assert abs(raw3+2*s)<1e-12 and abs(raw4-2*s)<1e-12
print(json.dumps({'model':'pair-only Hamiltonian, 2*Omega binary pair sites; BCS product; energies in epsilon units','rows':rows,'stationary_t':tstar,'stationary_slope_numeric':slope,'stationary_curvature_numeric':curvature,'Gcrit_pair_only':eps/(2*O-1),'Gcrit_Suhonen':2*eps/(4*O-1),'lambda_pair_only':-g/2,'lambda_Suhonen':-3*g/4,'eigenvector_uv_positive':[u,v],'matrix_minus_residual':res_minus,'matrix_plus_residual':res_plus,'positive_B_raw_three_point':raw3,'positive_B_raw_four_point':raw4},indent=2))
