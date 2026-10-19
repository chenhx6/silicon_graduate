#!/usr/bin/env python3
"""Post-grid rank4 and uncertainty controls for D66's actual AD summary."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as s
from sympy.physics.wigner import wigner_6j
from day16_diamond1966_three_ad_feasibility import kernel,coefficients


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    a=p.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='D66-THREEAD-POSTGRID-RANK4-CERTIFICATE-01'
    r=a.contract.parent;root=Path(__file__).resolve().parents[2]
    assert sha(r/c['base_contract'])==c['base_contract_sha256']
    assert sha(r/c['grid_result'])==c['grid_result_sha256']
    cfg=json.loads((r/c['base_contract']).read_text());grid=json.loads((r/c['grid_result']).read_text())
    assert sha(root/'system/scripts/day16_diamond1966_three_ad_feasibility.py')==grid['script_sha256']
    ratios=[]
    for top,mid in c['pairs2']:
        J,M,B=s.Rational(top,2),s.Rational(mid,2),s.Rational(9,2)
        ratio=s.simplify((-1)**(M-B)*wigner_6j(2,2,4,J,J,M)/wigner_6j(2,2,4,J,J,B))
        K1,K2=kernel(top,mid,cfg['quadrature_nodes']),kernel(top,9,cfg['quadrature_nodes'])
        residual=float(np.max(abs(K1[4][1]-float(ratio)*K2[4][1])))
        assert residual<1e-12 and ratio<0
        assert np.max(abs(K1[4][0]))<1e-12 and np.max(abs(K1[4][2]))<1e-12
        assert np.max(abs(K2[4][0]))<1e-12 and np.max(abs(K2[4][2]))<1e-12
        ratios.append({'top_spin2':top,'middle_spin2':mid,'exact_pureE2_rank4_ratio':str(ratio),
            'kernel_ratio_residual':residual,'central_nonzero_A4_pair_sign_incompatible':True,
            'source_marginal_boxes_still_include_A4331_A4701_zero':True})
    k=s.symbols('k',nonnegative=True)
    R=(s.Rational(2,100)+s.Rational(3,100)*k)/(s.Rational(3,100)+s.Rational(4,100)*k)
    assert s.simplify(R-s.Rational(2,3))>=0
    assert s.simplify(s.Rational(3,4)-R)>0
    derivative=s.factor(s.diff(R,k));assert derivative>0
    # Recompute every claimed existence point from the original operators.
    max_reconstruction=max_box_residual=0.;witness_count=0
    def check_population(Ji2,beta,Jf2,q,line,stored,mode):
        nonlocal max_reconstruction,max_box_residual
        assert abs(sum(q)-1)<1e-10 and min(q)>cfg['LP']['strict_pair_probability']
        V=coefficients(Ji2,Jf2,beta,cfg['quadrature_nodes'])
        for rank in [2,4]:
            val=float(V[rank]@q);mean,err=cfg['observations'][line]['a'+str(rank)]
            max_reconstruction=max(max_reconstruction,abs(val-stored['a'+str(rank)]))
            max_box_residual=max(max_box_residual,max(0.,val-(mean+err),(mean-err)-val))
        if mode=='extra_lowm_u2nonpositive':
            J=Ji2/2;m=np.array([J-i for i in range(len(q))]);assert q@(3*m*m-J*(J+1))<1e-9
    for row in grid['sameparent_results']:
        if row['strict_upper_witness'] is None:continue
        witness_count+=1;w=row['strict_upper_witness'];q=np.array(w['q_pair']);mode=row['population_mode']
        check_population(row['top_spin2'],w['beta331_native_deg'],row['middle_spin2'],q,'331',w['observations']['331'],mode)
        check_population(row['top_spin2'],w['beta701_native_deg'],9,q,'701',w['observations']['701'],mode)
        mw=grid['middle_level_witnesses'][row['middle_witness_key']]
        check_population(row['middle_spin2'],mw['beta_native_deg'],9,np.array(mw['q_pair']),'370',mw['observations']['370'],mode)
    assert witness_count==11 and max_reconstruction<1e-12 and max_box_residual<1e-10
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'base_and_grid_and_script_unchanged':True,
        'exact_rank4_controls':ratios,
        'uncertainty_bound':{'residual_definition':'r=A4331+k*A4701, k>=0 from negative rank4 ratio timesnonnegativephotonfractions',
            'central_residual_abs':'.02+.03k','maximum_sigma_over_PSD_marginal_covariance':'.03+.04k',
            'residual_over_sigma_max_expression':str(R),'derivative':str(derivative),
            'range_lower_inclusive':'2/3','range_upper_supremum':'3/4',
            'not_actual_z_or_jointCI':True,'no_covariance_independent_one_sigma_rejection_from_this_pair':True},
        'reconstructed_strict_witnesses':witness_count,'max_observable_reconstruction_error':max_reconstruction,
        'max_marginal_box_residual':max_box_residual,
        'scope':{'no_claim_only_eight_or_only_three_solutions':True,
            'no_gridzero_exclusion_or_source_five_count_reproduction':True,
            'point_model_native_delta_not_new_experimental_spin_or_delta':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
