#!/usr/bin/env python3
"""Reproduce a pinned historic-method component and conditional matching algebra."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import subprocess
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
TMP=ROOT/'tmp/day17-root522'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    c=json.loads((RUN/'root522-exercise-contract.json').read_text())
    assert c['identity']=='ROOT522-BACKGROUND-ERROR-CONTRACT-01'
    assert sha(ROOT/c['source_manifest'])==c['source_manifest_sha256']
    source=json.loads((ROOT/c['source_manifest']).read_text())
    for row in source['rows']:
        assert sha(TMP/Path(row['path']).name)==row['sha256']
    cpp=ROOT/c['component']
    assert sha(cpp)==c['component_sha256']
    flags=subprocess.check_output(['/opt/root/bin/root-config','--cflags','--libs'],text=True).split()
    cmd=['g++',str(cpp),'-o',str(TMP/'legacy-component-delivery'),*flags]
    build=subprocess.run(cmd,capture_output=True,text=True)
    receipt={'at':datetime.now(timezone.utc).isoformat(),'command':cmd,'exit_code':build.returncode,'stdout':build.stdout,'stderr':build.stderr}
    (RUN/'root522-delivery-build.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    assert build.returncode==0
    run=subprocess.run([str(TMP/'legacy-component-delivery')],capture_output=True,text=True)
    receipt={'command':[str(TMP/'legacy-component-delivery')],'exit_code':run.returncode,'stderr':run.stderr}
    (RUN/'root522-delivery-run.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    assert run.returncode==0
    native=json.loads(run.stdout)
    (RUN/'root522-delivery-result.json').write_text(json.dumps(native,ensure_ascii=False,indent=2)+'\n')
    no,stored=native['cases']
    checks={'stored_smooth_content_changes':stored['before_content']!=stored['after_smooth_content'],
            'stored_smooth_errors_unchanged':stored['before_error']==stored['after_smooth_error'],
            'stored_background_errors_zero':all(x==0 for x in stored['background_error']),
            'stored_background_content_nonzero':any(x>0 for x in stored['background_content']),
            'no_stored_background_fallback_sqrt':all(abs(e*e-y)<1e-12 for e,y in zip(no['background_error'],no['background_content'])),
            'same_background_content_across_error_buffer_cases':no['background_content']==stored['background_content']}
    d=np.array(c['declared_matching_data'],dtype=float)
    b=np.array(c['declared_matching_background'],dtype=float)
    k=c['matching_index'];a=d[k]/b[k];n=len(d)
    jd=np.eye(n);jb=-a*np.eye(n)
    jd[:,k]-=b/b[k]
    jb[:,k]+=a*b/b[k]
    jac=np.concatenate([jd,jb],axis=1)
    cov=jac@np.diag(np.concatenate([d,b]))@jac.T
    fixed=np.diag(d+a*a*b)
    residual=d-a*b
    assert residual[k]==0 and max(abs(x) for x in cov[k,:])<1e-15
    assert np.linalg.eigvalsh(cov).min()>-1e-12
    checks['matched_bin_joint_variance_zero_but_fixed_scale_diagonal_positive']=cov[k,k]==0 and fixed[k,k]>0
    checks={key:bool(value) for key,value in checks.items()}
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(RUN/'root522-exercise-contract.json'),'source_commit':source['commit'],
         'component_helper_ROOT':native['ROOT_helper_version'],'checks':checks,
         'matching_algebra_declared_design':{'D':d.tolist(),'B':b.tolist(),'k':k,'estimated_a':a,
              'residual':residual.tolist(),'Jacobian':jac.tolist(),'conditional_joint_covariance':cov.tolist(),
              'fixed_a_Add_diagonal_variance':fixed.diagonal().tolist(),
              'boundary':'independent primitive Poisson design, unsmoothed B, single-bin matching; no source histogram or CI'},
         'source_API_does_not_propagate_smoothing_or_matching_covariance':True,
         'not_full_ROOT522_binary_or_original_job':True,
         'no_experimental_Bp_tau_or_CI_recomputed':True,'ok':all(checks.values())}
    (RUN/'root522-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'ok':out['ok'],'checks':checks,'matching_cov':cov.tolist(),'fixed_diagonal':fixed.diagonal().tolist()},indent=2))
    return 0 if out['ok'] else 1


if __name__=='__main__':
    raise SystemExit(main())
