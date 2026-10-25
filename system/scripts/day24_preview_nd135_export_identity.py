#!/usr/bin/env python3
"""135Nd export identity/clock/unit audit, uncredited preview; no data refit."""
import argparse
import collections
import csv
import hashlib
import io
import json
import math
from pathlib import Path


def read_csv(path):
    raw=list(csv.reader(io.StringIO(path.read_text())))
    header=raw[0];rows=[];blank=0
    counts=collections.Counter(header)
    names=[name if counts[name]==1 else f'{name}__column_{i}' for i,name in enumerate(header)]
    for line,row in enumerate(raw[1:],2):
        if not any(row):
            blank+=1
            continue
        if len(row)!=len(header):
            raise ValueError(f'Nonempty malformed CSV row{line}')
        rows.append({'csv_line':line,'fields':dict(zip(names,row)),'raw_values':row})
    return header,rows,blank


def calculate(gamma_path,level_path,guide_path):
    gh,gr,gb=read_csv(gamma_path);lh,lr,lb=read_csv(level_path)
    levels={r['fields']['idx']:r for r in lr}
    gammas={(r['fields']['start_level_idx'],r['fields']['end_level_idx'],r['fields']['gamma_idx']):r for r in gr}
    controls={
        'all_nonempty_csv_rows_strict_width':True,
        'duplicate_level_unc_hl_positions_preserved':[i for i,k in enumerate(lh) if k=='unc_hl']==[12,15],
        'unique_level_and_gamma_snapshot_identifiers':len(levels)==len(lr) and len(gammas)==len(gr),
        'all_rows_target_nuclide':all(r['fields']['z']=='60' and r['fields']['n']=='75' and r['fields']['symbol']=='Nd' for r in gr+lr),
    }
    joins=[];all_join=True
    for row in gr:
        g=row['fields'];s=levels[g['start_level_idx']]['fields'];e=levels[g['end_level_idx']]['fields']
        good=(g['start_level_energy']==s['energy'] and g['end_level_energy']==e['energy']
              and g['start_level_jp']==s['jp'] and g['end_level_jp']==e['jp'])
        all_join=all_join and good
        residual=float(g['start_level_energy'])-float(g['end_level_energy'])-float(g['energy'])
        joins.append({'snapshot_id':[g['start_level_idx'],g['end_level_idx'],g['gamma_idx']],
                      'field_join_exact':good,'printed_energy_centre_closure_keV':residual})
    controls['all_snapshot_endpoint_energy_spin_joins_match']=all_join
    target_ids=[('59','52','2'),('60','52','1'),('66','60','1'),('66','59','2')]
    target=[gammas[k] for k in target_ids]
    controls['648_and_649_are_distinct_snapshot_outlets']=target[0]['fields']['energy']=='648' and target[1]['fields']['energy']=='649.2' and target[0]['fields']['start_level_jp']=='(31/2-)' and target[1]['fields']['start_level_jp']=='(33/2-)'
    controls['590_and_591_are_distinct_final_spins']=target[2]['fields']['energy']=='590' and target[3]['fields']['energy']=='591' and target[2]['fields']['end_level_jp']=='(33/2-)' and target[3]['fields']['end_level_jp']=='(31/2-)'
    controls['nearenergy_identity_cannot_merge_deltaI1_deltaI2']=target[2]['fields']['end_level_idx']!=target[3]['fields']['end_level_idx']
    clocks=[];clock_error=0.
    # MU07 actual Table I central values, not fitted and not independent data.
    parents=[('A','55',31,.75),('A','60',33,.44),('A','63',35,.28),('A','68',37,.23),('A','72',39,.22),
             ('B','59',31,1.46),('B','61',33,.87),('B','66',35,.64),('B','69',37,.48),('B','73',39,.24)]
    for band,index,two_spin,mu_tau in parents:
        row=levels[index];s=row['fields']
        if s['unit_hl']!='ps':
            raise ValueError('Explicit target clock is not ps')
        half=float(s['half_life']);seconds=float(s['half_life_sec'])
        clock_error=max(clock_error,abs(half-seconds*1e12))
        tau=half/math.log(2)
        clocks.append({'declared_candidate_band':band,'two_I':two_spin,'level_snapshot_idx':index,
                       'level_energy_keV_string':s['energy'],'jp_string':s['jp'],
                       'half_life_ps_string':s['half_life'],'half_life_seconds_string':s['half_life_sec'],
                       'raw_unc_hl_column12':s['unc_hl__column_12'],'raw_unc_hl_seconds_column15':s['unc_hl__column_15'],
                       'derived_mean_tau_ps':tau,'MU07_printed_mean_tau_ps_centre':mu_tau,
                       'central_arithmetic_difference_ps':tau-mu_tau,
                       'boundary':'Half-to-mean arithmetic on an adopted evaluation chain, not a new measurement, CI or independent validation. Candidate family identity follows the earlier scheme and must not bind MU07 graph components automatically.'})
    controls['half_life_ps_and_seconds_units_consistent']=clock_error<1e-12
    controls['half_life_not_used_as_mean_tau']=all(abs(float(r['half_life_ps_string'])-r['derived_mean_tau_ps'])>.01 for r in clocks)
    energy_pairs=[]
    for two_spin in [31,33,35,37,39]:
        pa=next(p for p in clocks if p['declared_candidate_band']=='A' and p['two_I']==two_spin)
        pb=next(p for p in clocks if p['declared_candidate_band']=='B' and p['two_I']==two_spin)
        energy_pairs.append({'two_I':two_spin,'A_idx':pa['level_snapshot_idx'],'B_idx':pb['level_snapshot_idx'],
                             'A_E_keV_string':pa['level_energy_keV_string'],'B_E_keV_string':pb['level_energy_keV_string'],
                             'central_B_minus_A_keV':float(pb['level_energy_keV_string'])-float(pa['level_energy_keV_string']),
                             'boundary':'Declared historical family and same-spin pairing, export centre arithmetic only, no new measured splitting/CI or static-chirality threshold.'})
    controls['near_4007_levels_are_not_same_spin_partners']=levels['59']['fields']['jp']!=levels['60']['fields']['jp']
    guide=guide_path.read_text()
    controls['official_guide_identifies_RTPW_as_Weisskopf_units']='RTPW stands for Reduced Electric (Magnetic) Transition Probabilities in Weisskopf Units' in guide
    controls['API_mixing_ratio_uncertainty_not_filled']=gammas[('59','56','0')]['fields']['mixing_ratio']=='0.14' and gammas[('59','56','0')]['fields']['unc_mr']==''
    cutoffs=sorted({g['fields']['ensdf_publication_cut-off'] for g in gr})
    dates=sorted({g['fields']['Extraction_date'] for g in gr})
    controls['evaluation_cutoff_and_extraction_date_retained_separately']=len(cutoffs)==1 and len(dates)==1 and cutoffs!=dates
    return {'status':'official-export-identity-and-readiness-only','formal_day_index':23,'uncredited_preview_day':24,
            'source_snapshots':{str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in [gamma_path,level_path,guide_path]},
            'row_counts':{'gammas_nonempty':len(gr),'levels_nonempty':len(lr),'gammas_ignored_fully_blank':gb,'levels_ignored_fully_blank':lb},
            'gamma_headers':gh,'level_headers_with_duplicate_positions':list(enumerate(lh)),
            'evaluation_cutoffs':cutoffs,'extraction_dates':dates,
            'evaluation_authors':sorted({g['fields']['ensdf_authors'] for g in gr}),
            'close_energy_outlets_raw':target,'candidate_parent_clocks':clocks,
            'declared_candidate_same_spin_level_pairs':energy_pairs,
            'specific_226_snapshot_outlet_raw':gammas[('59','56','0')],
            'selected_parent_all_outlets_raw':{idx:[r for r in gr if r['fields']['start_level_idx']==idx] for idx in ['59','61','66','69','73']},
            'all_endpoint_joins':joins,'clock_unit_error_ps':clock_error,
            'controls':controls,'all_controls_pass':all(controls.values()),
            'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'limitations':['Snapshot idx is local to these exact files. Near energy is not a line identity, and latest adopted endpoints do not independently establish the 2007 plotted component mapping.',
                           'API b_e2/b_m1 are Weisskopf-unit fields per guide, not raw e2b2/muN2. No unverified numerical conversion is applied.',
                           'The positive literal mixing_ratio0.14 lacks uncertainty and original adopted notes/phase convention here; it is not a newly measured signed delta or a restored225.8 polarization/exclusion result.',
                           'Relative intensity100 is a parent normalization, not an absolute photon rate or proof no omitted branch. No complete gamma/IC budget is certified.',
                           'Original adopted reference notes and full experimental response/covariance remain absent; export-derived tau and strength fields reuse evaluations, not independent acquisitions.',
                           'No real joint confidence interval, Q, g, polarization prediction, count rate or beamtime calculated. Raw archive deferred; public snapshots remain tmp staging.']}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--gammas',type=Path,required=True);p.add_argument('--levels',type=Path,required=True)
    p.add_argument('--guide',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate(a.gammas,a.levels,a.guide);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),'rows':r['row_counts'],
                      'cutoffs':r['evaluation_cutoffs'],'dates':r['extraction_dates'],
                      'target_energies':[g['fields']['energy'] for g in r['close_energy_outlets_raw']],
                      'mean_tau_centre_arithmetic_max_difference_ps':max(abs(v['central_arithmetic_difference_ps']) for v in r['candidate_parent_clocks'])},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
