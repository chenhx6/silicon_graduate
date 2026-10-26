#!/usr/bin/env python3
"""Central summary algebra under global positive scaling of the entire M1 operator."""
from pathlib import Path
from fractions import Fraction as F
from math import sqrt
import json,datetime,hashlib
OUT=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:raise AssertionError(name)

# Native table values transcribed and source-bound. None is missing, never zero.
experimental=[
 {'label':'625','Ei':'832.0','I_i':'13/2-','I_f':'11/2-','delta':'-1.5','delta_printed_plus':'0.97','delta_printed_minus':'5.7','rE2_in':None,'rM1_in':None,'rE2_out':'1.15','rM1_out':'0.14','photon_energy_exact_keV':'624.6'},
 {'label':'582','Ei':'1409.8','I_i':'17/2-','I_f':'15/2-','delta':'-0.55','delta_printed_plus':'0.12','delta_printed_minus':'0.25','rE2_in':'0.33','rM1_in':'0.25','rE2_out':'5.06','rM1_out':'3.95','photon_energy_exact_keV':'582.7'},
 {'label':'465','Ei':'1809.1','I_i':'19/2-','I_f':'17/2-','delta':'-0.17','delta_printed_plus':'0.09','delta_printed_minus':'0.2','rE2_in':'0.09','rM1_in':'0.47','rE2_out':'1.06','rM1_out':'5.54','photon_energy_exact_keV':'464.4'}
]
models={
 'QTR_table6.9':{'pdf_page':111,'delta':['0.89','-2.24','-2.72'],'rE2_in':[None,'0.75','0.32'],'rM1_in':[None,'0.01','0.03']},
 'FA_table6.10':{'pdf_page':111,'delta':['-0.58','-0.49','-0.49'],'rE2_in':[None,'0.44','0.11'],'rM1_in':[None,'0.19','0.062']}
}
out=[]
for name,mod in models.items():
    rows=[]
    for i,exp in enumerate(experimental):
        dm=F(mod['delta'][i]);de=F(exp['delta'])
        eta_delta=dm/de
        item={'label':exp['label'],'I_i':exp['I_i'],'model_delta':str(dm),'experimental_delta':str(de),
              'eta_delta_signed_candidate':str(eta_delta),'positive_eta_delta_exists':eta_delta>0,
              'eta_from_delta':float(eta_delta) if eta_delta>0 else None,
              'eta_magnitude_only_not_a_signed_solution':float(abs(eta_delta)) if eta_delta<=0 else None}
        check(name+'_sign_preserved_'+exp['label'],(dm*de>0)==(eta_delta>0))
        if eta_delta>0:check(name+'_delta_exact_match_'+exp['label'],dm/eta_delta==de)
        if mod['rM1_in'][i] is not None:
            mm=F(mod['rM1_in'][i]);me=F(exp['rM1_in'])
            eta2=me/mm
            item.update(model_rM1_in=str(mm),experimental_rM1_in=str(me),
                        eta_squared_from_rM1=str(eta2),eta_from_rM1=sqrt(float(eta2)),
                        eta_from_delta_squared=str(eta_delta**2),
                        eta_delta_vs_rM1_squared_equal_exact=eta_delta**2==eta2,
                        model_rE2_in_unchanged=mod['rE2_in'][i],
                        experimental_rE2_in=exp['rE2_in'],
                        rE2_central_equal_before_and_after_any_eta=F(mod['rE2_in'][i])==F(exp['rE2_in']))
            check(name+'_rate_exact_match_'+exp['label'],mm*eta2==me)
            # This is deliberate expected nonclosure, not an experimental rejection.
            check(name+'_summary_delta_rate_required_scale_distinct_'+exp['label'],eta_delta**2!=eta2)
        else:
            item.update(model_rM1_in=None,experimental_rM1_in=None,eta_from_rM1=None,
                        missing_reason='No out/in ratio for this line in model and Table6.11; do not use the out/out value')
        rows.append(item)
    eta_low=F(mod['delta'][1])/F(experimental[1]['delta'])
    eta_high=F(mod['delta'][2])/F(experimental[2]['delta'])
    model_m1_spinratio=F(mod['rM1_in'][2])/F(mod['rM1_in'][1])
    exp_m1_spinratio=F(experimental[2]['rM1_in'])/F(experimental[1]['rM1_in'])
    delta_spinratio=F(mod['delta'][2])/F(mod['delta'][1])
    exp_delta_spinratio=F(experimental[2]['delta'])/F(experimental[1]['delta'])
    check(name+'_central_delta_no_common_scale',eta_low!=eta_high)
    check(name+'_central_rM1_no_common_scale',model_m1_spinratio!=exp_m1_spinratio)
    out.append({'model':name,'rows':rows,'invariants':{
        'rM1_19over17_model':str(model_m1_spinratio),'rM1_19over17_experimental':str(exp_m1_spinratio),
        'delta_19over17_model':str(delta_spinratio),'delta_19over17_experimental':str(exp_delta_spinratio),
        'central_common_eta_exactly_closes_two_delta_points':False,
        'central_common_eta_exactly_closes_two_rate_points':False,
        'meaning':'Exact central-summary diagnosis only, not a confidence/coverage or model-error test'}})

# Independent controls start from raw matrix elements, not printed ratios.
aE=F(3,2);aM=F(-2,3);bE=F(5,4);Ea=F(3,5);eta=F(7,3)
baseE=aE*aE/(bE*bE);baseM=aM*aM/(bE*bE)
scaledE=aE*aE/(bE*bE);scaledM=(eta*aM)**2/(bE*bE)
delta2=F(7,10)*Ea*Ea*aE*aE/(aM*aM)
scaled_delta2=F(7,10)*Ea*Ea*aE*aE/((eta*aM)**2)
check('matrix_element_control_E2_invariant',scaledE==baseE)
check('matrix_element_control_M1_scales_eta2',scaledM==eta*eta*baseM)
check('matrix_element_control_delta2_inverse_eta2',scaled_delta2==delta2/(eta*eta))
check('matrix_element_control_positive_eta_preserves_M1_sign',(eta*aM<0)==(aM<0))
check('dependency_delta2_rE2_rM1_control',delta2==F(7,10)*Ea*Ea*baseE/baseM)
check('dependency_after_scaling_control',scaled_delta2==F(7,10)*Ea*Ea*scaledE/scaledM)
# Holding matrix elements E2 fixed does NOT hold the model total mixed photon yield fixed.
# Choose CM1=1, CE2=.7 and a pure-E2 reference at Eb=4/5 MeV; arbitrary exact control.
Eb=F(4,5);CE2=F(7,10)
u0=(Ea**3*aM*aM+CE2*Ea**5*aE*aE)/(CE2*Eb**5*bE*bE)
u1=(Ea**3*(eta*aM)**2+CE2*Ea**5*aE*aE)/(CE2*Eb**5*bE*bE)
check('mixed_yield_changes_control',u1!=u0)
check('mixed_yield_transformation_control',u1==u0*(eta*eta+delta2)/(1+delta2))
check('branch_reconstruction_before_control',u0*delta2/(1+delta2)*(Eb/Ea)**5==baseE)
check('branch_reconstruction_after_control',u1*scaled_delta2/(1+scaled_delta2)*(Eb/Ea)**5==scaledE)
m1a,m1b=F(1,100),F(3,100)
check('spin_ratio_invariant_control',(eta*eta*m1b)/(eta*eta*m1a)==m1b/m1a)
check('delta_relative_sign_invariant_control',(F(-2,eta)*F(3,eta)<0)==(F(-2)*F(3)<0))
# Explicit gs-only counterexample with unequal component fractions, not a fit.
core_l_terms=[F(1),F(2)];spin_terms=[F(1),F(-1)];eta_s=F(2)
before=[c+s for c,s in zip(core_l_terms,spin_terms)]
after=[c+eta_s*s for c,s in zip(core_l_terms,spin_terms)]
check('gs_only_not_whole_operator_control',after[0]/before[0]!=after[1]/before[1])
figure_branch={
 'source':'Fig6.16/PDF114; visual order-of-magnitude, not digitized points',
 'QTR_rM1_first':'about 0.10 in figure versus 0.01 in Table6.9',
 'QTR_rM1_second':'about 0.03 in figure and Table6.9',
 'QTR_qualitative_trend_figure':'decreasing; unchanged by a positive common eta-squared',
 'QTR_qualitative_trend_table':'increasing 0.01 to0.03, preserved as a different source branch',
 'FA_rE2_figure':'about .044/.011 versus Table6.10 .44/.11; no M1 scaling changes either branch rE2',
 'graph_eta_fit_performed':False,
 'graph_values_substituted_into_table':False
}
r={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'scope':'Fixed H/states/E2/energies, entire M1 operator times common real eta>0; no actual g fit',
   'source_sha256':hashlib.sha256(Path('/workspace/wiki/raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf').read_bytes()).hexdigest(),
   'units':{'eta':'dimensionless','rE2':'dimensionless','rM1':'muN^2/(e^2 b^2)','delta':'dimensionless'},
   'experimental_printed_table6.11':experimental,'models_printed':models,'required_scales':out,
   'figure_conflict_branch':figure_branch,
   'independent_matrix_element_control':{'eta':str(eta),'E2_element':str(aE),'M1_element':str(aM),'E2_reference':str(bE),'Ea_MeV':str(Ea),'base_rE2':str(baseE),'base_rM1':str(baseM),'base_delta2':str(delta2),'scaled_rE2':str(scaledE),'scaled_rM1':str(scaledM),'scaled_delta2':str(scaled_delta2),'pure_E2_reference_Eb_MeV':str(Eb),'mixed_photon_yield_before':str(u0),'mixed_photon_yield_after':str(u1),'mixed_yield_fixed':False},
   'checks':checks,'all_pass':all(c['passed'] for c in checks),
   'nonclaims':['No significance or confidence interval','No lifetime or absolute B estimate','No actualresponse or global g-factor fit','No exclusion of arbitrary gs/gl/gR/H/space changes','No model-producer error judgment','Printed signed-error endpoints are not coverage']}
(OUT/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
print(json.dumps({'all_pass':r['all_pass'],'checks':len(checks),'required_scales':out},ensure_ascii=False,indent=2))
