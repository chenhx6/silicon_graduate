#!/usr/bin/env python3
"""Reproduce one bounded MODEL packet; never treat it as experimental input."""
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import ROOT as pyroot

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
SOURCE=ROOT/'tmp/day17-kirsebom2016/simdsam-source'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    contract=json.loads((RUN/'simdsam-event-packet-contract.json').read_text())
    manifest=json.loads((RUN/'simdsam-full-source-manifest.json').read_text())
    expected=json.loads((RUN/'simdsam-event-packet-schema.json').read_text())
    assert all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files'])
    work=Path(tempfile.mkdtemp(prefix='packet-replay-',dir=ROOT/'tmp/day17-kirsebom2016'))
    for name in ['source','ROOTanal','RootFiles','SimOutput']:(work/name).mkdir()
    for row in manifest['files']:
        if row['path'].startswith('data/'):
            p=work/row['path'];p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes((SOURCE/row['path']).read_bytes())
    oldcard=(RUN/'simdsam-event-packet-MODEL-job.CARD').read_text()
    oldbase=str((ROOT/contract['workdir']).resolve())
    card=oldcard.replace(oldbase,str(work))
    assert card.replace(str(work),oldbase)==oldcard
    job=work/'MODEL-job.CARD';job.write_text(card)
    frozen=json.loads((RUN/'simdsam-event-packet-replay-result.json').read_text())
    assert sha(RUN/'simdsam-event-packet-main.cc')==frozen['fixture_sha256']
    command=list(frozen['commands'][0]['command'])
    exe=work/'simdsam-packet'
    command[command.index('-o')+1]=str(exe)
    receipt={'MODEL_only':True,'script_sha256':sha(__file__),'workdir':str(work),
             'card_sha256':sha(job),'N_detected':64,'N_array':10000,'commands':[]}

    def run(cmd,**kwargs):
        p=subprocess.run(cmd,capture_output=True,text=True,**kwargs)
        receipt['commands'].append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        (RUN/'simdsam-event-packet-strict-replay.json').write_text(json.dumps(receipt,indent=2)+'\n')
        assert p.returncode==0,p.stderr
        return p

    run(command,cwd=ROOT)
    env=dict(os.environ);env['ROOT_HIST']='0';env['TMPDIR']=str(work)
    p=run([str(exe),'0',str(job)],cwd=work/'source',env=env,input='',timeout=180)
    assert 'MODEL_RNG,TRandom3,4357' in p.stdout
    assert 'MODEL_BOOKKEEP,6820,64,64' in p.stdout
    ascii_file=work/'SimOutput/MODEL-alpha-gamma.dat'
    assert sha(ascii_file)==expected['ASCII_sha256']
    f=pyroot.TFile.Open(str(work/'SimOutput/MODEL-alpha-gamma.root'),'READ')
    assert f and not f.IsZombie()
    tree=f.Get('dsamTree');assert int(tree.GetEntries())==64
    data=list(csv.DictReader((RUN/'simdsam-event-packet-MODEL-joint.csv').open()))
    assert len(data)==64
    for i,row in enumerate(data):
        tree.GetEntry(i)
        assert float(tree.EPART)==float(row['EPART_keV_Float32'])
        assert float(tree.EGAMMA)==float(row['EGAMMA_keV_Float32'])
    h=f.Get('EQa')
    assert h.GetEntries()==h.Integral(0,h.GetNbinsX()+1,0,h.GetNbinsY()+1)==6820
    f.Close()
    receipt.update({'ASCII_sha256':sha(ascii_file),'ROOT_values_exactly_equal':True,
                    'bookkeeping_allbins_equal':True,'all52hashes_preserved':all(sha(SOURCE/x['path'])==x['sha256'] for x in manifest['files']),
                    'knownphysics_and_runtime_warning_boundaries_preserved':True,
                    'original_experimental_data_or_CI_recovered':False,'ok':True})
    (RUN/'simdsam-event-packet-strict-replay.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('64 MODEL pairs and 6820-proposal bookkeeping reproduced')


if __name__=='__main__':
    main()
