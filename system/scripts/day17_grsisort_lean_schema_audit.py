#!/usr/bin/env python3
"""Pinned full Lean consumer on declared ROOT schema fixtures, in batch mode."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import resource
import shlex
import subprocess

ROOT=Path(__file__).resolve().parents[2]
CACHE=ROOT/'tmp/day17-grsisort'
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source=CACHE/'util/LeanAnalyzeComptonMatrices.cxx'
    assert sha(source)=='f76a79440cbe84b4b1fce1a952341b90bf481d09379b86246152b78ae2c001e6'
    build=CACHE/'lean-schema-build';build.mkdir(exist_ok=True)
    flags=shlex.split(subprocess.check_output(['root-config','--cflags','--libs'],text=True))
    generator=build/'generate.cxx'
    generator.write_text(r'''
#include "TFile.h"
#include "TH2D.h"
#include "TROOT.h"
#include "TMath.h"
#include <array>
#include <string>
int main(int argc,char** argv){
 gROOT->SetBatch(kTRUE);bool legacy=std::string(argv[1])=="legacy";
 std::array<const char*,6> oldNames={"XiHist2D_DetDetCoincidenceTheta","XiHist2D_CryCryCoincidenceTheta","XiHist2D_DetDetCoincidenceTheta_Geo","XiHist2D_CryCryCoincidenceTheta_Geo","XiHist2D_DetDetCoincidenceTheta_NonCo","XiHist2D_CryCryCoincidenceTheta_NonCo"};
 std::array<const char*,6> newNames={"xiThetaDet","xiThetaCry","xiThetaDetCount","xiThetaCryCount","xiThetaDetMixed","xiThetaCryMixed"};
 TFile out(argv[2],"RECREATE");
 for(int i=0;i<6;++i){TH2D h((legacy?oldNames:newNames)[i],"declared-schema-fixture",180,0.,180.000001,180,0.,180.000001);
 for(int x=1;x<=180;++x)for(int y=1;y<=180;++y){double mean=i<2?1000.*(1.-.2*TMath::Cos(2*h.GetXaxis()->GetBinCenter(x)*TMath::DegToRad())):(i<4?1.:1000.);h.SetBinContent(x,y,mean);}
 h.Write();}out.Close();return 0;
}
''')
    entry=build/'batch-entry.cxx';entry.write_text('#define main OriginalLeanMain\n#include "'+str(source)+'"\n#undef main\nint main(int argc,char** argv){gROOT->SetBatch(kTRUE);return OriginalLeanMain(argc,argv);}\n')
    inspect=build/'inspect.cxx';inspect.write_text(r'''
#include "TFile.h"
#include "TList.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TROOT.h"
#include <iostream>
#include <iomanip>
int main(int argc,char** argv){gROOT->SetBatch(kTRUE);TFile f(argv[1]);std::cout<<std::setprecision(17);for(const char* n:{"AsymmetryNonCo","AsymmetryBinnedNonCo","AsymmetryBinFoldNonCo","AGATATheory"}){auto* g=dynamic_cast<TGraph*>(f.Get(n));if(g){std::cout<<n<<" points="<<g->GetN();auto* fun=g->GetFunction("fun1");if(fun)std::cout<<" fitA="<<fun->GetParameter(0)<<" fitErr="<<fun->GetParError(0)<<" chi2="<<fun->GetChisquare()<<" ndf="<<fun->GetNDF();std::cout<<"\n";}else std::cout<<n<<" missing\n";}return 0;}
''')
    record={'input_kind':'declared-schema-and-asymmetry-expectations-not-experimental-data','original_source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'commands':[],'scope':'complete original Lean source included unchanged with renamed entry and gROOT batch runtime setting; real ROOT fixture files; no complete GRSISort/GRSIData build or experimental event data'}
    def execute(command,cwd=None,timeout=40):
        def no_core():resource.setrlimit(resource.RLIMIT_CORE,(0,0))
        try:
            z=subprocess.run(command,cwd=cwd,capture_output=True,text=True,timeout=timeout,preexec_fn=no_core)
            row={'command':list(map(str,command)),'cwd':str(cwd) if cwd else str(ROOT),'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr}
        except subprocess.TimeoutExpired as e:
            row={'command':list(map(str,command)),'timeout_seconds':timeout,'stdout':str(e.stdout),'stderr':str(e.stderr)}
        record['commands'].append(row);return row
    for cpp,name,extra in [(generator,'generate',[]),(entry,'lean',['-DHAS_MATHMORE','-lMathMore']),(inspect,'inspect',[])]:
        cmd=['g++','-O1','-I'+str(CACHE/'include'),str(cpp),'-o',str(build/name),*flags,*extra]
        r=execute(cmd);assert r.get('exit_code')==0,r
    cases={}
    for kind in ('new-helper-schema','legacy'):
        work=build/kind;work.mkdir(exist_ok=True);input_file=work/'fixture.root'
        r=execute([str(build/'generate'),kind,str(input_file)]);assert r.get('exit_code')==0
        r=execute([str(build/'lean'),str(input_file)],cwd=work)
        case={'input_sha256':sha(input_file),'execution_command_index':len(record['commands'])-1,'execution_exit':r.get('exit_code'),'input_keys_kind':kind,'not_experimental_data':True}
        output=work/'CompPlots_10577.root'
        if output.exists():
            case['output_sha256']=sha(output);case['output_inspection']=execute([str(build/'inspect'),str(output)])
        cases[kind]=case
    record.update({'cases':cases,'fixture_definition':{'bins':[180,180],'angle_range':[0,180.000001],'prompt_mean':'1000*(1-0.2*cos(2*xi))','mixed_mean':1000,'geometry_content':1,'random_sampling':False,'uncertainty_boundary':'synthetic mean histograms; native fit errors are program outputs, not experimental intervals or coverage'},'generated_inputs':{'generator_sha256':sha(generator),'batch_entry_sha256':sha(entry),'inspection_sha256':sha(inspect)},'binaries':{x:sha(build/x) for x in ['generate','lean','inspect']},'root_version':subprocess.check_output(['root-config','--version'],text=True).strip(),'generated_at':datetime.now(timezone.utc).isoformat()})
    record['observations']={'new_helper_schema_does_not_complete_in_legacy_consumer':cases['new-helper-schema']['execution_exit']!=0,'legacy_schema_positive_control_completes':cases['legacy']['execution_exit']==0}
    record['ok']=all(record['observations'].values());(RUN/'grsisort-lean-schema-result.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'ok':record['ok'],'observations':record['observations'],'cases':cases,'commands':[{'command':x['command'],'exit_code':x.get('exit_code'),'stderr_tail':x.get('stderr','')[-1000:]} for x in record['commands']]},ensure_ascii=False,indent=2));return 0 if record['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
