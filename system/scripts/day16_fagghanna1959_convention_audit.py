#!/usr/bin/env python3
"""FH59 original formula/table audit, without event reconstruction or new delta fit."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    cfg=json.loads(args.contract.read_text())
    assert cfg['identity']=='FH59-ORIGINAL-RATIO-POLYNOMIAL-01'
    root=Path(__file__).resolve().parents[2]
    raw=root/'raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf'
    assert sha(raw)==cfg['raw_sha256']
    p,R=sp.symbols('p R',positive=True)
    r=(p+R)/(p*R+1)
    P=(p-1)/(p+1)
    Q=(R-1)/(R+1)
    A=sp.factor((1-r)/(1+r))
    assert sp.simplify(A-P*Q)==0
    assert sp.simplify(r.subs(p,1)-1)==0
    assert sp.simplify(r.subs(R,1)-1)==0
    assert sp.simplify(sp.limit(r,p,sp.oo)-1/R)==0
    assert sp.simplify(sp.limit(r,R,sp.oo)-1/p)==0
    # Counter direction exchange inverts r, flips A; it does not invert a
    # photon amplitude mixing ratio.
    assert sp.simplify((1-1/r)/(1+1/r)+A)==0
    kappa=[]
    for L,Lp,nu,expected in cfg['kappa_TableIIb_entries']:
        assert nu>=2 and abs(L-Lp)<=nu<=L+Lp
        cm=clebsch_gordan(L,Lp,nu,1,-1,0)
        cp=clebsch_gordan(L,Lp,nu,1,1,2)
        assert cm!=0
        value=sp.simplify(-sp.sqrt(sp.factorial(nu-2)/sp.factorial(nu+2))*cp/cm)
        assert sp.simplify(value-sp.Rational(expected))==0,(L,Lp,nu,value,expected)
        kappa.append({'L':L,'Lprime':Lp,'rank':nu,'kappa':str(value),'printed':expected})
    # Printed I-15/I-17: one overall sign still follows the source's EM axes.
    t=sp.symbols('t',real=True)
    W=sum(sp.Integer(a)*t**i for i,a in enumerate(cfg['source_equations']['W_E3_coeff_t']))
    G=sum(sp.Integer(a)*t**i for i,a in enumerate(cfg['source_equations']['G_E3_coeff_t']))
    j0=sp.factor((W+G)/2);j90=sp.factor((W-G)/2)
    assert sp.simplify(j0-t*(11-15*t)**2)==0
    assert sp.simplify(j90-(1-5*t)**2)==0
    # Both intensities are nonnegative on the physical domain and never
    # vanish at the same t, hence |G/W|<=1 without clipping.
    assert sp.gcd(j0,j90)==1
    exact=[]
    for value in [sp.Rational(0),sp.Rational(1,5),sp.Rational(11,15)]:
        assert W.subs(t,value)>0
        g=sp.simplify(G.subs(t,value)/W.subs(t,value))
        assert abs(g)==1
        angle=math.degrees(math.acos(math.sqrt(float(value))))
        exact.append({'cos2theta':str(value),'G_over_W':str(g),
            'theta_deg':[angle] if value==0 else [angle,180-angle]})
    # A field-radiation-vector check uses the electric L3 M=+/-1 harmonic:
    # Y31 proportional to sin(theta)*(5 cos(theta)^2-1).
    theta=sp.symbols('theta',real=True)
    y=sp.sin(theta)*(5*sp.cos(theta)**2-1)
    e_theta=sp.diff(y,theta)
    e_phi=y/sp.sin(theta)
    local0=sp.trigsimp(e_theta**2)
    local90=sp.trigsimp(e_phi**2)
    assert sp.trigsimp(sp.expand_trig(local0-sp.cos(theta)**2*(11-15*sp.cos(theta)**2)**2))==0
    assert sp.trigsimp(local90-(1-5*sp.cos(theta)**2)**2)==0
    samples=[]
    for a in [0,30,60,62,90,118,150,180]:
        z=math.cos(math.radians(a))**2
        w=float(W.subs(t,z));g=float(G.subs(t,z))
        assert w>0 and abs(g)<=w+1e-10
        samples.append({'theta_deg':a,'W_printed_unscaled':w,
            'G_over_W_in_declared_plus_convention':g/w})
    grid=np.linspace(0,1,10001)
    wg=sp.lambdify(t,W,'numpy')(grid);gg=sp.lambdify(t,G,'numpy')(grid)
    assert np.all(wg>0) and np.max(abs(gg/wg))<=1+1e-12
    # Source4-2-0 example: 1/8+1/24=1/6, hence ratio 7/5 if E2,E2.
    pco=sp.Rational(1,8)+sp.Rational(1,24)
    assert pco==sp.Rational(1,6)
    rco=sp.factor((1+pco)/(1-pco));assert rco==sp.Rational(7,5)
    yobs,sigma=cfg['source_equations']['French_Newton_quoted']
    pred=cfg['source_equations']['French_Newton_predictions_M3_E3']
    residuals=[(yobs-v)/sigma for v in pred]
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),
        'source_sha256':sha(raw),
        'linear_ratio_map':{'N0_N90':str(r),'P_plane':str(P),'Q_response':str(Q),
            'A_N90minusN0':str(A),'A_equals_PQ':True,
            'counter_swap_flips_A':True,'p1_or_R1_nulls_passed':True,
            'pure_parallel_limit_N0_N90':str(sp.limit(r,p,sp.oo))},
        'kappa_TableIIb_exact_replay':kappa,
        'printed_E3':{'W':str(W),'G':str(G),
            'J0_declared_plus':str(j0),'J90_declared_plus':str(j90),
            'intensities_have_no_common_zero':True,'exact_complete_polarization':exact,
            'electric_vector_spherical_harmonic_control':True,
            'physicality_grid_points':len(grid),'samples':samples,
            'source_approx_angles_not_replaced':cfg['source_equations']['source_approx_complete_angles_deg']},
        'source_4_2_0':{'Pplane90_pureE2':str(pco),'p_FH_pureE2':str(rco),
            'new_experimental_Co60_calibration':False},
        'review_FrenchNewton_E3_comparison':{'observed_named_ratio':yobs,'sigma':sigma,
            'printed_M3_E3_predictions':pred,'standardized_residual_M3_E3_if_predictions_fixed':residuals,
            'original_FrenchNewton_count_roles_or_fit_replayed':False,
            'sign_not_transferred_without_primary_angle_count_contract':True},
        'circular_R_boundary':{'source_definition':'2*(Nplus-Nminus)/(Nplus+Nminus)',
            'not_linear_response_R':True,'factor2_not_deleted':True},
        'readiness':{'historical_delta_to_KS_RB_bridge_established':False,
            'new_experiment_fit_or_events_generated':False,
            'whole_Ferentz_tables_or_primary_historical_experiments_replayed':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'18_kappa_exact':len(kappa),'A_equals_PQ':True,
        'WplusG_over2':str(j0),'WminusG_over2':str(j90),
        'complete_angles':exact,'E3_samples':samples},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
