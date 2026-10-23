#!/usr/bin/env python3
"""Declared QTR/HFA scale and parameter checks, not the authors' solver or fit."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    a = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    raw = root / 'raw/papers/2014_Frauendorf_Dönau_Transverse wobbling.pdf'
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == '36794ee1308adc1b34206ccdbf62353d6e79b3b485979e78709fd31efe5f57e3'
    controls = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        controls.append({'label': label, 'declared_math_check': True})

    # Source Eqs16/17 with chosen n/J, x/y, Q0/Q2; e=1 units.
    def e2(q0, q2):
        jtot, n, x, y = 12., 1., np.cosh(.3), np.sinh(.3)
        return np.array([5/(16*np.pi)*q2*q2,
                         5/(16*np.pi)*n/jtot*(np.sqrt(3)*q0*x-np.sqrt(2)*q2*y)**2])
    base = e2(2., 1.)
    scaled = e2(2.4, 1.2)
    check('Common chosen quadrupole amplitude scales both E2 B by c^2', np.allclose(scaled, base*1.2**2))
    check('Common amplitude cancels in the HFA E2 out/in ratio', np.isclose(scaled[1]/scaled[0], base[1]/base[0]))
    # Generic CQM algebra H=H0-kappa*V(Q); NOT a QTR diagonalization.
    h0 = np.diag([0., 1.]); v = np.array([[1., .2], [.2, -.5]])
    coupling, c = .4, 1.2
    check('Declared free-coupling rescaling Q->cQ,kappa->kappa/c preserves H',
          np.allclose(h0-coupling*v, h0-(coupling/c)*(c*v)))
    crit = {}
    for label, (jm, js, jl) in {'fit':(21.,13.,4.), 'hydrodyn':(20.,6.,4.), 'cranking':(17.,7.,3.)}.items():
        particle_j = 5.5  # Chosen FA value, not a fitted full-model alignment.
        jc = particle_j*jm/(jm-js)
        ac = particle_j*(1/(2*js))/((1/(2*js))-(1/(2*jm)))
        ic = (np.sqrt(1+4*jc*jc)-1)/2
        check(label+' Critical J formula agreement under hbar=1', np.isclose(jc, ac))
        crit[label] = {'Jm':jm,'Js':js,'Jl':jl,'chosen_j':particle_j,'Jc':jc,'I_if_J_sqrt_I_Iplus1':ic,'Jm_over_Js':jm/js}
    table = [
        {'I':8.5,'BE2_in_cal':.637,'BE2_con_cal':.488,'BM1_con_cal':.243,'rE2_cal':.767,'rM1_cal':.381},
        {'I':10.5,'BE2_in_cal':.744,'BE2_con_cal':.399,'BM1_con_cal':.187,'rE2_cal':.536,'rM1_cal':.252},
        {'I':12.5,'BE2_in_cal':.838,'BE2_con_cal':.331,'BM1_con_cal':.167,'rE2_cal':.395,'rM1_cal':.199},
        {'I':14.5,'BE2_in_cal':.930,'BE2_con_cal':.267,'BM1_con_cal':.167,'rE2_cal':.288,'rM1_cal':.180},
        {'I':16.5,'BE2_in_cal':1.023,'BE2_con_cal':.194,'BM1_con_cal':.155,'rE2_cal':.190,'rM1_cal':.151},
    ]
    for row in table:
        for kind, key in [('E2','BE2_con_cal'),('M1','BM1_con_cal')]:
            low=(row[key]-.0005)/(row['BE2_in_cal']+.0005)
            high=(row[key]+.0005)/(row['BE2_in_cal']-.0005)
            printed=row['r'+kind+'_cal']
            check(f"Printed ratio rounding intervals overlap: I={row['I']}, {kind}",
                  max(low,printed-.0005)<=min(high,printed+.0005))
    out = {'checkpoint':'044','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
           'source_E2_equation_control':{'chosen_Q0_Q2':[2.,1.],'chosen_scale':c,'Bin_Bcon':base.tolist(),'scaled_Bin_Bcon':scaled.tolist(),'ratio':float(base[1]/base[0]),'boundary':'Chosen HFA example. No actual nuclear moments, calibration or full QTR reproduced.'},
           'CQM_scaling_boundary':'Algebraic free-kappa reparameterization only; actual paper constrains shape and coupling from specified inputs. Does not invalidate their parameterization or identify a measured quadrupole magnitude.',
           'Pr_HFA_critical_controls':crit,'critical_boundary':'TableI ratios plus chosen j=11/2 in HFA; J=sqrt(I(I+1)) differs from I. Not an experimental threshold or full quantum eigenvalue minimum.',
           'TableII_calculated_rows':table,
           'Pr_tentative2014_vs_published2015':[
               {'I':10.5,'rM1_2014':[.130,.011],'rM1_2015':[.164,.014],'rE2_2014':[.92,.03],'rE2_2015':[.843,.032]},
               {'I':12.5,'rM1_2014':[.021,.004],'rM1_2015':[.035,.009],'rE2_2014':[.535,.01],'rE2_2015':[.500,.025]},
               {'I':14.5,'rM1_2014':[.010,.002],'rM1_2015_upper_literal':'<0.016±0.004','rE2_2014':[.28,.01],'rE2_2015_lower_literal':'>0.261±0.014'}],
           'lineage_boundary':'2014TableII explicitly preliminary private communication Ref26, not independent replication of2015 or evidence of new absolute lifetimes. Printed bounds preserved, no likelihood/CI inference.',
           'literal_discrepancies':['PDF8 body prints Js/Jm=2.34 though TableI hydro Lu Jm68/Js29 gives Jm/Js=2.3448. Do not silently exchange literal symbols.', 'PDF11 Appendix prints Qbar0=f epsilon cosgamma and Qbar2=f epsilon cosgamma/sqrt2, including cosgamma in EqA2. Actualproducer/erratum not obtained; no silent sin substitution or complete implementation certification.'],
           'controls':controls,'certification_scope':'Literal source and declared math only, not fullmodel/sourceclaim closure.'}
    p=a.run_dir/'qtr-e2-contract-result-044.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'artifact':str(p),'controls':len(controls),'Pr_HFA_critical':crit}))


if __name__=='__main__':
    main()
