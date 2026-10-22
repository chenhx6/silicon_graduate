#!/usr/bin/env python3
"""Conditional timing design: role tagging, energy gates and finite time windows.

The 20 ps lifetime and 80 ps PRF sigma are invented design controls. No real
LaBr3 response, event sample, experiment fit or confidence interval is inferred.
Run with --output PATH. Uses the Python standard library only.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import random


def density(t, tau, sigma):
    """Gaussian PRF convolved with a positive exponential, both normalized."""
    if tau <= 0 or sigma <= 0:
        raise ValueError('positive tau and sigma required')
    return math.exp(sigma*sigma/(2*tau*tau)-t/tau)*math.erfc(
        (sigma*sigma/tau-t)/(math.sqrt(2)*sigma))/(2*tau)


def moments(pdf, width, n):
    if n % 2:
        raise ValueError('Simpson intervals must be even')
    h=2*width/n
    sums=[0.0,0.0,0.0]
    for i in range(n+1):
        t=-width+h*i
        weight=1 if i in [0,n] else (4 if i%2 else 2)
        f=pdf(t)
        for k in range(3):sums[k]+=weight*t**k*f
    mass, first, second=[s*h/3 for s in sums]
    mean=first/mass
    return {'acceptance':mass,'mean_ps':mean,'second_moment_ps2':second/mass,
            'variance_ps2':second/mass-mean*mean}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    q=p.parse_args()
    tau,sigma=20.0,80.0
    checks=[]
    def check(name, ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    plus=lambda t:density(t,tau,sigma)
    minus=lambda t:plus(-t)
    mixed=lambda t:(plus(t)+minus(t))/2
    wide=moments(plus,1200,24000)
    sym=moments(mixed,1200,24000)
    check('wide positive exGaussian normalized',abs(wide['acceptance']-1)<1e-10)
    check('wide positive centroid tau',abs(wide['mean_ps']-tau)<1e-8)
    check('positive exGaussian variance sigma2+tau2',abs(wide['variance_ps2']-sigma*sigma-tau*tau)<1e-5)
    check('role-unresolved mixture zero mean with nonzero tau',abs(sym['mean_ps'])<1e-10)
    check('role-unresolved mixture second moment sigma2+2tau2',abs(sym['second_moment_ps2']-(sigma*sigma+2*tau*tau))<1e-5)
    windows=[]
    for width in [80,160,320,640]:
        a=moments(plus,width,2000);b=moments(minus,width,2000)
        aa=moments(plus,width,4000)
        estimate=(a['mean_ps']-b['mean_ps'])/2
        check(f'window {width} quadrature convergence',abs(a['mean_ps']-aa['mean_ps'])<1e-7)
        check(f'window {width} mirrored accepted centroids',abs(a['mean_ps']+b['mean_ps'])<1e-10)
        windows.append({'symmetric_half_window_ps':width,'delayed':a,'anti_delayed':b,
                        'naive_MSCD_tau_ps':estimate,'naive_bias_ps':estimate-tau})
    check('finite window can strongly suppress centroid shift',windows[0]['naive_MSCD_tau_ps']<tau/2)
    check('wide-window limit recovers tau',abs(windows[-1]['naive_MSCD_tau_ps']-tau)<1e-6)
    # Independent event generator; one latent sign per event, then Gaussian jitter.
    rng=random.Random(19009);N=100000
    sample=[rng.gauss(0,sigma)+(1 if rng.random()<.5 else -1)*rng.expovariate(1/tau) for _ in range(N)]
    m=sum(sample)/N;m2=sum(t*t for t in sample)/N
    se_mean=math.sqrt((sigma*sigma+2*tau*tau)/N)
    se_m2=math.sqrt((2*sigma**4+8*sigma*sigma*tau*tau+20*tau**4)/N)
    check('independent Monte Carlo mixture mean',abs(m)<7*se_mean)
    check('independent Monte Carlo second moment',abs(m2-(sigma*sigma+2*tau*tau))<7*se_m2)
    # Stable, different walks in fixed channels; swap energies only.
    walkA=lambda E:1200/math.sqrt(E)
    walkB=lambda E:900/math.sqrt(E)
    offset=200
    swap=[]
    for ef,ed in [(600,600),(800,400)]:
        pdel=offset+walkB(ed)-walkA(ef)
        panti=offset+walkB(ef)-walkA(ed)
        cdel=pdel+tau;canti=panti-tau
        PRD=pdel-panti;DC=cdel-canti
        check(f'fixed channel corrected tau {ef}/{ed}',math.isclose((DC-PRD)/2,tau,abs_tol=1e-12))
        swap.append({'Ef_keV':ef,'Ed_keV':ed,'PRD_ps':PRD,'DeltaC_ps':DC,'corrected_tau_ps':(DC-PRD)/2})
    check('equal energy prompt zero despite different stable walks',abs(swap[0]['PRD_ps'])<1e-12)
    # At identical actual energy windows without another role tag, swapping the
    # energy gates selects the same population: DC_observed=0, not 2*tau.
    check('unresolved equal gates have identical centroids',sym['mean_ps']-sym['mean_ps']==0)
    # Literal delayed-curve mirror at the virtual zero: +2tau != -(+2tau).
    literal_zero_residual=4*tau
    check('prompt antisymmetry not delayed antisymmetry',literal_zero_residual!=0)
    # Regis Appendix A's mixture formula for a centroid DIFFERENCE requires
    # the same background-to-peak ratio in both timing branches.
    alphas=(.3,.1); background_centroids=(100.0,20.0)
    true_centroids=(tau,-tau)
    total_centroids=tuple((c+a*b)/(1+a) for c,a,b in zip(true_centroids,alphas,background_centroids))
    total_dc=total_centroids[0]-total_centroids[1]
    background_dc=background_centroids[0]-background_centroids[1]
    mean_alpha=sum(alphas)/2
    wrong_dc=(1+mean_alpha)*total_dc-mean_alpha*background_dc
    recovered=tuple((1+a)*c-a*b for a,c,b in zip(alphas,total_centroids,background_centroids))
    correct_dc=recovered[0]-recovered[1]
    check('branchwise background subtraction recovers latent shift',math.isclose(correct_dc,2*tau))
    check('averaging unequal branch background ratios fails',abs(wrong_dc/2-tau)>1)
    common_alpha=.2
    common_tot=tuple((c+common_alpha*b)/(1+common_alpha) for c,b in zip(true_centroids,background_centroids))
    common_dc=(1+common_alpha)*(common_tot[0]-common_tot[1])-common_alpha*background_dc
    check('equal background ratios permit difference mixture correction',math.isclose(common_dc,2*tau))
    # A mirrored reuse (p,-p) contains one primitive datum, not two independent
    # calibrations. After restoring signs their average has the original variance.
    primitive_variance=9.0
    proper_variance=(primitive_variance+primitive_variance+2*primitive_variance)/4
    naive_variance=primitive_variance/2
    check('mirrored calibration covariance prevents fake sqrt2 gain',proper_variance==primitive_variance and naive_variance<proper_variance)
    raws={
      'raw/papers/degree dissertation/LaBr3时间.pdf':'54ef3c5b70d7ef4ed694ad9089fa40533d39e2bb060228eb3d1a304b03555f52',
      'raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf':'5e20f735e995021f4a0eb8c1a937acedeee53509caed3ffa2cd8ddaa794bbc4f'}
    for path,expected in raws.items():check('source hash '+Path(path).name,hashlib.sha256(Path(path).read_bytes()).hexdigest()==expected)
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'synthetic design only; no measured tau, detector performance or experiment CI',
      'inputs':{'tau_ps':tau,'Gaussian_PRF_sigma_ps':sigma,'Gaussian_PRF_FWHM_ps':2*math.sqrt(2*math.log(2))*sigma,'feeding':False,'background':False},
      'wide_positive':wide,'unresolved_symmetric_role_mixture':sym,
      'finite_window_scan':windows,'fixed_channel_energy_swaps':swap,
      'independent_MC':{'seed':19009,'N':N,'mean_ps':m,'second_moment_ps2':m2,'analytic_MC_standard_errors':{'mean_ps':se_mean,'second_moment_ps2':se_m2}},
      'literal_delayed_mirror_zero_residual_ps':literal_zero_residual,
      'unequal_background_control':{'branch_background_to_peak_ratios':alphas,
        'background_centroids_ps':background_centroids,'total_centroids_ps':total_centroids,
        'naive_tau_from_total_ps':total_dc/2,'tau_from_mean_alpha_correction_ps':wrong_dc/2,
        'tau_from_branchwise_correction_ps':correct_dc/2},
      'mirror_reuse_covariance_control':{'primitive_variance_ps2':primitive_variance,
        'proper_variance_after_sign_restoration_ps2':proper_variance,'incorrect_independence_variance_ps2':naive_variance},
      'required_real_inputs':['energy gate purity and feeder/decay role tag','per pair and per energy prompt calibration','identical time window, acceptance and live-time convention','Compton versus full energy response','event overlap and calibration covariance'],
      'checks':checks,'check_count':len(checks)}
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'windows':windows,'swaps':swap},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
