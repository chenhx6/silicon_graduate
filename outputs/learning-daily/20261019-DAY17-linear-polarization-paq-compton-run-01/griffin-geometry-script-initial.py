#!/usr/bin/env python3
"""Actual published GRIFFIN coordinate table versus unchanged pinned position code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import shlex
import subprocess

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def direction(v):
    n=math.sqrt(sum(x*x for x in v));return [x/n for x in v]


def angle(a,b):
    a,b=direction(a),direction(b)
    return math.degrees(math.acos(max(-1.,min(1.,sum(x*y for x,y in zip(a,b))))))


def clusters(values,tolerance=1e-7):
    result=[]
    for x in sorted(values):
        if result and abs(x-result[-1][0])<tolerance:result[-1][1]+=1
        else:result.append([x,1])
    return result


def main():
    inp=RUN/'griffin-geometry-table-input.json';d=json.loads(inp.read_text());source=ROOT/d['code_path'];assert sha(source)==d['code_sha256'];text=source.read_text()
    array=text[text.index('std::array<TVector3, 17> TGriffin::fCloverPosition'):text.index('\nTGriffin::TGriffin(')]
    # The selected initializer may have comments/blank lines after it; no expressions are changed.
    array=array[:array.index('};')+2]
    function=text[text.index('TVector3 TGriffin::GetPosition('):text.index('\nTVector3 TGriffin::GetDetectorPosition(')]
    build=ROOT/'tmp/day17-griffin-facility/geometry-build';build.mkdir(exist_ok=True)
    cpp=build/'geometry.cxx';cpp.write_text('#include <array>\n#include <iostream>\n#include <iomanip>\n#include "TVector3.h"\n#include "TMath.h"\nclass TGriffin{public:static std::array<TVector3,17> fCloverPosition;static TVector3 GetPosition(int,int,double);};\n'+array+'\n'+function+r'''
int main(){std::cout<<std::setprecision(17);for(double distance:{110.,145.})for(int det=1;det<=16;++det)for(int cry=0;cry<4;++cry){auto v=TGriffin::GetPosition(det,cry,distance);auto front=v-45.*TGriffin::fCloverPosition[det];std::cout<<distance<<" "<<det<<" "<<cry<<" "<<v.Theta()*TMath::RadToDeg()<<" "<<std::fmod(v.Phi()*TMath::RadToDeg()+360.,360.)<<" "<<v.X()<<" "<<v.Y()<<" "<<v.Z()<<" "<<front.Theta()*TMath::RadToDeg()<<" "<<std::fmod(front.Phi()*TMath::RadToDeg()+360.,360.)<<"\n";} }
''')
    binary=build/'geometry';flags=shlex.split(subprocess.check_output(['root-config','--cflags','--libs'],text=True));command=['g++','-O1',str(cpp),'-o',str(binary),*flags];comp=subprocess.run(command,capture_output=True,text=True);assert comp.returncode==0,comp.stderr
    ex=subprocess.run([str(binary)],capture_output=True,text=True);assert ex.returncode==0,ex.stderr
    native={};rows=[]
    for line in ex.stdout.splitlines():
        dist,det,cry,th,ph,x,y,z,fth,fph=map(float,line.split());native[(int(dist),int(det),int(cry))]=[th,ph,x,y,z,fth,fph]
    for template in d['ring_templates']:
        for index,det in enumerate(template['detectors']):
            for dist in [110,145]:
                t=template[str(dist)]
                for cry in range(4):
                    th,ph,x,y,z,fth,fph=native[(dist,det,cry)];printed_theta=t['theta'][cry];printed_phi=(t['phi'][cry]+index*template['phi_step_degrees'])%360
                    phi_delta=(ph-printed_phi+180)%360-180;front_phi_delta=(fph-printed_phi+180)%360-180
                    rows.append({'distance_mm':dist,'detector':det,'crystal_code':cry,'printed_theta':printed_theta,'printed_phi':printed_phi,'native_theta':th,'native_phi':ph,'native_theta_difference':th-printed_theta,'native_phi_difference':phi_delta,'front_control_theta_difference':fth-printed_theta,'front_control_phi_difference':front_phi_delta,'native_vector':[x,y,z]})
    half=d['printed_direction_half_last_digit_degrees'];residuals=[abs(r[k]) for r in rows for k in ['native_theta_difference','native_phi_difference']]
    front_residuals=[abs(r[k]) for r in rows for k in ['front_control_theta_difference','front_control_phi_difference']]
    census={}
    for dist in (110,145):
        positions=[native[(dist,det,cry)][2:5] for det in range(1,17) for cry in range(4)]
        all_angles=[angle(a,b) for a in positions for b in positions]
        # Endpoint floating point affects acos at 0/180; group interior values separately.
        all_angles=[0. if x<1e-5 else 180. if x>180-1e-5 else x for x in all_angles]
        groups=clusters(all_angles);census[str(dist)]={'ordered_pairs':len(all_angles),'angle_clusters_at_1e_7_degrees':groups,'cluster_count':len(groups),'boundary':d['angular_census_boundary']}
    checks={'all128_crystal_positions_serialized':len(native)==128 and len(rows)==128,'all256_native_angles_within_printed_rounding_boxes':max(residuals)<=half+1e-10,'declared_front_control_is_distinct':max(front_residuals)>.1,'pair_census4096_each_distance':all(x['ordered_pairs']==4096 and sum(n for _,n in x['angle_clusters_at_1e_7_degrees'])==4096 for x in census.values())}
    result={'input_sha256':sha(inp),'script_sha256':sha(Path(__file__)),'paper_pdf_sha256':d['paper_pdf_sha256'],'source_code_sha256':sha(source),'extracted_array_sha256':hashlib.sha256(array.encode()).hexdigest(),'extracted_function_sha256':hashlib.sha256(function.encode()).hexdigest(),'compile':{'command':command,'exit_code':comp.returncode,'stderr':comp.stderr},'execution':{'exit_code':ex.returncode,'stderr':ex.stderr},'binary_sha256':sha(binary),'generated_cpp_sha256':sha(cpp),'comparison_summary':{'positions':len(rows),'native_max_absolute_angle_residual_degrees':max(residuals),'front_control_max_absolute_angle_residual_degrees':max(front_residuals),'native_all_rounding_boxes':max(residuals)<=half+1e-10},'rows':rows,'census':census,'checks':checks,'ok':all(checks.values()),'boundary':'Native source uses constant45mm most-likely interaction depth. Rounding agreement with Table2 is geometry-point identity evidence, not actual event depth, detector response, Q or original producer certification. No coordinates/identity permutation fitted.','generated_at':datetime.now(timezone.utc).isoformat()}
    (RUN/'griffin-geometry-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['rows','census']},ensure_ascii=False,indent=2));print('CENSUS',[(k,v['cluster_count']) for k,v in census.items()]);return 0 if result['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
