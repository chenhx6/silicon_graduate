"""Finite rational spot checks of high-K energy differences and SI normalization."""
import json
from fractions import Fraction as F
from pathlib import Path
checks=[]
# Units: choose numerical hbar, J; K may be integer or half-integer.
for K in [F(1),F(3,2),F(8),F(25,2),F(100)]:
 for n in [1,2,3]:
  h,J=F(3),F(7)
  spectrum=lambda I: h*h*(I*(I+1)-K*K)/(2*J)
  observed=spectrum(K+n)-spectrum(K)
  harmonic=n*h*h*K/J
  correction=h*h*n*(n+1)/(2*J)
  checks.append({'K':str(K),'n':n,'bandhead_difference':str(observed),'equals_harmonic_plus_finite_K_correction':observed==harmonic+correction})
# A dimensionless ratio is invariant when M_S=M_mu/c and q=E/(hbar*c).
E,h,c,E2,M=F(13),F(5),F(299),F(17),F(19)
charge_type=(E/(h*c))*E2/(M/c)
magnetic_type=(E/h)*E2/M
result={'kind':'finite exact rational spot checks, not a proof or model validation','energy_cases':checks,'SI_forms_equal':charge_type==magnetic_type,'missing_c_produces_relative_factor':str(((E/(h*c))*E2/M)/magnetic_type)}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'energy_cases':len(checks),'all_energy_cases_pass':all(x['equals_harmonic_plus_finite_K_correction'] for x in checks),'SI_forms_equal':result['SI_forms_equal'],'missing_c_produces_relative_factor':result['missing_c_produces_relative_factor']},ensure_ascii=False))
if not result['SI_forms_equal'] or not all(x['equals_harmonic_plus_finite_K_correction'] for x in checks): raise SystemExit(1)
