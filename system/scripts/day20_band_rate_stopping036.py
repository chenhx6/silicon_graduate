#!/usr/bin/env python3
"""Literal band/rate/stopping ledger with conditional response controls, no original fit/CI."""
import argparse,hashlib,json,math
from pathlib import Path


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args()
 controls=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  controls.append(name)
 # Klemme TableI mean/error column, not individual ring row or TableII adopted errors.
 entries=[['6g',1.38,.04,1.63,.06],['8g',.85,.06,1.03,.10],['8gamma',1.04,.20,1.24,.30],['10S1',.58,.02,.71,.04],['12S1',.47,.02,.59,.04],['16S2',.55,.11,.68,.13]]
 corrections=[]
 for name,t,e,tc,ec in entries:
  half=(t+tc)/2;corrections.append({'state':name,'TableI_mean_ps':t,'TableI_mean_error_ps':e,'TableI_corrected_ps':tc,'TableI_corrected_error_ps':ec,'central_correction_factor':tc/t,'chosen_half_chart_tau_ps':half,'conditional_Qt_relative_shift_half_vs_full':math.sqrt(tc/half)-1})
 check('nonuniform central finite-stopping corrections',max(v['central_correction_factor'] for v in corrections)-min(v['central_correction_factor'] for v in corrections)>.07)
 changes=[]
 for a,b in [('12S1','10S1'),('8g','6g')]:
  x=next(r for r in corrections if r['state']==a);y=next(r for r in corrections if r['state']==b)
  ratio=math.sqrt((y['chosen_half_chart_tau_ps']/x['chosen_half_chart_tau_ps'])/(y['TableI_corrected_ps']/x['TableI_corrected_ps']))
  changes.append({'ratio':a+'/'+b,'conditional_ratio_change_half_vs_full':ratio-1})
 check('half-chart small ratio shifts are not exactly zero',all(abs(r['conditional_ratio_change_half_vs_full'])>1e-4 for r in changes))
 # TableII prints B in10^3 e^2 fm^4: 10^3 fm^4=0.1 b^2.
 strengths=[{'parent':'4g+','daughter':'2g+','Egamma_keV':495,'printed_B_number':5.53,'printed_B_error':.13,'printed_Qt_eb':4.40,'printed_Qt_error_eb':.05}, {'parent':'10S2+','daughter':'8g+','Egamma_keV':925,'printed_B_number':.09,'printed_B_error':.02,'printed_Qt_eb':.51,'printed_Qt_error_eb':.04}]
 for r in strengths:r['B_e2b2']=r['printed_B_number']*.1;r['B_error_e2b2']=r['printed_B_error']*.1
 check('literal TableII units yield.553 and.009, not1.87 and.029',math.isclose(strengths[0]['B_e2b2'],.553) and math.isclose(strengths[1]['B_e2b2'],.009))
 # Literal MU07 TableI, errors omitted in ratio controls but retained in table ledger.
 arows=[[29,1.,.05,3.2,.2,.32,.02],[31,.75,.08,2.5,.3,.32,.03],[33,.44,.02,2.2,.2,.32,.03],[35,.28,.02,2.4,.3,.32,.03],[37,.23,.02,1.7,.3,.32,.04],[39,.22,.02,2.1,.3,.13,.03],[41,.18,.02,2.1,.3,.19,.03],[43,.16,.02,2.,.3,.21,.04]]
 brows=[[31,1.46,.02,2.7,.3,.28,.03],[33,.87,.06,2.1,.2,.28,.03],[35,.64,.05,2.2,.2,.28,.04],[37,.48,.03,1.7,.2,.29,.04],[39,.24,.04,1.9,.3,.11,.03]]
 fields=['two_I','tau_ps','tau_error_ps','B_M1_muN2','B_M1_error','B_E2_e2b2','B_E2_error']
 bandA=[dict(zip(fields,row)) for row in arows];bandB=[dict(zip(fields,row)) for row in brows];ratios=[]
 for y in bandB:
  x=next(r for r in bandA if r['two_I']==y['two_I']);tr=y['tau_ps']/x['tau_ps'];br=y['B_E2_e2b2']/x['B_E2_e2b2']
  ratios.append({'two_I':x['two_I'],'tau_B_over_A':tr,'B_E2_B_over_A':br,'B_M1_B_over_A':y['B_M1_muN2']/x['B_M1_muN2'],'conditional_p_over_E5_B_over_A':tr*br})
 check('39/2 E2 ratio outside old.875-.906 blanket interval',ratios[-1]['B_E2_B_over_A']<.85)
 span=60.1/.16
 check('literal low/high central lifetime span375.625 not500.8',math.isclose(span,375.625))
 # LV21TableII: each gamma has explicit identity, not invented delta_max bounds.
 links=[['TiP1','D1',13,11,518.1,-.11,.05,-.024,.010],['TiP1','D1',15,13,566.8,-.48,.14,-.019,.006],['TiP1','D1',17,15,618.3,-.32,.05,-.012,.004],['TiP1','D1',19,17,566.0,-.33,.09,-.081,.072],['TiP1','D1',21,19,560.7,-.16,.07,None,None],['TiP2','TiP1',17,15,518.3,-.26,.08,-.14,.08]]
 fields2=['initial_band','final_band','two_I_initial','two_I_final','Egamma_keV','delta','delta_printed_error','AP','AP_printed_error'];tip=[dict(zip(fields2,row)) for row in links]
 for r in tip:r['central_E2_fraction_from_delta']=r['delta']**2/(1+r['delta']**2)
 check('566.8keV printed delta endpoint permits M1 fraction below80percent',1/(1+(.48+.14)**2)<.8)
 out={'checkpoint':'036','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'Klemme_TableI_stopping':corrections,'half_chart_ratio_response':changes,'stopping_contract':'tau(f)=standard+f(corrected-standard),f=.5..1 is chosen affine sensitivity chart, not original refit or physical response map to electronic stopping+30percent; no Cov recovery.',
 'Klemme_TableII_selected_strengths':strengths,'branch_geometry_boundary':'Different parents/spins, one in-band and one interband: central B or effective Qt quotients are not same-state shape ratios, orthogonality proof or mixing mechanism identification.',
 'MU07_TableI_bandA':bandA,'MU07_TableI_bandB':bandB,'matched_central_ratios':ratios,
 'rate_identity_boundary':'p_gamma/Egamma^5 ratio from tau and derivedB is algebraic recycling under same rate coefficient, not independent branch/energy determination. TableI lacks line-specific E2 energy/final state; do not infer actual9–14percent energy shift.',
 'central_tau_span':{'Klemme_low_spin_tau_ps':60.1,'MU07_43over2_tau_ps':.16,'ratio':span,'boundary':'Different campaigns/configurations/parents; central numerical span not continuous phase trajectory.'},
 'LV21_TableII_selected_links':tip,'interpretation_boundary':'M1-dominated links plus QTR comparison support author TiP interpretation, not unique identity proof. 566.8 error endpoint allows M1<80percent; missing AP not negative measurement. No measured29/2 universal static-chirality threshold; MU07 RPA critical point model offset about1h from closest-data point and harmonic approximation breaks down there.',
 'controls':controls,'certification_scope':'Literal table and chosen response algebra only; no original experimental precision or complete phase diagram certification.'}
 path=args.run_dir/'band-rate-stopping-result-036.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(path),'controls':len(controls),'span':span,'strengths_e2b2':[r['B_e2b2'] for r in strengths],'ratios':changes}))
if __name__=='__main__':main()
