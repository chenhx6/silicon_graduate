#!/usr/bin/env python3
"""Selected single-j algebra control. No paper producer, data or model fit."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt, sqrt
import json, hashlib, datetime
import numpy as np

OUT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    checks.append({'name':name,'passed':bool(ok),'detail':detail})
    if not ok: raise AssertionError(name)

def squarefree(n):
    """sqrt(n)=s sqrt(d), positive integer n; exact trial division."""
    if n==0:return 0,1
    s=1;d=n;f=2
    while f*f<=d:
        while d%(f*f)==0:s*=f;d//=f*f
        f+=1
    return s,d

class E:
    """Finite sum c_d sqrt(d), c_d=(rational real,rational imaginary)."""
    def __init__(self,terms=None):
        self.t={d:(F(r),F(i)) for d,(r,i) in (terms or {}).items() if r or i}
    @staticmethod
    def scalar(x):return x if isinstance(x,E) else E({1:(F(x),F(0))})
    @staticmethod
    def root(n):
        s,d=squarefree(n);return E({d:(F(s),F(0))})
    def __add__(self,o):
        o=E.scalar(o);t=dict(self.t)
        for d,(r,i) in o.t.items():
            a,b=t.get(d,(F(0),F(0)));t[d]=(a+r,b+i)
        return E(t)
    __radd__=__add__
    def __neg__(self):return E({d:(-r,-i) for d,(r,i) in self.t.items()})
    def __sub__(self,o):return self+-E.scalar(o)
    def __rsub__(self,o):return E.scalar(o)+-self
    def __mul__(self,o):
        o=E.scalar(o);t={}
        for d,(r,i) in self.t.items():
            for e,(s,j) in o.t.items():
                a,b=squarefree(d*e);rr=(r*s-i*j)*a;ii=(r*j+i*s)*a
                u,v=t.get(b,(F(0),F(0)));t[b]=(u+rr,v+ii)
        return E(t)
    __rmul__=__mul__
    def conj(self):return E({d:(r,-i) for d,(r,i) in self.t.items()})
    def __eq__(self,o):return self.t==E.scalar(o).t
    def floating(self):return sum(complex(float(r),float(i))*sqrt(d) for d,(r,i) in self.t.items())
    def serial(self):return {str(d):{'real':str(r),'imag':str(i)} for d,(r,i) in sorted(self.t.items())}

Z=E();ONE=E.scalar(1);II=E({1:(F(0),F(1))})
def zeros(n,m=None):return [[E() for _ in range(n if m is None else m)] for _ in range(n)]
def ident(n):return [[E.scalar(i==j) for j in range(n)] for i in range(n)]
def madd(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def mm(a,b):
    n=len(a);k=len(b);m=len(b[0]);out=zeros(n,m)
    for i in range(n):
        for l in range(k):
            if not a[i][l].t:continue
            for j in range(m):
                if b[l][j].t:out[i][j]=out[i][j]+a[i][l]*b[l][j]
    return out

def dag(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def conjugate(a):return [[x.conj() for x in row] for row in a]
def same(a,b):return all(x==y for r,s in zip(a,b) for x,y in zip(r,s))
def sub(a,b):return madd(a,scale(b,-1))
def extract(a,ix):return [[a[i][j] for j in ix] for i in ix]
def serial(a):return [[x.serial() for x in row] for row in a]
def floating(a):return np.array([[x.floating() for x in row] for row in a],dtype=complex)
def exact_spin(j):
    ms=[-j+i for i in range(int(2*j)+1)];n=len(ms);plus=zeros(n);z=zeros(n);u=zeros(n)
    for k,m in enumerate(ms):
        z[k][k]=E.scalar(m)
        u[n-1-k][k]=E.scalar((-1)**int(j-m))
        if k<n-1:
            c=j*(j+1)-m*(m+1);assert c.denominator==1
            plus[k+1][k]=E.root(c.numerator)
    minus=dag(plus);x=scale(madd(plus,minus),F(1,2));y=scale(sub(plus,minus),-II*F(1,2))
    return ms,{'x':x,'y':y,'z':z},plus,minus,u

def ladder_action(j,m,direction):
    dest=m+direction
    if abs(dest)>j:return None,F(0)
    # Independent closed action formula (not read from the generated matrices).
    squared=(j-m)*(j+m+1) if direction==1 else (j+m)*(j-m+1)
    return dest,squared

def numeric_spin(j):
    """Independent float matrix generation directly from m destination/action."""
    ms=np.arange(-j,j+1,1.0);n=len(ms);jp=np.zeros((n,n),complex)
    for col,m in enumerate(ms):
        if m+1<=j:jp[col+1,col]=np.sqrt((j-m)*(j+m+1))
    jm=jp.conj().T
    return [(jp+jm)/2,(jp-jm)/(2j),np.diag(ms)]

j=F(11,2);m=F(9,2)
ms,ops,jp,jm,U=exact_spin(j);n=len(ms);I=ident(n)
ix=[ms.index(m),ms.index(-m)];q=[i for i in range(n) if i not in ix]
P=zeros(n)
for k in ix:P[k][k]=ONE
Q=sub(I,P)
check('P_Hermitian',same(P,dag(P)))
check('P_idempotent',same(mm(P,P),P))
check('Q_orthogonal_complement',same(mm(P,Q),zeros(n)))
check('ladder_hermiticity',same(jm,dag(jp)))
for k in ops:check('Hermitian_'+k,same(ops[k],dag(ops[k])))
check('exact_SU2_xy',same(sub(mm(ops['x'],ops['y']),mm(ops['y'],ops['x'])),scale(ops['z'],II)))
check('exact_Casimir',same(madd(madd(mm(ops['x'],ops['x']),mm(ops['y'],ops['y'])),mm(ops['z'],ops['z'])),scale(I,j*(j+1))))
check('exact_T_squared_minus_identity',same(mm(U,conjugate(U)),scale(I,-1)))
check('exact_TR_projector_invariant',same(mm(mm(U,conjugate(P)),dag(U)),P))
for k,a in ops.items():check('exact_TR_odd_'+k,same(mm(mm(U,conjugate(a)),dag(U)),scale(a,-1)))

projected={};leaks={};smallI=ident(2)
expected_second={'x':F(31,4),'y':F(31,4),'z':F(81,4)}
for k,a in ops.items():
    b=extract(a,ix);a2=extract(mm(a,a),ix);b2=mm(b,b)
    leak=extract(mm(mm(a,Q),a),ix)
    check('compression_identity_'+k,same(sub(a2,b2),leak))
    check('second_moment_'+k,same(a2,scale(smallI,expected_second[k])))
    check('leak_exact_diagonal_PSD_'+k,same(leak,scale(smallI,F(31,4) if k in ['x','y'] else 0)))
    check('second_TR_even_'+k,same(mm(mm(extract(U,ix),conjugate(a2)),dag(extract(U,ix))),a2))
    projected[k]={'PjP':serial(b),'Pj2P':serial(a2),'PjP_squared':serial(b2),'leakage':serial(leak)}
    leaks[k]=leak
check('projected_x_zero',same(extract(ops['x'],ix),zeros(2)))
check('projected_y_zero',same(extract(ops['y'],ix),zeros(2)))
check('projected_z_exact',same(extract(ops['z'],ix),[[E.scalar(m),Z],[Z,E.scalar(-m)]]))
# Lost commutator is carried by the Q-space cross terms.
xy_leak=extract(sub(mm(mm(ops['x'],Q),ops['y']),mm(mm(ops['y'],Q),ops['x'])),ix)
check('projected_SU2_leakage_balance',same(xy_leak,scale(extract(ops['z'],ix),II)))

# Exact independently evaluated ladder paths and analytic second moment.
lad=[]
for state in [m,-m,j,-j]:
    branches=[]
    for d in [1,-1]:
        dest,c2=ladder_action(j,state,d);branches.append({'direction':d,'destination_m':str(dest),'amplitude_squared':str(c2),'jx_amplitude_squared':str(c2/4)})
    transverse=sum(F(x['amplitude_squared'])/4 for x in branches)
    formula=(j*(j+1)-state*state)/2
    check('ladder_analytic_second_moment_m_'+str(state),transverse==formula)
    ii=ms.index(state)
    check('ladder_matrix_second_moment_m_'+str(state),ops['x'] and mm(ops['x'],ops['x'])[ii][ii]==E.scalar(formula))
    lad.append({'m':str(state),'branches':branches,'transverse_second_moment':str(transverse),'analytic_formula':str(formula)})
check('highest_weight_transverse_j_over_2',F(lad[2]['transverse_second_moment'])==j/2)

# Kramers-selected 2x2 time reversal: basis is [+m,-m].
smallU=extract(U,ix)
check('selected_T_squared_minus_identity',same(mm(smallU,conjugate(smallU)),scale(smallI,-1)))
# Any TR-even Hermitian 2x2 operator is scalar for this irreducible Kramers pair.
paulis=[[[Z,ONE],[ONE,Z]],[[Z,-II],[II,Z]],[[ONE,Z],[Z,-ONE]]]
for k,s in enumerate(paulis):check('selected_pauli_TR_odd_'+str(k),same(mm(mm(smallU,conjugate(s)),dag(smallU)),scale(s,-1)))

# Controls where compressing transverse first is not zero: m=1/2.
ixhalf=[ms.index(F(1,2)),ms.index(-F(1,2))]
check('m_half_projected_x_nonzero',not same(extract(ops['x'],ixhalf),zeros(2)))
check('m_half_projected_x_offdiag_3',extract(ops['x'],ixhalf)[0][1]==3)
halfx=extract(ops['x'],ixhalf)
halfleak=sub(extract(mm(ops['x'],ops['x']),ixhalf),mm(halfx,halfx))
check('m_half_transverse_leak_35_over_4',same(halfleak,scale(smallI,F(35,4))))
check('selected_projected_SU2_not_closed',not same(sub(mm(extract(ops['x'],ix),extract(ops['y'],ix)),mm(extract(ops['y'],ix),extract(ops['x'],ix))),scale(extract(ops['z'],ix),II)))
rankone=zeros(n);rankone[ix[0]][ix[0]]=ONE
check('rankone_orientation_not_TR_invariant',not same(mm(mm(U,conjugate(rankone)),dag(U)),rankone))
for k,a in ops.items():
    fullQ=sub(I,I)
    check('full_space_zero_leakage_'+k,same(mm(mm(a,fullQ),a),zeros(n)))

# Independent floating path and external tensor factor; selected algebra control only.
J=numeric_spin(5.5);exactJ=[floating(ops[k]) for k in ['x','y','z']]
floatdiff=max(float(np.max(np.abs(a-b))) for a,b in zip(J,exactJ))
check('independent_float_vs_exact_ladder_matrices',floatdiff<1e-13,floatdiff)
L=2;X=numeric_spin(L);dX=len(X[0]);A=[F(1,3),F(2,5),F(1,2)]
H=np.zeros((dX*n,dX*n),complex)
for a,x,jk in zip(A,X,J):
    v=np.kron(x,np.eye(n))-np.kron(np.eye(dX),jk)
    H+=float(a)*(v@v)
check('external_H_Hermitian',np.max(np.abs(H-H.conj().T))<1e-12)
sel=np.zeros((n,2))
for col,row in enumerate(ix):sel[row,col]=1
W=np.kron(np.eye(dX),sel);Hp=W.conj().T@H@W
Hnaive=np.zeros_like(Hp)
for a,x,jk in zip(A,X,J):
    jsmall=sel.T@jk@sel
    v=np.kron(x,np.eye(2))-np.kron(np.eye(dX),jsmall)
    Hnaive+=float(a)*(v@v)
recoil=F(31,4)*(A[0]+A[1]);res=float(np.max(np.abs(Hp-Hnaive-float(recoil)*np.eye(len(Hp)))))
check('projected_H_recoil_identity',res<1e-12,res)
_,_,_,_,UX=exact_spin(F(L));Ut=np.kron(floating(UX),floating(U))
trres=float(np.max(np.abs(Ut@H.conj()@Ut.conj().T-H)))
check('external_H_TR_even',trres<1e-12,trres)
check('external_total_T_squared_minus_identity',np.max(np.abs(Ut@Ut.conj()+np.eye(len(Ut))))<1e-13)
# Classical fixed +m vector (not Kramers pair) agrees with naive +sector only, lacks recoil.
Hclass=sum(float(a)*((x-(float(m) if k==2 else 0)*np.eye(dX))@(x-(float(m) if k==2 else 0)*np.eye(dX))) for k,(a,x) in enumerate(zip(A,X)))
plusids=[2*a for a in range(dX)]
plusres=float(np.max(np.abs(Hp[np.ix_(plusids,plusids)]-Hclass-float(recoil)*np.eye(dX))))
check('classical_plus_sector_recoil_difference',plusres<1e-12,plusres)
# Nested subspaces at fixed H and fixed energy zero.
spaces=[('P_m9pair',ix),('P_m9_m7pairs',ix+[ms.index(F(7,2)),ms.index(F(-7,2))]),('full',list(range(n)))]
spectra=[]
for name,indices in spaces:
    s=np.eye(n)[:,indices];w=np.kron(np.eye(dX),s);h=w.conj().T@H@w;e=np.linalg.eigvalsh(h)
    pairres=float(np.max(np.abs(e[::2]-e[1::2])))
    check('Kramers_degeneracy_'+name,pairres<1e-11,pairres)
    spectra.append({'space':name,'intrinsic_m':[str(ms[i]) for i in indices],'dimension':len(e),'eigenvalues':e.tolist(),'Kramers_pair_max_gap':pairres})
vari=[]
for small,large in zip(spectra,spectra[1:]):
    se=np.array(small['eigenvalues']);le=np.array(large['eigenvalues'])[:len(se)];margin=se-le
    check('Rayleigh_Ritz_nested_'+small['space'],np.min(margin)>-1e-11,float(np.min(margin)))
    vari.append({'smaller':small['space'],'larger':large['space'],'min_ordered_small_minus_large':float(np.min(margin))})
# Explicit same-H, different subtraction counterexample to extending RR to excitation gaps.
gap_examples=[]
for label,diagonal,direction in [
    ('gap_increases',[F(0),F(1),F(100)],1),
    ('gap_decreases',[F(0),F(99),F(100)],-1),
]:
    restricted=diagonal[1:]
    fullgap=diagonal[1]-diagonal[0]
    subgap=restricted[1]-restricted[0]
    check('RR_absolute_ordered_bounds_'+label,
          all(restricted[k]>=diagonal[k] for k in range(2)))
    check('excitation_gap_'+label, direction*(subgap-fullgap)>0)
    hf=np.diag([float(x) for x in diagonal])
    wf=np.eye(3)[:,[1,2]]
    eg=np.linalg.eigvalsh(wf.T@hf@wf)
    check('independent_eigencompression_'+label,
          np.allclose(eg,[float(x) for x in restricted],atol=1e-13,rtol=0))
    gap_examples.append({
        'label':label,'full_same_H_diagonal':[str(x) for x in diagonal],
        'restricted_indices':[1,2],'restricted_absolute_eigenvalues':[str(x) for x in restricted],
        'full_first_gap':str(fullgap),'restricted_first_gap':str(subgap),
        'ordered_absolute_bounds_hold':True,
        'interpretation':'same H nested spaces bound each ordered absolute eigenvalue; subtracting each own ground permits either gap direction'
    })
# TR-even formal field H retains Kramers pairs; projection P generated by two partners is essential.
uncertainty={'selected_m_plus':{'mean_j':['0','0',str(m)],'variance_j':['31/4','31/4','0'],'delta_jx_delta_jy':'31/4','Robertson_lower_bound_abs_m_over_2':'9/4'},'highest_weight_plus':{'m':str(j),'variance_jx':str(j/2),'variance_jy':str(j/2),'Robertson_product_equals_bound':True},'arbitrary_normalized_state_in_P':'jx and jy mean zero and second moments31/4 for every state; jz variance depends on Kramers superposition'}
results={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'selected lab single-j analytic control, not actual 133Ce |18>, not paper FA reproduction','units':'hbar=1; j dimensionless; external A in arbitrary consistent energy units','j':str(j),'selected_m_order':[str(m),str(-m)],'basis_m_ascending':[str(x) for x in ms],'selected_time_reversal_U':serial(smallU),'time_reversal_convention':'T|j,m>=(-1)^(j-m)|j,-m>; T=U complex_conjugation','projection_results':projected,'xy_commutator_leakage':serial(xy_leak),'independent_ladder_action':lad,'uncertainty':uncertainty,'external_H_control':{'X_spin_L':L,'Axyz':[str(a) for a in A],'not_physical_QTR_total_I':True,'recoil_shift':str(recoil),'recoil_shift_numeric':float(recoil),'compression_residual':res,'TR_residual':trres,'classical_plus_sector_residual':plusres,'spectra_nested_same_H':spectra,'Rayleigh_Ritz_margins':vari,'different_reference_excitation_counterexamples':gap_examples}}
results['checks']=checks;results['all_pass']=all(x['passed'] for x in checks)
(OUT/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps({'all_pass':results['all_pass'],'check_count':len(checks),'selected_transverse_second_moment':'31/4','highest_weight_transverse_second_moment':'11/4','recoil_shift':str(recoil),'max_compression_residual':res,'TR_residual':trres},indent=2))
