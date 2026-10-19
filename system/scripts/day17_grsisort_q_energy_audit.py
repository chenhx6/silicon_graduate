#!/usr/bin/env python3
"""Unmodified ScaleQ program, exact role controls, and explicit KN weight comparison."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "tmp/day17-grsisort"
RUN = ROOT / "outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_means(energy, n=4000):
    """Declared single free-electron scattering, uniform theta or KN*dOmega."""
    step = math.pi/n
    scalar, weighted_numerator, weighted_denominator = [], [], []
    for i in range(n+1):
        theta=i*step
        r=1/(1+energy/510.9989*(1-math.cos(theta)))
        sin2=math.sin(theta)**2
        base=r+1/r-sin2
        simpson=1 if i in (0,n) else (4 if i%2 else 2)
        scalar.append(simpson*sin2/base)
        weighted_numerator.append(simpson*r*r*sin2*math.sin(theta))
        weighted_denominator.append(simpson*r*r*base*math.sin(theta))
    return {"uniform_theta":math.fsum(scalar)*step/3/math.pi,"KN_dOmega_weighted":math.fsum(weighted_numerator)/math.fsum(weighted_denominator)}


def main():
    source=CACHE/'util/Compton_Scale_Plot.cxx'
    assert sha(source)=='ef011abde04415030bec5dd5534ae2766cfa8f36d1ce27bcce8d45d4f7cce090'
    build=CACHE/'q-energy-build';build.mkdir(exist_ok=True)
    flags=shlex.split(subprocess.check_output(['root-config','--cflags','--libs'],text=True))
    base=['g++','-O1','-I'+str(CACHE/'include')]
    record={'source_sha256':sha(source),'Globals_sha256':sha(CACHE/'include/Globals.h'),'script_sha256':sha(Path(__file__)),'input_kind':'declared energy/role controls; no experimental data','components':[]}
    original=build/'original';command=base+[str(source),'-o',str(original)]+flags
    comp=subprocess.run(command,capture_output=True,text=True);record['components'].append({'kind':'complete-original-program','compile_command':command,'compile_exit':comp.returncode,'compile_stderr':comp.stderr})
    if comp.returncode:raise RuntimeError(comp.stderr)
    executed=subprocess.run([str(original)],capture_output=True,text=True);record['components'][-1].update({'execution_exit':executed.returncode,'stdout':executed.stdout,'stderr':executed.stderr,'binary_sha256':sha(original)})
    adapter=build/'role-adapter.cxx';adapter.write_text('#define main OriginalPlotMain\n#include "'+str(source)+'"\n#undef main\n#include <iomanip>\nint main(){std::cout<<std::setprecision(17);for(double E:{100.,500.,1332.,3000.})std::cout<<E<<" "<<ScaleQ(1332.,E)<<" "<<ScaleQ(E,1332.)<<"\\n";}\n')
    binary=build/'role-adapter';command=base+[str(adapter),'-o',str(binary)]+flags;comp=subprocess.run(command,capture_output=True,text=True);record['components'].append({'kind':'source-included-role-adapter','compile_command':command,'compile_exit':comp.returncode,'compile_stderr':comp.stderr,'adapter_sha256':sha(adapter)})
    if comp.returncode:raise RuntimeError(comp.stderr)
    executed=subprocess.run([str(binary)],capture_output=True,text=True);record['components'][-1].update({'execution_exit':executed.returncode,'stdout':executed.stdout,'stderr':executed.stderr,'binary_sha256':sha(binary)})
    raw_rows=[[float(x) for x in row.split()] for row in record['components'][0]['stdout'].splitlines()]
    rows=[];mean_ref=independent_means(1332.)
    for line in executed.stdout.splitlines():
        energy,forward,reverse=map(float,line.split());means=independent_means(energy)
        row={'energy_keV':energy,'source_ScaleQ_cal1332_to_target':forward,'source_ScaleQ_target_to_cal1332':reverse,'independent_uniform_theta_means':means['uniform_theta'],'independent_uniform_theta_scale':means['uniform_theta']/mean_ref['uniform_theta'],'declared_KN_dOmega_mean':means['KN_dOmega_weighted'],'declared_KN_dOmega_scale':means['KN_dOmega_weighted']/mean_ref['KN_dOmega_weighted'],'proper_role_scaled_Q_from_2509':.2509*forward,'reversed_role_scaled_Q':.2509*reverse,'roundtrip_product':forward*reverse}
        if energy in (100.,500.,3000.):row['original_plot_printed_Q']=dict(raw_rows)[energy]
        rows.append(row)
    checks={'original_execution_zero':record['components'][0]['execution_exit']==0,'adapter_execution_zero':record['components'][1]['execution_exit']==0,'source_scales_are_reciprocal':all(abs(r['roundtrip_product']-1)<1e-12 for r in rows),'source_uniform_theta_matches_independent_integration':all(abs(r['source_ScaleQ_cal1332_to_target']-r['independent_uniform_theta_scale'])<1e-10 for r in rows),'original_plot_uses_reversed_role_relative_to_fixed1332_calibration':all(abs(r['original_plot_printed_Q']-r['reversed_role_scaled_Q'])<1e-6 for r in rows if 'original_plot_printed_Q' in r),'equal_energy_scale_one':abs(rows[2]['source_ScaleQ_cal1332_to_target']-1)<1e-12}
    low_energy_means=independent_means(0.)
    checks['declared_Thomson_uniform_theta_limit']=abs(low_energy_means['uniform_theta']-(math.sqrt(2)-1))<1e-12
    checks['declared_Thomson_KN_dOmega_limit']=abs(low_energy_means['KN_dOmega_weighted']-.5)<1e-12
    record.update({'rows':rows,'reference_means':mean_ref,'analytic_low_energy_limits':{'uniform_theta':'sqrt(2)-1','KN_dOmega_weighted':'1/2','point_theta90':'1','independent_numeric':low_energy_means,'boundary':'analytic E→0 control of the kernel; original ScaleQ never called with zero energy'},'checks':checks,'ok':all(checks.values()),'scope':'whole original standalone plotting program plus original ScaleQ included unchanged in a role adapter; independent integrals are declared single-scatter mathematical controls, not detector response or observed Q(E)','boundary':'Neither uniform-theta averaging nor the all-angle free-electron KN weight contains actual clover geometry, thresholds, multiple scattering, calibration covariance or event selection. No inferred experimental polarization.','generated_at':datetime.now(timezone.utc).isoformat()})
    (RUN/'grsisort-q-energy-result.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps(record,ensure_ascii=False,indent=2));return 0 if record['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
