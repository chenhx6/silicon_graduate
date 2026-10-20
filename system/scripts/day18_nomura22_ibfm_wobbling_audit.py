#!/usr/bin/env python3
"""Primary-anchored model-vector and conditional mixing-fraction audit.

No experimental response refit, branch confidence, or universal mode verdict.
Old result-033/result-021 are superseded; this script never overwrites them.
"""
import hashlib,json,math
from pathlib import Path
import pymupdf
RUN=Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
NOM=Path('raw/papers/2022_Nomura et al_Questioning the wobbling interpretation of low-spin bands in γ -soft nuclei within the interacting b.pdf')
TIM=Path('raw/papers/2019_Timár et al_Experimental Evidence for Transverse Wobbling in Pd 105.pdf')

def fractions(delta):
    return delta*delta/(1+delta*delta),1/(1+delta*delta)

def main():
    checks=[]
    def check(name,ok,**evidence):
        checks.append({'name':name,'passed':bool(ok),**evidence});assert ok,name
    expected={NOM:'e61e3dd6fe5e67fb55543f3a136c7cce0fda98ad01f112d81d5eef70b613465f',TIM:'3948cf32712a400aa8df0aee489ebebd89df7480508bddc60156a359ed322909'}
    for f,h in expected.items():check(f.name+' hash',hashlib.sha256(f.read_bytes()).hexdigest()==h)
    with pymupdf.open(NOM) as d:
        check('Nomura eleven pages',len(d)==11)
        table=d[9].get_text().replace('−','-')
        check('Nomura TableII exact selected printed tokens',all(v in table for v in ['-0.368','-1.801','0.163','0.401']))
    with pymupdf.open(TIM) as d:
        check('Timar six pages',len(d)==6)
        p3,p5=d[2].get_text(),d[4].get_text()
        check('author explicitly supports larger deltas with polarization','strongly support' in p3 and 'smaller mixing ratios' in p3)
        check('author gives scissors-mode rationale','scissors' in p5 and '0.36' in p5)
        check('TableI labels normalization point','Normalization point' in p5)
    for delta in [0.,-.37,.59,-1.,1.801,100.]:
        fe,fm=fractions(delta)
        check(f'photon fraction normalization {delta}',math.isclose(fe+fm,1.,abs_tol=1e-14))
        check(f'sign invariant fraction {delta}',fractions(-delta)==(fe,fm))
    controls=[]
    for energy,old,new,re2,rm1 in [(991,1.8,.59,.66,.162),(1034,2.3,.40,.60,.089)]:
        fe_old,fm_old=fractions(old);fe_new,fm_new=fractions(new)
        a,b=re2*fe_new/fe_old,rm1*fm_new/fm_old
        check(f'{energy} replacement conserves specified total photon rate',math.isclose(fe_old*(a/re2)+fm_old*(b/rm1),1.,abs_tol=1e-14))
        controls.append({'energy_keV':energy,'adopted_delta':old,'DCO_alternative_delta':new,'conditional_RE2':a,'conditional_RM1':b,'actual_branch_likelihood':'not calculated; same experiment polarization supports adopted branch'})
    q=.36
    check('coefficient amplitude vs strength',math.isclose(q*q,.1296) and math.isclose(1/(q*q),7.71604938271605))
    gnu,grot=-.3,.4
    check('quenching difference differs from quenching neutron alone',not math.isclose(q*(gnu-grot),q*gnu-grot))
    xe_fraction=fractions(-1.801)[0]
    check('Xe same model row remains E2 dominant',xe_fraction>.5)
    check('Pr central proximity is arithmetic only',math.isclose(abs(-.368-(-.37)),.002,abs_tol=1e-14))
    out={'kind':'primary-token-and-conditional-algebra-not-experiment-fit','sources':[{'path':str(p),'sha256':h} for p,h in expected.items()], 'supersedes':['nomura22-ibfm-wobbling-result-033.json','timar19-105pd-wobbling-result-021.json'],'nomura_selected_model_vector':{'Pr813':{'delta':-.368,'RE2':.040,'reported_Lv_delta':-.37,'reported_Lv_error_plus':.10,'reported_Lv_error_minus':.14,'reported_Lv_RE2':.12,'RE2_error':.08},'Xe735':{'delta':-1.801,'RE2':.163,'E2_photon_fraction':xe_fraction},'comparison_boundary':'selected RE2 proximity to prior .164 does not identify same delta, matrix elements or physical solution'},'conditional_delta_controls':controls,'effective_g_scaling':{'q':q,'amplitude_multiplier':q,'strength_multiplier':q*q,'inverse_strength':1/(q*q),'delta_multiplier':1/q,'actual_operator_producer':'not recovered'},'unsupported_994_delta_035_excluded':True,'independent_experiment_or_CI':False,'checks':checks,'valid':all(v['passed'] for v in checks)}
    p=RUN/'mixed-boundary-result-047.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valid':out['valid'],'checks':len(checks),'Xe_E2_fraction':xe_fraction,'output':str(p)}))
if __name__=='__main__':main()
