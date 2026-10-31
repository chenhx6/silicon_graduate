#!/usr/bin/env python3
"""PRD calibration graph and conditional blind directions, not an experiment fit.

Central fit-1 coefficients are transcribed from Regis 2011 p.44 Eq.4.13.
No parameter covariance or error distribution is reconstructed from marginal
printed errors. The adversarial drift is a declared synthetic control only.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def exact_rank(rows):
    a=[[F(x) for x in row] for row in rows]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        divisor=a[rank][j];a[rank]=[v/divisor for v in a[rank]]
        for i in range(len(a)):
            if i==rank:continue
            divisor=a[i][j]
            a[i]=[x-divisor*y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    q=p.parse_args()
    a,b,c,d=-826391.0,3316.85,-1.28444,14104.7
    def curve(E):return a/math.sqrt(b+E)+c*E+d
    def prd(Ef,Ed):return curve(Ef)-curve(Ed)
    checks=[]
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    # Nodes are gamma energies, oriented edges denote an ordered feeder/decay
    # combination. This is a mathematical calibration model, not new event data.
    nodes=[244,344,444,609,1120]
    chain=list(zip(nodes[1:],nodes[:-1]))
    edges=chain+[(444,244),(244,444)]
    incidence=[[int(n==u)-int(n==v) for n in nodes] for u,v in edges]
    ranks={'chain':exact_rank(incidence[:4]),'with_mirrored_edge':exact_rank(incidence)}
    check('connected graph rank n-1',ranks['chain']==len(nodes)-1)
    check('mirrored edges do not increase rank',ranks['with_mirrored_edge']==ranks['chain'])
    for E in nodes:check(f'self PRD zero at {E}',prd(E,E)==0)
    cycles=[]
    for u,v,w in [(444,344,244),(1120,609,444),(1120,444,244)]:
        residual=prd(u,w)-prd(u,v)-prd(v,w)
        check(f'telescoping calibration cycle {u}/{v}/{w}',abs(residual)<1e-10)
        cycles.append({'energies_keV':[u,v,w],'residual_ps':residual})
    for u,v in edges:
        shifted_prd=(curve(u)+10000)-(curve(v)+10000)
        check(f'gauge offset cancellation {u}/{v}',math.isclose(shifted_prd,prd(u,v),abs_tol=1e-10))
    # Recover node potentials from the tree, up to a shared time-origin offset.
    recovered={nodes[0]:0.0}
    for u,v in chain:recovered[u]=recovered[v]+prd(u,v)
    for E in nodes:check(f'gauge-fixed tree recovery {E}',math.isclose(recovered[E],curve(E)-curve(nodes[0]),abs_tol=1e-10))
    pair_values=[{'Ef_keV':u,'Ed_keV':v,'deltaE_keV':u-v,'PRD_ps':prd(u,v)}
                 for u,v in [(800,400),(1000,600)]]
    check('equal energy differences do not fix PRD',abs(pair_values[0]['PRD_ps']-pair_values[1]['PRD_ps'])>40)
    # Compare only central printed values, at their available rounding precision.
    check('published central 1120/609 PRD ~126 ps',abs(prd(1120,609)-126)<.5)
    check('published central 344/609 shift ~-129 ps',abs(prd(344,609)+129)<.5)
    # A gradient-shaped calibration error is invisible to all cycle tests.
    h=lambda E:.02*E
    biased=lambda u,v:prd(u,v)+h(u)-h(v)
    blind_cycles=[]
    for u,v,w in [(444,344,244),(1120,609,244)]:
        residual=biased(u,w)-biased(u,v)-biased(v,w)
        check(f'gradient drift passes cycle test {u}/{v}/{w}',abs(residual)<1e-10)
        blind_cycles.append(residual)
    target=(1120,609);tau=20
    observed_dc=prd(*target)+2*tau
    biased_tau=(observed_dc-biased(*target))/2
    check('cycle closure is insufficient for unbiased lifetime',math.isclose(biased_tau,14.89,abs_tol=1e-10))
    # A single non-gradient edge perturbation, in contrast, is cycle-visible.
    corruption=8.0
    corrupted_residual=(prd(444,244)+corruption)-prd(444,344)-prd(344,244)
    check('non-gradient edge error has detectable cycle residual',math.isclose(corrupted_residual,8.0,abs_tol=1e-10))
    raw=Path('raw/theses/degree-dissertation/LaBr3时间.pdf')
    check('source hash',hashlib.sha256(raw.read_bytes()).hexdigest()=='54ef3c5b70d7ef4ed694ad9089fa40533d39e2bb060228eb3d1a304b03555f52')
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'printed central calibration-curve evaluation and synthetic identifiability controls; no fit/CI',
      'source_locator':'Regis2011 PDF44 Eq4.13 fit1; PDF48 Eqs4.15/4.18',
      'coefficients':{'a_ps_sqrtkeV':a,'b_keV':b,'c_ps_per_keV':c,'d_ps':d},
      'nodes_keV':nodes,'edges_keV':edges,'incidence_matrix':incidence,'exact_ranks':ranks,
      'gauge_fixed_potentials_ps':recovered,'cycles':cycles,'same_deltaE_pairs':pair_values,
      'printed_central_controls':{'PRD_1120_609_ps':prd(1120,609),'shift_344_609_ps':prd(344,609)},
      'synthetic_gradient_error':{'h_ps':'.02*E_keV','cycle_residuals_ps':blind_cycles,
        'target_pair_keV':target,'input_tau_ps':tau,'apparent_tau_ps':biased_tau},
      'synthetic_single_edge_cycle_residual_ps':corrupted_residual,
      'covariance_not_recovered':True,'checks':checks,'check_count':len(checks)}
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'ranks':ranks,'same_deltaE':pair_values,'blind_direction_tau':biased_tau},indent=2))


if __name__=='__main__':main()
