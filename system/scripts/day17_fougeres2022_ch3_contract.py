#!/usr/bin/env python3
"""Actual thesis calibration coefficients, geometry and native conversion audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import ROOT as R

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def efficiency(energy, coeff):
    x = math.log(energy)
    return math.exp(sum(a*x**i for i, a in enumerate(coeff)))


def main():
    cp = RUN / 'fougeres2022-thesis-ch3-exercise-contract.json'
    c = json.loads(cp.read_text())
    for name, key in [('pdf', 'pdf_sha256'), ('tools_source', 'tools_sha256'), ('native_fragment', 'fragment_sha256')]:
        assert sha(ROOT / c[name]) == c[key]
    assert R.gInterpreter.Declare('#include <cmath>\n' + (ROOT / c['native_fragment']).read_text())
    efficiency_rows = []
    for e in c['efficiency_probe_keV']:
        rounded = efficiency(e, c['literal_Eq3p9_coeff'])
        full = efficiency(e, c['Fig3p19_full_coeff'])
        efficiency_rows.append({'energy_keV': e, 'Eq3p9_fraction': rounded, 'Fig3p19_fraction': full,
                                'rounded_over_full_minus_one': rounded/full-1})
    doppler_rows = []
    beta, e0 = c['declared_beta'], c['rest_gamma_keV']
    for angle in c['declared_theta_DS_degrees']:
        observed = e0*math.sqrt(1-beta*beta)/(1-beta*math.cos(math.radians(angle)))
        doppler_rows.append({'theta_DS_degrees': angle, 'declared_beta': beta, 'observed_energy_keV': observed,
                             'Eq3p9_efficiency_observed_over_rest': efficiency(observed, c['literal_Eq3p9_coeff'])/efficiency(e0, c['literal_Eq3p9_coeff']),
                             'boundary': 'declared point kinematics; original efficiency evaluation role unknown'})
    x = c['literal_Eq3p6']
    r = x['B_Tm']*x['charge_C']/(x['c_m_s']*x['mass_kg'])
    printed = x['mass_rest_MeV']*(1/math.sqrt(1-r*r)-1)
    exact = x['mass_rest_MeV']*(math.sqrt(1+r*r)-1)
    n = c['native_conversion_inputs']
    native = float(R.Brho_Ekin_conv(n['B_Tm'], n['Mnuc_MeV'], n['A'], n['Z'], 1))
    back = float(R.Brho_Ekin_conv(native, n['Mnuc_MeV'], n['A'], n['Z'], 0))
    rn = n['B_Tm']*n['factor']*n['Z']/n['A']
    same_constants_exact = n['Mnuc_MeV']*(math.sqrt(1+rn*rn)-1)
    assert abs(back-n['B_Tm']) < 1e-12
    assert abs(native-n['Mnuc_MeV']*(1/math.sqrt(1-rn*rn)-1)) < 1e-12
    assert native-same_constants_exact > .5
    geometry = []
    for row in c['Table3p5_rings'] + [{'label': 'public generic default', **c['public_default_geometry']}]:
        geometry.append({**row, 'point_target_front_face_angles_degrees': [math.degrees(math.atan(row[key]/row['Z_mm'])) for key in ['inner_mm','outer_mm']],
                         'boundary': 'single face geometric descriptor; not measured efficiency or joint telescope aperture'})
    out = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'ROOT_helper': R.gROOT.GetVersion(),
           'efficiency_coefficient_crosscheck': efficiency_rows, 'energy_role_control': doppler_rows,
           'literal_Eq3p6': {'r_p_over_mc': r, 'printed_energy_MeV': printed, 'momentum_consistent_energy_MeV': exact,
                            'nominal_difference_MeV': printed-exact},
           'original_native_conversion': {'energy_MeV': native, 'inverse_B_Tm': back,
                'same_constant_momentum_consistent_energy_MeV': same_constants_exact,
                'nominal_difference_MeV': native-same_constants_exact,
                'boundary': 'literal source component and reciprocal closure; original paper producer/Brho calibration unknown'},
           'single_face_geometry_crosschecks': geometry,
           'Table3p7_FWHM_divided_by_2p35_sigma_keV': [v/2.35 for v in c['Table3p7_FWHM_keV']],
           'source_and_native_literal_momentum_beta_boundary_demonstrated': True,
           'raw_source_unchanged': True, 'no_new_experimental_energy_tau_branch_or_CI': True, 'ok': True}
    (RUN / 'fougeres2022-thesis-ch3-exercise-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
