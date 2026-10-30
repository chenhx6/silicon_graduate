#!/usr/bin/env python3
"""Synthetic two-configuration shears demonstration; no isotope is fitted.

Angular momenta are in hbar, energies in MeV, M1 strengths in mu_N^2,
and E2 strengths in e^2 b^2. The core-free model uses classical vectors.
Diagonal transition kernels and their relative signs are assumptions.
"""
from pathlib import Path
import json
import numpy as np

OUT = Path(__file__).resolve().parent
CONFIG = {
    'a': dict(jp=11.0, jn=14.5, V2=1.2, delta_g=0.7, Q=0.5),
    'b': dict(jp=11.0, jn=18.5, V2=1.8, delta_g=0.7, Q=0.5),
}
IC = 24.5
W = 0.04


def geometry(I, p):
    c = (I*I-p['jp']**2-p['jn']**2)/(2*p['jp']*p['jn'])
    if abs(c) > 1+1e-12:
        raise ValueError('Spin outside classical triangle domain')
    c = float(np.clip(c, -1, 1))
    theta = float(np.arccos(c))
    sin_theta_p = p['jn']*np.sin(theta)/I
    return c, theta, sin_theta_p


def raw_energy(I, p):
    c, _, _ = geometry(I, p)
    return p['V2']*(3*c*c-1)/2


OFFSET_B = raw_energy(IC, CONFIG['a'])-raw_energy(IC, CONFIG['b'])


def states(I):
    ea = raw_energy(I, CONFIG['a'])
    eb = raw_energy(I, CONFIG['b'])+OFFSET_B
    e, u = np.linalg.eigh([[ea, W], [W, eb]])
    return e, u, [ea, eb]


def unmixed_B(I, p, multipole):
    _, _, sp = geometry(I, p)
    if multipole == 'M1':
        return 3/(8*np.pi)*(p['delta_g']*p['jp']*sp)**2
    return 15/(32*np.pi)*p['Q']**2*sp**4


records = []
for I in np.arange(22.5, 25.51, 1.0):
    e, u, bare = states(float(I))
    rec = {'I_hbar':float(I), 'bare_E_MeV':bare, 'mixed_E_MeV':e.tolist(),
           'lower_a_probability':float(u[0,0]**2), 'gap_MeV':float(e[1]-e[0]),
           'theta_deg':{k:float(np.degrees(geometry(I,p)[1])) for k,p in CONFIG.items()},
           'transitions':{}}
    for multipole, delta_I in [('M1',1),('E2',2)]:
        If = I-delta_I
        try:
            _, uf, _ = states(float(If))
        except ValueError:
            rec['transitions'][multipole] = {'status':'final spin outside one configuration domain'}
            continue
        strengths = [unmixed_B(I,p,multipole) for p in CONFIG.values()]
        kernels = np.diag(np.sqrt((2*I+1)*np.array(strengths)))
        mixed_kernel = uf.T @ kernels @ u
        mixed_B = np.abs(mixed_kernel)**2/(2*I+1)
        rec['transitions'][multipole] = {
            'I_final_hbar':float(If), 'pure_B':list(map(float,strengths)),
            'mixed_B_final_rows_initial_columns':mixed_B.tolist(),
            'sum_all_mixed_B':float(mixed_B.sum()),
            'sum_all_pure_B':float(sum(strengths)),
            'assumptions':'Real positive diagonal kernels; off-diagonal kernels zero; independent mixing at initial and final spins.'}
    records.append(rec)
result = {'kind':'synthetic-demonstration-not-fit','configurations':CONFIG,
          'crossing_spin_hbar':IC,'W_MeV':W,'offset_b_MeV':OFFSET_B,
          'minimum_continuous_gap_MeV':2*abs(W),
          'evidence_boundary':'No experimental V2, W, mixing angle or isotope-specific fit is inferred.',
          'records':records}
(OUT/'multi-band-shears-mixing-model.json').write_text(json.dumps(result,indent=2)+'\n')
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    grid=np.linspace(22.5,25.5,301)
    bare=np.array([states(i)[2] for i in grid]);mixed=np.array([states(i)[0] for i in grid])
    fig,axs=plt.subplots(1,3,figsize=(12,3.6))
    for k in range(2):
        axs[0].plot(grid,bare[:,k],ls='--',label=f'bare {"ab"[k]}')
        axs[0].plot(grid,mixed[:,k],label=['lower','upper'][k])
    axs[0].set_ylabel('Energy (MeV; arbitrary zero)');axs[0].legend(fontsize=7)
    axs[1].plot(grid,[states(i)[1][0,0]**2 for i in grid]);axs[1].set_ylabel('a probability in lower state')
    for key,p in CONFIG.items():axs[2].plot(grid,[np.degrees(geometry(i,p)[1]) for i in grid],label=key)
    axs[2].set_ylabel('Shears opening angle (degree)');axs[2].legend()
    for ax in axs:ax.set_xlabel('I / hbar');ax.axvline(IC,color='grey',lw=.7);ax.grid(alpha=.2)
    fig.suptitle('Synthetic two-configuration shears model: no isotope fit')
    fig.tight_layout();fig.savefig(OUT/'multi-band-shears-mixing-model.svg');plt.close(fig)
except ImportError:
    pass
print(json.dumps({'output':str(OUT/'multi-band-shears-mixing-model.json'),'kind':result['kind'],'grid_rows':len(records),'gap_at_bare_crossing_MeV':states(IC)[0][1]-states(IC)[0][0]}))
