#!/usr/bin/env python3
"""Audit matched ENSDF Mg23 fields and declared rate constraints; no fit or CI."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
from day17_pb207_reference_audit import records, value_sigma

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique_level(obj, energy):
    found = [x for x in obj['levels'] if abs(x['energy']['value'] - energy) < 0.01]
    assert len(found) == 1, (energy, found)
    return found[0]


def half_life(level):
    value, unit = level['half_life_field'].split()
    assert unit == 'FS'
    return value_sigma(value, level['half_life_uncertainty_field'])


def branches(obj, parent_energy):
    return [x for x in obj['gammas'] if x['parent'] and
            abs(x['parent']['energy']['value'] - parent_energy) < .01]


def main():
    contract = RUN / 'mg23-reference-exercise-contract.json'
    c = json.loads(contract.read_text())
    assert c['identity'] == 'MG23-OFFICIAL-LIFETIME-STRENGTH-01'
    assert sha(ROOT / c['parser_helper']) == c['parser_helper_sha256']
    data = {}
    for name, path in c['source_paths'].items():
        p = ROOT / path
        assert sha(p) == c['source_hashes'][name]
        data[name] = records(p)
    limits = []
    for energy, tau in c['K16_upper_mean_fs']:
        level = unique_level(data['he3ag'], energy)
        h = half_life(level)
        assert level['half_life_uncertainty_field'] == 'LT'
        limits.append({'compiled_level': level, 'original_mean_limit_fs': tau,
                       'mean_times_ln2_fs': tau * math.log(2),
                       'printing_residual_fs': h['value'] - tau * math.log(2),
                       'same_source_not_new_measurement': True})
    finite = []
    for energy, tau, sigma in c['K16_direct_mean_fs']:
        level = unique_level(data['he3ag'], energy)
        h = half_life(level)
        finite.append({'compiled_level': level, 'original_mean_fs': tau,
                       'original_mean_scale_fs': sigma,
                       'mean_times_ln2_fs': tau * math.log(2),
                       'scale_times_ln2_fs': sigma * math.log(2),
                       'printing_residual_fs': h['value'] - tau * math.log(2)})
    old = unique_level(data['c12ng'], 7785.2)
    current = unique_level(data['adopted'], 7784.7)
    capture = unique_level(data['pg'], 7784.7)
    assert old['Jpi'] == '7/2(+)'
    assert current['Jpi'] == '3/2+,5/2+' and capture['Jpi'] == '3/2+,5/2+'
    assert half_life(old)['value'] == half_life(current)['value'] == 6.9
    normalized = []
    for name, energy in [('c12ng', 7769.4), ('adopted', 7770.4),
                         ('pg', 7784.7), ('adopted', 7784.7)]:
        rows = branches(data[name], energy)
        vals = [x['intensity']['value'] for x in rows]
        assert len(vals) == 2 and all(x is not None and x > 0 for x in vals)
        total = sum(vals)
        p = [x / total for x in vals]
        jac = [[((total if i == j else 0) - vals[i]) / total ** 2
                for j in range(2)] for i in range(2)]
        assert max(abs(jac[0][j] + jac[1][j]) for j in range(2)) < 1e-15
        assert abs(sum(p) - 1) < 1e-15
        normalized.append({'dataset': name, 'parent_energy': energy,
                           'gamma_records': rows, 'listed_photon_fractions': p,
                           'normalization_jacobian': jac,
                           'boundary': 'conditional on listed photon inventory; no total branch or fit covariance supplied'})
    rates = []
    width = c['hbar_meV_fs'] / c['conditioned_tau_fs']
    for spin in c['J_candidates']:
        g = (2 * spin + 1) / ((2 * c['target_spin'] + 1) * (2 * c['projectile_spin'] + 1))
        product = c['conditioned_omega_meV'] / (g * width)
        discriminant = 1 - 4 * product
        roots = None if discriminant < 0 else [(1 - math.sqrt(discriminant)) / 2,
                                              (1 + math.sqrt(discriminant)) / 2]
        if roots:
            for b in roots:
                assert abs(g * width * b * (1 - b) - c['conditioned_omega_meV']) < 1e-13
        rates.append({'J': spin, 'statistical_factor_g': g, 'Gamma_total_meV': width,
                      'omega_max_at_fixed_tau_meV': g * width / 4,
                      'Bp_product_required': product, 'discriminant': discriminant,
                      'Bp_roots_conditioned': roots,
                      'tau_ceiling_fs_at_fixed_omega': g * c['hbar_meV_fs'] / (4 * c['conditioned_omega_meV']),
                      'not_spin_exclusion_or_joint_CI': True})
    checks = {'hashes_and_parser_locked': True,
              'all_nine_limits_nominal_ln2_within_0p05fs': all(abs(x['printing_residual_fs']) < .05 for x in limits),
              'two_unaveraged_finite_nominal_ln2_within_0p05fs': all(abs(x['printing_residual_fs']) < .05 for x in finite),
              'reaction_and_adopted_spin_differ': old['Jpi'] != current['Jpi'],
              'capture_parent_matches_adopted_but_not_old_spin': current['Jpi'] == capture['Jpi'],
              'no_7785_in_selected_resonant_scattering_dataset': all(x['energy']['value'] > 8600 for x in data['p-res']['levels']),
              'central_J3p2_combination_has_no_root': rates[0]['Bp_roots_conditioned'] is None,
              'central_J5p2_J7p2_combinations_each_have_two_roots': all(len(x['Bp_roots_conditioned']) == 2 for x in rates[1:])}
    result = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
              'contract_sha256': sha(contract), 'source_hashes': c['source_hashes'],
              'limit_half_mean_bridge': limits, 'finite_half_mean_bridge': finite,
              'matching_parent_records': {'fusion': old, 'adopted': current, 'capture': capture},
              'listed_gamma_normalization': normalized, 'conditional_rate_constraints': rates,
              'no_new_experimental_lifetime_strength_spin_or_CI': True,
              'checks': checks, 'ok': all(checks.values())}
    (RUN / 'mg23-reference-exercise-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'ok': result['ok'], 'checks': checks, 'rate_constraints': rates,
                      'normalized_photon_fractions': [(x['dataset'], x['parent_energy'], x['listed_photon_fractions']) for x in normalized]}, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
