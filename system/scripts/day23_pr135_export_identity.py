#!/usr/bin/env python3
"""Actual legacy135Pr export parent/endpoint/readiness audit, no new fit."""
import argparse
import hashlib
import json
from pathlib import Path

from day24_preview_nd135_export_identity import read_csv


TARGETS=[(('33','13','0'),526.2,1477.9,951.8),
         (('33','10','1'),747.3,1477.9,730.6),
         (('54','33','0'),726.0,2203.9,1477.9),
         (('54','29','1'),813.2,2203.9,1390.8)]


def calculate(gamma_path,level_path):
    gh,gr,gb=read_csv(gamma_path);lh,lr,lb=read_csv(level_path)
    levels={r['fields']['idx']:r for r in lr}
    gamma={(r['fields']['start_level_idx'],r['fields']['end_level_idx'],r['fields']['gamma_idx']):r for r in gr}
    controls={'strict_nonempty_CSV_widths_and_blank_terminators_classified':True,
              'all_rows_target_Pr135':all(r['fields']['z']=='59' and r['fields']['n']=='76' and r['fields']['symbol']=='Pr' for r in gr+lr),
              'unique_snapshot_ids':len(levels)==len(lr) and len(gamma)==len(gr),
              'duplicate_level_unc_hl_columns_retained':[i for i,k in enumerate(lh) if k=='unc_hl']==[12,15]}
    joins=[]
    for row in gr:
        g=row['fields'];a=levels[g['start_level_idx']]['fields'];b=levels[g['end_level_idx']]['fields']
        exact=(g['start_level_energy']==a['energy'] and g['end_level_energy']==b['energy']
               and g['start_level_jp']==a['jp'] and g['end_level_jp']==b['jp'])
        joins.append({'gamma_snapshot_id':[g['start_level_idx'],g['end_level_idx'],g['gamma_idx']],
                      'same_snapshot_level_energy_Jp_join':exact,
                      'reported_gamma_energy_centre_closure_keV':float(a['energy'])-float(b['energy'])-float(g['energy'])})
    controls['all_gamma_endpoints_join_actual_level_rows']=all(r['same_snapshot_level_energy_Jp_join'] for r in joins)
    targets=[]
    for key,new_gamma,new_parent,new_daughter in TARGETS:
        row=gamma[key];g=row['fields']
        targets.append({'legacy_gamma_snapshot_raw':row,'latest_L22_candidate_values':{
                            'gamma_energy_keV':new_gamma,'parent_energy_keV':new_parent,'daughter_energy_keV':new_daughter},
                        'legacy_minus_new_gamma_centre_keV':float(g['energy'])-new_gamma,
                        'modern_energy_plus_minus_point7_filter_would_select':abs(float(g['energy'])-new_gamma)<=.7,
                        'same_parent_endpoint_candidate_crosswalk_not_event_identity':True,
                        'boundary':'Legacy2008 evaluation and2022 published values remain separately frozen. No significance, energy correction or proof the two campaigns select identical events/components.'})
    controls['endpoint_crosswalk_keeps_legacy814_even_if_energy_filter_misses']=targets[3]['legacy_gamma_snapshot_raw']['fields']['energy']=='814' and not targets[3]['modern_energy_plus_minus_point7_filter_would_select']
    controls['legacy527_not_erased_by_modern526_energy_window']=targets[0]['legacy_gamma_snapshot_raw']['fields']['energy']=='527' and not targets[0]['modern_energy_plus_minus_point7_filter_would_select']
    mothers={idx:levels[idx] for idx in ['33','54']}
    lower={idx:levels[idx] for idx in ['10','29']}
    controls['disputed_target_parent_clocks_really_empty']=all(v['fields']['half_life']=='' and v['fields']['half_life_sec']=='' for v in mothers.values())
    controls['lower_yrast_clocks_not_transferred_to_target_parent']=all(v['fields']['half_life']!='' and v['fields']['unit_hl']=='ps' for v in lower.values()) and not(set(mothers)&set(lower))
    controls['selected_delta_and_strength_gaps_not_filled']=all(
        t['legacy_gamma_snapshot_raw']['fields'][f]=='' for t in targets for f in ['mixing_ratio','b_m1','b_e2','tot_conv_coeff'])
    controls['D_rank_labels_not_promoted_to_M1_or_delta']=targets[1]['legacy_gamma_snapshot_raw']['fields']['multipolarity']=='D' and targets[3]['legacy_gamma_snapshot_raw']['fields']['multipolarity']=='D'
    controls['P_and_Rac_are_not_export_observation_columns']='P' not in gh and 'Rac' not in gh
    cutoff=sorted({r['fields']['ensdf_publication_cut-off'] for r in gr});date=sorted({r['fields']['Extraction_date'] for r in gr})
    controls['evaluation_cutoff_and_extraction_roles_distinct']=cutoff!=date
    upstream=[gamma[('44','33','0')],gamma[('65','54','1')]]
    controls['upstream_old450_and796_flow_bound_by_ID']=upstream[0]['fields']['energy']=='450' and upstream[1]['fields']['energy']=='796'
    clock_consistency=max(abs(float(v['fields']['half_life'])-float(v['fields']['half_life_sec'])*1e12) for v in lower.values())
    controls['lower_clock_ps_seconds_field_units_consistent']=clock_consistency<1e-12
    ri747=float(gamma[('33','10','1')]['fields']['relative_intensity'])/float(gamma[('33','13','0')]['fields']['relative_intensity'])
    ri813=float(gamma[('54','29','1')]['fields']['relative_intensity'])/float(gamma[('54','33','0')]['fields']['relative_intensity'])
    return {'status':'actual-legacy-Pr135-endpoint-clock-readiness','formal_day_index':23,
            'scope':'Official export field identities/versions only; no independent gamma acquisition or2015/2022 analysis reconstruction.',
            'actual_input_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [gamma_path,level_path]},
            'nonempty_row_counts':{'gammas':len(gr),'levels':len(lr)},'fully_blank_tail_records':{'gammas':gb,'levels':lb},
            'gamma_headers':gh,'duplicate_level_headers_with_positions':list(enumerate(lh)),
            'evaluation_cutoffs':cutoff,'extraction_dates':date,'evaluation_authors':sorted({r['fields']['ensdf_authors'] for r in gr}),
            'target_endpoint_crosswalks':targets,'disputed_mothers_raw':mothers,'different_lower_yrast_clock_rows_raw':lower,
            'target_mother_mean_tau_value_assigned':None,'absolute_target_strength_assigned':None,
            'legacy_upstream_gate_rows_raw':upstream,
            'parent_normalized_relative_I_quotient_centres':{'legacy747p1_over527':ri747,'new_L22_747p3_over526p2':9.4/.4,
                'legacy814_over726':ri813,'new_L22_813p2_over726':6.4/3.7,
                'boundary':'Different version/acquisition/adopted intensity chains and large marginal errors; no joint covariance, significance or independent root vote supplied.'},
            'all_snapshot_endpoint_joins':joins,'lower_clock_unit_error_ps':clock_consistency,
            'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day24_preview_nd135_export_identity.py')]},
            'limitations':['The export publicationcutoff is2008, before the2015/2022 wobbling controversy. Current retrieval is not a new evaluation or evidence against later P/Rac/delta data.',
                           'Snapshot IDs are local. Cross-version endpoint/Jp/energy candidates do not establish identical events, original placement notes or a common error/response model.',
                           'Disputed parent33/54 clocks and B/mixing fields are empty. Lower15/2 and19/2 yrast half-lives are different states and cannot be substituted for target mean tau.',
                           'A D multipolarity label gives a dipole-rank annotation, not a newly certified M1, zero mixing ratio or polarization sign. Empty fields are unknown, not measured zeros.',
                           'The coarse legacy527/814 energies explain why an energy-only filter misses lines; no original/new gamma energy is silently corrected or merged.',
                           'RelativeI quotients cancel one parent normalization, not missing branches, absolute yields, component purity or cross-campaign covariance. No new delta/Q/g/tau CI/rate/beamtime produced.',
                           'Public snapshots remain tmp staging, formal raw archive deferred. ExistingDay23 andonlyDay24uncreditedpreview/noDay25+ boundaries remain.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--gammas',type=Path,required=True);p.add_argument('--levels',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate(a.gammas,a.levels);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'rows':r['nonempty_row_counts'],'cutoff':r['evaluation_cutoffs'],'extraction':r['extraction_dates'],
                      'legacy_target_energies':[v['legacy_gamma_snapshot_raw']['fields']['energy'] for v in r['target_endpoint_crosswalks']],
                      'target_parent_clocks':[v['fields']['half_life'] for v in r['disputed_mothers_raw'].values()],
                      'lower_different_state_clocks':[v['fields']['half_life'] for v in r['different_lower_yrast_clock_rows_raw'].values()]},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
