#!/usr/bin/env python3
"""Finite-N pairing controls. Analytical finite model; not a Cd/Pd CSM solver.

Same Hamiltonian H= sum e_i N_i - G(P1+P2+h.c.) for exact and BCS,
with e1=-eps,e2=eps, and the diagonal i=j pair term explicitly excluded.
The BCS variational state has <N>=2; exact result is in N=2.
"""
from pathlib import Path
import csv,json,math
OUT=Path(__file__).parent
G=0.8

def pair_model(eps):
    # N=2 seniority-0 matrix [[-2eps,-G],[-G,2eps]].
    root=math.sqrt(4*eps*eps+G*G)
    x_exact=(1+2*eps/root)/2 # lower-pair probability
    coherence=G/root # <P1^dagger P2 + h.c.>
    # Variational BCS with x=v1^2=1-v2^2.
    # E=2eps(1-2x)-2G*x*(1-x); x=min(1,1/2+eps/G).
    x_bcs=min(1.0,0.5+eps/G)
    k_bcs=math.sqrt(max(0.0,x_bcs*(1-x_bcs)))
    E_bcs=2*eps*(1-2*x_bcs)-2*G*x_bcs*(1-x_bcs)
    return {'epsilon_MeV':eps,'two_epsilon_over_G':2*eps/G,'G_MeV':G,
        'E_exact_N2_MeV':-root,'E_BCS_MeV':E_bcs,
        'Delta_BCS_MeV':G*k_bcs,'N_mean_BCS':2.0,'N_var_BCS':8*x_bcs*(1-x_bcs),
        'N_exact':2,'N_var_exact':0.0,'anomalous_pair_amplitude_exact':0.0,
        'pair_transfer_coherence_exact':coherence,'P1daggerP1_exact':x_exact,
        'P2daggerP2_exact':1-x_exact,'number_pair_occupation_var_exact':x_exact*(1-x_exact),
        'HP_expect_exact_MeV':-G*coherence,
        'HP_variance_exact_MeV2':G*G*(1-coherence*coherence),
        'one_body_matrix_between_two_pair_configs':0.0}
rows=[pair_model(0.01*k) for k in range(121)]
with (OUT/'bcs_exact_shellgap_control.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Genuine cranking crossing between different J sectors in the same exact-N model.
# J = 1/2(n1+ + n2+ - n1- - n2-); pair configs J=0;
# blocked (+,+) config J=1 and Hpair=0. Therefore Eground=min(Epair,-omega).
eps=0.2
paired=pair_model(eps); wc=-paired['E_exact_N2_MeV']
crank=[]
for om in [0.0,0.5,wc-1e-4,wc,wc+1e-4,1.2,1.6]:
    before=om<wc
    crank.append({'omega_MeV_per_hbar':om,'omega_c_exact':wc,'Epair_MeV':-wc,
      'Eblocked_MeV':-om,'Eground_MeV':min(-wc,-om),
      'Jground_hbar':'degenerate 0 or 1' if om==wc else (0 if before else 1),
      'pair_coherence_ground':'branch dependent at degeneracy' if om==wc else (paired['pair_transfer_coherence_exact'] if before else 0.0),
      'N_exact':2,'N_var_exact':0.0})
with (OUT/'exact_N_genuine_cranking_crossing.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(crank[0]));w.writeheader();w.writerows(crank)
# Two-level avoided crossing algebra for an effective off-diagonal configuration matrix W.
# E_A=0, E_B=-s(omega-omega0); positive s difference in alignment.
avoided=[]
s=6.0;om0=0.4
for W in (0.0,0.02,0.10):
    for om in (0.30,0.35,0.39,0.40,0.41,0.45,0.50):
        delta=-s*(om-om0)
        root=math.sqrt(delta*delta+4*W*W)
        pB=None if root==0 else (1-delta/root)/2
        avoided.append({'W_effective_MeV':W,'omega':om,'omega0':om0,
          'pB_lower_eigenstate':pB,'J_lower_hbar':None if pB is None else s*pB,
          'E_lower_MeV':(delta-root)/2,
          'minimum_adiabatic_gap_MeV':2*W,
          'mixing_width_estimate_MeV_per_hbar':2*W/s})
with (OUT/'effective_avoided_crossing.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(avoided[0]));w.writeheader();w.writerows(avoided)
summary={
 'scope':'Analytic finite-model demonstrations; no nuclear fit and no full PNC CSM',
 'G_MeV':G,'hamiltonian':'e1*N1+e2*N2-G(P1dagger*P2+P2dagger*P1), e1=-eps,e2=eps, no diagonal self-pair term',
 'BCS_variational_equations':{'v1sq':'x=min(1,0.5+eps/G)','v2sq':'1-x',
  'energy':'2eps*(1-2x)-2G*x*(1-x)','gap':'G*sqrt(x*(1-x))','collapse_epsilon':'G/2'},
 'exact_N2_pair_matrix':'[[-2eps,-G],[-G,2eps]]',
 'exact_pair_coherence':'G/sqrt(4eps^2+G^2)',
 'at_BCS_critical_point':pair_model(G/2),
 'exact_cranking_counterexample':{'eps':eps,'omega_c':wc,'cause':'Exact crossing between distinct conserved-J sectors; exact N alone does not remove a genuine crossing'},
 'avoided_crossing_boundary':'Off-diagonal W smooths a same-symmetry crossing but does not move its center omega0; a delay requires unequal diagonal correlation-energy shifts or frequency-dependent W.',
 'pair_vs_onebody_offdiagonal':'Two pair configurations differ by two occupied orbitals: HP_AB=-G, but any one-body O_AB=0. Pair coherence does not equal one-body off-diagonal alignment.',
 'numerical_generation':'Closed-form formulas evaluated in Python standard library; no stochastic fit or numerical diagonalization claim.'}
(OUT/'pairing_model_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
