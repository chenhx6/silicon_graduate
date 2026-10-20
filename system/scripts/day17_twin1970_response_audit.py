#!/usr/bin/env python3
"""TW70 actual angle/energy identity and conditional point-response audit."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def point(energy_keV, angle_deg):
    psi=math.radians(angle_deg)
    ratio=1/(1+energy_keV/510.99895*(1-math.cos(psi)))
    s2=math.sin(psi)**2
    return {'scattered_energy_keV':energy_keV*ratio,
            'R_point':s2/(1/ratio+ratio-s2)}


def main():
    path=RUN/'twin1970-response-contract.json'
    c=json.loads(path.read_text())
    values=[{'Egamma_keV':e,'psi82':point(e,82),'psi90':point(e,90)} for e in c['point_energy_keV']]
    for e in c['point_energy_keV']:
        assert point(e,0)['R_point']==0
        assert abs(point(e,180)['R_point'])<1e-14
    assert abs(point(1e-9,90)['R_point']-1)<1e-10
    identities=[]
    for ei,ef,eg in c['Egamma_identity_rows']:
        delta=(ei-ef)*1000-eg
        assert abs(delta)<1e-9
        identities.append({'Ei_MeV':ei,'Ef_MeV':ef,'Egamma_keV':eg,'residual_keV':delta})
    a2=c['2231_AD_a2']
    p_e1=-3*a2/(2-a2)
    p=c['actual_P_for_2231'];r=c['actual_R_for_2231']
    source_angle=next(x for x in values if x['Egamma_keV']==2231)
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'point_response_comparisons':values,
            'actual_2231_R_over_point82':r/source_angle['psi82']['R_point'],
            'conditional_pureE1_P90_from_a2_041':p_e1,
            'reported_2231_P90':p,
            'derived_corrected_count_asymmetry_R_times_P_not_raw_counts':r*p,
            'photon_identity_checks':identities,
            'null_efficiency_reference_is_not_an_R_calibration':True,
            'psi82_is_Compton_not_emission_angle':True,
            'R021_belongs_to_2231_not1500':True,
            'no_actual_finite_geometry_or_raw_counts_reconstructed':True,
            'no_new_spin_parity_delta_P_R_CI':True,'ok':True}
    (RUN/'twin1970-response-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
