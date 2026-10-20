#!/usr/bin/env python3
"""Audit EK79's actual table and the object of its MANDY error prescription."""
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import numpy as np
from sympy import Rational
from sympy.physics.wigner import clebsch_gordan

from day17_draper1970_gaussian_audit import angular_kernel

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


@lru_cache(None)
def complete_alignment(twice_j):
    j = Rational(twice_j, 2)
    jf = j - 2
    ms = [Rational(0)] if twice_j % 2 == 0 else [Rational(-1,2), Rational(1,2)]
    weights_q = np.zeros(5)
    for m in ms:
        for mf2 in range(-int(2*jf), int(2*jf)+1, 2):
            mf = Rational(mf2, 2)
            q = m-mf
            if abs(q) <= 2:
                weights_q[2-int(q)] += float(clebsch_gordan(jf, 2, j, mf, q, m)**2)/len(ms)
    assert abs(weights_q.sum()-1) < 1e-14
    x, wt, kernel = angular_kernel(16)
    w = weights_q @ kernel
    return [float((2*k+1)*np.dot(wt, w*np.polynomial.legendre.legval(x,[0]*k+[1]))/2)
            for k in [2,4]]


def main():
    path = RUN/'ekstrom1979-table1-contract.json'
    data = json.loads(path.read_text())
    rows = data['rows']
    assert len(rows)==39 and sum(r[12] is not None for r in rows)==32
    groups = defaultdict(list)
    results = []
    for n, row in enumerate(rows, 1):
        nuc, ei, ef, j2, reaction, energy, a2, sa2, a4, sa4, al2, sal2, al4, sal4, model, ref = row
        measured, uncertainty, predicted = al2/100, sal2/100, model/100
        sigma_model = max(.15*predicted, .04)
        residual = (predicted-measured)/np.hypot(uncertainty, sigma_model)
        group = '<=1' if energy<=1 else ('1<E<=2' if energy<=2 else '>2')
        groups[group].append(residual)
        ca2, ca4 = complete_alignment(j2)
        recalculated_alpha2 = (a2/100)/ca2
        recalculated_alpha4 = (a4/100)/ca4
        results.append({'row':n,'identity':[nuc,ei,ef,reaction,ref],
                        'energy_above_threshold_group_as_printed':group,
                        'alpha2_MANDY_error_Eq6':sigma_model,
                        'conditional_diagonal_standardized_residual':float(residual),
                        'CG_complete_alignment_A2_A4':[ca2,ca4],
                        'rounded_A2_to_alpha2':recalculated_alpha2,
                        'alpha2_central_rounding_residual':recalculated_alpha2-measured,
                        'rounded_A4_to_alpha4':recalculated_alpha4 if al4 is not None else None,
                        'alpha4_central_rounding_residual':recalculated_alpha4-al4/100 if al4 is not None else None})
    # Selected contrasts retain the covariance unknown rather than assigning independence.
    contrasts = []
    for label, difference, sigma1, sigma2 in [
        ('61Ni_2.41_sameparent_alpha2_branches', .69-.50,.04,.08),
        ('61Ni_3.44_B_alpha4_minus_alpha2', .88-.66,.14,.05)]:
        sigma_min,sigma_max=abs(sigma1-sigma2),sigma1+sigma2
        contrasts.append({'label':label,'central_difference':difference,
                          'conditional_sigma_difference_bounds_for_any_PSD_2x2_Cov':[sigma_min,sigma_max],
                          'diagonal_only_standardized_contrast':difference/np.hypot(sigma1,sigma2),
                          'not_a_joint_CI_or_pvalue':True})
    out={'at':datetime.now(timezone.utc).isoformat(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'angular_dependency_sha256':hashlib.sha256((ROOT/'system/scripts/day17_draper1970_gaussian_audit.py').read_bytes()).hexdigest(),
         'row_count':39,'rows_with_alpha4':32,'rows':results,
         'group_descriptive_N_inverse_sum_square':{k:{'N':len(v),'mean_squared_residual':float(np.mean(np.array(v)**2))} for k,v in groups.items()},
         'reference_counts':dict(Counter(r[-1] for r in rows)),
         'private_or_unpublished_references':[8,11,16,19],
         'selected_covariance_unknown_contrasts':contrasts,
         'all_data_same_lab_and_error_prescription_tuned_on_this_compilation':True,
         'no_independent_validation_pvalue_or_new_alignment_prior':True,
         'not_actual_MANDY_replay_or_new_tau_P_Q_delta':True,'ok':True}
    (RUN/'ekstrom1979-table1-result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    print('max rounded alpha residuals',max(abs(x['alpha2_central_rounding_residual']) for x in results),
          max(abs(x['alpha4_central_rounding_residual']) for x in results if x['alpha4_central_rounding_residual'] is not None))


if __name__=='__main__':
    main()
