#!/usr/bin/env python3
"""Independent, synthetic probability and dimensional controls; no physical fit."""
import json
import math
from pathlib import Path

# Parent->i is .6, parent->terminal beta state .2, unrelated branch .2.
# Each transition is (destination, number of neutrons, probability).
network = {
    'i': [('j', 0, .3), ('k', 1, .5), ('t', 0, .2)],
    'j': [('t', 1, .8), ('t', 0, .2)],
    'k': [('t', 1, .4), ('t', 0, .6)],
    't': [],
}
def enumerate_paths(node, n=0, weight=1.0):
    if not network[node]:
        return [(n, weight)]
    out = []
    for target, increment, prob in network[node]:
        out.extend(enumerate_paths(target, n + increment, weight * prob))
    return out

paths = enumerate_paths('i')
pi = [sum(w for n, w in paths if n == x) for x in range(3)]
px = [.6 * pi[0] + .2, .6 * pi[1], .6 * pi[2]]
# Add non-beta branch to zero-neutron response before smearing.
full = [px[0] + .2, px[1], px[2]]
eps = .5
obs = [sum(full[x] * math.comb(x, y) * eps**y * (1-eps)**(x-y)
           for x in range(y, len(full))) for y in range(len(full))]
# The kinetic energy available before recoil for a synthetic EC transition.
q_ec_mev, ex_mev, daughter_hole_mev = 3.0, .4, .03
result = {
    'nature': 'Synthetic arithmetic examples, not experimental numbers.',
    'ec': {'Q_EC_MeV': q_ec_mev, 'daughter_hole_energy_MeV': daughter_hole_mev,
           'excitation_MeV': ex_mev,
           'neutrino_energy_before_recoil_MeV': q_ec_mev-ex_mev-daughter_hole_mev,
           'beta_plus_Q_MeV_using_me_c2_0_511': q_ec_mev-2*.511},
    'spectrum_dimensional_powers': {'GF_energy_power': -2, 'GF_squared': -4,
        'electron_rest_energy_fifth': 5, 'hbar_energy_power': 1,
        'hbar_time_power': 1, 'overall_energy_power': -4+5-1,
        'overall_time_power': -1},
    'cascade': {'single_step_neutron_width_fraction_at_i': .5,
        'pi_0_1_2_at_i': pi, 'beta_branch': sum(px), 'beta_only_P0_P1_P2': px,
        'non_beta_zero_neutron_branch': .2, 'P_at_least_1': sum(px[1:]),
        'mean_neutron_count': sum(x*p for x,p in enumerate(px)),
        'epsilon': eps, 'observed_y0_y1_y2_all_parent_decays': obs,
        'explicit_paths': [{'neutrons': n, 'probability': w} for n,w in paths]},
}
assert math.isclose(sum(pi),1) and math.isclose(sum(full),1)
assert math.isclose(sum(obs),1)
Path(__file__).with_name('results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
