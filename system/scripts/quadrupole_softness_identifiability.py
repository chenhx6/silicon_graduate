#!/usr/bin/env python3
"""Finite Legendre-Galerkin gamma model; no nuclear-data inference."""
import csv
import datetime
import hashlib
import json
import platform
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.special import eval_jacobi, eval_legendre, roots_legendre

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs/l4/20261108-shape-softness-identifiability'


def solve(n, nq, kappa, scale=1.0):
    # x=cos(3 gamma), gamma in [0,pi/3], dmu=dx after reorientation.
    # Orthonormal P_l in L2([-1,1], dx). H=scale*(9 L+ kappa*x^2).
    x, w = roots_legendre(nq)
    p = np.vstack([np.sqrt((2*l+1)/2)*eval_legendre(l, x)
                   for l in range(n)]).T
    kin = np.diag(9*np.arange(n)*(np.arange(n)+1.0))
    xmat = (p.T * (w*x)) @ p
    x2mat = (p.T * (w*x*x)) @ p
    en, vec = eigh(scale*(kin + kappa*x2mat))
    ground = vec[:, 0]
    if ground[0] < 0: ground = -ground
    density = (p @ ground)**2
    avg = lambda v: float(np.dot(w, density*v))
    amps = vec.T @ (xmat @ ground)
    return {'n': n, 'nq': nq, 'kappa': kappa, 'scale': scale,
            'norm': avg(np.ones_like(x)), 'x': avg(x), 'x2': avg(x*x),
            'gamma_rms_rad': float(np.sqrt(avg((np.arccos(x)/3-np.pi/6)**2))),
            'e0': float(en[0]), 'gap1': float(en[1]-en[0]),
            'gap2': float(en[2]-en[0]),
            'strength1': float(amps[1]**2),
            'variance_sum': float(np.sum(amps[1:]**2)),
            'ew_strength': float(np.dot(en-en[0], amps**2)),
            'state': ground}


def plot_models(flat, base, scaled):
    """Plot the physical gamma density including its Jacobian, not |psi|^2."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from scipy.integrate import simpson

    matplotlib.rcParams.update({'font.size': 10, 'svg.hashsalt': 'wiki-shape-softness'})
    gamma = np.linspace(0, np.pi/3, 1001)
    x = np.cos(3*gamma)
    basis = np.vstack([np.sqrt((2*l+1)/2)*eval_legendre(l, x)
                       for l in range(len(base['state']))]).T
    densities = [3*np.sin(3*gamma)*(basis @ case['state'])**2
                 for case in (flat, base, scaled)]
    integrals = [float(simpson(density, x=gamma)) for density in densities]
    if any(abs(value-1) > 1e-9 for value in integrals):
        raise AssertionError({'gamma_density_integrals': integrals})
    with (OUT/'gamma-density.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle, lineterminator='\n')
        writer.writerow(['gamma_rad', 'gamma_deg', 'p_flat_per_rad',
                         'p_kappa18_per_rad', 'p_scaled_per_rad'])
        writer.writerows(zip(gamma, np.rad2deg(gamma), *densities))
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), layout='constrained')
    colors = ['#0072B2', '#D55E00', '#009E73']
    labels = [r'$\kappa=0,\ \lambda=1$', r'$\kappa=18,\ \lambda=1$',
              r'$\kappa=18,\ \lambda=3$']
    for density, color, label, style in zip(densities, colors, labels, ['-', '-', '--']):
        axes[0].plot(np.rad2deg(gamma), density, color=color, label=label,
                     linestyle=style, linewidth=2)
    axes[0].set(xlim=(0, 60), ylim=(0, None), xlabel=r'$\gamma$ (degrees)',
                ylabel=r'Probability density $p(\gamma)$ (rad$^{-1}$)',
                title='A. Low moments match; densities differ')
    axes[0].legend(fontsize=9, frameon=False)
    axes[0].text(0.03, 0.04, r'$q_2=1,\ q_3=0$ for all three',
                 transform=axes[0].transAxes, fontsize=9)
    for position, case, color in zip(range(3), (flat, base, scaled), colors):
        for energy in (0.0, case['gap1'], case['gap2']):
            axes[1].hlines(energy, position-0.25, position+0.25, color=color, linewidth=2)
            axes[1].text(position+0.28, energy, f'{energy:.2f}', va='center', fontsize=8)
    axes[1].set(xlim=(-0.5, 2.85), ylim=(-8, 190),
                ylabel='Excitation energy (common model units)',
                title='B. Same static shape, different energy scales')
    axes[1].set_xticks(range(3), ['Flat potential', 'Local minimum', 'Scaled Hamiltonian'],
                      rotation=12, ha='right')
    axes[1].text(0.02, 0.95, r'Only the first three model $0^+$ levels',
                 transform=axes[1].transAxes, va='top', fontsize=9)
    fig.suptitle('Fixed charge Q = 1; I = 0; controlled gamma Hamiltonian', fontsize=12)
    for suffix, metadata in [('png', {'Software': 'Wiki controlled quadrupole model'}),
                             ('pdf', {'CreationDate': None, 'ModDate': None}),
                             ('svg', {'Date': None})]:
        target = OUT/f'shape-versus-dynamics.{suffix}'
        fig.savefig(target, dpi=200, metadata=metadata)
        if suffix == 'svg':
            target.write_text('\n'.join(line.rstrip() for line in
                              target.read_text().splitlines())+'\n')
    plt.close(fig)
    return integrals


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for n in (4, 8, 12, 20, 32):
        for k in (0.0, 18.0):
            records.append(solve(n, max(128, 4*n), k))
    base = solve(32, 256, 18.0)
    scaled = solve(32, 256, 18.0, 3.0)
    flat = solve(32, 256, 0.0)
    finequad = solve(32, 1024, 18.0)
    coarse = next(r for r in records if r['n'] == 4 and r['kappa'] == 18)
    def endpoint_flux(eps):
        xx = np.array([-1+eps, 1-eps])
        derivative = sum(base['state'][l] * np.sqrt((2*l+1)/2)
                         * ((l+1)/2) * eval_jacobi(l-1, 1, 1, xx)
                         for l in range(1, len(base['state'])))
        return float(np.max(np.abs((1-xx**2)*derivative)))
    flux_coarse, flux_fine = endpoint_flux(1e-4), endpoint_flux(1e-8)
    checks = {
        'normalization': abs(base['norm']-1)<1e-12,
        'regular_endpoint_flux_tends_to_zero': flux_fine < 1e-5 and flux_fine < flux_coarse/1000,
        'flat_legendre_spectrum': abs(flat['gap1']-18)<1e-10 and abs(flat['gap2']-54)<1e-10,
        'flat_x2_one_third': abs(flat['x2']-1/3)<1e-12,
        'parity_same_q3': abs(base['x'])<1e-12 and abs(flat['x'])<1e-12,
        'sixth_order_distinguishes': flat['x2']-base['x2']>0.02,
        'scalar_closure': abs(base['variance_sum']-(base['x2']-base['x']**2))<1e-12,
        'scale_wavefunction': np.linalg.norm(base['state']-scaled['state'])<1e-11,
        'scale_all_shown_gaps': abs(scaled['gap1']/base['gap1']-3)<1e-11 and abs(scaled['gap2']/base['gap2']-3)<1e-11,
        'scale_energy_weighted_strength': abs(scaled['ew_strength']/base['ew_strength']-3)<1e-11,
        # For F=x and H=-9 d_x[(1-x^2)d_x]+V(x),
        # 1/2 <[x,[H,x]]> = 9 <1-x^2>. This is an independent
        # differential-operator check of the complete spectral response.
        'double_commutator_sum_rule': abs(base['ew_strength']-9*(base['norm']-base['x2']))<1e-10,
        'deliberately_underresolved_fails_precision': abs(coarse['x2']-base['x2'])>1e-7,
        'galerkin_converged': abs(records[-1]['x2']-records[-3]['x2'])<1e-10,
        'gamma_quadrature_converged': abs(base['gamma_rms_rad']-finequad['gamma_rms_rad'])<1e-6,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()): raise AssertionError(checks)
    allrows = records + [scaled, finequad]
    fields = ['n','nq','kappa','scale','norm','x','x2','gamma_rms_rad','e0','gap1','gap2','strength1','variance_sum','ew_strength']
    with (OUT/'results.csv').open('w', encoding='utf-8', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
        writer.writeheader(); writer.writerows(allrows)
    density_integrals = plot_models(flat, base, scaled)
    checks['plotted_gamma_densities_normalized_with_jacobian'] = True
    data = {'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'command':'python3 system/scripts/quadrupole_softness_identifiability.py',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'artifacts':[{'path':path.relative_to(ROOT).as_posix(),
                          'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
                         for path in sorted(OUT.iterdir())
                         if path.suffix in {'.csv', '.png', '.pdf', '.svg'}],
            'plotted_gamma_density_integrals':density_integrals,
            'python':sys.version, 'numpy':np.__version__, 'scipy':scipy.__version__,
            'matplotlib':version('matplotlib'),
            'platform':platform.platform(), 'random_seed':None,
            'units':'hbar=1, fixed charge Q=1; reference gamma mass M=1/2, lambda=1',
            'basis':'n normalized Legendre polynomials; Gauss-Legendre quadrature',
            'potential':'lambda*18*cos(3gamma)^2; lambda=1 or 3, M=1/(2 lambda)',
            'checks':checks,
            'errors':{'n4_minus_n32_x2':abs(coarse['x2']-base['x2']),
                      'n20_minus_n32_x2':abs(records[-3]['x2']-base['x2']),
                      'nq256_minus_1024_gamma_rms_rad':abs(base['gamma_rms_rad']-finequad['gamma_rms_rad']),
                      'closure_abs':abs(base['variance_sum']-(base['x2']-base['x']**2)),
                      'scaled_ground_l2':float(np.linalg.norm(base['state']-scaled['state'])),
                      'endpoint_flux_eps_1e-4':flux_coarse, 'endpoint_flux_eps_1e-8':flux_fine}}
    (OUT/'run-provenance.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'checks':checks,'errors':data['errors'],
                      'flat':{k:flat[k] for k in fields},
                      'base':{k:base[k] for k in fields},
                      'scaled':{k:scaled[k] for k in fields}}, indent=2))

if __name__ == '__main__': main()
