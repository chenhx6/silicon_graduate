#!/usr/bin/env python3
"""MI07 rounded count-design, efficiency and dipole reference checks."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'miller2007-count-contract.json'
    c=json.loads(path.read_text())
    n,q=c['design_photopeak_N'],c['Qcentral']
    x,y=n*c['fperp'],n*c['fparallel']
    a=x/y; d=x+a*y
    gradient=[2*a*y/d**2,-2*a*x/d**2,-2*x*y/d**2]
    variance=gradient[0]**2*x+gradient[1]**2*y
    assert math.isclose(variance,.25*(1/x+1/y))
    # Exclusive fixed-total categories include the rejected category.
    fixed_variance=variance-(gradient[0]*x+gradient[1]*y)**2/n
    assert math.isclose(fixed_variance,variance)
    sigma_a_example=c['a333'][1]
    design={'N_total_photopeak':n,'selected_expected_perp':x,'selected_expected_parallel':y,
            'a_rounded_fraction_null':a,'A_null':(x-a*y)/(x+a*y),
            'sigma_P_known_a_Q_design':math.sqrt(variance)/q,
            'extra_sigmaP_if_0_007_were_independent_sigma_a_design_only':abs(gradient[2])*sigma_a_example/q,
            'not_actual_counts_or_source_unit_spread_as_independent_error':True}
    eps=(c['fparallel']+c['fperp'])/2*c['photopeak_eff_single']
    fm=q*q*eps
    refs=[]
    for energy,key in [(333,'a2_333'),(388,'a2_388')]:
        aa=c[key][0]
        vals=[]
        for theta in c['gamma_angles_deg']:
            sin2=math.sin(math.radians(theta))**2
            pp=-3*aa*sin2/(2+2*aa-3*aa*sin2)
            vals.append({'theta_nominal_deg':theta,'point_E1_P':pp})
        refs.append({'Egamma_keV':energy,'a2':aa,'point_values':vals})
    moments=[]
    for energy,aa,pvals in [(388,c['a2_388'][0],c['source_P_list_order388_then333'][:2]),
                            (333,c['a2_333'][0],c['source_P_list_order388_then333'][2:])]:
        for p in pvals:
            moment=2*p*(1+aa)/(3*aa*(p-1))
            assert 0<moment<1
            restored=-3*aa*moment/(2+2*aa-3*aa*moment)
            assert math.isclose(restored,p)
            moments.append({'Egamma_keV':energy,'printed_P':p,'conditional_acceptance_sin2_moment':moment,
                            'effective_point_angle_deg_not_real_geometry':math.degrees(math.asin(math.sqrt(moment)))})
    residuals=[]
    for pp,yy,ss in zip(c['source_P_list_order388_then333'],c['source_relative_A_groups'],c['source_relative_A_sigma']):
        residuals.append((yy-c['Qrel'][0]*pp)/ss)
    table=[]
    for values in c['source_Table1_rows']:
        row=dict(zip(c['source_Table1_columns'],values));row['central_Q_squared_epsilon']=row['Q']**2*row['epsilon_c']
        table.append(row)
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'design_count_budget':design,
            'rounding_efficiency_control':{'epsilon_c':eps,'FM':fm,
                 'from_printed_epsilon_c_FM':q*q*c['reported_epsilon_c']},
            'point_E1_references':refs,'source_P_to_acceptance_moment_controls':moments,
            'summary_residuals_at_source_Qrel_fixed_no_refit':residuals,
            'Table1_central_controls':table,
            'count_gradient_and_fixedN_and_Pmoment_inverse_controls':True,
            'no_original_detector_Q_fit_or_experimental_P_CI_reestimated':True,
            'actual_a_ratio_is_inverse_of_ST99_convention':True,'ok':True}
    (RUN/'miller2007-count-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(design,indent=2));print(json.dumps(result['rounding_efficiency_control'],indent=2))


if __name__=='__main__':
    main()
