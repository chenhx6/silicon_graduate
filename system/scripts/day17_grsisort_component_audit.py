#!/usr/bin/env python3
"""Compile pinned GRSISort components with explicit shims; never an event-data fit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shlex
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01"
CACHE = ROOT / "tmp/day17-grsisort"
BUILD = CACHE / "component-build"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inp = RUN / "grsisort-component-input.json"
    config = json.loads(inp.read_text())
    for path, expected in config['source_hashes'].items():
        assert sha(CACHE/path) == expected, path
    BUILD.mkdir(parents=True, exist_ok=True)
    source = (CACHE/'util/AnalyzeComptonMatrices.cxx').read_text()
    functions = source[source.index('double KCoefficent(int mu, int L1, int L2)'):source.index('\n#else')]
    helper = (CACHE/'examples/ComptonPolarimetryHelper.cxx').read_text()
    exec_body = helper[helper.index('void ComptonPolarimetryHelper::Exec('):]
    header = (CACHE/'examples/ComptonPolarimetryHelper.hh').read_text()
    predicates = header[header.index('   double TimeDiff('):header.index('\npublic:')]
    errors = re.search(r'\(1\. - \(xiPrompt->GetBinContent\(bin\) / promptIntegral\) / \(xiMixed->GetBinContent\(bin\) / mixedIntegral\)\) \*\s*TMath::Sqrt\(1\. / xiPrompt->GetBinContent\(bin\) \+ 1\. / promptIntegral \+ 1\. / xiMixed->GetBinContent\(bin\) \+\s*1\. / mixedIntegral\)',source).group()
    prelude = r'''
#include <algorithm>
#include <array>
#include <cmath>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include "TMath.h"
#include "TVector3.h"
#include "TH1D.h"
#include "TGraphErrors.h"
#include "Math/SpecFuncMathMore.h"
struct TUserSettings {
 std::map<std::string,std::vector<double>> vectors;
 std::map<std::string,double> doubles;
 std::vector<double> GetDoubleVector(const std::string& s){return vectors.at(s);}
 double GetDouble(const std::string& s){return doubles.at(s);}
 int GetInt(const std::string& s){return static_cast<int>(doubles.at(s));}
 bool GetBool(const std::string&){return false;}
};
struct TGriffinHit {
 double energy; int detector,crystal,array; TVector3 position;
 double GetEnergy() const {return energy;}
 int GetDetector() const {return detector;}
 int GetCrystal() const {return crystal;}
 int GetArrayNumber() const {return array;}
 TVector3 GetPosition(double) const {return position;}
 double GetTime() const {return 0.;}
 long GetTimeStampNs() const {return 0;}
};
struct TGriffin {
 std::vector<TGriffinHit> hits;
 int GetMultiplicity() const {return static_cast<int>(hits.size());}
 TGriffinHit* GetGriffinHit(int i){return &hits.at(i);}
 static TVector3 GetPosition(int d,int c,double){return TVector3(d,c+1.,1.);}
};
struct TGriffinBgo {};
struct Sink {long entries=0; void Fill(double){++entries;} void Fill(double,double){++entries;}};
class ComptonPolarimetryHelper {
public:
 double fGriffinDistance=145.; bool fUseTimestamps=false; double fPrompt=200.;
 std::array<double,2> fGammaGateLow={1170.,1329.},fGammaGateHigh={1176.,1335.};
 std::map<unsigned,std::deque<TGriffin*>> fGriffinDeque;
 std::map<unsigned,std::map<std::string,Sink*>> fH1,fH2;
 bool ExcludeDetector(int) const{return false;}
 bool ExcludeCrystal(int) const{return false;}
'''
    closing = r'''
 void Exec(unsigned int,TGriffin&,TGriffinBgo&);
};
'''
    first, second = config['controls'][0]['first_coefficients_from_legacy_Co60_template'],config['controls'][0]['second_coefficients_from_legacy_Co60_template']
    main_code = r'''
int main(){
 std::cout<<std::setprecision(17);
 TUserSettings st;
 st.vectors["F.Ji.Jx"]={FIRST};st.vectors["F.Jf.Jx"]={SECOND};
 st.doubles={{"Mixing.1",0.},{"Mixing.2",0.},{"L2",2.},{"Theta",90.}};
 const double original=Polarization(&st);
 st.vectors["F.Jf.Jx"]=std::vector<double>(12,0.);
 const double changedSecond=Polarization(&st);
 const double prod2=(-.1707)*(-.5976),prod4=(-.0085)*(-1.069);
 const double oracle=(1.5*prod2+.625*prod4)/(1.-.5*prod2+.375*prod4);
 std::cout<<"POL "<<original<<" "<<changedSecond<<" "<<oracle<<"\n";
 TH1D prompt("prompt","",10,0,10),mixed("mixed","",10,0,10);
 for(int i=1;i<=10;++i){prompt.SetBinContent(i,100.);mixed.SetBinContent(i,100.);}
 TH1D* xiPrompt=&prompt;TH1D* xiMixed=&mixed;int bin=1;
 double promptIntegral=xiPrompt->Integral(),mixedIntegral=xiMixed->Integral();
 double literalError=ERROR_EXPRESSION;
 TGraphErrors graph;graph.SetPoint(0,.5,0.);graph.SetPointError(0,.5,literalError);
 double independentNormalizedVariance=1./100.-1./1000.+1./100.-1./1000.;
 std::cout<<"ERROR "<<literalError<<" "<<graph.GetErrorY(0)<<" "<<std::sqrt(independentNormalizedVariance)<<"\n";
 TH1D bins("bins","",180,0,180.000001);for(int i=1;i<=180;++i)bins.SetBinContent(i,1.);
 std::cout<<"BINS "<<bins.FindBin(0.)<<" "<<bins.FindBin(2.)<<" "<<bins.FindBin(3.)<<" "<<bins.Integral(bins.FindBin(0.),bins.FindBin(2.))<<" "<<bins.Integral(bins.FindBin(2.),bins.FindBin(3.))<<"\n";
 const std::vector<std::string> h1={"gammaSingles","gammaSingles_g1","gammaSingles_g2","gammaSingles_g3","ggTimeDiff_g1g2","ggTimeDiff_g1g3","ggTimeDiff_g2g3"};
 const std::vector<std::string> h2={"gammagamma","gammaCrystal","xiThetaCry","xiThetaDet","xiCrystal","thetaCrystal","gammaXi_g1","gammaXi_g2","xiThetaCryMixed","xiThetaDetMixed"};
 for(int validIndex=0;validIndex<3;++validIndex){
  ComptonPolarimetryHelper h;
  for(const auto& name:h1)h.fH1[0][name]=new Sink;
  for(const auto& name:h2)h.fH2[0][name]=new Sink;
  TGriffin current;current.hits={{800.,1,0,1,TVector3(1,0,0)},{373.,1,1,2,TVector3(1,1,0)},{1332.,2,0,5,TVector3(0,1,0)}};
  TGriffin history;history.hits={{100.,3,0,9,TVector3(0,0,1)},{200.,4,0,13,TVector3(1,0,1)}};
  history.hits.insert(history.hits.begin()+validIndex,TGriffinHit{1332.,2,0,5,TVector3(0,1,0)});
  for(int i=0;i<9;++i)h.fGriffinDeque[0].push_back(new TGriffin);
  h.fGriffinDeque[0].push_back(new TGriffin(history));TGriffinBgo bgo;h.Exec(0,current,bgo);
  std::cout<<"MIX "<<validIndex<<" "<<h.fH2[0]["xiThetaCry"]->entries<<" "<<h.fH2[0]["xiThetaCryMixed"]->entries<<"\n";
  for(auto* event:h.fGriffinDeque[0])delete event;
  for(auto& x:h.fH1[0])delete x.second;for(auto& x:h.fH2[0])delete x.second;
 }
}
'''.replace('FIRST',','.join(map(str,first))).replace('SECOND',','.join(map(str,second))).replace('ERROR_EXPRESSION',errors)
    cpp=BUILD/'audit.cxx';cpp.write_text(prelude+predicates+closing+exec_body+'\n'+functions+'\n'+main_code)
    (BUILD/'LICENSE').write_bytes((CACHE/'LICENSE').read_bytes())
    flags=shlex.split(subprocess.check_output(['root-config','--cflags','--libs'],text=True))
    binary=BUILD/'audit'
    command=['g++','-std=c++17','-O1',str(cpp),'-o',str(binary),*flags,'-lMathMore']
    comp=subprocess.run(command,capture_output=True,text=True)
    record={'run_id':'2026-10-19-day-17-01','input_kind':config['input_kind'],'input_sha256':sha(inp),'script_sha256':sha(Path(__file__)),'repository_commit':config['repository_commit'],'compile':{'command':command,'exit_code':comp.returncode,'stdout':comp.stdout,'stderr':comp.stderr},'generated_cpp_sha256':sha(cpp),'extracted_components':{'Exec_sha256':hashlib.sha256(exec_body.encode()).hexdigest(),'time_energy_predicates_sha256':hashlib.sha256(predicates.encode()).hexdigest(),'polarization_functions_sha256':hashlib.sha256(functions.encode()).hexdigest(),'error_expression_sha256':hashlib.sha256(errors.encode()).hexdigest()},'scope':'unmodified selected source bodies with declared minimal hit/settings/histogram sinks; real ROOT mathematics/histogram/bin behavior; not full GRSISort build, actual geometry or experimental data'}
    if comp.returncode==0:
        result=subprocess.run([str(binary)],capture_output=True,text=True)
        record.update({'binary_sha256':sha(binary),'root_version':subprocess.check_output(['root-config','--version'],text=True).strip(),'execution':{'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr}})
        parsed={};mix=[]
        for line in result.stdout.splitlines():
            key,*vals=line.split()
            if key=='MIX':mix.append(list(map(float,vals)))
            else:parsed[key]=list(map(float,vals))
        record['observed']=parsed;record['mixed_history_index_probes']=mix
        record['component_observations']={'second_F_input_does_not_change_original_output':parsed['POL'][0]==parsed['POL'][1],'source_literal_differs_from_declared_pure_E2_oracle':abs(parsed['POL'][0]-parsed['POL'][2])>1e-3,'null_source_literal_error_is_zero_but_design_variance_positive':parsed['ERROR'][0]==0 and parsed['ERROR'][2]>0,'adjacent_inclusive_groups_overlap_boundary_bin':parsed['BINS'][1]==2 and parsed['BINS'][3]+parsed['BINS'][4]>3,'mixed_selection_depends_on_distinct_event_list_index':[x[2] for x in mix]==[0,0,1],'same_event_prompt_control_unchanged':all(x[1]==1 for x in mix)}
        record['ok']=result.returncode==0 and all(record['component_observations'].values())
    else:record['ok']=False
    record['generated_at']=datetime.now(timezone.utc).isoformat();(RUN/'grsisort-component-result.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False,indent=2));return 0 if record['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
