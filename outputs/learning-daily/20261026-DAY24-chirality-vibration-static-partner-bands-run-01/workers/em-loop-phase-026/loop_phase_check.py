"""Gauge versus EM-loop information: conditional matrices, no nuclear fit."""
from pathlib import Path
import json
import numpy as np

OUT=Path(__file__).resolve().parent

def loop(M):
    return M[0,0]*M[1,1]*np.conj(M[0,1])*np.conj(M[1,0])

def invariants(M):
    mod2=abs(M)**2
    L=loop(M)
    D=abs(np.linalg.det(M))**2
    direct=mod2[0,0]*mod2[1,1]+mod2[0,1]*mod2[1,0]-2*np.real(L)
    S=float(np.sum(mod2))
    sigma2=np.linalg.svd(M,compute_uv=False)**2
    assert np.isclose(D,direct,rtol=1e-13,atol=1e-12)
    assert np.allclose(sigma2,[(S+np.sqrt(max(0.,S*S-4*D)))/2,
                               (S-np.sqrt(max(0.,S*S-4*D)))/2])
    return dict(modulus_squared=mod2.tolist(),Frobenius_squared=S,
                loop_real=float(np.real(L)),loop_imag=float(np.imag(L)),
                det_modulus_squared=float(D),singular_values_squared=sigma2.tolist())

M=np.array([[1+2j,2-.3j],[3+.4j,4-1j]])
eta=np.array([.31,-.72]);chi=np.array([.43,.19])
phase=np.exp(-1j*eta[:,None]+1j*chi[None,:])
Mp=phase*M
assert np.allclose(abs(M),abs(Mp)) and np.allclose(loop(M),loop(Mp))
assert np.allclose(np.linalg.svd(M,compute_uv=False),np.linalg.svd(Mp,compute_uv=False))
assert np.allclose(np.linalg.det(Mp),np.exp(1j*(sum(chi)-sum(eta)))*np.linalg.det(M))
assert not np.isclose(np.trace(Mp),np.trace(M))

# Generic DeltaI=1, equal-parity block: both M1 and E2 are allowed.
# This is NOT the source's DeltaI=2 block, where M1 is forbidden.
# Every E2 magnitude, row norm, column norm and one mixed-line delta stays fixed.
A=np.array([[1.,2.],[3.,4.]])
B=np.array([[1.,2.],[3.,-4.]])
N=np.ones((2,2))  # A fixed illustrative M1 block, not actual PE06 data.
assert np.array_equal(A*A,B*B)
assert A[0,0]/N[0,0]==B[0,0]/N[0,0]==1.
assert loop(A)==24 and loop(B)==-24
ia,ib=invariants(A),invariants(B)
assert not np.allclose(ia['singular_values_squared'],ib['singular_values_squared'])
# A state sign change affects both operators identically and cannot change the loop.
S=np.diag([-1.,1.])
assert loop(S@A)==loop(A)
assert (S@A)[0,0]/(S@N)[0,0]==A[0,0]/N[0,0]

# Complex forward blocks interpolate while every magnitude remains fixed.
complex_family=[]
for phi in [0.,np.pi/2,np.pi]:
    C=A.astype(complex);C[1,1]*=np.exp(1j*phi)
    assert np.allclose(abs(C)**2,A*A)
    complex_family.append(dict(phi=phi,**invariants(C)))

out=dict(scope='conditional forward real/complex2x2 RME block; no nuclear data or fit',
    mixed_counterexample_spin_scope='generic Ii=3,If=2,sameparity;NOTPE06I->I-2;amplitudesnormalizedtoownmultipoleunitsandkappa11=1',
    gauge_law='Mprime_ab=exp(-i eta_a+i chi_b) M_ab',
    gauge_example_before=invariants(M),gauge_example_after=invariants(Mp),
    real_counterexample_A=ia,real_counterexample_B=ib,
    same_signed_delta_11=1.,M1_block=N.tolist(),
    complex_family=complex_family,
    exclusions=['No actual134Pr phase or singular value assigned.',
                'No symmetricQ/source-alpha inverse fit claimed.',
                'A loop invariant is not automatically measured by incoherent widths.',
                'No quantumgeometry or sourceHamiltonian change claimed.'])
(OUT/'loop-phase-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(A=ia,B=ib,delta11=1.),indent=2))
