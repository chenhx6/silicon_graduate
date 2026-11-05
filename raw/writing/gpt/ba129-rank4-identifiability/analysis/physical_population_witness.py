#!/usr/bin/env python3
"""Non-Gaussian aligned-population feasibility under literal marginal boxes.

The objective is the smallest common multiplier of quoted coefficient margins.
It is a deterministic compatibility metric, never a confidence level or p-value.
Detector response ratios are fixed to one for this declared control.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
from scipy.optimize import linprog
from rank4_invariant import cg2,native_f,phase,load_rows
from companion_profile import coefficient_ratios

ROOT=Path(__file__).resolve().parents[1]


def reference_vertices():
    # q_m=P(+m)+P(-m); all even statistical tensors agree within a pair.
    vertices=[]
    for tm in range(1,14,2):
        row=[]
        for rank in (2,4):
            rho=math.sqrt(14)*phase((13-tm)//2)*cg2(13,13,2*rank,tm,-tm,0)
            row.append(rho*native_f(13,9,rank,2,2))
        vertices.append(row)
    vertex=np.array(vertices).T
    assert np.allclose(vertex[:,0],[40/91,-216/1001],atol=1e-13)
    return vertex


def solve(y,scales,delta):
    reference=reference_vertices()
    factors=coefficient_ratios(math.atan(delta))
    design=np.vstack((factors[:,None]*reference,reference))
    # |design q-y| <= t*scales; q>=0 and sum q=1.
    a_ub=np.vstack((np.c_[design,-scales],np.c_[-design,-scales]))
    b_ub=np.r_[y,-y]
    a_eq=np.array([[1.]*7+[0.]])
    objective=np.array([0.]*7+[1.])
    result=linprog(objective,A_ub=a_ub,b_ub=b_ub,A_eq=a_eq,b_eq=[1.],bounds=[(0,None)]*8,method='highs')
    if not result.success:raise RuntimeError(result.message)
    q=result.x[:7];prediction=design@q;residual=(prediction-y)/scales
    dual=float(b_ub@result.ineqlin.marginals+result.eqlin.marginals[0])
    assert q.min()>-1e-10 and abs(q.sum()-1)<1e-10
    assert np.max(np.abs(residual))<=result.fun+1e-9
    assert abs(dual-result.fun)<1e-9
    return {'delta_chosen':delta,'f_E2_chosen':delta*delta/(1+delta*delta),
            'minimum_literal_margin_multiplier':float(result.fun),
            'inside_two_margin_box':bool(result.fun<=2.),
            'absolute_m_values':(np.arange(1,14,2)/2).tolist(),
            'pair_weights_witness':q.tolist(),
            'predicted_A2t_A4t_A2r_A4r':prediction.tolist(),
            'scaled_residuals':residual.tolist(),
            'dual_objective':dual,
            'not_a_population_measurement_or_confidence_interval':True}


def main():
    cp=ROOT/'data/input-contract.json';contract=json.loads(cp.read_text());cases=[]
    for version in contract['uncertainty_scenarios']:
        path=ROOT/version['dataset_file'];r=load_rows(path,require_reference_nonzero=False);t,ref=r['target_365'],r['reference_462']
        y=np.array([t['A2'],t['A4'],ref['A2'],ref['A4']],float)
        scales=np.array(version['standard_error_scales'],float)
        for delta in [-2.,-.88,-.33]:
            cases.append({'source_version':version['id'],'dataset_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),**solve(y,scales,delta)})
    out={'scope':'literal-box feasibility with a shared nonnegative symmetric parent density',
         'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'reference_vertices_A2_A4':reference_vertices().tolist(),
         'response_assumption':'Q2t=Q2r=Q4t=Q4r=1; pure E2 reference; M1/E2 target',
         'cases':cases,
         'boundaries':['Feasible weights are existence witnesses, not estimates of a measured alignment.',
                       'Arbitrary positive diagonal populations need not be reachable by the actual reaction.',
                       'Quoted margins and chosen multipliers have no asserted simultaneous coverage.',
                       'Selected delta hypotheses are not a full root or collective-mode inference.']}
    (ROOT/'analysis/results/physical-population-witness.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{'version':c['source_version'],'delta':c['delta_chosen'],'margin_multiplier':c['minimum_literal_margin_multiplier'],'two_margin_feasible':c['inside_two_margin_box']} for c in cases],indent=2))


if __name__=='__main__':main()
