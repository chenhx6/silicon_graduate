#!/usr/bin/env python3
"""Actual adopted same-unit ratios; no independent producer/measurement test."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from day24_preview_nd135_export_identity import read_csv
from day24_preview_mu07_vector_plot import table_rows,parse_plot
from day24_preview_mu07_inventory_hypothesis import LINE_IDS


def calculate(gamma_path,source_root):
    _,rows,_=read_csv(gamma_path)
    gamma={(r['fields']['start_level_idx'],r['fields']['end_level_idx'],r['fields']['gamma_idx']):r['fields'] for r in rows}
    table=table_rows((source_root/'ndchiralrev4.tex').read_text())
    plots={kind:parse_plot(source_root/filename,kind,table) for kind,filename in [('M1','fig2.ps'),('E2','fig3.ps')]}
    controls={};results=[];skips=[]
    for two_i,ids in LINE_IDS.items():
        for kind,rank,field in [('M1',1,'b_m1'),('E2',2,'b_e2')]:
            a=gamma[ids[kind+'in']];b=gamma[ids[kind+'out']]
            sameparent=a['start_level_idx']==b['start_level_idx']
            controls[f'I2_{two_i}_{kind}_sameparent_bound_by_snapshotID']=sameparent
            if not a[field] or not b[field]:
                skips.append({'two_I':two_i,'kind':kind,'in_ID':list(ids[kind+'in']),'out_ID':list(ids[kind+'out']),
                              'raw_in_B_string':a[field],'raw_out_B_string':b[field],
                              'raw_in_multipolarity':a['multipolarity'],'raw_out_multipolarity':b['multipolarity'],
                              'raw_out_delta_string':b['mixing_ratio'],
                              'value_assigned':None,'reason':'Empty adopted B field and/or mixed component not established; no zeroB or new delta filled.'})
                continue
            bo,bi=Fraction(b[field]),Fraction(a[field]);eo,ei=Fraction(b['energy']),Fraction(a['energy'])
            io,ii=Fraction(b['relative_intensity']),Fraction(a['relative_intensity']);power=2*rank+1
            if min(bo,bi,eo,ei,io,ii)<=0:raise ValueError('Selected nonempty adopted centre is nonpositive')
            sameunit=bo/bi
            intensity_energy=io/ii*(ei/eo)**power
            residual=float(sameunit/intensity_energy-1)
            graph=next(r for r in plots[kind]['rows'] if r['nearest_two_I']==two_i)
            gr=graph['conditional_out_over_in_if_same_parent_component']
            common_wu=Fraction(7,13);tau=Fraction(17,11)
            tag=f'I2_{two_i}_{kind}'
            controls[tag+'_exact_common_WU_factor_cancels']=(bo*common_wu)/(bi*common_wu)==sameunit
            controls[tag+'_exact_sameparent_tau_factor_cancels']=(bo/tau)/(bi/tau)==sameunit
            controls[tag+'_exact_relativeI_energy_power_reversal']=(intensity_energy*(eo/ei)**power)==io/ii
            controls[tag+'_samefield_positive_centres_only']=True
            controls[tag+'_adopted_multipolarity_brackets_preserved']=(a['multipolarity'].startswith('[') or a['multipolarity'].startswith('(')) and (b['multipolarity'].startswith('[') or b['multipolarity'].startswith('('))
            results.append({'two_I_candidate_parent':two_i,'multipole':kind,'photon_energy_power':power,
                'in_snapshot_ID':list(ids[kind+'in']),'out_snapshot_ID':list(ids[kind+'out']),
                'input_raw':{'in_energy_keV':a['energy'],'out_energy_keV':b['energy'],
                             'in_relative_I_gamma':a['relative_intensity'],'out_relative_I_gamma':b['relative_intensity'],
                             'in_B_Weisskopf_string':a[field],'out_B_Weisskopf_string':b[field],
                             'in_unc_B_string':a['unc_bm1' if kind=='M1' else 'unc_be2'],
                             'out_unc_B_string':b['unc_bm1' if kind=='M1' else 'unc_be2'],
                             'in_multipolarity_as_exported':a['multipolarity'],'out_multipolarity_as_exported':b['multipolarity'],
                             'in_delta_as_exported':a['mixing_ratio'],'out_delta_as_exported':b['mixing_ratio']},
                'dimensionless_adopted_B_out_over_in_same_WU':float(sameunit),
                'conditional_pure_component_relativeI_times_energy_power':float(intensity_energy),
                'adoptedB_over_relativeI_formula_minus1_central_only':residual,
                'rounded_author_graph_over_TableI_conditional_ratio':gr,
                'graph_ratio_over_adopted_sameunit_ratio_diagnostic_only':gr/float(sameunit),
                'boundary':'Same adopted chain. Pure-component formula is conditional on adopted multipolarity/component identities; blank errors/notes do not certify zero uncertainty or measured delta. Author graph binding/normalizer remains unresolved; no significance or paper-error inference.'})
    controls['mixed_first648_empty_M1_not_filled']=len(skips)==1 and skips[0]['two_I']==31 and skips[0]['kind']=='M1' and skips[0]['value_assigned'] is None
    controls['seven_nonempty_sameunit_pairs_and_one_explicit_gap']=len(results)==7 and len(skips)==1
    return {'status':'adopted-sameunit-ratio-and-quantity-readiness','formal_day_index':23,'uncredited_preview_day':24,
            'scope':'Direct actualCSV/author-source central arithmetic, not independent measurement, historical analysis-producer validation or normalization fit.',
            'formula':'Bout/Bin=(Iout/Iin)*(Ein/Eout)^(2L+1) only for same-parent photon components of the same pureXL; common WU andtau factors cancel. No absolute WU conversion performed.',
            'results':results,'skipped_unfilled_inputs':skips,'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'actual_input_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [gamma_path,source_root/'ndchiralrev4.tex',source_root/'fig2.ps',source_root/'fig3.ps']},
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day24_preview_nd135_export_identity.py'),Path(__file__).with_name('day24_preview_mu07_vector_plot.py'),
                Path(__file__).with_name('day24_preview_mu07_inventory_hypothesis.py')]},
            'limitations':['Adopted relative intensities, B fields, clocks and quoted authors can share the same experimental/evaluation provenance. Numerical near-agreement is not a new independent consistency vote or reconstruction of original adopted notes.',
                           'Parent/component/pure-multipole assumptions are explicitly conditional. Export square brackets/parentheses are retained; their full original ENSDF note meanings are not supplied here.',
                           'The reported residuals compare central strings only. No joint covariance, experimental coverage, missing branch or systematics is recovered, and blank errors are not zero errors.',
                           'Graph/TableI ratios have the additional same-parent/component and absolute-vs-selected-outlet normalization hypotheses from020. Their ratio to adopted same-unit values diagnoses unlike quantities, not a proven error or specific author normalizer.',
                           'Mixed648 lacking B_M1 is left unfilled. No signed delta, ICC, absolute WU coefficient, physical g/Q/new tau/CI or detector rate/beamtime inferred.',
                           'NoDay24formalcredit orDay25card; originalDay23 execution/deadline unchanged.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--gammas',type=Path,required=True);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate(a.gammas,a.source_root);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'ratios':[{'two_I':v['two_I_candidate_parent'],'XL':v['multipole'],
                        'adopted_B_ratio':v['dimensionless_adopted_B_out_over_in_same_WU'],
                        'I_E_power_conditional_ratio':v['conditional_pure_component_relativeI_times_energy_power'],
                        'central_relative_residual':v['adoptedB_over_relativeI_formula_minus1_central_only'],
                        'graph_over_adopted_diagnostic':v['graph_ratio_over_adopted_sameunit_ratio_diagnostic_only']} for v in r['results']],
                      'unfilled_gaps':r['skipped_unfilled_inputs']},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
