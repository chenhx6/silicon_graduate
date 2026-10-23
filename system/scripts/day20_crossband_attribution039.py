#!/usr/bin/env python3
"""Literal cross-band comparison and declared Babra table diagnostics, no universal laws/CI."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.stats import t as student_t


def fit(x,y,e):
 X=np.column_stack([np.ones(len(x)),x-np.mean(x)]);W=np.diag(e**-2);C=np.linalg.inv(X.T@W@X);b=C@X.T@W@y
 return {'slope':float(b[1]),'slope_se':float(math.sqrt(C[1,1])),'z':float(b[1]/math.sqrt(C[1,1]))}


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);a=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 # Full TableII MU08 central ledger, missing Band1 E2/Qt15 retained None.
 rows1=[[15,.93,.09,2.7,.3,None,None,None,None],[16,.88,.10,1.7,.2,.26,.03,1.73,.10],[17,.71,.06,1.1,.1,.08,.01,.95,.06],[18,.56,.08,.9,.2,.14,.02,1.26,.09],[19,.32,.05,1.7,.3,.11,.02,1.11,.10]]
 rows2=[[15,1.27,.06,4.4,.3,.54,.08,2.50,.19],[16,.87,.08,3.5,.3,.51,.07,2.42,.17],[17,.61,.07,1.4,.2,.44,.06,2.24,.15],[18,.51,.07,1.,.2,.04,.01,.67,.08],[19,.31,.05,1.6,.3,.05,.01,.75,.08]]
 fields=['I','tau_ps','tau_error','B_M1','B_M1_error','B_E2','B_E2_error','Qt_eb','Qt_error'];table=[{'band':band,**dict(zip(fields,r))} for band,data in [(1,rows1),(2,rows2)] for r in data]
 diag_sums={i:sum(r['B_E2'] for r in table if r['I']==i) for i in [17,18]}
 check('two diagonal sums differ, without identifying missing channels',math.isclose(diag_sums[17],.52) and math.isclose(diag_sums[18],.18))
 check('literal Band2 center quotients11 and3.343',math.isclose(.44/.04,11) and math.isclose(2.24/.67,3.3432835820895526))
 # Babra TableI finite Qt asymmetric errors plus effective upper tau/lower Qt at20.
 spins=np.array([8,10,12,14,16,18]);q=np.array([5.66,5.59,5.70,5.38,4.85,5.05]);minus=np.array([.19,.79,.20,.33,.32,.33]);plus=np.array([.19,.78,.21,.34,.34,.37]);err=(plus+minus)/2
 qrows=[{'I':int(i),'Qt':float(v),'minus':float(lo),'plus':float(hi)} for i,v,lo,hi in zip(spins,q,minus,plus)]
 mean=lambda vs,es:float(np.sum(vs/es**2)/np.sum(es**-2));se=lambda es:float(1/math.sqrt(np.sum(es**-2)))
 pre,post=mean(q[:3],err[:3]),mean(q[3:],err[3:]);epre,epost=se(err[:3]),se(err[3:]);delta=post-pre;edelta=math.hypot(epre,epost)
 full=fit(spins,q,err);lower=fit(spins,q,minus);upper=fit(spins,q,plus)
 X=np.column_stack([np.ones(len(spins)),spins-np.mean(spins)]);beta=np.linalg.lstsq(X/err[:,None],q/err,rcond=None)[0];chi=float(np.sum(((q-X@beta)/err)**2));df=len(spins)-2;ts=full['z']/math.sqrt(chi/df)
 check('known-variance Gaussian and unknown-scale Student contracts differ',df==4 and not math.isclose(ts,full['z']))
 check('prepost central difference aboutminus10.3percent',-.104<(post/pre-1)<-.102)
 # Within a complete fixed initial/final space, Frobenius norm is preserved by
 # orthogonal basis change. That does not equate matrices at different spins.
 m17=np.diag(np.sqrt([.08,.44]));m18=np.diag(np.sqrt([.14,.04]))
 check('distinct transition operators can change total without interband transfer',np.count_nonzero(m17-np.diag(np.diag(m17)))==0 and np.count_nonzero(m18-np.diag(np.diag(m18)))==0 and not math.isclose(float(np.sum(m17*m17)),float(np.sum(m18*m18))))
 out={'checkpoint':'039','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'MU08_TableII_literal':table,'MU08_selected_central_diagonal_sums':diag_sums,
 'MU08_boundary':'Band2 I17/I18 central B and Qt quotient only; not gamma17->18 transition. Different spin operators, branch and configuration assignments; absent complete measured interbandE2 matrix cannot assign.34 missing-strength budget. Author model excludes band mixing; two-configuration mixing is interpretation, not fully solved transfer.',
 'Babra_TableI_finite_Qt':qrows,'Babra_TableI20_limit':{'tau_literal_ps':'<0.16(4)','Qt_literal_eb':'>4.74(55)','role':'effective lifetime upper limit with100percent topfeeding assumption and Qt lower limit; not seventh finiteGaussian point'},
 'Babra_conditional_symmetric_independent':{'pre_mean':pre,'pre_se':epre,'post_mean':post,'post_se':epost,'post_minus_pre':delta,'difference_se':edelta,'difference_z':delta/edelta,'relative_center_change':post/pre-1,'six_point_line':full,'residual_scaled':{'chi2':chi,'degrees_of_freedom':df,'t':ts,'two_sided_Student_p':float(2*student_t.sf(abs(ts),df))},'all_lower_error_diagnostic':lower,'all_upper_error_diagnostic':upper,'boundary':'Fixed split8–12vs14–18; symmetrized independentGaussian diagnostics only. Asymmetric likelihood, actualCov, allnuisance unknown; no author significance or causal identification.'},
 'Babra_author_interpretation':'Original lifetime/Qt trend plus TRS/TPSM supports authors gamma-soft to more stable triaxial interpretation. Chosen mixing counterexamples do not exclude this or establish actual singlemechanism.',
 'discarded_atlas_generalizations':['Universal nu_i13/2 polarization step and7.2eb platform','Different parent interband/inband Qt quotient is shape collapse','Computed deficit is observed transfer to interband branches','Prepost mean ratio implies totalB strength ratio for different transitions','Commonstopping errors necessarily cancel for actualexperiment'],
 'spin_operator_counterexample':'Own independent diagonal matrices at17and18, scaled reduced amplitudes. Different norms without offdiagonal elements demonstrates no automatic crossspin conservation; not fit of136Nd.',
 'audit_hypothesis_correction':'Initial expectation that known-error Gaussian result should equaloldminus2.721 failed; exact recomputation confirmed oldminus2.18 Gaussian arithmetic. minus2.721 is residual-scaled Student t(df4), not Gaussian z. Source wording and mechanisms, not correct Gaussian center, are repaired.',
 'controls':checks,'certification_scope':'Literal central ledger and explicitly conditional diagnostics only; no universal mechanism, independent newmeasurement or experimentalCI.'}
 path=a.run_dir/'crossband-attribution-result-039.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(path),'controls':len(checks),'prepost':[pre,post,delta,edelta,delta/edelta],'full_line':full}))
if __name__=='__main__':main()
