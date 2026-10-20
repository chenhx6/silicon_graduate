#!/usr/bin/env python3
"""DR99 Eq8–15: joint response algebra and typed central summaries only."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path = RUN/'droste1999-response-contract.json'
    actual = json.loads(path.read_text())
    q1, q2, p1, p2, c = sp.symbols('q1 q2 p1 p2 c', real=True)
    w = sp.Matrix([1+p1+p2+c, 1+p1-p2-c, 1-p1+p2-c, 1-p1-p2+c])/4
    def channel(q):
        return sp.Matrix([[1-q, 1+q], [1+q, 1-q]])/2
    matrix = sp.kronecker_product(channel(q1), channel(q2))
    n = sp.simplify(matrix*w)
    total = sum(n)
    aa1 = sp.simplify((n[0]-n[1]-n[2]+n[3])/total)
    aa2 = sp.simplify((n[3]-n[0])/(n[3]+n[0]))
    pp2 = sp.simplify((w[0]-w[3])/(w[0]+w[3]))
    assert sp.simplify(aa1-q1*q2*c) == 0
    assert sp.simplify(aa2-(q1*p1+q2*p2)/(1+q1*q2*c)) == 0
    assert sp.simplify(pp2-(p1+p2)/(1+c)) == 0
    r1, r2 = (1+q1)/(1-q1), (1+q2)/(1-q2)
    printed14 = ((n[3]-n[0])*(r1*r2-1)-(n[1]-n[2])*(r2-r1))/(
        (n[3]+n[0])*(r1*r2+1)-(n[1]+n[2])*(r2+r1))
    assert sp.simplify(printed14-pp2) == 0
    assert sp.simplify(matrix.det()-q1*q1*q2*q2) == 0
    assert sp.simplify(aa2.subs({q1:1, q2:1})-pp2) == 0
    equal = sp.simplify(aa2.subs(q2,q1) - q1*(1+c)*pp2/(1+q1*q1*c))
    assert equal == 0
    # Exclusively classified, unweighted, background-free fixed-N counts ONLY.
    v = sp.Matrix(sp.symbols('n0:4', positive=True))
    a = (v[0]-v[1]-v[2]+v[3])/sum(v)
    b = (v[3]-v[0])/(v[3]+v[0])
    ga = sp.Matrix([sp.diff(a,x) for x in v])
    gb = sp.Matrix([sp.diff(b,x) for x in v])
    count_cov = sp.diag(*v)-v*v.T/sum(v)
    assert sp.simplify((ga.T*count_cov*gb)[0]) == 0
    assert sp.simplify((ga.T*count_cov*ga)[0]-(1-a*a)/sum(v)) == 0
    assert sp.simplify((gb.T*count_cov*gb)[0]-(1-b*b)/(v[0]+v[3])) == 0
    qone = (actual['R490']-1)/(actual['R490']+1)
    qtwo = (actual['R569']-1)/(actual['R569']+1)
    product = qone*qtwo
    controls = []
    for corr in [.8, -.4]:
        sub = {p1:0, p2:0, c:corr, q1:qone, q2:qtwo}
        ww, nn = [float(x.subs(sub)) for x in w], [float(x.subs(sub)) for x in n]
        assert min(ww)>0 and min(nn)>0
        assert abs(sum(nn)-1)<1e-12
        controls.append({'design_P1':0, 'design_P2':0, 'design_PP1':corr,
                         'positive_W':ww, 'normalized_N_not_actual_counts':nn,
                         'AA1':float(aa1.subs(sub)), 'AA2':float(aa2.subs(sub))})
    result = {
        'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'formulas':{'AA1':str(aa1),'AA2':str(aa2),'PP2':str(pp2),
                    'matrix_det':str(sp.factor(matrix.det())),
                    'Var_AA1':'(1-AA1^2)/N', 'Var_AA2':'(1-AA2^2)/(N_parallel_parallel+N_perp_perp)',
                    'Cov_AA1_AA2':'0 at local Jacobian order for the declared exclusive multinomial model only'},
        'source_central_R_to_Q':{'Q490':qone,'Q569':qtwo,'product':product,
            'inverse_joint_moment_amplification':1/product,
            'PP1_from_AA1_fixedQ':actual['AA1_490_569'][0]/product,
            'sigma_PP1_from_printed_AA1_only_fixedQ':actual['AA1_490_569'][1]/product,
            'Q1P1_plus_Q2P2_from_central_AA2_AA1':actual['AA2_490_569'][0]*(1+actual['AA1_490_569'][0]),
            'not_full_covariance_or_confidence_interval':True},
        'same_single_P_different_joint_design':controls,
        'source_Table1_hypotheses':[dict(zip(actual['hypothesis_columns'],x)) for x in actual['hypotheses']],
        'author_rejects_positive_parity_hypotheses':[2,3,6,7],
        'author_retains_positive_parity_hypotheses':[1,4,5,8],
        'symbolic_Eq8_11_15_and_count_covariance_controls':True,
        'same_single_P_does_not_fix_joint_PP1':True,
        'no_actual_counts_or_original_chi2_fit_pvalue_CI':True,
        'ok':True,
    }
    (RUN/'droste1999-response-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['source_central_R_to_Q'],indent=2))


if __name__ == '__main__':
    main()
