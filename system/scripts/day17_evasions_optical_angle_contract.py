#!/usr/bin/env python3
"""Actual stored-angle convention checks, without a recoil or lifetime refit."""
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


def stats(x):
    return {'mean_signed_degrees':float(x.mean()),'rms_degrees':float(np.sqrt(np.mean(x*x))),
            'absolute_quantiles_degrees':dict(zip(['0','50','90','99','100'],
                    map(float,np.quantile(np.abs(x),[0,.5,.9,.99,1]))))}


def main():
    cp = RUN/'evasions2023-optical-angle-contract.json'
    c = json.loads(cp.read_text())
    source = ROOT/'tmp/day17-fougeres2023/producer-source'
    manifest = json.loads((ROOT/c['source_manifest']).read_text())
    assert all(sha(source/x['path'])==x['sha256'] for x in manifest['files'])
    assert sha(ROOT/c['data'])==c['data_sha256']
    f=R.TFile.Open(str(ROOT/c['data']),'READ')
    values=R.RDataFrame(f.Get('TreeMaster')).AsNumpy(['Brho','ThetaLdeg','Theta','Phi'])
    values={k:np.asarray(v,dtype=float) for k,v in values.items()}
    assert all(np.isfinite(v).all() for v in values.values())
    keep=(values['Brho']>0)&(values['ThetaLdeg']>=0)&(values['ThetaLdeg']<12)
    assert int(keep.sum())==c['base_events']
    a,b=values['Theta'][keep]*.001,values['Phi'][keep]*.001
    stored=values['ThetaLdeg'][keep]
    z=np.cos(a)*np.cos(b)
    outofplane=np.rad2deg(np.arccos(np.clip(z,-1,1)))
    projected=np.rad2deg(np.arctan(np.hypot(np.tan(a),np.tan(b))))
    results={}
    for label,pred in [('Eq3p5_out_of_horizontal_plane',outofplane),('two_projected_slopes',projected)]:
        error=stored-pred
        results[label]={**stats(error),'fraction_within_predeclared_tolerance':float(np.mean(np.abs(error)<c['tolerance_degrees']))}
    x=np.cos(b)*np.sin(a);y=np.sin(b)
    norm=x*x+y*y+z*z
    assert np.max(np.abs(norm-1))<1e-14
    pplus=np.arctan2(y,x);pminus=np.arctan2(y,-x)
    delta=np.rad2deg(np.arctan2(np.sin(pminus-pplus),np.cos(pminus-pplus)))
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'base_events':int(keep.sum()),'convention_comparisons':results,
         'source_two_theta_conventions_difference':stats(outofplane-projected),
         'two_x_reflected_direction_controls':{'max_unit_norm_residual':float(np.max(np.abs(norm-1))),
              'theta_is_exactly_unchanged_by_reflection':True,'azimuth_wrapped_difference':stats(delta),
              'boundary':'mathematical candidate frames on actual fields; theta cannot choose correct relative handedness'},
         'no_angle_scale_offset_fit_or_extra_formula_search':True,
         'not_original_phi_or_recoil_response_certification':True,
         'source34_and_data_hashes_preserved':True,'no_new_experimental_tau_branch_or_CI':True,'ok':True}
    assert sha(ROOT/c['data'])==c['data_sha256']
    (RUN/'evasions2023-optical-angle-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
