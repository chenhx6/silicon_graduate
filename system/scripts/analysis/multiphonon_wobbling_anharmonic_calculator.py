#!/usr/bin/env python3
"""Descriptive three-level ratios, with no automatic wobbling assignment.

A common spin/yrast reference must be established before comparing excitations.
Harmonic oscillator scaling is conditional on the specified transition operator;
no universal ratio interval or direct 2->0 branch threshold identifies a nucleus.
"""
import argparse
import json
from multiphonon_wobbling_anharmonic_spectrum_solver import finite


def evaluate_multiphonon_wobbling_energies(omega_wob_keV=350.,Delta_anharm_keV=-40.):
    hw=finite(omega_wob_keV,'omega_wob_keV',positive=True)
    shift=finite(Delta_anharm_keV,'Delta_anharm_keV')
    e2=2*hw+shift
    if e2<=hw:
        raise ValueError('requested synthetic level sequence is not ordered')
    a=shift/(2*hw)
    return {'one_phonon_energy_E1_keV':hw,'two_phonon_energy_E2_keV':e2,
            'anharmonic_shift_Delta_keV':shift,'energy_ratio_R21':e2/hw,
            'anharmonicity_parameter_A':a,
            'classification':'Subharmonic_Softening (ansatz)' if a<0 else 'Stiffening (ansatz)' if a>0 else 'Harmonic_spacing (ansatz)',
            'data_origin':'synthetic energy ansatz; no measured nuclear input',
            'physical_assignment':None}


def audit_multiphonon_wobbling_candidate(E0_keV,E1_keV,E2_keV,
        be2_2_to_1=None,be2_1_to_0=None,be2_2_to_0=None,*,reference_is_common=False):
    e0,e1,e2=[finite(x,'energy') for x in (E0_keV,E1_keV,E2_keV)]
    if not isinstance(reference_is_common,bool):
        raise ValueError('reference_is_common must be boolean')
    d1,d2=e1-e0,e2-e0
    if reference_is_common and d1<=0:
        raise ValueError('common-reference excitation denominator must be positive')
    vals=[None if x is None else finite(x,'B(E2)',minimum=0)
          for x in (be2_2_to_1,be2_1_to_0,be2_2_to_0)]
    b21,b10,b20=vals
    def ratio(a,b): return None if a is None or b is None or b==0 else a/b
    r21=d2/d1 if reference_is_common else None
    return {'energy_splitting_1_phonon_keV':d1,'energy_splitting_2_phonon_keV':d2,
            'energy_ratio_R21':r21,'anharmonicity_index_A':None if r21 is None else r21/2-1,
            'common_reference':'caller-asserted' if reference_is_common else 'not-established',
            'be2_ratio_stepover':ratio(b21,b10),'be2_ratio_crossover':ratio(b20,b21),
            'score':None,'physical_assignment':None,
            'verdict':'DESCRIPTORS_ONLY; no two-phonon confirmation or rejection',
            'audit_checks':['establish spin/signature and yrast references',
                            'preserve all mixing-ratio branches and strength uncertainties',
                            'relative out/in strengths from different bands have different normalizers',
                            'compare full model and competing configurations; no fixed universal gates']}


def format_text_report(summary):
    lines=['Three-level descriptors; no automatic nuclear mode assignment',
           json.dumps(summary['theoretical_model'],indent=2,allow_nan=False)]
    if 'experimental_audit' in summary:
        lines.append(json.dumps(summary['experimental_audit'],indent=2,allow_nan=False))
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--hw',type=float,default=320.)
    p.add_argument('--delta-anharm',type=float,default=-40.)
    p.add_argument('--audit',action='store_true',help='Describe supplied inputs; never assigns a nuclear mode')
    p.add_argument('--common-reference',action='store_true',help='Caller asserts energies use a physically comparable reference')
    for key in ('e0','e1','e2','be2-21','be2-10','be2-20'): p.add_argument('--'+key,type=float)
    p.add_argument('--json',action='store_true');a=p.parse_args()
    try:
        r={'theoretical_model':evaluate_multiphonon_wobbling_energies(a.hw,a.delta_anharm)}
        if a.audit:
            if any(v is None for v in (a.e0,a.e1,a.e2)): p.error('--audit requires --e0, --e1 and --e2')
            r['experimental_audit']=audit_multiphonon_wobbling_candidate(a.e0,a.e1,a.e2,
                a.be2_21,a.be2_10,a.be2_20,reference_is_common=a.common_reference)
    except ValueError as e: p.error(str(e))
    print(json.dumps(r,indent=2,allow_nan=False) if a.json else format_text_report(r))


if __name__=='__main__': main()
