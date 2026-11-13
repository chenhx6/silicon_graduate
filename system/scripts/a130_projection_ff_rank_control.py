#!/usr/bin/env python3
"""Finite projection counterexample and angular-rank orthogonality controls."""
from fractions import Fraction as F
from math import factorial, sqrt, isclose
from pathlib import Path
import json


def three_j(j1,j2,j3,m1,m2,m3):
    # Integer-j Racah formula, sufficient for this finite test.
    if m1+m2+m3 or any(abs(m)>j for j,m in [(j1,m1),(j2,m2),(j3,m3)]): return 0.0
    if not abs(j1-j2)<=j3<=j1+j2: return 0.0
    delta=F(factorial(j1+j2-j3)*factorial(j1-j2+j3)*factorial(-j1+j2+j3),factorial(j1+j2+j3+1))
    pref=(-1)**(j1-j2-m3)*sqrt(float(delta)*factorial(j1+m1)*factorial(j1-m1)*factorial(j2+m2)*factorial(j2-m2)*factorial(j3+m3)*factorial(j3-m3))
    zmin=max(0,j2-j3-m1,j1-j3+m2)
    zmax=min(j1+j2-j3,j1-m1,j2+m2)
    s=F(0)
    for z in range(zmin,zmax+1):
        den=factorial(z)*factorial(j1+j2-j3-z)*factorial(j1-m1-z)*factorial(j2+m2-z)*factorial(j3-j2+m1+z)*factorial(j3-j1-m2+z)
        s += F((-1)**z,den)
    return pref*float(s)


def main():
    # RME=1 in Appendix A convention, Ji=1 Mi=0 -> Jf=0 Mf=0, q=0.
    lab=three_j(0,1,1,0,0,0)
    assert isclose(lab,-1/sqrt(3),abs_tol=1e-14)
    # T0 R(Omega)|1,0> has only d^1_00=cos(theta) after <0|T0.
    # Simpson integration is EXACT for the relevant polynomials in x=cos(theta).
    nodes=[F(-1),F(0),F(1)]; weights=[F(1,3),F(4,3),F(1,3)]
    i1=sum((w*x for w,x in zip(weights,nodes)),F(0))
    i2=sum((w*x*x for w,x in zip(weights,nodes)),F(0))
    wrong_integral=lab*float(4*i1)  # phi and psi integrations contribute (2pi)^2
    correct_projection_factor=F(3,2)*i2
    assert i1==0 and i2==F(2,3) and correct_projection_factor==1
    assert wrong_integral==0 and lab!=0
    # The unpolarized magnetic-index trace of ranks K and K' for Ji=Jf=1.
    # K=0,1,2; separate q, q' as well. No assumption of cross-rank zero is hard-coded.
    gram=[]
    labels=[(k,q) for k in range(3) for q in range(-k,k+1)]
    for k,q in labels:
        row=[]
        for kp,qp in labels:
            val=sum(three_j(1,k,1,-mf,q,mi)*three_j(1,kp,1,-mf,qp,mi)/3
                    for mi in range(-1,2) for mf in range(-1,2))
            expected=(1/(3*(2*k+1))) if (k,q)==(kp,qp) else 0
            assert isclose(val,expected,abs_tol=1e-14)
            row.append(val)
        gram.append(row)
    cross=max(abs(gram[i][j]) for i in range(len(labels)) for j in range(len(labels)) if labels[i][0]!=labels[j][0])
    # Same-rank amplitudes multiply the same angular factor and retain interference.
    x,u=F(2),F(3)
    incoherent=x*x+u*u; coherent=(x+u)**2
    assert coherent-incoherent==2*x*u!=0
    out={'status':'pass','projection_toy':{'Ji':1,'Mi':0,'Jf':0,'Mf':0,'L':1,'mu':0,'RME_convention':'Appendix A 3j convention','unit_RME':1,'lab_matrix_element':lab,'3j':lab,'frozen_single_integral_normalized_Haar':0,'original_unweighted_Haar_integral':wrong_integral,'initial_projector_factor':str(correct_projection_factor),'exact_integrals':{'integral_minus1_to1_x':str(i1),'integral_minus1_to1_x2':str(i2)},'note':'Normalization kernels of both pure states are one; original integral is zero even before its missing 3/(8pi^2) projector factor.'},'unpolarized_angular_control':{'Ji':1,'Jf':1,'ranks':[0,1,2],'labels':labels,'max_cross_rank_gram_abs':cross,'diagonal_gram':'1/[3(2K+1)]','same_rank_x':str(x),'same_rank_u':str(u),'coherent_square':str(coherent),'separate_squares':str(incoherent),'cross_term':str(coherent-incoherent),'scope':'finite angular algebra control, not a substitute for Zhi Eq.6-8 or a statement about polarized or angle-resolved observables'}}
    result_path=Path(__file__).resolve().parents[2]/'outputs/l4/20261114-A130-projection-ff-rank-controls/results.json'
    result_path.parent.mkdir(parents=True,exist_ok=True)
    result_path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
