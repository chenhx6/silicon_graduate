#!/usr/bin/env python3
"""Declared slowing and DDCM error-propagation counterexamples, no source fit.

Both numerical sections are synthetic. Rate parameters, intensities, reference
counts and calibration errors are assumptions, never original experiment data.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01'


def simpson(f, lo, hi, n=6000):
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))


def trajectory(t, a, b):
    # du/dt = -a*u - b*sqrt(u), u(0)=1, u >= 0.
    w=(1+b/a)*math.exp(-a*t/2)-b/a
    return max(w,0.)**2


def attenuation(tau, a, b):
    end=2/a*math.log1p(a/b)
    c,d=1+b/a,b/a
    z=1/tau
    f=lambda r:-math.expm1(-r*end)/(tau*r)
    return c*c*f(a+z)-2*c*d*f(a/2+z)+d*d*f(z)


def fit_tau(target, a, b):
    lo,hi=1e-5,100.
    for _ in range(90):
        mid=(lo+hi)/2
        if attenuation(mid,a,b)>target:lo=mid
        else:hi=mid
    return (lo+hi)/2


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def tr(a):return [list(x) for x in zip(*a)]


def inverse(a):
    n=len(a);b=[row.copy()+[float(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        pivot=max(range(i,n),key=lambda j:abs(b[j][i]))
        b[i],b[pivot]=b[pivot],b[i]
        scale=b[i][i]
        if abs(scale)<1e-18:raise ValueError('singular matrix')
        b[i]=[x/scale for x in b[i]]
        for j in range(n):
            if j!=i:
                scale=b[j][i];b[j]=[x-scale*y for x,y in zip(b[j],b[i])]
    return [row[n:] for row in b]


def quad(v,a):return sum(v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))


def main():
    checks=[]
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    a,b=.6,.4
    taus=[.1,.3,1.,3.]
    rows=[]
    for tau in taus:
        target=attenuation(tau,a,b)
        end=2/a*math.log1p(a/b)
        independent=simpson(lambda t:trajectory(t,a,b)*math.exp(-t/tau)/tau,0,end)
        check(f'closed attenuation agrees with time quadrature tau={tau}',abs(target-independent)<1e-8)
        uniform=[];component=[]
        for k in [.8,1.,1.3]:
            uf=fit_tau(target,k*a,k*b)
            ef=fit_tau(target,k*a,b)
            check(f'uniform total trajectory scaling tau={tau} k={k}',abs(uf*k/tau-1)<1e-11)
            check(f'component fit reproduces target tau={tau} k={k}',abs(attenuation(ef,k*a,b)-target)<1e-12)
            uniform.append({'k_total':k,'fitted_tau_ps':uf})
            component.append({'k_e_only':k,'fitted_tau_ps':ef,'tau_ratio_to_baseline':ef/tau,
                              'B_factor_with_fixed_branch':tau/ef,'Q_factor_with_fixed_geometry':math.sqrt(tau/ef)})
        h=.0001
        lder=math.log(fit_tau(target,a*(1+h),b)/fit_tau(target,a*(1-h),b))/math.log((1+h)/(1-h))
        check(f'electronic-only local sensitivity between minus one and zero tau={tau}',-1<lder<0)
        rows.append({'tau_baseline_ps':tau,'F_target':target,'uniform_total_scale':uniform,
                     'electronic_only_scale':component,'dlog_tau_dlog_ke_local':lder})
    qf=[x['electronic_only_scale'][-1]['Q_factor_with_fixed_geometry'] for x in rows]
    ratio_change=qf[0]/qf[-1]
    double_change=(qf[0]**2/qf[1]**2)/(qf[2]**2/qf[3]**2)
    check('electronic-only response is state dependent',abs(rows[0]['dlog_tau_dlog_ke_local']-rows[-1]['dlog_tau_dlog_ke_local'])>.05)
    check('electronic-only Q ratio need not be invariant',abs(ratio_change-1)>.005)
    check('electronic-only double ratio need not be invariant',abs(double_change-1)>1e-4)
    # Synthetic pointwise normalized intensities from Poisson-thinned S/U and
    # an independent Poisson reference R, common to S and U at that distance.
    n=7;h=.5;ta=2.;exposure=1e6;ref_factor=4.;rmean=ref_factor*exposure
    times=[.5+i*h for i in range(n)]
    fs=[-math.expm1(-t/ta) for t in times];us=[math.exp(-t/ta) for t in times]
    values=fs+us
    cov=[[0.]*(2*n) for _ in range(2*n)]
    for i,(s,u) in enumerate(zip(fs,us)):
        cov[i][i]=s/exposure+s*s/rmean
        cov[i+n][i+n]=u/exposure+u*u/rmean
        cov[i][i+n]=cov[i+n][i]=s*u/rmean
    check('shared reference induces positive S U covariance',all(cov[i][i+n]>0 for i in range(n)))
    centers=list(range(1,n-1))
    def estimates(x):return [x[i+n]/((x[i+1]-x[i-1])/(2*h)) for i in centers]
    tau_app=estimates(values)
    jac=[]
    for i in centers:
        d=(fs[i+1]-fs[i-1])/(2*h);row=[0.]*(2*n)
        row[i+n]=1/d
        row[i+1]=-us[i]/(2*h*d*d);row[i-1]=us[i]/(2*h*d*d)
        jac.append(row)
    for j in range(2*n):
        step=1e-7;up=values.copy();dn=values.copy();up[j]+=step;dn[j]-=step
        numerical=[(x-y)/(2*step) for x,y in zip(estimates(up),estimates(dn))]
        check(f'lifetime estimator Jacobian at input{j}',all(abs(x-row[j])<1e-7 for x,row in zip(numerical,jac)))
    cov_stat=mm(mm(jac,cov),tr(jac))
    zero_offdiag=[[cov[i][i] if i==j else 0 for j in range(2*n)] for i in range(2*n)]
    no_ref_cross=mm(mm(jac,zero_offdiag),tr(jac))
    check('discarding same-distance reference covariance changes output offdiagonal',max(abs(cov_stat[i][j]-no_ref_cross[i][j]) for i in range(5) for j in range(5))>1e-8)
    check('shared endpoints induce negative separated-point covariance',cov_stat[0][2]<0)
    exact_discrete=ta*(h/ta)/math.sinh(h/ta)
    check('finite difference has known small bias in this prompt design',all(abs(t-exact_discrete)<1e-12 for t in tau_app) and exact_discrete<ta)
    # A common fractional velocity/distance-scale uncertainty is not five
    # independent nuisance parameters. Treating its diagonal alone shrinks it.
    calibration_sigma=math.hypot(.03,.02)
    common=[[calibration_sigma**2*x*y for y in tau_app] for x in tau_app]
    total=[[cov_stat[i][j]+common[i][j] for j in range(5)] for i in range(5)]
    diagonal_weights=[1/total[i][i] for i in range(5)]
    diagonal_weights=[w/sum(diagonal_weights) for w in diagonal_weights]
    independent_claim=math.sqrt(1/sum(1/total[i][i] for i in range(5)))
    actual_same_weights=math.sqrt(quad(diagonal_weights,total))
    inv_stat=inverse(cov_stat);row_sums=[sum(row) for row in inv_stat]
    gls_weights=[x/sum(row_sums) for x in row_sums]
    stat_gls_var=quad(gls_weights,cov_stat)
    total_gls_var=quad(gls_weights,total)
    floor=calibration_sigma*exact_discrete
    check('normalized GLS weights sum to one',abs(sum(gls_weights)-1)<1e-12)
    check('common calibration adds variance independently of normalized weights',abs(total_gls_var-stat_gls_var-floor**2)<1e-14)
    check('diagonal approximation understates shared-calibration mean uncertainty',actual_same_weights>independent_claim*1.5)
    check('GLS does not beat common calibration floor',math.sqrt(total_gls_var)>=floor)
    # Matrix inversion consistency independent of the variance-floor identity.
    ident=mm(inv_stat,cov_stat)
    check('propagated statistical covariance has invertible finite design',max(abs(ident[i][j]-float(i==j)) for i in range(5) for j in range(5))<1e-12)
    src=ROOT/'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf'
    out={'created_at_utc':datetime.now(timezone.utc).isoformat(),
         'session_id':'01a15dcc-49f9-7623-b0e9-75fd73c74a80',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
         'scope':'Declared mathematical response/covariance controls; no actual counts, original fit, experimental CI or structure decision.',
         'slowing_design':{'du_dt':'-ke*a*u-kn*b*sqrt(u)','a_ps_inverse':a,'b_ps_inverse':b,
              'u_initial':1.,'source_parameterization_role':'Nolan Eq2.16 motivates distinct e/n nuisance roles; this positive law is not its quantitative stopping model.',
              'feeding':False,'scattering':False,'infinite_homogeneous_medium':True,
              'rows':rows,'relative_Q_ratio_change_for_ke1p3':ratio_change,
              'relative_B_double_ratio_change_for_ke1p3':double_change},
         'derivative_covariance_design':{'tau_ps':ta,'times_ps':times,'time_halfspacing_ps':h,
              'synthetic_exposure_per_distance':exposure,'synthetic_reference_count_mean':rmean,
              'statistical_model':'Poisson-thinned S/U and independent Poisson R per distance; first-order error propagation only',
              'normalized_intensity_covariance':cov,'estimator_Jacobian':jac,
              'tau_app_ps':tau_app,'statistical_covariance_ps2':cov_stat,
              'common_calibration_covariance_ps2':common,'total_covariance_ps2':total,
              'common_fractional_velocity_sigma':.03,'common_fractional_distance_gain_sigma':.02,
              'independent_sigma_claim_ps':independent_claim,
              'actual_sigma_same_weights_ps':actual_same_weights,
              'GLS_weights':gls_weights,'GLS_stat_sigma_ps':math.sqrt(stat_gls_var),
              'GLS_total_sigma_ps':math.sqrt(total_gls_var),'common_calibration_floor_ps':floor},
         'checks':checks,'check_count':len(checks),'all_checks_passed':all(c['passed'] for c in checks),
         'boundaries':['Whole-trajectory time rescaling is sufficient for inverse tau scaling; electronic-only changes need not do so.',
                       'Real branching, finite foils, recoil distributions, feeding, scattering, normalizers and covariance remain to be supplied.',
                       'Correlations and errors here are not actual experimental uncertainty estimates.']}
    (RUN/'stopping-covariance-response-result-090.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'all_passed':out['all_checks_passed'],
        'e_only_sensitivities':[r['dlog_tau_dlog_ke_local'] for r in rows],
        'relative_Q_ratio_change':ratio_change,'relative_double_ratio_change':double_change,
        'independent_sigma_claim_ps':independent_claim,'actual_sigma_same_weights_ps':actual_same_weights,
        'GLS_total_sigma_ps':math.sqrt(total_gls_var),'common_floor_ps':floor},indent=2))


if __name__=='__main__':main()
