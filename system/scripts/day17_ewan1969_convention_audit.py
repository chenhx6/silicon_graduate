#!/usr/bin/env python3
"""EW69 actual percent-count definition and literal formula audit."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'ewan1969-calibration-contract.json'
    c=json.loads(path.read_text())
    calibration=[]
    for nucleus,eg,q,sq,qc,sqc in c['calibration_rows']:
        p=q/qc
        a=q/200
        response=qc/200
        assert abs(a/response-p)<1e-14
        calibration.append({'nucleus':nucleus,'Egamma_MeV':eg,
                            'author_Qraw_percent':q,'author_Qcorr100P_percent':qc,
                            'implied_P_from_Qraw_over_Qcorr':p,
                            'ordinary_count_A':a,'ordinary_AoverP_sensitivity':response,
                            'sigma_sensitivity_from_same_source_scale_only':sqc/200,
                            'ordinary_A_error_same_scale_only':sq/200,
                            'no_new_experimental_P_or_independent_error':True})
    ru=[]
    for eg,a2,s2,a4,s4,q,sq in c['Ru_rows']:
        is_author_E2 = eg < .8
        literal=(1+a2+a4)/(1-2*a2-a4/4) if is_author_E2 else None
        point=(3*a2+1.25*a4)/(2-a2+.75*a4) if is_author_E2 else None
        ru.append({'Egamma_MeV':eg,'ordinary_A':q/200,
                   'ordinary_sigmaA_same_scale_only':sq/200,
                   'literal_printed_P_expression_intensity_ratio':literal,
                   'mapped_bounded_degree_from_literal':(literal-1)/(literal+1) if literal is not None else None,
                   'conditional_TW70_pureE2_P90_not_generic_mixed_line':point,
                   'conditional_corrected_Q_EW69_percent_using_TW70':q/point if point is not None else None,
                   'conditional_AoverP_sensitivity_using_TW70':q/200/point if point is not None else None,
                   'pureE2_formula_not_applied_to_author_mixed833':not is_author_E2,
                   'not_a_multipolarity_fit_or_current_response':True})
    assert ru[0]['literal_printed_P_expression_intensity_ratio']>2
    assert 0<ru[0]['conditional_TW70_pureE2_P90_not_generic_mixed_line']<1
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'actual_calibration_rows':calibration,'actual_Ru_rows':ru,
            'factor2_and_percent_conversion_controls':True,
            'literal_expression_has_exact_intensity_ratio_interpretation':True,
            'prior_over_one_failure_interpretation_withdrawn':True,
            'no_low_energy_photoelectric_fraction_or_Cov_inferred':True,
            'no_new_experimental_P_Q_delta_Jpi_or_CI':True,'ok':True}
    (RUN/'ewan1969-calibration-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
