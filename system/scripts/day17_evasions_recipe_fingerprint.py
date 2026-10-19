#!/usr/bin/env python3
"""Actual derived-data fingerprint of a public archived recipe, not raw replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import numpy as np
import ROOT as R

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp = RUN / 'evasions2023-recipe-fingerprint-contract.json'
    c = json.loads(cp.read_text())
    manifest = json.loads((ROOT/c['source_manifest']).read_text())
    source = ROOT/'tmp/day17-fougeres2023/producer-source'
    assert len(manifest['files']) == 34
    assert all(sha(source/x['path']) == x['sha256'] for x in manifest['files'])
    assert sha(ROOT/c['data']) == c['data_sha256']
    file = R.TFile.Open(str(ROOT/c['data']), 'READ')
    tree = file.Get('TreeMaster')
    frame = R.RDataFrame(tree)
    values = frame.Filter('Si_dE>0').AsNumpy(['Si_theta'])['Si_theta'].astype(float)
    theta, number = np.unique(values, return_counts=True)
    r0, step, distance = c['first_strip_center_mm'], c['strip_pitch_mm'], c['Target_SPIDER_mm']
    continuous = (distance*np.tan(np.deg2rad(theta))-r0)/step
    index = np.rint(continuous).astype(int)
    expected = np.rad2deg(np.arctan((r0+step*index)/distance))
    residual = theta-expected
    matched = bool(np.all((index>=0)&(index<16)) and np.max(np.abs(residual))<c['angle_tolerance_degrees'])
    rows = [{'stored_theta_degrees':float(t),'events':int(n),'nearest_recipe_strip_index':int(i),
             'predicted_recipe_theta_degrees':float(e),'stored_minus_recipe_degrees':float(err),
             'implied_Z_mm_if_recipe_index_assumed':float((r0+step*i)/np.tan(np.deg2rad(t)))}
            for t,n,i,e,err in zip(theta,number,index,expected,residual)]
    q = frame.Define('day17_inside_nominal_veto',
                     'int n=0; for(auto e:trackE) if(std::abs(e-6875.f)<=8.f) ++n; return n;')
    track_count = int(q.Sum('day17_inside_nominal_veto').GetValue())
    event_count = int(q.Filter('day17_inside_nominal_veto>0').Count().GetValue())
    out = {'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
           'contract_sha256':sha(cp),'positive_Si_dE_records':len(values),'unique_Si_theta_values':len(theta),
           'recipe_formula':'theta=atan((24+.75+1.5*index)/119.8), index 0..15',
           'actual_angle_rows':rows,'max_abs_angle_residual_degrees':float(np.max(np.abs(residual))),
           'matches_predeclared_recipe_within_float_tolerance':matched,
           'raw_track_energy_6867_to_6883_keV_inclusive':{'tracks':track_count,'events':event_count,
               'boundary':'raw observed energy window; no nuclide/purity/original veto attribution'},
           'cannot_recover_quadrant_raw_amplitude_or_full_PID':True,
           'recipe_compatibility_is_not_independent_geometry_precision_or_original_producer_certification':True,
           'source34_and_data_hashes_unchanged':True,'no_new_experimental_tau_branch_or_CI':True,'ok':True}
    assert sum(x['events'] for x in rows) == len(values)
    assert sha(ROOT/c['data']) == c['data_sha256']
    (RUN/'evasions2023-recipe-fingerprint-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
