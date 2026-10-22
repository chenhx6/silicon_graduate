#!/usr/bin/env python3
"""Reproducible conditional checks; never an experimental lifetime refit.

CG algebra uses exact factorial sums and a separate closed rotor expression.
All calibration amplitudes, walk functions and covariances below are declared
controls. They are not recovered experiment inputs or confidence intervals.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def fact(x):
    x = F(x)
    if x.denominator != 1 or x < 0:
        raise ValueError(f"factorial domain: {x}")
    return math.factorial(int(x))


def cg_squared(j1, j2, j3, m1, m2, m3):
    """Racah factorial sum; return the exact squared CG coefficient."""
    j1, j2, j3, m1, m2, m3 = map(F, (j1, j2, j3, m1, m2, m3))
    if m1 + m2 != m3 or any(abs(m) > j for j, m in [(j1,m1),(j2,m2),(j3,m3)]):
        return F(0)
    if not abs(j1-j2) <= j3 <= j1+j2:
        return F(0)
    a, b, c = j1+j2-j3, j1-j2+j3, -j1+j2+j3
    prefactor = F(fact(a)*fact(b)*fact(c), fact(j1+j2+j3+1))
    for j, m in [(j1,m1),(j2,m2),(j3,m3)]:
        prefactor *= fact(j+m)*fact(j-m)
    total = F(0)
    for z in range(int(j1+j2+j3)+2):
        args = [z, a-z, j1-m1-z, j2+m2-z, j3-j2+m1+z, j3-j1-m2+z]
        if any(v < 0 for v in args):
            continue
        total += F((-1)**z, math.prod(fact(v) for v in args))
    return (2*j3+1)*prefactor*total**2


def rotor_cg_squared(I, K):
    I, K = F(I), F(K)
    if I < 2 or abs(K) > I-2:
        raise ValueError("I->I-2 fixed-K transition outside domain")
    return 3*(I+K-1)*(I+K)*(I-K-1)*(I-K)/(2*I*(I-1)*(2*I-1)*(2*I+1))


def signed_cg(j1,j2,j3,m1,m2,m3):
    # The sign is evaluated with a factorial sum independent of the square.
    j1,j2,j3,m1,m2,m3 = map(F,(j1,j2,j3,m1,m2,m3))
    sq = cg_squared(j1,j2,j3,m1,m2,m3)
    if not sq:
        return 0.0
    a=j1+j2-j3
    total=F(0)
    for z in range(int(j1+j2+j3)+2):
        args=[z,a-z,j1-m1-z,j2+m2-z,j3-j2+m1+z,j3-j1-m2+z]
        if any(x<0 for x in args):continue
        total+=F((-1)**z,math.prod(fact(x) for x in args))
    # CG phase cancels the Racah 3j prefactor for m3=m1+m2.
    return math.copysign(math.sqrt(float(sq)), float(total))


def weighted_fit(errors):
    xs=[7.5,13.5,15.5,17.5]; ys=[2.93,2.26,2.66,2.43]
    ws=[1/e**2 for e in errors]
    xb=sum(w*x for w,x in zip(ws,xs))/sum(ws)
    yb=sum(w*y for w,y in zip(ws,ys))/sum(ws)
    sxx=sum(w*(x-xb)**2 for w,x in zip(ws,xs))
    slope=sum(w*(x-xb)*(y-yb) for w,x,y in zip(ws,xs,ys))/sxx
    se=1/math.sqrt(sxx)
    return {"slope":slope,"standard_error":se,"z":slope/se,
            "assumptions":"fixed tabulated centers, independent Gaussian errors; no cross-point covariance or censored likelihood"}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    q=p.parse_args()
    checks=[]
    def check(name, condition):
        checks.append({"name":name,"passed":bool(condition)})
        if not condition:raise AssertionError(name)
    grid=[]
    for twiceI in range(4,61):
        I=F(twiceI,2)
        for twiceK in range(twiceI%2,twiceI-3,2):
            K=F(twiceK,2)
            exact=cg_squared(I,2,I-2,K,0,K)
            check(f'CG I={I} K={K}',exact==rotor_cg_squared(I,K))
            grid.append({"I":str(I),"K":str(K),"CG_squared":str(exact)})
    check('K0 2->0 = 1/5', rotor_cg_squared(2,0)==F(1,5))
    check('27/2 K11/2 = 76/325',rotor_cg_squared(F(27,2),F(11,2))==F(76,325))
    check('27/2 K1/2 = 26/75',rotor_cg_squared(F(27,2),F(1,2))==F(26,75))
    I,K=F(27,2),F(11,2)
    old2=3*(I-K)*(I-K-1)/(2*(2*I-1)*(2*I+1))
    check('old formula fails nonzero-K transition',old2!=rotor_cg_squared(I,K))
    def qt(B,I,K):return math.sqrt(16*math.pi*B/(5*float(rotor_cg_squared(I,K))))
    geometry=[]
    for I,B in [(F(23,2),.2416),(F(27,2),.1723)]:
        geometry.append({"I":str(I),"B_e2_b2":B,"hypothetical_fixed_K":[
            {"K":str(K),"Qt_eb":qt(B,I,K)} for K in [F(1,2),F(5,2),F(11,2)]]})
    # A negative Gaussian trend statistic does not establish a constant shape.
    regressions={
        'mean_asymmetric_errors':weighted_fit([.45,.30,.125,.21]),
        'all_lower_errors':weighted_fit([.30,.23,.12,.20]),
        'all_upper_errors':weighted_fit([.60,.37,.13,.22]),
    }
    # Sign of a lifetime bias at fixed E2 branch/geometry is unambiguous.
    tau_bias=2.0; qt_ratio=1/math.sqrt(tau_bias)
    check('overestimated tau lowers inferred Qt',qt_ratio<1)
    # Independent positive toy angular response: orientation sign reverses bias.
    def G(a,g,t):return a+(1-a)*math.exp(-g*t)
    def SH(a,g,tau,t):return a+(1-a)*(-math.expm1(-(g+1/tau)*t))/((1+g*tau)*(-math.expm1(-t/tau)))
    deorientation=[]
    tau=8.36;t=8.36;a=.18;g=.142
    for A in [-.35,0,.35]:
        us=G(a,g,t);sh=SH(a,g,tau,t)
        s=-math.expm1(-t/tau);u=math.exp(-t/tau)
        P=s*(1+A*sh)/(s*(1+A*sh)+u*(1+A*us))
        apparent=-t/math.log1p(-P)
        deorientation.append({"synthetic_A2":A,"physical_t_ps":t,"apparent_tau_ps":apparent,"relative_bias":apparent/tau-1})
    check('synthetic A2 changes bias sign',deorientation[0]['relative_bias']>0>deorientation[2]['relative_bias'])
    check('zero A2 no bias',abs(deorientation[1]['relative_bias'])<1e-14)
    # Fixed detector channels, exchanged ENERGY gates (MSCD): unequal stable
    # detector walk functions cancel at equal energies. A single centroid does
    # not have that property; a drift between gate datasets also survives.
    E=600; tau_timing=15;wA=1200/math.sqrt(E);wB=900/math.sqrt(E)
    residual=wB-wA
    delayed=tau_timing+residual
    antidelayed=-tau_timing+residual
    ms_tau=(delayed-antidelayed)/2
    reverse_drift=8.0
    drifted_tau=(delayed-(antidelayed+reverse_drift))/2
    check('single-centroid walk bias survives at equal E',abs(residual)>1)
    check('equal E MSCD cancels unequal stable walks',math.isclose(ms_tau,tau_timing))
    check('reversal-dataset drift survives MSCD',math.isclose(drifted_tau-tau_timing,-4))
    # The earlier Qspec formula already fails the axial limit, by factor three.
    check('old DF formula fails axial limit',not math.isclose(-2/7/3,-2/7))
    # An axial I=3,K=2 rotor has zero diagonal moment and a nonzero E2 link.
    qspec32=F(3*2**2-3*(3+1),(3+1)*(2*3+3))
    check('axial Qspec zero counterexample',qspec32==0 and cg_squared(3,2,2,2,0,2)>0)
    check('signed CG reproduces axial Qspec 2+',math.isclose(
        signed_cg(2,2,2,2,0,2)*signed_cg(2,2,2,0,0,0),-2/7))
    result={
      'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'scope':'conditional algebra and bias controls, no experimental re-fit or CI',
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'checks':checks,'check_count':len(checks),'cg_grid':grid,
      'geometry_sensitivity_not_author_K_identification':geometry,
      'printed_ratios':{'Li_27overSingh_reuse':2.72/2.28,'candidate_K11overKhalf':math.sqrt(F(169,114))},
      'singh_conditional_regression':regressions,
      'feeding_sign_control':{'tau_multiplier':tau_bias,'Qt_multiplier':qt_ratio},
      'synthetic_deorientation_bias':deorientation,
      'equal_energy_control':{'energy_keV':E,'walkA_ps':wA,'walkB_ps':wB,
          'single_centroid_without_prompt_ps':delayed,'fixed_channel_energy_swapped_MSCD_tau_ps':ms_tau,
          'reverse_dataset_drift_ps':reverse_drift,'MSCD_tau_with_dataset_drift_ps':drifted_tau},
      'withdrawn':'old truncated CG, fixed K=5/2 attribution, universal -4.6% bias, perfect equal-energy walk cancellation, exact DF normalization, full experimental reconciliation',
    }
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['check_count','geometry_sensitivity_not_author_K_identification','printed_ratios','singh_conditional_regression','synthetic_deorientation_bias']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
