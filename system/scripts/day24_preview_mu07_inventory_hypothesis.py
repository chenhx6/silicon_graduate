#!/usr/bin/env python3
"""Compound parent/component/normalization hypotheses, not a paper-error test.

All widths below are CONDITIONAL nuclear photon partial widths, not detector
count rates. The line/parent/component binding is explicitly not established.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re

from day24_preview_mu07_vector_plot import table_rows,parse_plot,central
from day24_preview_nd135_export_identity import read_csv


CONSTANTS={'hbar_MeV_s':6.582119569e-22,'hbarc_MeV_fm':197.3269804,
           'fine_structure_alpha':7.2973525693e-3,'proton_mass_MeV':938.27208816}
LINE_IDS={31:{'M1in':('59','56','0'),'E2in':('59','54','1'),'M1out':('59','52','2'),'E2out':('59','48','3')},
          33:{'M1in':('61','59','0'),'E2in':('61','56','1'),'M1out':('61','55','2'),'E2out':('61','52','3')},
          35:{'M1in':('66','61','0'),'E2in':('66','59','2'),'M1out':('66','60','1'),'E2out':('66','55','3')},
          37:{'M1in':('69','66','0'),'E2in':('69','61','2'),'M1out':('69','63','1'),'E2out':('69','60','3')}}


def coefficients():
    hb=CONSTANTS['hbar_MeV_s'];hc=CONSTANTS['hbarc_MeV_fm']
    alpha=CONSTANTS['fine_structure_alpha'];mp=CONSTANTS['proton_mass_MeV']
    e2_gaussian=alpha*hc
    muN2_gaussian=e2_gaussian*(hc/(2*mp))**2
    def prefactor(rank):
        odddf=math.prod(range(1,2*rank+2,2))
        return 8*math.pi*(rank+1)/(rank*odddf*odddf*hb)
    cm=prefactor(1)/hc**3*muN2_gaussian*1e-12
    ce=prefactor(2)/hc**5*e2_gaussian*1e4*1e-12
    cm_alt=4*math.pi/9*alpha/(hb*mp*mp)*1e-12
    ce_alt=4*math.pi/75*alpha*1e4/(hb*hc**4)*1e-12
    return cm,ce,cm_alt,ce_alt


def spin2(jp):
    m=re.search(r'(\d+)/2',jp)
    if not m:raise ValueError('Target snapshot Jp is not the declared half-integer form')
    return int(m.group(1))


def calculate(source_root,gamma_path):
    tex=source_root/'ndchiralrev4.tex';rows=table_rows(tex.read_text())
    pm=parse_plot(source_root/'fig2.ps','M1',rows)
    pe=parse_plot(source_root/'fig3.ps','E2',rows)
    _,gamma_rows,_=read_csv(gamma_path)
    gamma={(r['fields']['start_level_idx'],r['fields']['end_level_idx'],r['fields']['gamma_idx']):r['fields'] for r in gamma_rows}
    cm,ce,cm_alt,ce_alt=coefficients()
    controls={'M1_rate_coefficient_two_unit_routes':math.isclose(cm,cm_alt,rel_tol=1e-13),
              'E2_rate_coefficient_two_unit_routes':math.isclose(ce,ce_alt,rel_tol=1e-13),
              'rate_ratio_matches_printed_rounded_point835_kinematic_coefficient':abs(math.sqrt(ce/cm)-.835)<.0005,
              'positive_fixed_rate_coefficients':cm>0 and ce>0,
              'M1_energy_cube_scaling':math.isclose(cm*.8**3/(cm*.4**3),8,rel_tol=1e-14),
              'E2_energy_fifth_scaling':math.isclose(ce*.8**5/(ce*.4**5),32,rel_tol=1e-14)}
    results=[]
    for two_i,ids in LINE_IDS.items():
        parent=next(r for r in rows if r['band']=='B' and r['two_I']==two_i)
        tau=central(parent['mean_tau_ps_raw'])
        mout=next(r for r in pm['rows'] if r['nearest_two_I']==two_i)
        eout=next(r for r in pe['rows'] if r['nearest_two_I']==two_i)
        bvalues={'M1in':central(parent['B_M1_muN2_raw']),'E2in':central(parent['B_E2_e2b2_raw']),
                 'M1out':mout['drawn_B_centre'],'E2out':eout['drawn_B_centre']}
        components={};spin_binding=True
        for label,key in ids.items():
            g=gamma[key];rank=1 if label.startswith('M1') else 2
            expected_delta=2*rank
            spin_binding=spin_binding and spin2(g['start_level_jp'])==two_i and spin2(g['end_level_jp'])==two_i-expected_delta
            e=float(g['energy'])/1000
            width=(cm if rank==1 else ce)*e**(2*rank+1)*bvalues[label]
            components[label]={'snapshot_id':list(key),'source_E_gamma_keV_string':g['energy'],
                               'source_Ji_string':g['start_level_jp'],'source_Jf_string':g['end_level_jp'],
                               'source_multipolarity_string':g['multipolarity'],
                               'source_relative_I_gamma_string':g['relative_intensity'],
                               'B_from_TableI_or_rounded_plot':bvalues[label],
                               'conditional_photon_partial_width_ps_inverse':width,
                               'conditional_tau_times_width':tau*width}
        qi=components['M1in']['conditional_tau_times_width']+components['E2in']['conditional_tau_times_width']
        qo=components['M1out']['conditional_tau_times_width']+components['E2out']['conditional_tau_times_width']
        total=qi+qo
        shape=components['M1out']['conditional_tau_times_width']/qo
        im=float(components['M1out']['source_relative_I_gamma_string'])
        ie=float(components['E2out']['source_relative_I_gamma_string'])
        relative_shape=im/(im+ie)
        controls[f'I2_{two_i}_all_declared_endpoint_spin_differences']=spin_binding
        controls[f'I2_{two_i}_all_conditional_component_widths_nonnegative']=all(
            r['conditional_photon_partial_width_ps_inverse']>=0 for r in components.values())
        controls[f'I2_{two_i}_tau_width_inventory_homogeneity']=math.isclose(
            sum(2*tau*r['conditional_photon_partial_width_ps_inverse'] for r in components.values()),2*total,rel_tol=1e-13)
        controls[f'I2_{two_i}_photon_shape_fractions_in_unit_interval']=0<shape<1 and 0<relative_shape<1
        results.append({'two_I_plot_candidate_parent':two_i,'TableI_B_mean_tau_ps_centre':tau,
                        'components_under_declared_binding':components,
                        'conditional_in_only_photon_inventory':qi,'conditional_out_pair_photon_inventory':qo,
                        'compound_H_absolute_same_parent_total_photon_inventory':total,
                        'compound_H_absolute_central_assignment_feasible':total<=1,
                        'out_pair_M1_component_fraction_from_drawn_B':shape,
                        'out_pair_total_gamma_fraction_from_export_relative_I':relative_shape,
                        'difference_is_diagnostic_not_delta_fit':shape-relative_shape,
                        'necessary_upper_scale_f_for_out_pair_if_in_components_held':max(0,(1-qi)/qo) if qi<=1 else None,
                        'bound_scope':'Only if graph I, B components, candidate lines and total mean lifetime are all bound as specified. Out-pair-only closure/shape suggests a testable selected-outlet normalization alternative, not evidence that authors used it. The scale domain is not a branch measurement or confidence interval; no source B is replaced.'})
    return {'status':'compound-binding-and-normalization-diagnostic-only','formal_day_index':23,'uncredited_preview_day':24,
            'source_premises':['LKH82 printed121Eq2.2/2.3 Gaussian photon rate and B definition','actualMU07 TeX/TableI+roundedauthorPS019','actualIAEA135Ndgamma snapshot018; binding is hypothetical'],
            'declared_constants':CONSTANTS,'derived_rate_coefficients':{'C_M1_ps_inverse_MeV_minus3_muN_minus2':cm,
                'C_E2_ps_inverse_MeV_minus5_e2b2_inverse':ce,'sqrt_CE2_over_CM1':math.sqrt(ce/cm)},
            'results':results,'controls':controls,'all_controls_pass':all(controls.values()),
            'frozen_actual_input_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [tex,source_root/'fig2.ps',source_root/'fig3.ps',gamma_path]},
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day24_preview_mu07_vector_plot.py'),Path(__file__).with_name('day24_preview_nd135_export_identity.py')]},
            'limitations':['H_abs is a compound parent/line/component/absolute-normalization interpretation. A central over-budget outcome rejects that joint assignment only, not the paper, published observations or chirality.',
                           'An approximately unit out-pair inventory is a representation/normalization clue, not proof of a conditioned normalization or a choice of a more credible interpretation.',
                           'H_cond would need explicit original branch/normalizer documentation; H_other could change initial I, line or component. No likelihood or equal plausibility is assigned.',
                           'The first648 outlet is mixed in the export. Its total gamma relative intensity need not equal its M1 photon-component intensity; no delta is inferred from shape comparisons.',
                           'No internal conversion, unknown omitted branch or experimental covariance/uncertainty propagation is supplied. Nonnegative extra decay cannot reduce an already over-budget photon-only assignment.',
                           'The widths are conditional nuclear photon decay quantities, not new detector rates, facility yield or beamtime. No physical g/Q/delta/new tau/CI calculated.',
                           'AL11 multiple-m transition formalism does not supply135Nd line identities or original experimental normalizers; neighbouring-nucleus curves are not substituted.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--gammas',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate(a.source_root,a.gammas);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
        'rate_coefficients':r['derived_rate_coefficients'],'diagnostics':[{
        'two_I':v['two_I_plot_candidate_parent'],'q_in':v['conditional_in_only_photon_inventory'],
        'q_out_pair':v['conditional_out_pair_photon_inventory'],
        'q_total_compound_H_abs':v['compound_H_absolute_same_parent_total_photon_inventory'],
        'drawn_component_shape':v['out_pair_M1_component_fraction_from_drawn_B'],
        'export_total_gamma_shape':v['out_pair_total_gamma_fraction_from_export_relative_I']}
        for v in r['results']]},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
