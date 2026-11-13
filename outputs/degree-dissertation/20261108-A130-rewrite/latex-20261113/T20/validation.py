#!/usr/bin/env python3
"""T20: explicit coupled-basis and exact angular-momentum convention controls."""
import sys, json, hashlib
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, '/workspace/wiki/tmp/a130-network-control-deps')
import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_3j, wigner_6j, wigner_9j
S=sp.S
HERE=Path(__file__).resolve().parent

def ms(j): return [-j+S(i) for i in range(int(2*j)+1)]
def coupled_component(which):
    # T has single-subsystem RME 1; other subsystem identity. Explicit magnetic sums.
    j1=j2=J=S(1); jp=JP=S(2); k=M=Mp=S(1); q=S(0)
    j1p=jp if which==1 else j1; j2p=jp if which==2 else j2
    total=S(0)
    for m1 in ms(j1):
      for m2 in ms(j2):
       for m1p in ms(j1p):
        for m2p in ms(j2p):
         c0=clebsch_gordan(j1,j2,J,m1,m2,M)
         c1=clebsch_gordan(j1p,j2p,JP,m1p,m2p,Mp)
         if which==1:
          one=(-1)**(j1p-m1p)*wigner_3j(j1p,k,j1,-m1p,q,m1)*int(m2==m2p)
         else:
          one=int(m1==m1p)*(-1)**(j2p-m2p)*wigner_3j(j2p,k,j2,-m2p,q,m2)
         total+=c0*c1*one
    factor=(-1)**(JP-Mp)*wigner_3j(JP,k,J,-Mp,q,M)
    direct=sp.simplify(total/factor)
    if which==1:
     six=wigner_6j(j1p,JP,j2,J,j1,k)
     formula=(-1)**(j1p+j2+J+k)*sp.sqrt((2*J+1)*(2*JP+1))*six
     nine=wigner_9j(j1p,j1,k,j2,j2,0,JP,J,k)
     frozen9=(-1)**(j1+j2+J+k)*six/sp.sqrt((2*j2+1)*(2*k+1))
     correct9=(-1)**(j1p+j2+J+k)*six/sp.sqrt((2*j2+1)*(2*k+1))
    else:
     six=wigner_6j(j2p,JP,j1,J,j2,k)
     formula=(-1)**(j1+j2+JP+k)*sp.sqrt((2*J+1)*(2*JP+1))*six
     nine=wigner_9j(j1,j1,0,j2p,j2,k,JP,J,k)
     frozen9=correct9=None
    product=sp.sqrt((2*J+1)*(2*JP+1)*(2*k+1))*nine*sp.sqrt(2*(j2 if which==1 else j1)+1)
    assert sp.simplify(direct-formula)==0 and sp.simplify(direct-product)==0
    return {'coupled_component':str(sp.simplify(total)), 'WE_factor':str(factor), 'direct_rme':str(direct),'one_body_6j_rme':str(sp.simplify(formula)),'tensor_product_9j_rme':str(sp.simplify(product)),'9j':str(nine),'6j':str(six),'9j_reduction_frozen':str(sp.simplify(frozen9)) if frozen9 is not None else None,'9j_reduction_correct':str(sp.simplify(correct9)) if correct9 is not None else None}

one=coupled_component(1); two=coupled_component(2)
assert one['9j'] != one['9j_reduction_frozen'] and one['9j']==one['9j_reduction_correct']
# 3j-CG counterexample in the same real, integer-rank electromagnetic setting.
ji=k=jf=mi=mf=S(1); q=S(0)
a=wigner_3j(jf,k,ji,-mf,q,mi)
old1=(-1)**(ji-k+mf)*clebsch_gordan(ji,k,jf,mi,q,mf)/sp.sqrt(2*jf+1)
old2=(-1)**(jf-k-mi)*clebsch_gordan(k,ji,jf,q,mi,mf)/sp.sqrt(2*jf+1)
new1=(-1)**(jf-mf)*clebsch_gordan(ji,k,jf,mi,q,mf)/sp.sqrt(2*jf+1)
new2=(-1)**(ji+k-mf)*clebsch_gordan(k,ji,jf,q,mi,mf)/sp.sqrt(2*jf+1)
assert a!=old1 and a==new1==new2
ji=S(1);k=S(1);jf=S(2);mi=S(1);mf=S(1);q=S(0)
a2=wigner_3j(jf,k,ji,-mf,q,mi)
old2b=(-1)**(jf-k-mi)*clebsch_gordan(k,ji,jf,q,mi,mf)/sp.sqrt(2*jf+1)
new2b=(-1)**(ji+k-mf)*clebsch_gordan(k,ji,jf,q,mi,mf)/sp.sqrt(2*jf+1)
assert a2!=old2b and a2==new2b
# Non-equal lower middle/right entries expose accidental index permutation.
j1,j2,j4,j3,j5,j6=map(S,[1,2,2,1,1,2]); xs=[S(1),S(2),S(3)]
terms=[wigner_6j(j1,j2,x,j4,j3,j5) for x in xs]
orth=sp.simplify(sum((2*x+1)*wigner_6j(j1,j2,x,j4,j3,j5)**2 for x in xs))
off=sp.simplify(sum((2*x+1)*wigner_6j(j1,j2,x,j4,j3,j5)*wigner_6j(j1,j2,x,j4,j3,j6) for x in xs))
assert orth==S(1)/3 and off==0
old_terms=[wigner_6j(1,2,x,1,2,2) for x in (1,2,3)]
assert old_terms==[-S(1)/10,S(1)/6,S(1)/15]
# Self-adjoint rank-1 angular momentum: diagonal reduced element is real nonzero.
Jr=sp.sqrt(S(3)/2)
# SI: modern constants (hbar and mp rounded as stated), never mix SI and Gaussian e.
e=1.602176634e-19; hbar=1.054571817e-34; mp=1.67262192595e-27; c=299792458.0
mu=e*hbar/(2*mp); length=hbar/(2*mp*c)/1e-15
results={'coupled_basis':{'quantum_numbers':'j1=j2=J=1, jprime=Jprime=2, k=1, M=Mprime=1, q=0; subsystem RME=1', 'subsystem_1':one,'subsystem_2':two,'interpretation':'The 9j reduction is sign-inconsistent; both separately printed 6j one-body formulas match direct component sums for these cases.'},'cg_phase':{'case_A':'ji=k=jf=mi=mf=1, q=0','three_j':str(a),'frozen_first':str(old1),'correct_first':str(new1),'case_B':'ji=k=mi=mf=1, jf=2, q=0','three_j_B':str(a2),'frozen_second_B':str(old2b),'correct_second_B':str(new2b),'correct_relations_for_integer_k':'3j=(-1)^(jf-mf) C(ji mi,k q|jf mf)/hat(jf) =(-1)^(ji+k-mf) C(k q,ji mi|jf mf)/hat(jf)'},'hermitian':{'example':'spin 1/2, T=J, k=1; hbar=1','diagonal_rme':str(Jr),'frozen_relation_rhs':str(-Jr),'correct_relation_rhs':str(Jr),'correct_exchange_phase':'(-1)^(jf-ji)'},'sixj':{'original_example_values':[str(v) for v in old_terms],'original_weighted_sum':'1/5','unequal_bottom_case':'{1,2,x;2,1,1} versus {1,2,x;2,1,2}, x=1,2,3','diagonal_values':[str(v) for v in terms],'weighted_diagonal':str(orth),'weighted_cross':str(off),'boundary':'Two exact examples only; neither proves all identities or applications.'},'magnetic':{'si_input_constants':'e=1.602176634e-19 C, hbar=1.054571817e-34 J s, mp=1.67262192595e-27 kg, c=299792458 m/s','mu_N_J_per_T':mu,'mu_N_eV_per_T':mu/e,'length_hbar_over_2mpc_fm':length,'B_S_per_e2fm2_for_b_1':length*length,'numeric_b_equal_in_named_units':True},'provenance':{'sympy_version':sp.__version__,'sympy_path':sp.__file__,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
(HERE/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
