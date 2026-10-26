#!/usr/bin/env python3
"""Exact finite Fock and Wigner-Eckart normalization controls; not a paper producer."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,datetime
O=Path(__file__).resolve().parent;checks=[]
def check(name,ok,detail=None):
 checks.append({'name':name,'passed':bool(ok),'detail':detail})
 if not ok:raise AssertionError(name)
def zero(n):return [[F(0) for _ in range(n)] for _ in range(n)]
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):
 n=len(a);out=[[F(0) for _ in range(len(b[0]))] for _ in range(n)]
 for i in range(n):
  for k in range(len(b)):
   if a[i][k]:
    for j in range(len(b[0])):
     if b[k][j]:out[i][j]+=a[i][k]*b[k][j]
 return out
def apply(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]
def inner(a,b):return sum(x*y for x,y in zip(a,b))
def close(a,b):return a==b
# Four modes: 0=1, 1=bar1, 2=2, 3=bar2, ascending mode creation convention.
N=16;Id=ident(N);cre=[]
for mode in range(4):
 a=zero(N)
 for mask in range(N):
  if not (mask>>mode)&1:
   sign=(-1)**((mask&((1<<mode)-1)).bit_count())
   a[mask|(1<<mode)][mask]=F(sign)
 cre.append(a)
ann=[transpose(a) for a in cre]
for a in range(4):
 for b in range(4):
  check(f'CAR_creation_annihilation_{a}_{b}',
        add(mul(ann[a],cre[b]),mul(cre[b],ann[a]))==scale(Id,F(a==b)))
# Antiunitary T=U K, real matrix convention T c_i^dag T^-1=c_bar_i^dag; partner -> -c_i^dag.
mapping=[1,0,3,2];phases=[1,-1,1,-1];U=zero(N)
for mask in range(N):
 occupied=[i for i in range(4) if (mask>>i)&1]
 transformed=[mapping[i] for i in occupied]
 inversions=sum(transformed[a]>transformed[b] for a in range(len(transformed)) for b in range(a+1,len(transformed)))
 sign=(-1)**inversions
 for i in occupied:sign*=phases[i]
 destination=sum(1<<i for i in transformed);U[destination][mask]=F(sign)
check('time_reversal_T2_fermion_parity',
      mul(U,U)==[[F(((-1)**i.bit_count()) if i==j else 0) for j in range(N)] for i in range(N)])
for mode in range(4):
 check(f'creation_time_reversal_{mode}',
       mul(mul(U,cre[mode]),transpose(U))==scale(cre[mapping[mode]],F(phases[mode])))
uv=[(F(3,5),F(4,5)),(F(5,13),F(12,13))]
vac=[F(0)]*N;vac[0]=F(1)
for p,(u,v) in enumerate(uv):
 check(f'uv_norm_{p}',u*u+v*v==1)
 pair=mul(cre[2*p],cre[2*p+1])
 vac=apply(add(scale(Id,u),scale(pair,v)),vac)
check('BCS_vacuum_normalized',inner(vac,vac)==1)
check('BCS_vacuum_TR_even',apply(U,vac)==vac)
alpha_dag=[];alpha=[]
for p,(u,v) in enumerate(uv):
 alpha_dag += [add(scale(cre[2*p],u),scale(ann[2*p+1],-v)),
               add(scale(cre[2*p+1],u),scale(ann[2*p],v))]
alpha=[transpose(a) for a in alpha_dag]
for mode in range(4):
 check(f'qp_annihilates_BCS_vacuum_{mode}',apply(alpha[mode],vac)==[F(0)]*N)
qp=[apply(a,vac) for a in alpha_dag]
for a in range(4):
 for b in range(4):check(f'one_qp_orthonormal_{a}_{b}',inner(qp[a],qp[b])==F(a==b))
# Off-diagonal number-conserving one-body operators, unit unbarred matrix element.
normal=add(mul(cre[0],ann[2]),mul(cre[2],ann[0]))
barred=add(mul(cre[1],ann[3]),mul(cre[3],ann[1]))
Teven=add(normal,barred);Todd=add(normal,scale(barred,-1))
check('prototype_even_operator_TR',mul(mul(U,Teven),transpose(U))==Teven)
check('prototype_odd_operator_TR',mul(mul(U,Todd),transpose(U))==scale(Todd,-1))
u1,v1=uv[0];u2,v2=uv[1]
odd_me=inner(qp[0],apply(Todd,qp[2]));even_me=inner(qp[0],apply(Teven,qp[2]))
plus=u1*u2+v1*v2;minus=u1*u2-v1*v2
check('T_odd_scattering_plus_factor',odd_me==plus==F(63,65),str(odd_me))
check('T_even_scattering_minus_factor',even_me==minus==F(-33,65),str(even_me))
# Diagonal T-even operator needs vacuum/core subtraction to isolate qp scattering.
even_diag=add(mul(cre[0],ann[0]),mul(cre[1],ann[1]))
odd_diag=add(mul(cre[0],ann[0]),scale(mul(cre[1],ann[1]),-1))
ve=inner(vac,apply(even_diag,vac));qe=inner(qp[0],apply(even_diag,qp[0]))
qo=inner(qp[0],apply(odd_diag,qp[0]))
check('T_even_diagonal_core_subtraction',qe-ve==u1*u1-v1*v1==F(-7,25))
check('T_odd_diagonal_factor_one',qo==u1*u1+v1*v1==1)
# Analytic unpaired limit independent of selected rational values.
check('unpaired_limit_plus_equals_minus',F(1)*F(1)+F(0)*F(0)==F(1)*F(1)-F(0)*F(0)==1)

def fact(x):
 x=F(x)
 if x.denominator!=1 or x<0:raise ValueError(x)
 return factorial(x.numerator)
def threej_squared(j1,j2,j3,m1,m2,m3):
 j1,j2,j3,m1,m2,m3=map(F,[j1,j2,j3,m1,m2,m3])
 if m1+m2+m3 or any(abs(m)>j for m,j in [(m1,j1),(m2,j2),(m3,j3)]):return F(0)
 if j3>j1+j2 or j3<abs(j1-j2):return F(0)
 terms=[j1+j2-j3,j1-j2+j3,-j1+j2+j3]
 if any(x.denominator!=1 for x in terms+[j1+m1,j2+m2,j3+m3]):return F(0)
 pref=F(fact(terms[0])*fact(terms[1])*fact(terms[2]),fact(j1+j2+j3+1))
 for j,m in [(j1,m1),(j2,m2),(j3,m3)]:pref*=fact(j+m)*fact(j-m)
 lower=max(F(0),j2-j3-m1,j1-j3+m2)
 upper=min(j1+j2-j3,j1-m1,j2+m2)
 if lower>upper:return F(0)
 total=F(0)
 for z in range(int(lower),int(upper)+1):
  args=[F(z),j1+j2-j3-z,j1-m1-z,j2+m2-z,j3-j2+m1+z,j3-j1-m2+z]
  denom=1
  for x in args:denom*=fact(x)
  total+=F((-1)**z,denom)
 return pref*total*total
def m_values(j):return [-j+i for i in range(int(2*j)+1)]
# Wigner-Eckart convention: matrix=(-1)^(Jf-Mf) 3j(Jf,k,Ji;-Mf,q,Mi) R.
reduced_squared=F(9,4);we_results=[]
for Ji,Jf,k in [(F(1,2),F(3,2),F(1)),(F(3,2),F(1,2),F(1)),
                (F(3,2),F(3,2),F(2)),(F(5,2),F(3,2),F(2)),(F(3,2),F(3,2),F(0))]:
 rows=[];total=F(0)
 for Mi in m_values(Ji):
  amount=F(0);transitions=[]
  for Mf in m_values(Jf):
   for q in m_values(k):
    sq=threej_squared(Jf,k,Ji,-Mf,q,Mi)
    amount+=sq*reduced_squared
    if sq:transitions.append({'Mf':str(Mf),'q':str(q),'matrix_element_squared':str(sq*reduced_squared)})
  check(f'WE_fixed_Mi_sum_Ji{Ji}_Jf{Jf}_k{k}_Mi{Mi}',amount==reduced_squared/(2*Ji+1),str(amount))
  total+=amount;rows.append({'Mi':str(Mi),'sum_Mf_q':str(amount),'transitions':transitions})
 check(f'WE_all_Mi_sum_reduced_Ji{Ji}_Jf{Jf}_k{k}',total==reduced_squared)
 check(f'WE_initial_average_Ji{Ji}_Jf{Jf}_k{k}',total/(2*Ji+1)==reduced_squared/(2*Ji+1))
 we_results.append({'Ji':str(Ji),'Jf':str(Jf),'rank':str(k),'reduced_matrix_element_squared':str(reduced_squared),'B':str(reduced_squared/(2*Ji+1)),'rows':rows})
# Independent known CG stretched coupling of 1/2 and1 to3/2, Mi=+1/2.
for q,expected in [(F(-1),F(1,12)),(F(0),F(1,6)),(F(1),F(1,4))]:
 check(f'known_CG_1half_to3half_q{q}',
       threej_squared(F(3,2),1,F(1,2),-(F(1,2)+q),q,F(1,2))==expected)
check('WE_detailed_balance_same_Hermitian_tensor',
      (2*F(1,2)+1)*F(we_results[0]['B'])==(2*F(3,2)+1)*F(we_results[1]['B']))
r={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'scope':'Exact selected controls, not1978 original or author code/actual133Ce calculation',
   'fock_modes':['1','bar1','2','bar2'],'Fock_dimension':16,
   'time_reversal_convention':'T c_i^dag T^-1=c_bar_i^dag, T c_bar_i^dag T^-1=-c_i^dag; real U and complex conjugation',
   'toy_BCS_uv':[{'u':str(u),'v':str(v)} for u,v in uv],
   'BCS_scattering':{'odd_direct_Fock':str(odd_me),'even_direct_Fock':str(even_me),'plus_formula':str(plus),'minus_formula':str(minus),
                     'T_even_diagonal_vacuum_expectation':str(ve),'T_even_diagonal_qp_expectation':str(qe),'T_even_diagonal_connected':str(qe-ve)},
   'WE_normalization':we_results,
   'checks':checks,'all_pass':all(x['passed'] for x in checks),
   'nonclaims':['No actual lambda, gap, operator normalization or source state recovered',
                'No1978 fulltext read','No spinor phase reconstruction for every body-fixed source orbital',
                'Single-particle coherence factors do not multiply whole core+particle E2/M1 by one number']}
(O/'fallback-results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
print(json.dumps({'all_pass':r['all_pass'],'check_count':len(checks),'BCS':r['BCS_scattering'],
                  'WE_B':[{'Ji':x['Ji'],'Jf':x['Jf'],'rank':x['rank'],'B':x['B']} for x in we_results]},ensure_ascii=False,indent=2))
