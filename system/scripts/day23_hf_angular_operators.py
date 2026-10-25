"""Source-motivated h/f angular blocks only; all radial and nuclear amplitudes absent."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import sph_harm_y

from day23_prm_basis_rotor import clebsch_gordan as cg, spin_matrices
from day23_multij_m1_operator import spherical


def orbital_C(lp, l, q):
    pref = math.sqrt((2 * l + 1) / (2 * lp + 1)) * cg(l, 0, 2, 0, lp, 0)
    return np.array([[pref * cg(l, m, 2, q, lp, mp) for m in range(-l, l + 1)]
                     for mp in range(-lp, lp + 1)])


def quadrature_C(lp, l, q, ntheta, nphi):
    x, wx = np.polynomial.legendre.leggauss(ntheta)
    phi = np.arange(nphi) * (2 * math.pi / nphi)
    theta = np.arccos(x)
    yp = np.array([sph_harm_y(lp, mp, theta[:, None], phi[None, :]) for mp in range(-lp, lp + 1)])
    yi = np.array([sph_harm_y(l, m, theta[:, None], phi[None, :]) for m in range(-l, l + 1)])
    yq = math.sqrt(4 * math.pi / 5) * sph_harm_y(2, q, theta[:, None], phi[None, :])
    return np.einsum('atp,tp,btp,t->ab', yp.conj(), yq, yi, wx) * (2 * math.pi / nphi)


def build():
    unc = [(l, m, s / 2) for l in [3, 5] for m in range(-l, l + 1) for s in [-1, 1]]
    coupled = [(l, tj, m / 2) for l in [3, 5] for tj in [2 * l - 1, 2 * l + 1] for m in range(-tj, tj + 1, 2)]
    u = np.array([[cg(l, m, .5, s, tj / 2, mj) if l == lp else 0 for lp, tj, mj in coupled]
                  for l, m, s in unc])
    size = len(unc)
    lops, sops = [np.zeros((size, size), complex) for _ in range(3)], [np.zeros((size, size), complex) for _ in range(3)]
    offset = 0
    for l in [3, 5]:
        dim = 2 * (2 * l + 1)
        sl = slice(offset, offset + dim)
        for axis in range(3):
            lops[axis][sl, sl] = np.kron(spin_matrices(2 * l)[axis], np.eye(2))
            sops[axis][sl, sl] = np.kron(np.eye(2 * l + 1), spin_matrices(1)[axis])
        offset += dim
    lc, sc = [u.T @ op @ u for op in lops], [u.T @ op @ u for op in sops]
    tensors = {}
    max_quadrature = max_convergence = max_hermiticity = 0.0
    offsets = {3: 0, 5: 14}
    for q in range(-2, 3):
        op = np.zeros((size, size), complex)
        for lp in [3, 5]:
            for l in [3, 5]:
                val = orbital_C(lp, l, q)
                quad = quadrature_C(lp, l, q, 18, 32)
                quad2 = quadrature_C(lp, l, q, 24, 48)
                max_quadrature = max(max_quadrature, float(np.max(abs(val - quad))))
                max_convergence = max(max_convergence, float(np.max(abs(quad - quad2))))
                op[offsets[lp]:offsets[lp] + 2 * (2 * lp + 1), offsets[l]:offsets[l] + 2 * (2 * l + 1)] = np.kron(val, np.eye(2))
        tensors[q] = u.T @ op @ u
    for q in range(-2, 3):
        max_hermiticity = max(max_hermiticity, float(np.max(abs(tensors[q].T.conj() - (-1) ** q * tensors[-q]))))
    selected = {'h9half': [i for i, (l, tj, m) in enumerate(coupled) if l == 5 and tj == 9],
                'f7half': [i for i, (l, tj, m) in enumerate(coupled) if l == 3 and tj == 7]}
    crosses = {name: float(max(np.max(abs(op[np.ix_(selected['f7half'], selected['h9half'])])) for op in ops))
               for name, ops in [('orbital_l', lc), ('spin_s', sc)]}
    max_projection = 0.0
    for name, spin_factor in [('h9half', -1 / 11), ('f7half', 1 / 7)]:
        ix = selected[name]
        for lo, so in zip(lc, sc):
            jj = (lo + so)[np.ix_(ix, ix)]
            max_projection = max(max_projection, float(np.max(abs(so[np.ix_(ix, ix)] - spin_factor * jj))))
    strengths = {}
    for initial, ii in selected.items():
        for final, ff in selected.items():
            strengths[initial + '_to_' + final] = float(sum(np.linalg.norm(op[np.ix_(ff, ii)]) ** 2 for op in tensors.values()) / len(ii))
    balance = abs(10 * strengths['h9half_to_f7half'] - 8 * strengths['f7half_to_h9half'])
    forbidden = max(float(np.max(abs(orbital_C(lp, l, q)))) for lp, l in [(0, 5), (4, 3)] for q in range(-2, 3))
    controls = {'full_l3_l5_CG_transform_unitary': np.max(abs(u.T @ u - np.eye(size))) < 1e-12,
                'orbital_and_spin_direct_h_f_blocks_zero': max(crosses.values()) < 1e-12,
                'selected_Lande_spin_projections': max_projection < 1e-12,
                'C2_Gaunt_CG_matches_independent_sphere_integral': max_quadrature < 1e-12,
                'sphere_quadrature_converged': max_convergence < 1e-12,
                'C2_tensor_hermiticity': max_hermiticity < 1e-12,
                'h9half_f7half_C2_angular_component_nonzero': strengths['h9half_to_f7half'] > 1e-5,
                'reverse_C2_detailed_balance': balance < 1e-12,
                'orbital_triangle_and_parity_forbidden_cases_zero': forbidden < 1e-12}
    return {'dimension_complete_angular_basis': size, 'hbar': 1,
            'selected_multiplets': {n: len(v) for n, v in selected.items()},
            'normalized_C2_angular_strengths': strengths, 'direct_hf_M1_component_norms': crosses,
            'controls': {k: bool(v) for k, v in controls.items()}, 'all_controls_pass': bool(all(controls.values())),
            'errors': {'Gaunt_vs_integral': max_quadrature, 'integral_convergence': max_convergence,
                       'tensor_hermiticity': max_hermiticity, 'Lande_projection': max_projection,
                       'C2_reverse_balance': balance, 'forbidden_orbital_C2': forbidden}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    out = build()
    out.update({'scope': cfg['scope'], 'formal_day_index': 23, 'conditions': cfg,
                'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
                'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'symbolic_gj': {'h9half': 'gl-(gs-gl)/11', 'f7half': 'gl+(gs-gl)/7'},
                'E2_normalization': 'C2q=sqrt(4pi/5)Y2q; each radial integral <nlprime|r^2|nl> is separate and unknown',
                'limitations': ['Angular components only, no actual radial, charge, BCS occupation, coherent QTR amplitudes or core rotor coupling.',
                                'Different bare j components are not asserted to form a good-total-I nuclear state without rotor coupling.',
                                'Direct h/f M1 zero does not imply a transition between mixed nuclear bands has zero M1.',
                                'Allowed C2 angular component is not a measured or physical B(E2); no absolute radial scale is assigned.',
                                'No physical g, delta, B, lifetime, covariance, confidence, rate or beamtime calculated.']})
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['all_controls_pass', 'dimension_complete_angular_basis', 'normalized_C2_angular_strengths', 'direct_hf_M1_component_norms', 'errors']}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
