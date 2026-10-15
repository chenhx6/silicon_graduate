#!/usr/bin/env python3
"""Actual D4 energy chains with declared finite-response/stencil controls.

Reported spins are assumptions for this exercise, including tentative 23.
No experimental covariance, Nd mean, or Pr rotation-axis assignment is fitted.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np

from day14_pr136_transition_candidates import table_rows, select
from day14_pr136_sameparent_strength import reported_M

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02'


def assigned_spin(row):
    m=re.search(r'(\(?\d+\s*[+-]\s*\)?)\s*→\s*(\(?\d+\s*[+-]\s*\)?)\s*$',row['remainder_literal'])
    if not m: raise ValueError('selected spin syntax needs source inspection')
    ji,jf=[int(re.search(r'\d+',x)[0]) for x in m.groups()]
    return ji,jf,any('(' in x for x in m.groups())


def secants(edges, lag=1, *, kind):
    if lag<1: raise ValueError('positive edge separation required')
    out=[]
    for a,b in zip(edges,edges[lag:]):
        k=a['Ji']-a['Jf']
        if k<=0 or b['Ji']-b['Jf']!=k:
            raise ValueError('this estimator requires the same positive photon spin step')
        di=b['Ji']-a['Ji']
        if di<=0: raise ValueError('ordered increasing parent spin required')
        de=float(Fraction(str(b['E']))-Fraction(str(a['E'])))
        numerator=1000*k*di
        val=None if de==0 else numerator/de
        out.append(dict(ids=[a['id'],b['id']],kind=kind,photon_step=k,parent_step=di,
                        parent_spins=[a['Ji'],b['Ji']],
                        effective_spin=(a['Ji']+b['Ji']-k)/2,
                        omega_mid_MeV=(a['E']+b['E'])/(2000*k),delta_E_keV=de,
                        J2_hbar2_per_MeV=val,
                        status='zero_denominator' if de==0 else 'negative_secant' if de<0 else 'finite_positive',
                        tentative_input=a['tentative'] or b['tentative']))
    return out


def declared_display_filter(points):
    eligible=[p for p in points if p['J2_hbar2_per_MeV'] is not None
              and p['J2_hbar2_per_MeV']>0 and p['omega_mid_MeV']>.3]
    initial=float(np.mean([p['J2_hbar2_per_MeV'] for p in eligible]))
    removed=[p for p in eligible if p['J2_hbar2_per_MeV']>=2*initial]
    kept=[p for p in eligible if p not in removed]
    return dict(kind='one-pass declared sensitivity; not the author Nd selection or an assigned Pr low group',
                actual_interaction_mask=None,chosen_interaction_mask='all selected points retained before display rule',
                frequency_cut_MeV=.3,initial_mean=initial,threshold=2*initial,
                excluded_before_display=[dict(ids=p['ids'],status=p['status'],omega_mid_MeV=p['omega_mid_MeV'])
                                         for p in points if p not in eligible],
                removed_ids=[p['ids'] for p in removed],kept_ids=[p['ids'] for p in kept],
                removed_values=[p['J2_hbar2_per_MeV'] for p in removed],
                retained_mean=float(np.mean([p['J2_hbar2_per_MeV'] for p in kept])))


def rotor_edges(k, spins, J=25, energy_zero=0):
    def level(i): return energy_zero+1000*i*(i+1)/(2*J)
    return [dict(id=f'chosen-{k}-{i}',Ji=i,Jf=i-k,E=level(i)-level(i-k),tentative=False)
            for i in spins]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=RUN/'pr136-inertia-paths.json')
    args=ap.parse_args();checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value: raise AssertionError(name)
    st=(ROOT/'knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md').read_text()
    raw=ROOT/re.search(r'^raw_file: "(.*)"$',st,re.M)[1]
    sha=re.search(r'^raw_sha256: (\w+)',st,re.M)[1]
    check('actual_source_hash',hashlib.sha256(raw.read_bytes()).hexdigest()==sha)
    pages=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True).split('\f')
    rows,rejected=table_rows(pages)
    check('actual_table_scope',len(rows)==156 and not rejected)
    pcst=(ROOT/'knowledge/sources/peng-chen-2022-chiral-rotation-rhodium-isotopes.md').read_text()
    pcraw=ROOT/re.search(r'^raw_file: "(.*)"$',pcst,re.M)[1]
    pcsha=re.search(r'^raw_sha256: (\w+)',pcst,re.M)[1]
    check('actual_PC22_source_hash',hashlib.sha256(pcraw.read_bytes()).hexdigest().lower()==pcsha.lower())
    pctext=subprocess.check_output(['pdftotext','-layout',str(pcraw),'-'],text=True).split('\f')[5]
    compact=re.sub(r'\s+','',pctext)
    check('actual_PC22_two_edge_denominator','Eγ(I+1→I)−Eγ(I−1→I−2)' in compact)
    parents={14:3729.4,15:3937.2,16:4210.8,17:4581.6,18:4990.9,19:5430.9,
             20:5934.5,21:6444.8,22:6974.9,23:7562.3}
    dipoles=[273.6,370.8,409.3,440.,503.6,510.3,530.1,587.4]
    crosses=[481.,644.1,780.3,849.4,943.8,1014.2,1040.,1117.9]
    ds,cs=[],[]
    for spin,ed,ec in zip(range(16,24),dipoles,crosses):
        for energy,k,target in [(ed,1,ds),(ec,2,cs)]:
            row=select(rows,'D4',energy)
            ji,jf,tentative=assigned_spin(row)
            check(f'actual_spin_parent_{spin}_{k}',ji==spin and jf==spin-k and row['P']==parents[spin])
            check(f'actual_literal_row_{spin}_{k}',row['raw'] in pages[6])
            target.append(dict(**row,Ji=ji,Jf=jf,tentative=tentative,reported_M=reported_M(row),
                               assigned_daughter_parent=parents[jf],
                               nominal_endpoint_residual_keV=float(Fraction(str(row['P']))-Fraction(str(row['E']))-Fraction(str(parents[jf])))))
    check('four_source_M_blanks_preserved',[(e['Ji'],k) for k,es in [(1,ds),(2,cs)] for e in es if not e['reported_M']]
          ==[(17,1),(23,1),(16,2),(23,2)])
    check('tentative_23_preserved',ds[-1]['tentative'] and cs[-1]['tentative'])
    for name,series in [('dipole',ds),('cross_even',cs[::2]),('cross_odd',cs[1::2])]:
        check('connected_reported_path_'+name,all(b['assigned_daughter_parent']==a['P'] for a,b in zip(series,series[1:])))
    low=select(rows,'D4',207.8);wrong_low=select(rows,'D4',265.)
    check('same_parent_same_deltaI_not_same_endpoint',low['P']==wrong_low['P']==parents[15]
          and assigned_spin(low)[:2]==assigned_spin(wrong_low)[:2]==(15,14)
          and abs(low['P']-low['E']-(wrong_low['P']-wrong_low['E']))>50)
    closures=[]
    for i,c in enumerate(cs):
        prev=low if i==0 else ds[i-1]
        residue=Fraction(str(c['E']))-Fraction(str(ds[i]['E']))-Fraction(str(prev['E']))
        closures.append(dict(parent_spin=c['Ji'],cross_id=c['id'],dipole_ids=[ds[i]['id'],prev['id']],
                             residual_keV=float(residue),covariance=None))
    check('printed_closure_residuals_not_forced_zero',max(abs(p['residual_keV']) for p in closures)==.4
          and any(p['residual_keV']!=0 for p in closures))
    wrong_closure=float(Fraction('481.0')-Fraction('273.6')-Fraction('265.0'))
    check('wrong_low_path_fails_nominal_closure',math.isclose(wrong_closure,-57.6))
    estimates={
        'dipole_adjacent':secants(ds,kind='k1 adjacent connected path'),
        'dipole_two_edge':secants(ds,lag=2,kind='k1 two-edge secant, declared midpoint convention'),
        'cross_even':secants(cs[::2],kind='k2 even-parent connected path'),
        'cross_odd':secants(cs[1::2],kind='k2 odd-parent connected path'),
        'cross_interleaved':secants(cs,kind='k2 parentstep1 interleaved estimate, not one connected E2 path')}
    check('different_stencil_locations_preserved',estimates['dipole_adjacent'][0]['effective_spin']==16
          and estimates['dipole_two_edge'][0]['effective_spin']==16.5)
    check('crossover_parentstep_distinguished',all(p['parent_step']==2 for p in estimates['cross_even'])
          and all(p['parent_step']==1 for p in estimates['cross_interleaved']))
    check('actual_interleaving_not_one_E2_path',not all(b['assigned_daughter_parent']==a['P'] for a,b in zip(cs,cs[1:])))
    for j,p in enumerate(estimates['dipole_two_edge']):
        a,b=estimates['dipole_adjacent'][j:j+2]
        harmonic=2/(1/a['J2_hbar2_per_MeV']+1/b['J2_hbar2_per_MeV'])
        check('two_edge_is_harmonic_not_arithmetic_'+str(j),math.isclose(p['J2_hbar2_per_MeV'],harmonic,rel_tol=1e-12))
    # Conditional covariance: quoted marginal errors interpreted as sigma and
    # independent photon errors only here. The actual experiment's Sigma is absent.
    grad=np.zeros((7,8))
    for j,p in enumerate(estimates['dipole_adjacent']):
        factor=1000/(p['delta_E_keV']**2)
        grad[j,j],grad[j,j+1]=factor,-factor
    sigma=np.array([e['dE'] for e in ds]);cov=grad@np.diag(sigma*sigma)@grad.T
    check('conditional_covariance_psd',np.linalg.eigvalsh(cov).min()>-1e-9)
    check('shared_gamma_induces_neighbor_covariance',all(cov[i,i+1]<0 for i in range(6)))
    vals=np.array([p['J2_hbar2_per_MeV'] for p in estimates['dipole_adjacent']])
    check('common_photon_offset_cancels_curvature',np.allclose(grad@np.ones(8),0))
    check('common_energy_gain_sensitivity',np.allclose(grad@np.array(dipoles),-vals))
    for j,p in enumerate(estimates['dipole_adjacent']):
        sa,sb=sigma[j:j+2];scale=1000/(p['delta_E_keV']**2)
        p['conditional_sigma_independent_first_order']=math.sqrt(cov[j,j])
        p['conditional_sigma_range_over_unknown_pair_correlation']=[scale*abs(sa-sb),scale*(sa+sb)]
    screen=declared_display_filter(estimates['dipole_adjacent'])
    check('declared_display_sensitivity_nonempty',len(screen['removed_ids'])==1 and screen['retained_mean']<screen['initial_mean'])
    r1=rotor_edges(1,range(16,24));r2=rotor_edges(2,range(16,24))
    for name,es in [('dipole',r1),('cross_all',r2),('cross_even',r2[::2]),('cross_odd',r2[1::2])]:
        check('quadratic_rotor_correct_parentstep_'+name,all(math.isclose(p['J2_hbar2_per_MeV'],25) for p in secants(es,kind='chosen rotor')))
    check('quadratic_rotor_two_edge',all(math.isclose(p['J2_hbar2_per_MeV'],25) for p in secants(r1,2,kind='chosen rotor')))
    check('wrong_four_factor_on_interleaved_crossovers_doubles',all(math.isclose(4000/(b['E']-a['E']),50) for a,b in zip(r2,r2[1:])))
    translated=copy.deepcopy(ds)
    for e in translated:e['Ji']+=4;e['Jf']+=4;e['P']+=1234;e['assigned_daughter_parent']+=1234
    check('absolute_spin_label_shift_invariant',np.allclose([p['J2_hbar2_per_MeV'] for p in secants(translated,kind='label shift')],vals))
    check('excitation_zero_cancels_before_photon_derivation',all(math.isclose(a['E'],b['E']) for a,b in zip(r1,rotor_edges(1,range(16,24),energy_zero=1234))))
    def energy_control(mult=1,offset=0):
        es=copy.deepcopy(ds)
        for e in es:e['E']=mult*e['E']+offset
        return secants(es,kind='chosen calibration control')
    check('common_energy_offset_changes_frequency_only',np.allclose([p['J2_hbar2_per_MeV'] for p in energy_control(offset=10)],vals))
    check('common_gain_not_cancelled',np.allclose([p['J2_hbar2_per_MeV'] for p in energy_control(mult=1.01)],vals/1.01))
    null=copy.deepcopy(ds[:2]);null[1]['E']=null[0]['E']
    check('zero_denominator_not_silent_drop',secants(null,kind='chosen zero')[0]['status']=='zero_denominator')
    null[1]['E']=null[0]['E']-1
    check('negative_secant_retained',secants(null,kind='chosen negative')[0]['J2_hbar2_per_MeV']<0)
    z=select(rows,'D4',319.2);ji,jf,t=assigned_spin(z)
    try:secants([dict(z,Ji=ji,Jf=jf,tentative=t),ds[0]],kind='invalid deltaI0')
    except ValueError:check('actual_deltaI0_outside_estimator',True)
    else:check('actual_deltaI0_outside_estimator',False)
    out=dict(kind='actual D4 nominal energy-chain finite-response exercise; not Nd reproduction or Pr axis/shape fit',
             source=dict(path='knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md',raw=str(raw.relative_to(ROOT)),sha256=sha,locator='PDF p.7 TableI D4 and PDF p.4 Fig1'),
             companion=dict(path='knowledge/sources/peng-chen-2022-chiral-rotation-rhodium-isotopes.md',sha256=pcsha.lower(),locator='PDF p.6 Eq3; targeted check only, source plot frequency labels retained'),
             definition=dict(frequency='x=Egamma/k in MeV',response='J2/hbar^2=delta(parent I)/delta x for same k',
                             effective_spin='mean(parent I)-k/2',frequency_location='mean(xa,xb)',
                             author_Pr_or_Nd_stencil_attested=False,actual_covariance=None),
             dipole_inputs=ds,crossover_inputs=cs,low_branch_counterexample=dict(correct=low,other=wrong_low,wrong_closure_keV=wrong_closure),
             nominal_cycle_closures=closures,estimates=estimates,
             conditional_adjacent_covariance=dict(assumption='quoted marginal dE interpreted as independent sigma; first-order only',matrix=cov.tolist(),source_covariance=None),
             declared_selection_sensitivity=screen,
             boundaries=['assigned spin steps/path conditional; tentative I23 and four M blanks preserved',
                         'photon energy common offset differs from an excitation-energy reference shift',
                         'stencil estimates are correlated and evaluated at different positions, not independent data',
                         'screen is declared Pr sensitivity, not Petrache Nd mask, fit, or published average reproduction',
                         'no absolute gamma/rotation-axis/shape assignment or actual response/covariance inferred'],
             checks=checks,check_count=len(checks),passed=all(checks.values()))
    args.output.resolve().relative_to(ROOT);args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),passed=True,adjacent_values=vals.tolist(),screen=screen),ensure_ascii=False))
    return 0


if __name__=='__main__':raise SystemExit(main())
