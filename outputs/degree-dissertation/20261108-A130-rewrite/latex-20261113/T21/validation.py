#!/usr/bin/env python3
"""T21 finite path enumeration, one-nucleon GT algebra and beta prefactor checks."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math

HERE=Path(__file__).resolve().parent

def paths(graph, start):
    """Enumerate complete paths; each edge is (probability, emitted n, next node)."""
    pending=[(start,0,F(1),())]; final=[]
    while pending:
        node,n,p,route=pending.pop()
        if node not in graph:
            final.append((node,n,p,route)); continue
        assert sum((e[0] for e in graph[node]),F())==1
        for w,dest_n,dest in graph[node]:
            pending.append((dest,n+dest_n,p*w,route+(node+'->'+dest,)))
    return final

def distribution(graph,start):
    out={}
    for terminal,n,p,_ in paths(graph,start):
        key=(terminal,n);out[key]=out.get(key,F())+p
    assert sum(out.values(),F())==1
    return {str(k):str(v) for k,v in sorted(out.items())}

cases={
 'pure_1n':({'a':[(F(1),1,'stable')]},'a'),
 'gamma_competition':({'a':[(F(1,4),0,'stable'),(F(3,4),1,'stable')]},'a'),
 'sequential_2n':({'a':[(F(1),1,'b')],'b':[(F(1,3),0,'stable'),(F(2,3),1,'stable')]},'a'),
 'fission_joint_terminal':({'a':[(F(1,2),1,'stable'),(F(1,2),2,'fission')]},'a')}
checked={name:distribution(*case) for name,case in cases.items()}
assert checked['pure_1n']=={"('stable', 1)":'1'}
assert checked['gamma_competition']=={"('stable', 0)":'1/4',"('stable', 1)":'3/4'}
assert checked['sequential_2n']=={"('stable', 1)":'1/3',"('stable', 2)":'2/3'}
# Same system, distinct normalization of beta events and all parent decays.
beta=F(4,5)
beta_per_parent={'0':str(beta*F(1,4)), '1':str(beta*F(3,4)), 'sum':str(beta)}
all_parent_other_alpha={'0':str(beta*F(1,4)+(1-beta)), '1':str(beta*F(3,4))}
all_parent_other_1n_fission={'0':str(beta*F(1,4)), '1':str(beta*F(3,4)+(1-beta))}
# Pauli spin operators act on an initial spin-up/down neutron; t_- maps n to p.
sigmas=[((0,1),(1,0)),((0,-1j),(1j,0)),((1,0),(0,-1))]
def apply(mat,v):return tuple(sum(row[j]*v[j] for j in range(2)) for row in mat)
def norm2(v):return sum(abs(z)**2 for z in v)
spin_strength=[sum(norm2(apply(m,v)) for m in sigmas) for v in ((1,0),(0,1))]
assert spin_strength==[3,3]
# A 1n->gamma path loses its earlier neutron in an unaugmented terminal category.
carry_graph={'a':[(F(1),1,'b')], 'b':[(F(1),0,'stable')]}
carry=distribution(carry_graph,'a')
assert carry=={"('stable', 1)":'1'}
# j=9/2: Omega=5, v=1. The reference n=v is a lowest-weight state.
Omega=5; seniority=1; sample_n=[1,3,5,7,9]
seniority_frozen_cg=[str(F(n-Omega,Omega-seniority)) for n in sample_n]
seniority_lowest=[str(F(Omega-n,Omega-seniority)) for n in sample_n]
assert seniority_frozen_cg[0]=='-1' and seniority_lowest[0]=='1'
assert Omega not in list(range(2,2*Omega-2+1,2))
# t+ acting on neutron gives 0; scaling both GT amplitudes by q scales S difference by q^2.
q=F(7,10); scaled=3*q*q
# Illustrative uncorrected phase-space constant, assumptions explicitly recorded.
GF=1.16638e-11;Vud=0.974;me=0.51099895;hbar=6.582119569e-22
K=2*math.pi**3*hbar*math.log(2)/(GF**2*Vud**2*me**5)
result={'model':'Discrete Markov decay paths, transition-independent full absorption; no fit to a measured nucleus.', 'cascade_paths':checked,'frozen_recursion_failure':'For a --1n--> stable, frozen formula returns Pi_0(a)=1 and Pi_1(a)=0 because x is never decremented.','markov_memory':{'network':'a --1n--> b --gamma--> stable','path_result':carry,'without_count_augmented_state':'terminal exit of b alone is a 0n step; it cannot encode the earlier 1n without remembering history','boundary':'A total neutron count or an equivalent sufficient history must be part of the state or represented by a generating function.'},'seniority':{'j':'9/2','Omega':Omega,'v':seniority,'allowed_n':sample_n,'frozen_top_denominator_ratios':seniority_frozen_cg,'lowest_reference_correct_ratios':seniority_lowest,'v2_allowed_n':[2,4,6,8],'v2_half_filling_accessible':False},'normalization':{'beta_branch':str(beta),'beta_conditional_gamma_competition':{'0':'1/4','1':'3/4','sum':'1'},'beta_delayed_per_parent':beta_per_parent,'all_parent_neutron_multiplicity_with_other_alpha':all_parent_other_alpha,'all_parent_neutron_multiplicity_with_other_fission_one_neutron':all_parent_other_1n_fission,'boundary':'Other neutron-producing channels are not beta-delayed even if they contribute to ungated counts.'},'ikeda_one_neutron':{'spin_up_strength_minus':spin_strength[0],'spin_down_strength_minus':spin_strength[1],'strength_plus':0,'initial_M_sum_without_division':sum(spin_strength),'two_Ji_plus_one':2,'initial_M_average':3,'N_minus_Z':1,'bare_difference':3,'q':str(q),'q_scaled_difference':str(scaled),'boundary':'Single-nucleon test of convention, not a proof of many-body sum rule.'},'beta_prefactor':{'GF_MeV_minus_2':GF,'Vud_illustrative':Vud,'electron_rest_energy_MeV':me,'hbar_MeV_s':hbar,'K_uncorrected_seconds':K,'boundary':'Leading-order illustrative normalization with gV=1; do not equate this constant to tabulated K without matching electroweak and radiative correction conventions.'},'provenance':{'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runtime':'Python standard library only'}}
(HERE/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
