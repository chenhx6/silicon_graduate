#!/usr/bin/env python3
"""AO75 ratio magnitude and single-Compton window controls, no data fit."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'aoki1975-response-contract.json'
    c=json.loads(path.read_text()); r,sr=c['ratio_reported']
    modulation=lambda ratio:(ratio-1)/(ratio+1)
    k=modulation(r); sigma=2*sr/(r+1)**2
    assert math.isclose(modulation(1/r),-k)
    rest=c['electron_rest_energy_keV']
    def scattered(energy,theta):
        return energy/(1+energy/rest*(1-math.cos(math.radians(theta))))
    rows=[]
    for energy in c['incident_energies_keV']:
        for theta in c['ring_geometry_theta_deg']:
            esc=scattered(energy,theta)
            reconstructed=1/(1/esc-(1-math.cos(math.radians(theta)))/rest)
            assert math.isclose(reconstructed,energy)
            assert 0<esc<energy
            rows.append({'incident_keV':energy,'theta_deg':theta,'scattered_keV':esc,
                         'in_160_240':160<=esc<=240,'in_70_240':70<=esc<=240})
    limits=[]
    for theta in c['ring_geometry_theta_deg']:
        u=1-math.cos(math.radians(theta)); lim=rest/u
        mapped=[]
        for gate in [70,100,160,240,250]:
            mapped.append({'ring_gate_keV':gate,'incident_keV':gate/(1-gate*u/rest)
                           if gate<lim else None})
        limits.append({'theta_deg':theta,'Eprime_infinite_incident_limit_keV':lim,'gate_map':mapped})
    result={
        'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'reported_ratio_magnitude_to_modulation':{'r':r,'sigma_r':sr,'abs_kappa':k,
              'sigma_kappa_delta_method':sigma,'mapped_r_minus_plus_sigma_not_CI':
                [modulation(r-sr),modulation(r+sr)],
              'geometry_prediction_abs_kappa':modulation(c['ratio_theory_geometry']),
              'direction_unresolved_text_vs_Fig6':True,'not_single_analyzer_Q':True},
        'single_Compton_window_controls':rows,'asymptotes_and_inverse_gate_map':limits,
        'ratio_reciprocal_and_gate_inverse_controls':True,
        'text_ratio_and_Fig6_direction_conflict_not_erased':True,
        'no_single_Q_peak_counts_original_fitCov_or_full_response_inferred':True,
        'spectrometer_efficiency_1over10_not_1over4':True,
        'ok':True,
    }
    (RUN/'aoki1975-response-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['reported_ratio_magnitude_to_modulation'],indent=2))
    print('1332-keV single-Compton controls', [x for x in rows if x['incident_keV']==1332])


if __name__=='__main__':
    main()
