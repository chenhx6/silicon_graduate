#!/usr/bin/env python3
"""Audit frozen public stopping rows and coverage; never fit experimental lifetimes."""
import csv
import hashlib
import io
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interp(points, energy, log=False):
    """Two declared interpolation choices; no statistical inference or extrapolation."""
    assert points[0][0] <= energy <= points[-1][0]
    for e, s in points:
        if energy == e:
            return s
    for (a, sa), (b, sb) in zip(points, points[1:]):
        if a < energy < b:
            if log:
                t = math.log(energy / a) / math.log(b / a)
                return math.exp(math.log(sa) + t * math.log(sb / sa))
            return sa + (sb - sa) * (energy - a) / (b - a)
    raise AssertionError('unbracketed input')


def main():
    contract = RUN / 'stopping-coverage-contract.json'
    c = json.loads(contract.read_text())
    assert c['identity'] == 'IAEA-STOPPING-SELECTED-COVERAGE-01'
    result = {'identity': c['identity'], 'script_sha256': sha(__file__),
              'contract_sha256': sha(contract), 'pairs': {}}
    n_exp = n_model = 0
    for path, expected in c['source_hashes'].items():
        assert sha(ROOT / path) == expected, path
        rows = list(csv.DictReader(io.StringIO((ROOT / path).read_text(encoding='utf-8-sig'))))
        pair = rows[0]['projectile_name'] + '-' + rows[0]['target_name']
        assert all(x['energy_unit'] == c['units']['energy'] and
                   x['stopping_unit'] == c['units']['stopping'] for x in rows)
        groups = defaultdict(list)
        for row in rows:
            groups[row['ref_id']].append(row)
        assert set(groups) == set(c['experimental_refs'][pair] + [c['model_ref']])
        model = sorted((float(x['energy']), float(x['stopping_power']))
                       for x in groups[c['model_ref']])
        assert len(set(e for e, _ in model)) == len(model)
        model_isotopes = set(x['ion_isotope'] for x in groups[c['model_ref']])
        summaries = []
        for ref in c['experimental_refs'][pair]:
            data = groups[ref]
            n_exp += len(data)
            ratios = []
            interpolation_sensitivity = []
            isotope_matches_model = set(x['ion_isotope'] for x in data) == model_isotopes
            for row in data:
                if not isotope_matches_model:
                    continue
                e, s = float(row['energy']), float(row['stopping_power'])
                sm = interp(model, e)
                sm_log = interp(model, e, log=True)
                ratios.append(s / sm)
                interpolation_sensitivity.append(abs(s / sm - s / sm_log))
            summaries.append({'ref': ref, 'count': len(data),
                              'isotopes': sorted(set(x['ion_isotope'] for x in data)),
                              'energy_min_MeV_u': min(float(x['energy']) for x in data),
                              'energy_max_MeV_u': max(float(x['energy']) for x in data),
                              'percentage_error_literal': sorted(set(x['percentage_error'] for x in data)),
                              'isotope_matches_model': isotope_matches_model,
                              'ratio_to_IAEA_SRIM2013_linear_min': min(ratios) if ratios else None,
                              'ratio_to_IAEA_SRIM2013_linear_max': max(ratios) if ratios else None,
                              'max_absolute_ratio_change_log_interpolation': max(interpolation_sensitivity) if ratios else None,
                              'not_fit_CI_or_actual_paper_model': True})
        n_model += len(model)
        result['pairs'][pair] = {'experimental': summaries, 'model_count': len(model)}

    # Unit identity using the database's target mass-to-atom ratio and exact SI N_A.
    s_au = list(csv.DictReader((RUN / 'stopping-S-Au-frozen.csv').open()))
    wr = next(x for x in s_au if x['ref_id'] == 'Wr1979')
    s_mass, mass_atom = float(wr['stopping_power']), float(wr['target_mass_atom_ratio'])
    s15 = s_mass * mass_atom * 1e24 / c['NA']
    assert math.isclose(s15 * 1e-15 * (c['NA'] * 1e-3 / mass_atom), s_mass * 1e6)
    result['unit_example'] = {'ref': 'Wr1979', 'energy_MeV_u': float(wr['energy']),
                            'S_MeV_per_mg_cm2': s_mass, 'S_in_1e_minus15_eV_cm2_per_atom': s15,
                            'conversion': 'S_15=S_mass*A_target*1e24/N_A',
                            'no_density_or_length_conversion_assumed': True}

    # Declared nonrelativistic mass-number proxy, before slowing; gamma momentum
    # triangle bound is deliberately generous and is not an actual cascade replay.
    ep, mp, u = c['Schuermann_Ep_MeV'], c['proton_MeV_mass_proxy'], c['u_MeV_mass_proxy']
    p = math.sqrt(2 * mp * ep)
    initial = p*p / (2 * 15 * u) / 15
    assert c['Schuermann_resonance_excitation_MeV_for_conservative_photon_bound'] + 15 * initial < c['design_total_gamma_energy_upper_MeV']
    bound = (p + c['design_total_gamma_energy_upper_MeV'])**2 / (2 * 15 * u) / 15
    lowest = min(x['energy_min_MeV_u'] for x in result['pairs']['O-Ta']['experimental'])
    assert lowest > 40 * bound
    result['O_Ta_coverage_proxy'] = {'initial_15O_MeV_u': initial,
                                  'generous_before_stopping_photon_triangle_bound_MeV_u': bound,
                                  'lowest_compiled_experimental_MeV_u': lowest,
                                  'minimum_energy_ratio_to_generous_proxy_bound': lowest/bound,
                                  'massnumber_approximation_not_actual_collision_or_cascade': True}
    assert n_exp == 63 and n_model == 329
    result.update({'experimental_rows': n_exp, 'model_rows': n_model,
                   'original_experimental_covariance_recovered': False,
                   'Sun_Geant4_stopping_base_recovered': False,
                   'new_lifetime_fit_or_prior_calibration': False,
                   'generated_at': datetime.now(timezone.utc).isoformat(), 'ok': True})
    (RUN / 'stopping-coverage-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
