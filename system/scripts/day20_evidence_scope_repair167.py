#!/usr/bin/env python3
"""Audit already-opened inputs; conditional calculations, no experimental CI."""
import hashlib,json,math
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from day20_invariant_network_ledger147 import ledger
root=Path(__file__).resolve().parents[2]
d=root/'outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02'
p=d/'invariant-network-input-147.json';inputs=json.loads(p.read_text())
source=Path(inputs['source_file']);assert hashlib.sha256(source.read_bytes()).hexdigest()==inputs['source_sha256']
a=np.array([float(x['central_eb']) for x in inputs['ground_to_two']]);D=np.zeros((6,6))
for x in inputs['two_to_two']:D[x['i']-1,x['j']-1]=D[x['j']-1,x['i']-1]=float(x['central_eb'])
assert D[0,0]==-.24 and D[0,1]==.535
full=ledger(inputs);prefix=[]
for n in range(1,4):
 v=a[:n];m=D[:n,:n];s=float(v@m@v);ratio=-math.sqrt(.7)*s/float(v@v)**1.5
 # Explicit loop summation is independent of matrix contraction implementation.
 loops=sum(float(v[i]*m[i,j]*v[j]) for i in range(n) for j in range(n))
 assert abs(loops-s)<1e-14
 prefix.append({'states':n,'aDa_eb3':s,'ratio':ratio,'effective_angle_deg':math.degrees(math.acos(ratio))/3,'meaning':'Truncated printed central values; outside projection unspecified'})
diag=a[0]**2*D[0,0];cross=2*a[0]*a[1]*D[0,1];net2=float(a[:2]@D[:2,:2]@a[:2]);coeff=abs(diag/net2)
# Q=1,2 equal weight: official FINT formula from sigma.f443-446.
M={k:(1+2**k)/2 for k in [2,3,4]};fint=((math.sqrt(M[2])+M[4]**.25)/2)**3
# Explicit positive counterexample to any universal downward FINT bias:
# Q=1,2 with weights .9,.1; no experimental attribution.
F01=((math.sqrt(1.3)+2.5**.25)/2)**3
assert fint<M[3] and F01>1.7
cg=math.sqrt(169/114);converted=2.72/cg
result={'observed_at_utc':datetime.now(timezone.utc).isoformat(),'kind':'Corrective transformations of existing source ledger, not new source or experiment','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_sha256_verified':inputs['source_sha256'],'ge76':{'prefixes':prefix,'D11_eb':D[0,0],'D12_eb':D[0,1],'diagonal_loop_eb3':diag,'two_cross_loops_eb3':cross,'D22_loop_eb3':a[1]**2*D[1,1],'cross_over_D11_abs_percent':abs(cross/diag)*100,'D11_relative_sensitivity_on_full_two_state_aDa':coeff,'unlisted_terms':full['unknown_in_selected_network'],'not_inferred':['true gamma','joint CI','missing RMEs zero','unavoidable failure of published fit']},'fint':{'official_expression':'((sqrt(M2)+M4**.25)/2)**3','Q1Q2_equal':{'M3':M[3],'FINT':fint,'true_angular_variance':0,'apparent_cos':M[3]/fint},'Q1Q2_unequal':{'M3':1.7,'FINT':F01,'proves':'Bias is not universally downward; Weights are declared mathematical probabilities, not fitted nuclear amplitudes'},'old_formula':'M2**.75*M4**.25 has Q**2.5 dimensions and is not official code'},'ce27':{'candidate_CG_ratio':cg,'Li_Qt_under_candidate_K_conversion_eb':converted,'relative_central_residual_to_Singh_percent':(converted/2.26-1)*100,'boundary':'Candidate convention change, not identification of actual K/producer or new precision test'},'scope_boundary':'Original time spectra, producer and Cov unavailable; 69 JSON rows and 653 text hits do not certify science or exact mapping.'}
out=d/'evidence-scope-repair-result-167.json'
with out.open('x') as h:json.dump(result,h,ensure_ascii=False,indent=2);h.write('\n')
print(json.dumps({'prefix_angles':[x['effective_angle_deg'] for x in prefix],'cross_fraction_pct':abs(cross/diag)*100,'FINT_Q1Q2_unequal':F01,'candidate_CG_residual_percent':(converted/2.26-1)*100}))
