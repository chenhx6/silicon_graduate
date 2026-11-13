#!/usr/bin/env python3
"""Bounded monopole, isospin-count and nonorthogonal-overlap algebra."""
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
here = ROOT / 'outputs/l4/20261108-A130-monopole-centroid-controls'
here.mkdir(parents=True, exist_ok=True)
input_path = here / 'control-input.json'
x = json.loads(input_path.read_text())
g = x['two_j'] + 1
n, e, v = x['n'], x['e0'], x['V']
energy = lambda k: e * k + v * k * (k - 1) / 2
addition, removal = energy(n+1)-energy(n), energy(n)-energy(n-1)
centroid = ((g-n)*addition + n*removal)/g
w0, w1 = (g+1)/(2*g), (g-1)/(2*g)
J0 = [J for J in range(x['two_j']+1) if J % 2 == 1]
J1 = [J for J in range(x['two_j']+1) if J % 2 == 0]
d0, d1 = sum(2*J+1 for J in J0), sum(2*J+1 for J in J1)
u1,u2=x['u1'],x['u2']
s=[a+b for a,b in zip(u1,u2)]
norm=math.sqrt(sum(a*a for a in s))
psi=[a/norm for a in s]
overlaps=[sum(a*b for a,b in zip(u,psi))**2 for u in (u1,u2)]
assert (d0,d1)==(g*(g+1)//2,g*(g-1)//2)
assert math.isclose(centroid,e+v*n*(1-1/g))
assert math.isclose(d0/g**2,w0) and math.isclose(d1/g**2,w1)
assert all(math.isclose(sum(a*a for a in u),1) for u in (u1,u2))
assert math.isclose(sum(a*a for a in psi),1)
assert sum(overlaps)>1
non_half=[]
for occ in (1, 2, 3):
    plus, minus = energy(occ+1)-energy(occ), energy(occ)-energy(occ-1)
    deriv = e+v*(occ-0.5)
    spectral = ((g-occ)*plus+occ*minus)/g
    assert math.isclose(spectral,e+v*occ*(1-1/g))
    if occ != g/2:
        assert not math.isclose(spectral,deriv)
    non_half.append({'n':occ,'addition':plus,'removal':minus,'continuous_derivative':deriv,'spectral_centroid':spectral})
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result={'executed_utc':datetime.now(timezone.utc).isoformat(), 'producer_sha256':sha(Path(__file__)), 'input_sha256':sha(input_path), 'g':g, 'J_T0':J0, 'J_T1':J1, 'dimensions_T0_T1':[d0,d1], 'weights_T0_T1':[w0,w1], 'pn_centroid':w0*x['T0']+w1*x['T1'], 'forward_addition':addition, 'removal':removal, 'continuous_derivative':e+v*(n-0.5), 'complete_centroid':centroid, 'overlap_probabilities':overlaps, 'overlap_sum':sum(overlaps), 'expansion_coefficient_square_sum':2/norm**2, 'non_half_filling_checks':non_half, 'status':'assertions_passed', 'scope':'illustrative algebra; no MCSM recomputation'}
(here/'control-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
