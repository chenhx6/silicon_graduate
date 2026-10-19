#!/usr/bin/env python3
"""Actual published GRIFFIN coordinate table versus unchanged pinned position code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import shlex
import subprocess
from collections import Counter

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
    table8=Counter((float(a),int(n)) for a,n in d['table8_110mm_ordered_angle_multiplicity_rows'])
    native_table8=Counter((round(float(a),1),int(n)) for a,n in census['110']['angle_clusters_at_1e_7_degrees'])
    for dist in (110,145):
        positions={(det,cry):native[(dist,det,cry)][2:5] for det in range(1,17) for cry in range(4)}
        axes={det:direction([sum(positions[(det,c)][i] for c in range(4))/4 for i in range(3)]) for det in range(1,17)}
        clover_pairs=[(a,b) for a in axes for b in axes if a!=b and abs(angle(axes[a],axes[b])-90.)<1e-6]
        accepted=[angle(positions[(a,c)],positions[(b,e)]) for a,b in clover_pairs for c in range(4) for e in range(4)]
        census[str(dist)]['clover90_gate']={'ordered_clover_pairs':len(clover_pairs),'crystal_pairs':len(accepted),'crystal_theta_range_degrees':[min(accepted),max(accepted)],'boundary':'geometric point combinations only, not actual event-selection probability or literal reconstruction of the source integer-degree cut'}
    near86=[a for a,n in census['110']['angle_clusters_at_1e_7_degrees'] if 86.15<a<86.25]
    printed_positions=[]
    for row in rows:
        if row['distance_mm']!=110:continue
        th,ph=map(math.radians,[row['printed_theta'],row['printed_phi']])
        printed_positions.append([math.sin(th)*math.cos(ph),math.sin(th)*math.sin(ph),math.cos(th)])
    central_angles=[angle(a,b) for a in printed_positions for b in printed_positions]
    # A path along theta then phi bounds each directional deviation by .05+.05deg.
    # The triangle inequality bounds a pair-angle deviation by .2deg; adding
    # Table8's .05deg printed interval gives a conservative .25deg outer bound.
    outer_bound=5*half
    central_comparisons=[]
    for printed,n in d['table8_110mm_ordered_angle_multiplicity_rows']:
        nearest=min(central_angles,key=lambda x:abs(x-printed));gap=abs(nearest-printed)
        central_comparisons.append({'Table8_angle':printed,'multiplicity':n,'nearest_angle_from_printed_Table2_centres':nearest,'central_gap_degrees':gap,'conservative_pair_plus_Table8_rounding_bound_degrees':outer_bound,'outside_same_geometry_printed_rounding_outer_set':gap>outer_bound+1e-10})
    comparison={'scientific_replay_status':'complete' if table8==native_table8 else 'partial-not-all-printed-rows-reproduced','printed_table8_rounded_angle_multiplicity_multiset_matches':table8==native_table8,'table8_expected_rows':len(d['table8_110mm_ordered_angle_multiplicity_rows']),'source_only_printed_rows':[[a,n,count] for (a,n),count in (table8-native_table8).items()],'native_only_printed_rows':[[a,n,count] for (a,n),count in (native_table8-table8).items()],'native_near86_degree_classes':near86,'native_near86_class_separation_degrees':max(near86)-min(near86),'independent_printed_Table2_pair_rounding_comparison':central_comparisons,'footnote_boundary':'Source repeated near86/94 geometries and three tenth-degree entries are not all reproduced by this different-version point model. Original source input is unchanged. No source erratum or experimental conflict inferred; Table2-based deterministic comparison is additionally conditional on both source tables using the same geometric point definition.'}
    checks={'all128_crystal_positions_serialized':len(native)==128 and len(rows)==128,'all256_native_angles_within_printed_rounding_boxes':max(residuals)<=half+1e-10,'declared_front_control_is_distinct':max(front_residuals)>.1,'pair_census4096_each_distance':all(x['ordered_pairs']==4096 and sum(n for _,n in x['angle_clusters_at_1e_7_degrees'])==4096 for x in census.values()),'Table8_input_has52_rows_and4096_ordered_pairs':len(d['table8_110mm_ordered_angle_multiplicity_rows'])==52 and sum(n for a,n in d['table8_110mm_ordered_angle_multiplicity_rows'])==4096}
    result={'input_sha256':sha(inp),'script_sha256':sha(Path(__file__)),'paper_pdf_sha256':d['paper_pdf_sha256'],'source_code_sha256':sha(source),'extracted_array_sha256':hashlib.sha256(array.encode()).hexdigest(),'extracted_function_sha256':hashlib.sha256(function.encode()).hexdigest(),'compile':{'command':command,'exit_code':comp.returncode,'stderr':comp.stderr},'execution':{'exit_code':ex.returncode,'stderr':ex.stderr},'binary_sha256':sha(binary),'generated_cpp_sha256':sha(cpp),'comparison_summary':{'positions':len(rows),'native_max_absolute_angle_residual_degrees':max(residuals),'front_control_max_absolute_angle_residual_degrees':max(front_residuals),'native_all_rounding_boxes':max(residuals)<=half+1e-10},'table8_comparison':comparison,'rows':rows,'census':census,'checks':checks,'ok':all(checks.values()),'boundary':'Native source uses constant45mm most-likely interaction depth. Rounding agreement with Table2 is geometry-point identity evidence, not actual event depth, detector response, Q or original producer certification. No coordinates/identity permutation fitted.','generated_at':datetime.now(timezone.utc).isoformat()}
    (RUN/'griffin-geometry-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['rows','census']},ensure_ascii=False,indent=2));print('CENSUS',[(k,v['cluster_count']) for k,v in census.items()]);return 0 if result['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
