#!/usr/bin/env python3
"""Published GRIFFIN summary versus a separately pinned code kernel; no new fit."""
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


def main():
    inp=RUN/'griffin-primary-calibration-input.json';d=json.loads(inp.read_text());assert sha(ROOT/d['pdf_path'])==d['pdf_sha256']
    source=ROOT/d['source_code_comparison']['path'];assert sha(source)==d['source_code_comparison']['sha256']
    build=ROOT/'tmp/day17-griffin-facility/calibration-build';build.mkdir(exist_ok=True)
    adapter=build/'scale-source.cxx';energies=','.join(str(float(x['energy_keV'])) for x in d['quality_factor_rows'])
    adapter.write_text('#define main OriginalScalePlot\n#include "'+str(source)+'"\n#undef main\n#include <iomanip>\nint main(){std::cout<<std::setprecision(17);for(double E:{'+energies+'})std::cout<<E<<" "<<ScaleQ(1332.,E)<<" "<<ScaleQ(E,1332.)<<"\\n";}\n')
    binary=build/'scale-source';flags=shlex.split(subprocess.check_output(['root-config','--cflags','--libs'],text=True));command=['g++','-O1','-I'+str(ROOT/'tmp/day17-grsisort/include'),str(adapter),'-o',str(binary),*flags]
    comp=subprocess.run(command,capture_output=True,text=True);assert comp.returncode==0,comp.stderr
    ex=subprocess.run([str(binary)],capture_output=True,text=True);assert ex.returncode==0,ex.stderr
    scales={int(float(a)):(float(b),float(c)) for a,b,c in (line.split() for line in ex.stdout.splitlines())}
    ref=next(x for x in d['quality_factor_rows'] if x['role']=='source calibration anchor');rows=[]
    for r in d['quality_factor_rows']:
        scale,reverse=scales[r['energy_keV']];pred=ref['Q']*scale
        rows.append({**r,'current_code_forward_scale':scale,'current_code_reverse_scale':reverse,'conditional_prediction':pred,'conditional_shared_anchor_sigma':ref['sigma_Q']*scale,'measured_minus_conditional_prediction':r['Q']-pred,'central_fractional_difference':r['Q']/pred-1,'reversed_role_prediction':ref['Q']*reverse})
    validation=[x for x in rows if x['role']!='source calibration anchor'];cov=[[ref['sigma_Q']**2*a['current_code_forward_scale']*b['current_code_forward_scale'] for b in validation] for a in validation]
    pref=1/6;A0=.5*ref['Q']*pref;sigma_A0=.5*ref['sigma_Q']*pref
    t=d['table7_companion'];total=t['area_245']*t['array_efficiency_122']/t['clovers'];photon=total/(1+t['alpha_121']);sigma=photon*math.sqrt((t['sigma_area_245']/t['area_245'])**2+(t['sigma_efficiency_122']/t['array_efficiency_122'])**2)
    rounding_low=(t['area_245']-50)*(t['array_efficiency_122']-.0005)/(t['clovers']*(1+t['alpha_121']+.0005))
    rounding_high=(t['area_245']+50)*(t['array_efficiency_122']+.0005)/(t['clovers']*(1+t['alpha_121']-.0005))
    table={'conditional_central_sum':photon,'independent_area_efficiency_only_sigma':sigma,'source_reported_expected':t['reported_expected_sum'],'central_difference':photon-t['reported_expected_sum'],'printed_half_last_digit_box':[rounding_low,rounding_high],'rounding_assumptions':{'area_half_last_digit':50,'efficiency_half_last_digit':.0005,'alpha_half_last_digit':.0005,'reported_sum_half_last_digit':.5},'omit_ICC_prediction':total,'omitting_ICC_ratio':total/photon,'boundary':'rounding box is a decimal-print diagnostic, not a confidence interval. Alpha and other covariance held fixed in the local sigma diagnostic; neither is the source full error recipe or independent experimental confirmation'}
    checks={'native_compile_and_execution':comp.returncode==0 and ex.returncode==0,'anchor_scale_one':scales[1332][0]==1.,'nominal_A0_002':abs(A0-.02)<1e-15,'role_scales_reciprocal':all(abs(x['current_code_forward_scale']*x['current_code_reverse_scale']-1)<1e-12 for x in rows),'conditional_anchor_covariance_rank_one':all(abs(cov[i][j]**2-cov[i][i]*cov[j][j])<1e-15 for i in range(3) for j in range(3)),'table7_printed_rounding_boxes_overlap':rounding_low<=t['reported_expected_sum']+.5 and rounding_high>=t['reported_expected_sum']-.5}
    result={'input_sha256':sha(inp),'script_sha256':sha(Path(__file__)),'pdf_sha256':d['pdf_sha256'],'code_sha256':sha(source),'source_vs_current_code_boundary':d['source_code_comparison']['role'],'rows':rows,'conditional_validation_order':[x['energy_keV'] for x in validation],'conditional_anchor_covariance':cov,'covariance_contract':d['covariance_contract'],'nominal_Co60_reference':{'P':pref,'Q':ref['Q'],'A0':A0,'sigma_A0_from_Q_only':sigma_A0,'boundary':'source adopts nominal P90=1/6; roundtrip is not an independent measurement of P'},'table7_replay':table,'compile':{'command':command,'exit_code':comp.returncode,'stderr':comp.stderr},'execution':{'exit_code':ex.returncode,'stdout':ex.stdout,'stderr':ex.stderr},'binary_sha256':sha(binary),'adapter_sha256':sha(adapter),'checks':checks,'ok':all(checks.values()),'generated_at':datetime.now(timezone.utc).isoformat()}
    (RUN/'griffin-primary-calibration-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
