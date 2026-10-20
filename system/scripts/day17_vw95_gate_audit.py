#!/usr/bin/env python3
"""VW95 actual line energies, known-order Compton gate and efficiency roles."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'vonderwerth1995-gate-contract.json'
    c=json.loads(path.read_text());mass=c['electron_rest_keV']
    rows=[]
    for energy in c['Eg_keV']:
        values=[]
        for angle in c['angles_degrees']:
            scattered=energy/(1+energy/mass*(1-math.cos(math.radians(angle))))
            electron=energy-scattered
            cos_inverse=1-mass*electron/(scattered*energy)
            recovered=math.degrees(math.acos(max(-1,min(1,cos_inverse))))
            assert abs(recovered-angle)<1e-11
            swapped_cos=1-mass*scattered/(electron*energy)
            swapped=None if not -1<=swapped_cos<=1 else math.degrees(math.acos(swapped_cos))
            values.append({'theta_deg':angle,'analyzer_scattered_Eprime_keV':scattered,
                           'central_scatter_electron_energy_keV':electron,
                           'recovered_theta_deg':recovered,
                           'wrong_role_swapped_theta_deg_or_null':swapped,
                           'both_above_declared60keV':min(scattered,electron)>=60})
        a=energy/mass;q0=(1+a)/(1+a+a*a)
        fits={name:q0*(p['m_per_MeV']*energy/1000+p['b'])
              for name,p in [('POLALI',c['source_Qfit_POLALI']),('MINIPOLA',c['source_Qfit_MINIPOLA'])]}
        rows.append({'Egamma_keV':energy,'kinematics':values,
                     'nominal_source_fit_Q_not_actual_calibration_points':fits})
    nsum,ns,es,flux=sp.symbols('Nsum Ns epsilon_s flux',positive=True)
    ec=nsum*es/(2*ns)
    assert sp.simplify(ec.subs(ns,flux*es)-nsum/(2*flux))==0
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'actual_line_energy_checks':rows,
            'epsilon_identity':'source epsilon_c=Nsum/(2Phi) only if Phi=Ns/epsilon_abs_single is the same unpolarized-source normalization',
            'Eq8_inverse_and_energy_role_controls':True,
            'source_half_sum_absolute_efficiency_identity':True,
            'not_MINIPOLA_order_reconstruction_or_actual_cut_retention':True,
            'no_actual_calibration_P_counts_Cov_or_new_Q_CI':True,'ok':True}
    (RUN/'vonderwerth1995-gate-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='actual_line_energy_checks'},indent=2))


if __name__=='__main__':
    main()
