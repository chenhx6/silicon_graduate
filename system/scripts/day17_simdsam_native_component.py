#!/usr/bin/env python3
"""Replay original-expression SimDSAM controls with the declared syntax adapter."""
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
SOURCE=ROOT/'tmp/day17-kirsebom2016/simdsam-source'
WORK=ROOT/'tmp/day17-kirsebom2016/native-component'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    manifest=json.loads((RUN/'simdsam-full-source-manifest.json').read_text())
    assert manifest['commit']=='21809a67ea9f3b0514cc57908659463f29b1e1ab'
    assert all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files'])
    fixture=RUN/'simdsam-native-component.cc'
    prior=json.loads((RUN/'simdsam-native-component-result.json').read_text())
    assert sha(fixture)==prior['fixture_sha256']
    flags=shlex.split(subprocess.check_output(['root-config','--cflags'],text=True))
    libs=shlex.split(subprocess.check_output(['root-config','--libs'],text=True))
    command=['c++',*flags,'-std=gnu++17','-O2',str(fixture),'-o',str(WORK/'component-replay'),*libs,'-lMathMore']
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    receipt={'fixture_sha256':sha(fixture),'script_sha256':sha(__file__),
             'compile':{'command':command,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}}
    assert p.returncode==0,p.stderr
    env=dict(os.environ);env['TMPDIR']=str(WORK);env['ROOT_HIST']='0'
    p=subprocess.run([str(WORK/'component-replay')],cwd=SOURCE/'source',env=env,
                     capture_output=True,text=True,timeout=180)
    receipt['run']={'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    assert p.returncode==0,p.stderr
    prefixes=('BEAM_RADIAL,','MIXTURE,','CLOCK_CONTROL,','ALPHA_DETECTION,','ALPHA_LAYERS,')
    selected=lambda text:[x for x in text.splitlines() if x.startswith(prefixes)]
    assert selected(p.stdout)==selected(prior['commands'][-1]['stdout'])
    receipt['all_physics_output_lines_equal']=True
    receipt['all52source_data_hashes_preserved']=all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files'])
    receipt['original_physical_discrepancies_retained_not_corrected']=True
    receipt['paper_fit_or_CI_recovered']=False
    (RUN/'simdsam-native-component-replay.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('original-expression controls replayed; known scope failures retained')


if __name__=='__main__':
    main()
