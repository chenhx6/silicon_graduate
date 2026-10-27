"""PE06 transition-kernel extension; forward algebra only, no data fit."""
from pathlib import Path
import json
import numpy as np

OUT=Path(__file__).resolve().parent

def R(a):
    b=np.sqrt(1-a*a)
    return np.array([[a,b],[b,-a]])

def explicit(ai,af,q1,q2,q):
    bi,bf=np.sqrt(1-ai*ai),np.sqrt(1-af*af)
    return np.array([[q1*af*ai+q*(af*bi+bf*ai)+q2*bf*bi,
                      q1*af*bi+q*(bf*bi-af*ai)-q2*bf*ai],
                     [q1*bf*ai+q*(bf*bi-af*ai)-q2*af*bi,
                      q1*bf*bi-q*(bf*ai+af*bi)+q2*af*ai]])

def forward(ai,af,q1,q2,q,swapped):
    Q=np.array([[q1,q],[q,q2]],float)
    M=R(af).T@Q@R(ai)
    assert np.allclose(M,explicit(ai,af,q1,q2,q),atol=2e-15)
    assert abs(np.sum(M*M)-np.sum(Q*Q))<1e-13
    assert abs(np.linalg.det(M)-np.linalg.det(Q))<1e-13
    assert np.allclose(np.linalg.svd(M,compute_uv=False),np.linalg.svd(Q,compute_uv=False))
    # Rephasing intrinsic state2 changes all kernel and mixing conventions together.
    S=np.diag([1.,-1.])
    assert np.allclose((S@R(af)).T@(S@Q@S)@(S@R(ai)),M)
    raw_ny=(M[0,1]/M[1,1])**2
    raw_y=(M[1,0]/M[0,0])**2
    table=np.array([raw_ny,raw_y])
    if swapped:table=1/table
    return dict(Q_in_Qref_units=Q.tolist(),M_in_Qref_units=M.tolist(),
                Eq4_ratio_ny=raw_ny,Eq5_ratio_y=raw_y,
                source_continuity_out_in_ny_y=table.tolist(),
                Frobenius2=float(np.sum(M*M)),det=float(np.linalg.det(M)),
                singular_values=np.linalg.svd(M,compute_uv=False).tolist())

transitions={}
limit_checks=[]
for ai,af in [(.118,.894),(.099,.427)]:
    # The source's equality shortcuts hold with diagonal Q; adding q12 need not.
    eq=forward(ai,af,1.,1.,0.,False)
    assert abs(eq['Eq4_ratio_ny']-eq['Eq5_ratio_y'])<1e-14
    z=forward(0.,af,2.,1.,0.,False)
    assert abs(z['Eq4_ratio_ny']-z['Eq5_ratio_y'])<1e-14
    off=forward(0.,af,2.,1.,.3,False)
    assert abs(off['Eq4_ratio_ny']-off['Eq5_ratio_y'])>1e-4
    limit_checks.append(dict(ai=ai,af=af,diagonal_equal_Q_shortcut=True,
                              diagonal_ai_zero_shortcut=True,
                              cross_kernel_ai_zero_shortcut_fails=True))
for label,ai,af,swap in [('17to15',.118,.894,True),('18to16',.099,.427,False)]:
    rows={}
    for name,q1,q2,q in [('source_forward_baseline',2.,1.,0.),
                         ('conditional_positive_cross_kernel',2.,1.,.25),
                         ('conditional_negative_cross_kernel',2.,1.,-.25),
                         ('equal_diagonal_not_equal_ratios',1.,1.,.3)]:
        rows[name]=forward(ai,af,q1,q2,q,swap)
    transitions[label]=dict(ai=ai,af=af,Table_continuity_swaps_y_ny_endpoints=swap,cases=rows)

# Real central Table17 ratios only: unknown norms and relative signs are explicit.
# Table rho_ny=.3,rho_y=.6 are inverse of Eq4/Eq5 for this crossing interval.
rny,ry=1/.3,1/.6
ratio_only_examples=[]
for sy,sn,A,B in [(1,1,1.,1.),(1,-1,1.,1.),(1,1,1.,4.)]:
    uy=np.array([1.,sy*np.sqrt(ry)])/np.sqrt(1+ry)
    uny=np.array([sn*np.sqrt(rny),1.])/np.sqrt(1+rny)
    M=np.column_stack([np.sqrt(A)*uy,np.sqrt(B)*uny])
    assert abs((M[1,1]/M[0,1])**2-.3)<1e-14
    assert abs((M[0,0]/M[1,0])**2-.6)<1e-14
    c=float(np.dot(uy,uny))
    eig=np.array([(A+B+np.sqrt((A-B)**2+4*A*B*c*c))/2,
                  (A+B-np.sqrt((A-B)**2+4*A*B*c*c))/2])
    assert np.allclose(np.linalg.svd(M,compute_uv=False)**2,eig)
    ratio_only_examples.append(dict(label='ratio-only illustration; NOT symmetric-Q fit',
        A=A,B=B,sy=sy,sn=sn,c=c,M=M.tolist(),Frobenius2=float(np.sum(M*M)),
        det2=float(np.linalg.det(M)**2),sigma2=eig.tolist()))

out=dict(scope='Day25 uncredited method preview inside Day24; source forward baseline and conditional extra q12 only; no fit/CI/geometry claim',
         units='q1,q2,q12,M in same arbitrary positive Qref unit; ratios dimensionless; no physical absolute Q scale chosen',
         source='PE06 PRL96,112502 Eqs1–5/TableI',transitions=transitions,
         diagonal_limits=limit_checks,
         Table17_central_ratio_only_examples=ratio_only_examples,
         invariant_scope='orthogonal basis changes at FIXED Q preserve norms/determinant/singular values; changing q12 changes their values',
         ratio_only_scope='These examples use unrestricted real M to prove what two ratios alone omit; they are not asserted to satisfy the extra symmetric-Q ansatz with source alphas.',
         producer_executed=False,data_fit=False,confidence_interval=False)
(OUT/'kernel-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(baselines={k:v['cases']['source_forward_baseline']['source_continuity_out_in_ny_y']for k,v in transitions.items()},
                     equal_diagonal={k:v['cases']['equal_diagonal_not_equal_ratios']['source_continuity_out_in_ny_y']for k,v in transitions.items()},
                     ratio_only_sigma2=[q['sigma2']for q in ratio_only_examples]),indent=2))
