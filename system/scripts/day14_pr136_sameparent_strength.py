#!/usr/bin/env python3
"""Conditional same-parent radiative strength ratios, not a 136Pr refit.

The actual Table-I rows are paired by parent. delta=0 and a pure E2 crossover
are DECLARED controls; blank source multipolarity cells remain blank. Quoted
marginal errors are combined only under an explicit independent-error model.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np
from scipy.constants import c,e,epsilon_0,mu_0,hbar,physical_constants

from day14_pr136_transition_candidates import select
from day14_ensdf67_strength_crosswalk import rate_coefficient_and_WU


def rate_coefficients():
    MeV=1e6*e
    barn=1e-28
    muN=physical_constants['nuclear magneton'][0]
    q=MeV/(hbar*c)
    electric2=8*math.pi*3/(2*15**2)/hbar*q**5/(4*math.pi*epsilon_0)*e**2*barn**2
    magnetic1=16*math.pi/9/hbar*q**3*mu_0/(4*math.pi)*muN**2
    return dict(E2_s_MeV5_e2b2=electric2,M1_s_MeV3_muN2=magnetic1,
                kappa=electric2/magnetic1,
                sqrt_kappa=math.sqrt(electric2/magnetic1))


def photon_intensity(row):
    literal=row['remainder_literal'].split()[0]
    m=re.fullmatch(r'(\d+(?:\.\d+)?)\((\d+)\)',literal)
    if m is None:
        raise ValueError('intensity limit/missing/asymmetric input must not be treated as a Gaussian value')
    decimals=len(m[1].split('.')[1]) if '.' in m[1] else 0
    return dict(value=float(m[1]),sigma=int(m[2])*10**(-decimals),literal=literal)


def reported_M(row):
    if 'M1+E2' in row['remainder_literal']:
        return 'M1+E2'
    return 'E2' if re.search(r'\bE2\b',row['remainder_literal']) else ''


def ratio(pair,delta_d,*,E2_crossover_fraction=1.):
    d,g=pair
    if d['P']!=g['P']:
        raise ValueError('different physical parents: population/total-rate cancellation is invalid')
    if delta_d is None:
        raise ValueError('unconditional result unavailable without a specified M1/E2 component model')
    if not 0<E2_crossover_fraction<=1:
        raise ValueError('positive E2 photon fraction required')
    Id,Ic=photon_intensity(d)['value'],photon_intensity(g)['value']
    Ed,Ec=d['E']/1000,g['E']/1000
    return rate_coefficients()['kappa']*Ec**5/Ed**3*Id/Ic/((1+delta_d**2)*E2_crossover_fraction)


def ledger_ratio(Ed,Ec,M1,E2_in_d,E2_c,other,alpha_d,alpha_c,parents=1e6):
    # Fixed photon partial rates; all other decay and IC rates enter ONE common
    # total parent rate. This tests cancellation, not a physical decay inventory.
    total=(M1+E2_in_d)*(1+alpha_d)+E2_c*(1+alpha_c)+other
    Id=parents*(M1+E2_in_d)/total
    Ic=parents*E2_c/total
    delta2=E2_in_d/M1
    k=rate_coefficients()['kappa']
    got=k*Ec**5/Ed**3*(Id/Ic)/(1+delta2)
    expected=k*Ec**5/Ed**3*M1/E2_c
    return got,expected,total


def audit(candidate_file):
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    fixture=json.loads(candidate_file.read_text())
    source=Path('knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md').read_text()
    raw=Path(re.search(r'^raw_file: "(.*)"$',source,re.M).group(1))
    check('actual_accepted_copy_hash',hashlib.sha256(raw.read_bytes()).hexdigest()==fixture['actual_new_pdf_sha256'])
    coeff=rate_coefficients()
    earlier_fm4_coefficient,_=rate_coefficient_and_WU(67)
    check('SI_E2_coefficient_matches_earlier_fm4_form',
          abs(coeff['E2_s_MeV5_e2b2']/1e4/earlier_fm4_coefficient-1)<1e-12)
    check('SI_M1_coefficient_in_expected_units',1.75e13<coeff['M1_s_MeV3_muN2']<1.77e13)
    check('SI_unit_factor_rounds_to_LKH_0835',format(coeff['sqrt_kappa'],'.3f')=='0.835')
    check('printed_unit_rounding_small_not_a_measurement_difference',
          abs(.835**2/coeff['kappa']-1)<.001)
    source_lkh=Path('knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md').read_text()
    lkhraw=Path(re.search(r'^raw_file: "(.*)"$',source_lkh,re.M).group(1))
    lkhsha=re.search(r'^raw_sha256: "?(\w+)',source_lkh,re.M).group(1)
    check('actual_LKH_source_hash',hashlib.sha256(lkhraw.read_bytes()).hexdigest()==lkhsha)
    pairs=[]
    for J,Ed,Ec,P in [(16,273.6,481.,4210.8),(17,370.8,644.1,4581.6),
                      (18,409.3,780.3,4990.9),(19,440.,849.4,5430.9),
                      (20,503.6,943.8,5934.5),(21,510.3,1014.2,6444.8),
                      (22,530.1,1040.,6974.9),(23,587.4,1117.9,7562.3)]:
        d=select(fixture['source_rows'],'D4',Ed)
        g=select(fixture['source_rows'],'D4',Ec)
        check('same_literal_parent_'+str(J),d['P']==g['P']==P)
        # Source literal verification independent of candidate JSON.
        if not pairs:
            pdftext=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True).split('\f')
        check('actual_D4_rows_'+str(J),d['raw'] in pdftext[d['pdf_page']-1]
              and g['raw'] in pdftext[g['pdf_page']-1])
        R=ratio((d,g),0.)
        Id,Ic=photon_intensity(d),photon_intensity(g)
        # Gradient order Id,Ic,Ed_keV,Ec_keV. First-order only.
        gradient=R*np.array([1/Id['value'],-1/Ic['value'],-3/d['E'],5/g['E']])
        sigmas=np.array([Id['sigma'],Ic['sigma'],d['dE'],g['dE']])
        variance_terms=(gradient*sigmas)**2
        sigma_diag=math.sqrt(float(np.sum(variance_terms)))
        common_norm_vector=np.array([Id['value'],Ic['value'],0.,0.])
        common_gain_vector=np.array([0.,0.,d['E'],g['E']])
        check('common_intensity_normalizer_cancels_'+str(J),
              abs(float(gradient@common_norm_vector))<1e-12)
        check('common_energy_gain_has_factor_two_'+str(J),
              abs(float(gradient@common_gain_vector)/R-2)<1e-12)
        check('delta_correction_not_absolute_strength_'+str(J),
              abs(ratio((d,g),.5)/R-.8)<1e-12)
        check('unknown_crossover_purity_is_explicit_'+str(J),
              abs(ratio((d,g),0.,E2_crossover_fraction=.5)/R-2)<1e-12)
        # An explicit intensity-unit change leaves the result invariant.
        scaled=[]
        for row in (d,g):
            x=dict(row)
            ii=photon_intensity(row)
            token=f"{ii['value']*10:.1f}({round(ii['sigma']*100)})"
            x['remainder_literal']=token+' '+row['remainder_literal'].split(' ',1)[1]
            scaled.append(x)
        check('arbitrary_common_I_scale_invariant_'+str(J),abs(ratio(scaled,0.)/R-1)<1e-12)
        pairs.append(dict(J_assigned=J,parent_E=P,
                          dipole_source=d,crossover_source=g,
                          reported_M_d=reported_M(d),reported_M_c=reported_M(g),
                          I_d=Id,I_c=Ic,R_delta0_purecrossover_control=R,
                          sigma_independent_quoted_marginals_first_order=sigma_diag,
                          variance_contributions=dict(zip(['I_d','I_c','E_d','E_c'],variance_terms.tolist())),
                          source_Cov=None,source_delta=None,source_crossover_fraction=None,
                          declared_delta0=True,declared_pure_E2_crossover=True,
                          assigned_spin_tentative=('(' in d['remainder_literal'].split('→')[0].rsplit('  ',1)[-1])))
    blank=[(x['J_assigned'],which) for x in pairs for which in ('d','c')
           if x['reported_M_'+which]=='']
    check('four_M_blanks_retained_not_reported_as_measured',blank==[(16,'c'),(17,'d'),(23,'d'),(23,'c')])
    check('late_spin_quoted_linear_error_large_flag',
          pairs[-1]['sigma_independent_quoted_marginals_first_order']/pairs[-1]['R_delta0_purecrossover_control']>.7)
    for i,(other,ad,ac) in enumerate([(0.,0.,0.),(8.,.3,2.),(1e6,20.,100.)]):
        got,expected,total=ledger_ratio(.440,.8494,2.3,.7,1.1,other,ad,ac)
        check('unknown_total_tau_IC_other_branch_cancel_in_declared_ledger_'+str(i),
              abs(got/expected-1)<1e-12 and total>0)
    for name,action in [
        ('different_parent_rejected',lambda:ratio((pairs[0]['dipole_source'],pairs[1]['crossover_source']),0.)),
        ('unconditional_unknown_delta_rejected',lambda:ratio((pairs[0]['dipole_source'],pairs[0]['crossover_source']),None)),
        ('limit_not_converted_to_symmetric_I',lambda:photon_intensity(select(fixture['source_rows'],'D5',237.)))]:
        try:
            action()
        except ValueError:
            check(name,True)
        else:
            check(name,False)
    a,b=pairs[0]['dipole_source'],pairs[0]['crossover_source']
    wrong=coeff['kappa']*b['E']**5/a['E']**3*photon_intensity(a)['value']/photon_intensity(b)['value']
    check('keV_as_MeV_error_factor_one_million',abs(wrong/ratio((a,b),0.)/1e6-1)<1e-12)
    return dict(model='sameparent photon-component ratio; delta0/purecrossover and diagonal quoted errors are declared controls',
                rate_coefficients_SI=coeff,printed_LKH_squared_factor=.835**2,
                pairs=pairs,blank_M_rows=blank,
                figure_check=dict(locator='acceptedPDF11 Fig9(c)',method='visual source audit only; no invented digitized y values',
                                  x_assigned_spins=list(range(16,24)),y_scale='log',
                                  y_units='mu_N^2/(e^2 b^2)',source_points=8),
                boundaries=['source delta/crossover purity and intensity-energy covariance not supplied',
                            'tau/ICC/other-branch cancellation requires SAME parent and matched corrected photon yields',
                            'B ratio is not samegamma delta squared; no absolute B inferred',
                            'large weak-denominator first-order error is not an experimental confidence interval',
                            'no full parent event/efficiency/angular-response replay; D6 lower-limit construction not recovered'],
                checks=checks,checks_passed=len(checks))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidates',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=audit(a.candidates)
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=out['checks_passed'],all_checks_true=all(out['checks'].values()),
                          output=str(a.output))))


if __name__=='__main__':
    main()
