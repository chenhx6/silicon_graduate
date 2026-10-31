#!/usr/bin/env python3
"""Replay SU59 printed inputs and distinguish its normal-axis P from B15's words.

All count-cancellation and covariance calculations are conditional derivations.
No original event counts or undocumented corrections are generated.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import sympy as sp


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    root = Path(__file__).resolve().parents[2]
    raw = root / 'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1959_Suffert et al_Polarization measurements of proton capture gamma rays.pdf'
    assert sha(raw) == cfg['raw_sha256']

    # Fig.3: in position1 B is along beam, A is normal to beam in the
    # transverse projection; position2 exchanges the two angular classes.
    L1, L2, eA, eB, nparallel, nnormal = sp.symbols(
        'L1 L2 eA eB nparallel nnormal', positive=True)
    counts = {'A1': L1*eA*nnormal, 'B1': L1*eB*nparallel,
              'A2': L2*eA*nparallel, 'B2': L2*eB*nnormal}
    cross2 = sp.factor((counts['B1']/counts['A1']) /
                       (counts['B2']/counts['A2']))
    assert sp.simplify(cross2 - (nparallel/nnormal)**2) == 0
    Rcounter = sp.sqrt(cross2)
    assert sp.simplify(Rcounter - nparallel/nnormal) == 0
    # A time-dependent relative efficiency is not removed by position exchange.
    eA1,eB1,eA2,eB2 = sp.symbols('eA1 eB1 eA2 eB2', positive=True)
    drift = sp.sqrt((eB1/eA1)/(eB2/eA2))

    Pnormal, Pmeridional, p, phi = sp.symbols(
        'Pnormal Pmeridional p phi', real=True)
    # The physical scatter-plane angle phi is measured from beam-gamma plane.
    n_su = 1+p*Pnormal*sp.cos(2*phi)
    n_meridional = 1-p*Pmeridional*sp.cos(2*phi)
    assert sp.simplify(n_su.subs(Pnormal,-Pmeridional)-n_meridional) == 0
    # Stokes angle also changes: electric angle eta_normal=eta_plane-pi/2.
    eta=sp.symbols('eta',real=True)
    assert sp.trigsimp(sp.cos(2*(eta-sp.pi/2))+sp.cos(2*eta)) == 0
    # Same raw Fig.3 ratio, not the inverse, follows from the two conventions.
    r_su = (1+p*Pnormal)/(1-p*Pnormal)
    r_meridional = (1-p*Pmeridional)/(1+p*Pmeridional)
    assert sp.simplify(r_su.subs(Pnormal,-Pmeridional)-r_meridional) == 0
    R=sp.symbols('R',positive=True)
    estimate=(R-1)/(p*(R+1))
    gradR=sp.simplify(sp.diff(estimate,R))
    assert sp.simplify(gradR-2/(p*(R+1)**2)) == 0

    table=[]
    for x in cfg['rows']:
        assert x['R_corrected']>0 and 0<x['p']<=1 and x['dR']>0
        rc=x['R_corrected']; eff=x['p']
        value=(rc-1)/(eff*(rc+1))
        sigma=2*x['dR']/(eff*(rc+1)**2)
        table.append(dict(x,P_before_unknown_final_theta_correction=value,
            sigma_from_quoted_correctedR_only=sigma,
            reported_minus_replayed_P=x['P_reported']-value,
            reported_minus_replayed_sigma=x['dP_reported']-sigma,
            unknown_theta_scale=(x['P_reported']/value if value else None)))
    assert max(abs(x['reported_minus_replayed_P']) for x in table)<.02
    assert max(abs(x['reported_minus_replayed_sigma']) for x in table)<.02
    # No fitted correction is applied; these are residual diagnostics.
    w=[1/x['sigma']**2 for x in cfg['null_control_R']]
    re=sum(v*x['value'] for v,x in zip(w,cfg['null_control_R']))/sum(w)
    dre=1/math.sqrt(sum(w))
    # If all corrected ratios use Rnet/Re, this nuisance contributes a shared
    # rank-one covariance. Quoted Table I errors may already contain it.
    reported_re=cfg['reported_eccentricity_R']
    reported_dre=cfg['reported_eccentricity_sigma']
    derivatives=[-2*x['R_corrected']/(x['p']*reported_re*(1+x['R_corrected'])**2)
                 for x in cfg['rows']]
    component=[[a*b*reported_dre**2 for b in derivatives] for a in derivatives]
    assert all(math.isfinite(x) for row in component for x in row)

    likelihood=[]
    Pobs=cfg['rows'][0]['P_reported'];sigmaobs=cfg['rows'][0]['dP_reported']
    for name in ['row1_original_AD_candidates','row1_alternative_AD_candidates']:
        ds=cfg[name]
        chi=[(Pobs-x['P'])**2/sigmaobs**2 for x in ds]
        likelihood.append({'dataset':name,'candidates':ds,
            'chi2_if_P_candidates_fixed_and_observed_sigma_gaussian':chi,
            'L_candidate1_over_candidate2':math.exp(-.5*(chi[0]-chi[1])),
            'predictive_sigma_or_AD_cov_omitted':True,
            'not_posterior_exclusion_or_new_delta_fit':True})
    # Differing angular datasets change the candidate model; never pool them.
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),
        'source_sha256':sha(raw),'contract_sha256':sha(args.contract),
        'four_count_crossratio':{'R_squared':str(cross2),'R':str(Rcounter),
            'efficiency_drift_multiplier':str(drift),
            'angle_class_ratio':'beam-plane scatter / normal-plane scatter',
            'assumptions':'fixed detector efficiencies, equal response angular classes, multiplicative per-position exposure; eccentricity/background separately corrected'},
        'normal_meridional_crosswalk':{'P_SU': '-P_meridional',
            'normal_axis_count_kernel':str(n_su),
            'meridional_axis_count_kernel':str(n_meridional),
            'same_observable_verified':True,
            'B15_operational_As_fit':'p*P_SU if same scatter-plane zero',
            'B15_endpoint_As_N90_minus_N0':'-p*P_SU if same beam-plane zero',
            'B15_actual_producer_verified':False},
        'P_formula':str(estimate),'dP_dR':str(gradR),'table_replay':table,
        'unpolarized_control_weighting_if_independent':{
            'weighted_R':re,'sigma':dre,'source_R':reported_re,
            'source_sigma':reported_dre,'same_experiment_null_controls_not_B15_replication':True},
        'conditional_shared_eccentricity_component':{
            'dP_dRe':derivatives,'sigmaP_from_Re_only':[abs(x)*reported_dre for x in derivatives],
            'covariance':component,'not_total_covariance':True,
            'do_not_add_twice_to_source_errors':True},
        'row1_conditional_branch_diagnostics':likelihood,
        'readiness':{'raw_counts_original_windows_joint_covariance_recovered':False,
            'legacy_x_to_KS_or_RB_phase_bridge_established':False,
            'experimental_refit_executed':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'sourcehash':result['source_sha256'],
          'normal_axis_kernel':str(n_su),'eight_rows':len(table),
          'largest_P_residual':max(abs(x['reported_minus_replayed_P']) for x in table),
          'null_R_weighted':re,'null_R_sigma':dre,
          'row1_likelihoods':likelihood},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
