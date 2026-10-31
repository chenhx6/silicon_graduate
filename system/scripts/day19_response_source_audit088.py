#!/usr/bin/env python3
"""Declared response design and literal table controls; no experimental fit/CI.

Inputs are visually transcribed from the original pages listed in the result.
Run from /workspace/wiki. Historical result files are never overwritten.
"""
from pathlib import Path
import hashlib
import json
import math
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01'


def simpson(f, lo, hi, n=4000):
    h = (hi-lo)/n
    return h/3 * (f(lo)+f(hi)+sum((4 if i % 2 else 2)*f(lo+i*h) for i in range(1,n)))


def response(beta, mu, a):
    d = math.sqrt(1-beta*beta)/(1-beta*mu)
    mu_rest = (mu-beta)/(1-beta*mu)
    return d, d*d*d**(-a), mu_rest


def main():
    # All a values below are synthetic efficiency slopes, not SPEEDY calibration.
    beta = .0450
    rings = [36.5,46.5,85.,95.,133.5,143.5]
    checks = []
    def check(name, condition):
        checks.append({'name': name, 'passed': bool(condition)})
    p = .5  # shifted probability at one known physical t/tau=ln(2)
    rows=[]
    for angle in rings:
        mu=math.cos(math.radians(angle))
        d,c,mup=response(beta,mu,1.)
        observed=c*p/(c*p+1-p)
        recovered=observed/(c*(1-observed)+observed)
        tau_ratio=math.log1p(-p)/math.log1p(-observed)
        rows.append({'theta_lab_deg':angle,'D':d,'mu_rest':mup,
                     'J':d*d,'efficiency_ratio_assumed':1/d,'C':c,
                     'shifted_observed':observed,'shifted_recovered':recovered,
                     'naive_tau_over_true':tau_ratio})
        check(f'inverse response recovers p at {angle}',abs(recovered-p)<1e-14)
        # Numerical derivative of aberration is independent of D^2 evaluation.
        step=1e-5
        derivative=(response(beta,mu+step,0)[2]-response(beta,mu-step,0)[2])/(2*step)
        check(f'Jacobian finite difference at {angle}',abs(derivative-d*d)<1e-9)
    check('isotropic angular probability normalized in lab',abs(simpson(lambda m:response(beta,m,0)[1],-1,1)/2-1)<1e-12)
    check('zero beta gives unity response for all slopes',all(abs(response(0,m,a)[1]-1)<1e-15 for m in [-1,0,1] for a in [0,1,2]))
    check('a=2 cancels boost only in this isotropic power-law design',all(abs(response(beta,m,2)[1]-1)<1e-14 for m in [-1,0,1]))
    check('forward backward bias directions',rows[0]['naive_tau_over_true']<1<rows[-1]['naive_tau_over_true'])
    # A common C error leaves exact apparent data unchanged if p is reparameterized.
    c0=rows[0]['C']; observed=rows[0]['shifted_observed']; wrongc=c0*1.05
    alias_p=observed/(wrongc*(1-observed)+observed)
    replay=wrongc*alias_p/(wrongc*alias_p+1-alias_p)
    check('calibration probability alias reproduces same data',abs(replay-observed)<1e-14 and abs(alias_p-p)>.01)
    # No acceptance probability determines tau uniquely from a time-window label.
    acceptance={str(tau): -math.expm1(-100/tau) for tau in [10.,100.,1000.]}
    check('long lived parents can still produce prompt-window events',0<acceptance['1000.0']<acceptance['100.0']<acceptance['10.0'])
    # Nolan Table5, PDF79 / printed77. Adopted row is not a 12th measurement.
    t5=[
        [700,300,'NRF','Rasmussen1961'],[570,140,'Coulex','Andreev1961'],
        [370,150,'NRF','Booth1964'],[570,80,'DSAM','RobinsonBent1968'],
        [530,100,'DSAM','Haeusser1968'],[300,80,'DSAM','deKock1970'],
        [700,300,'RDM','McDonald1971'],[610,180,'DSAM','Durrell1972'],
        [710,70,'electron-scattering','Lees1973'],
        [726,31,'Coulex','Schwalm1977'],[695,50,'DSAM','Schwalm1977']]
    adopted={'tau_fs':480,'error_fs':50,'reference':'EndtVanderLeun1973','depends_on_first_eight_rows':True}
    check('Table5 contains eleven measured rows plus one adopted row',len(t5)==11 and sum(r[2]=='RDM' for r in t5)==1 and sum(r[2]=='DSAM' for r in t5)==5)
    check('adopted value is not Lees electron-scattering measurement',adopted['tau_fs']!=t5[8][0] and t5[8][2]=='electron-scattering')
    # Nolan Table7 uses RDM/DSAM, and two rows belong to 36Cl.
    t7=[['13C',3.85,12.4,12.1,1.02,.05],['16N',.40,6.5,5.07,1.28,.10],
        ['18O',1.98,2.99,2.82,1.06,.05],['20O',1.67,14.2,9.8,1.45,.11],
        ['36Cl',.79,23.,19.9,1.16,.13],['36Cl',1.16,10.4,9.2,1.13,.07]]
    check('Table7 printed ratio direction matches raw columns',all(abs(row[2]/row[3]-row[4])<.006 for row in t7))
    check('Table7 sixth isotope is another 36Cl state',sum(r[0]=='36Cl' for r in t7)==2 and not any(r[0]=='30P' for r in t7))
    # Exact gamma/p total-width partition, conditional on J=7/2, only these channels.
    hbar_meV_fs=658.2119569
    def strength(bp,tau):return (4/7)*hbar_meV_fs/tau*bp*(1-bp)
    strengths={label:strength(bp,tau) for label,bp,tau in [('old_control',.037,10),('new_only',.0068,11),('recommended',.0066,10.2)]}
    check('exact partition is below narrow-p approximation',strength(.0066,10.2)<(4/7)*hbar_meV_fs/10.2*.0066)
    # Use exact radiative triangle, allowing DeltaJ=0 for L=1.
    generic=[j for j in range(15) if abs(7-j)<=1<=7+j and abs(j-6)<=1<=j+6]
    old_h0h2=[j for j in range(15) if abs(7-j)<=1<=7+j and abs(j-6) in [0,2]]
    check('generic two L1 necessary set includes J7',generic==[6,7])
    check('restricted H0 H2 alternative admits J8',old_h0h2==[6,8])
    # Regis PDF44 Fit1 marginal errors do not supply its joint covariance.
    par=[-826391.,3316.85,-1.28444,14104.7]
    sig=[111713.,357.39,.00944,1194.7]
    ef,ed=1120.,609.
    def prd(q):
        a,b,c,d=q
        return a*(1/math.sqrt(b+ef)-1/math.sqrt(b+ed))+c*(ef-ed)
    a,b,c,d=par
    jac=[1/math.sqrt(b+ef)-1/math.sqrt(b+ed),
         -a/2*((b+ef)**-1.5-(b+ed)**-1.5),ef-ed,0.]
    numerical=[]
    for i,step in enumerate([1.,.001,1e-6,1.]):
        plus=par.copy();minus=par.copy();plus[i]+=step;minus[i]-=step
        numerical.append((prd(plus)-prd(minus))/(2*step))
    check('PRD analytic parameter Jacobian agrees with finite differences',all(abs(x-y)<1e-6 for x,y in zip(jac,numerical)))
    check('reference difference exactly cancels offset d',prd(par)==prd(par[:3]+[d+1e9]) and jac[3]==0.)
    terms=[j*s for j,s in zip(jac,sig)]
    diag_sigma=math.sqrt(sum(x*x for x in terms))
    # Each Sigma = v v^T is PSD, with exactly the reported marginal diagonal.
    rank1=[]
    for signs in [(1,1,1,1),(1,-1,1,1)]:
        v=[s*g for s,g in zip(sig,signs)]
        covariance=[[u*w for w in v] for u in v]
        variance=sum(jac[i]*covariance[i][j]*jac[j] for i in range(4) for j in range(4))
        sigma=abs(sum(x*y for x,y in zip(jac,v)))
        check(f'rank1 covariance preserves marginals for {signs}',all(covariance[i][i]==sig[i]**2 for i in range(4)))
        check(f'rank1 contraction agrees with quadratic form for {signs}',abs(variance-sigma*sigma)<1e-8)
        rank1.append({'signs':signs,'covariance':covariance,'conditional_sigma_ps':sigma})
    check('same marginals admit very different propagated PRD variance',rank1[0]['conditional_sigma_ps']>100*rank1[1]['conditional_sigma_ps'])
    prd_contract={'parameters':par,'marginal_sigmas':sig,'energy_pair_keV':[ef,ed],
                  'central_PRD_ps':prd(par),'jacobian':jac,
                  'independent_parameter_assumption_sigma_ps':diag_sigma,
                  'rank1_counterexamples':rank1,
                  'interpretation':'Synthetic admissible covariances, not the actual fit covariance or experimental PRD uncertainty.',
                  'source':'Regis PDF44 Eq4.13 Fit1 and PDF45 Fig4.16; stated 8ps residual and 4ps limitation only for 240<Egamma<1300keV in this experiment.'}
    source_paths=[
        'raw/papers/2012_Radeck et al_Simultaneous deorientation and lifetime measurement in 98 Ru using the recoil distance Doppler shift.pdf',
        'raw/theses/degree-dissertation/LaBr3时间.pdf',
        'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf']
    result={'observed_at_utc':datetime.now(timezone.utc).isoformat(),
      'session_id':'01a15dcc-49f9-7623-b0e9-75fd73c74a80',
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'literal source transcriptions and declared isotropic point-ring response design; no original data fit or CI',
      'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths},
      'response_contract':{'beta_source':beta,'beta_uncertainty_source':.0006,'a_synthetic':1.,'rings_deg':rings,'isotropic':True,'feeding':False,'P':p,'D':'sqrt(1-beta^2)/(1-beta*cos(theta_lab))','C':'D^(2-a)','deorientation_included':False,'finite_acceptance_included':False,'measured_efficiency_included':False},
      'rings':rows,'calibration_alias':{'wrong_C':wrongc,'alias_shifted_probability':alias_p,'same_observed_probability':replay},
      'prompt_window_acceptance_design':acceptance,'nolan_table5_measured_rows':t5,'nolan_table5_adopted_row':adopted,
      'nolan_table7_rows_RDM_DSA_ratio':t7,'conditional_strengths_meV':strengths,
      'generic_two_L1_spin_set':generic,'restricted_H0H2_set':old_h0h2,
      'modern_PRD_covariance_contract':prd_contract,
      'checks':checks,'all_checks_passed':all(c['passed'] for c in checks),
      'limitations':['No actual detector efficiency or full joint covariance.','No historical reference pooled as independent statistical truth.','Result checks are mathematical controls, not independent experimental validations.']}
    (RUN/'response-source-repair-result-088.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'all_checks_passed':result['all_checks_passed'],'checks':len(checks),'strengths':strengths,'first_last_tau_ratio':[rows[0]['naive_tau_over_true'],rows[-1]['naive_tau_over_true']]}))
    if not result['all_checks_passed']:raise SystemExit(1)


if __name__=='__main__':main()
