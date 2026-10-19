#!/usr/bin/env python3
"""Audit actual archived producer contracts and public derived events, no fit repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import tempfile
import ROOT

ROOTDIR=Path(__file__).resolve().parents[2]
RUN=ROOTDIR/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    c=json.loads((RUN/'evasions2023-exercise-contract.json').read_text())
    assert c['identity']=='EVASIONS-RELEASE-NATIVE-READINESS-01'
    assert sha(ROOTDIR/c['source_manifest'])==c['source_manifest_sha256']
    m=json.loads((ROOTDIR/c['source_manifest']).read_text())
    src=ROOTDIR/c['source_dir']
    assert all(sha(src/x['path'])==x['sha256'] for x in m['files'])
    work=Path(tempfile.mkdtemp(prefix='native-contract-',dir=src.parent))
    for item in m['files']:
        target=work/item['path'];target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(src/item['path'],target)
    commands=[]
    def run(cmd,timeout=90):
        p=subprocess.run(cmd,cwd=work,capture_output=True,text=True,timeout=timeout)
        commands.append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        (RUN/'evasions2023-contract-native-commands.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'workdir':str(work.relative_to(ROOTDIR)),'commands':commands},ensure_ascii=False,indent=2)+'\n')
        return p
    initial=run(['make','-j2'])
    assert initial.returncode!=0 and 'No such file or directory' in initial.stderr
    (work/'lib').mkdir()
    build=run(['make','-j2'])
    assert build.returncode==0
    no=run(['./EVASIONSsim','0','0','0','0','0'],timeout=15)
    assert no.returncode==1 and 'EVASIONS finished' in no.stdout
    cpp=ROOTDIR/c['native_component'];assert sha(cpp)==c['native_component_sha256']
    flags=subprocess.check_output(['/opt/root/bin/root-config','--cflags','--glibs'],text=True).split()
    compile_result=run(['g++',str(cpp),'-I'+str(work),'lib/kinematics.o','lib/Tools.o','lib/Extraction_SRIM_stopping_powers.o','-o','component-contract',*flags,'-lGeom','-lEve','-lRGL'])
    assert compile_result.returncode==0
    loader=run(['./component-contract','loader'],timeout=3)
    kin=run(['./component-contract','vamos'],timeout=3)
    assert loader.returncode==kin.returncode==0
    ld=json.loads(loader.stdout);kd=json.loads(kin.stdout)
    assert ld['caller_n']==-123 and ld['first_energy']==999 and ld['first_electronic']==0
    assert kd['caller_beta']==.123456789
    data=src/'data/data.root';assert sha(data)==c['public_data_sha256']
    ROOT.gROOT.SetBatch(True)
    d=ROOT.RDataFrame('TreeMaster',str(data))
    observed={'entries':int(d.Count().GetValue()),'nbTrack_max':int(d.Max('nbTrack').GetValue()),
              'positive_Si_dE':int(d.Filter('Si_dE>0').Count().GetValue())}
    assert observed=={'entries':c['expected_entries'],'nbTrack_max':c['expected_nbTrack_max'],'positive_Si_dE':c['expected_positive_Si_dE']}
    original_preserved=all(sha(src/x['path'])==x['sha256'] for x in m['files'])
    copy_preserved=all(sha(work/x['path'])==x['sha256'] for x in m['files'])
    assert original_preserved and copy_preserved
    result={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
            'contract_sha256':sha(RUN/'evasions2023-exercise-contract.json'),'release_commit':m['release_commit'],
            'ROOT_version':ROOT.gROOT.GetVersion(),'workdir':str(work.relative_to(ROOTDIR)),
            'original_build_missing_lib_exit':initial.returncode,'build_after_output_directory_exit':build.returncode,
            'original_noanalysis_return':no.returncode,'loader_native':ld,'kinematics_native':kd,
            'actual_public_event_query':observed,'original34_hashes_preserved':original_preserved,
            'copied34_hashes_preserved':copy_preserved,
            'literal_release_not_ready_for_paper_fit':True,'no_original_release_source_patched':True,
            'no_experimental_lifetime_branch_or_CI_recomputed':True,'ok':True}
    (RUN/'evasions2023-exercise-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
