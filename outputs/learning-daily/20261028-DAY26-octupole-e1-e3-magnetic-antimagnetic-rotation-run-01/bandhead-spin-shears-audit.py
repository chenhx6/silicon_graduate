"""Band-head spin audit for fixed two-blade shears geometry.

Inputs are nominal configurations read from the cited review/primary sources.
The Pr neutron-pair j=10 assignment is a toy two-blade reduction; it is not
an absolute extraction of core angular momentum.
"""
from pathlib import Path
import csv,json,math
out=Path(__file__).resolve().parent
cases=[
 {'case':'199Pb Hübel Band 2','j1':11.0,'j2':14.5,'I0':17.5,'source':'Hübel2005 p.49: proton 11, neutron 29/2, coupled to 35/2'},
 {'case':'197Pb Hübel Band 2 cross-check','j1':11.0,'j2':14.5,'I0':18.5,'source':'Hübel2005 p.60: ABE11 band-head 37/2'},
 {'case':'135Pr nominal 3qp','j1':5.5,'j2':10.0,'I0':13.5,'source':'Garg2015 pp.7-8: low band begins at 27/2; neutron h11/2 hole pair nominal J=10'},
 {'case':'137Pr nominal 3qp','j1':5.5,'j2':10.0,'I0':13.5,'source':'Agarwal2007 pp.6-8: 3qp pi h11/2 x nu(h11/2)^-2; 27/2 low band identity'},
]
rows=[]
for d in cases:
 j1,j2,I0=d['j1'],d['j2'],d['I0']; S=j1*(j1+1)+j2*(j2+1)
 ic=math.sqrt(j1*j1+j2*j2); iq=(-1+math.sqrt(1+4*S))/2
 # nearest physically allowed half/integer spin to quantum root
 allowed=[abs(j1-j2)+n for n in range(int(j1+j2-abs(j1-j2))+1)]
 iq_near=min(allowed,key=lambda x:abs(x-iq))
 c_q=(I0*(I0+1)-S)/(2*math.sqrt(j1*(j1+1)*j2*(j2+1)))
 c_cl=(I0*I0-j1*j1-j2*j2)/(2*j1*j2)
 rows.append({**d,'I90_classical':ic,'I90_casimir_continuous':iq,'I90_allowed_nearest':iq_near,'delta_I0_classical':I0-ic,'delta_I0_casimir':I0-iq,'theta_casimir_at_observed_deg':math.degrees(math.acos(max(-1,min(1,c_q)))),'theta_classical_I2_at_observed_deg':math.degrees(math.acos(max(-1,min(1,c_cl)))),'allowed_spins':allowed})
with (out/'bandhead-spin-shears-audit.csv').open('w',newline='') as f:
 keys=['case','j1','j2','I0','I90_classical','I90_casimir_continuous','I90_allowed_nearest','delta_I0_classical','delta_I0_casimir','theta_casimir_at_observed_deg','theta_classical_I2_at_observed_deg','source']
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();
 for r in rows:w.writerow({k:r[k] for k in keys})
meta={'status':'conditional-audit','formula_classical':'I90=sqrt(j1^2+j2^2)','formula_quantum':'solve I(I+1)=j1(j1+1)+j2(j2+1)','caveat':'P2 minimum does not by itself fix observed bandhead when core energy, configuration mixing and finite-spin spacing are included','cases':rows,'not_an_absolute_core_spin_extraction':True}
(out/'bandhead-spin-shears-audit.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
