#!/usr/bin/env python3
"""Replay real compiled Mg/Au input versus the frozen public table reader."""
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
SOURCE=ROOT/'tmp/day17-kirsebom2016/simdsam-source'
WORK=ROOT/'tmp/day17-kirsebom2016/native-component'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    frozen=json.loads((RUN/'forster1976-public-table-component-result.json').read_text())
    assert sha(RUN/'forster1976-Mg-Au-frozen.csv')==frozen['frozen_data_sha256']
    assert sha(RUN/'forster1976-public-table-component.cc')==frozen['fixture_sha256']
    manifest=json.loads((RUN/'simdsam-full-source-manifest.json').read_text())
    assert all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files'])
    command=list(frozen['commands'][0]['command'])
    exe=WORK/'forster-reader-replay'
    command[command.index('-o')+1]=str(exe)
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    receipt={'script_sha256':sha(__file__),'compile':{'command':command,'exit_code':p.returncode,'stderr':p.stderr},'runs':[]}
    assert p.returncode==0,p.stderr
    env=dict(os.environ);env['ROOT_HIST']='0';env['TMPDIR']=str(WORK)
    data=list(csv.DictReader((RUN/'forster1976-Mg-Au-frozen.csv').open()))
    for old in frozen['commands'][1:]:
        mode=old['command'][-1]
        p=subprocess.run([str(exe),mode],cwd=SOURCE/'source',env=env,
                         input=frozen['input_MeV_u'],capture_output=True,text=True,timeout=60)
        assert p.returncode==0,p.stderr
        lines=lambda text:[x for x in text.splitlines() if x.startswith('TABLE_VALUE,')]
        assert lines(p.stdout)==lines(old['stdout']) and len(lines(p.stdout))==len(data)==10
        receipt['runs'].append({'mode':mode,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    receipt['all52hashes_preserved']=all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files'])
    receipt['reader_values_exactly_replayed']=True
    receipt['new_independent_calibration_or_fit']=False
    (RUN/'forster1976-reader-replay.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('Forster compiled-input/public-reader comparison replayed')


if __name__=='__main__':
    main()
