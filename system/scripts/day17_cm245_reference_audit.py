#!/usr/bin/env python3
"""Fixed-column identity of evaluated Cm245 polarimetry references."""
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'cm245-reference-contract.json';c=json.loads(path.read_text());records={}
    for name,item in c['objects'].items():
        data=(ROOT/item['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==item['sha256']
        lines=data.decode().splitlines();parent=None;rows=[]
        for number,text in enumerate(lines,1):
            line=text.ljust(80)
            if line[5:8]=='  L':
                parent={'energy':line[9:19].strip(),'Jpi':line[21:39].strip(),
                        'half_life':line[39:49].strip(),'sigma_half_life':line[49:55].strip(),'line':number}
            if line[5:8]=='  G':
                energy=line[9:19].strip()
                if energy in ['333.37','388.15','54.77']:
                    rows.append({'line':number,'parent':parent,'Egamma':energy,
                        'RI':line[21:29].strip(),'DRI':line[29:31].strip(),
                        'M':line[31:41].strip(),'MR':line[41:49].strip(),
                        'DMR':line[49:55].strip(),'CC':line[55:62].strip(),
                        'DCC':line[62:64].strip(),'raw_record':text})
        references=[x for x in rows if x['Egamma'] in ['333.37','388.15']]
        assert len(references)==2
        assert all(x['parent']['energy']=='388.170' and x['parent']['Jpi']=='9/2-' for x in references)
        assert all(x['M']=='(E1)' and x['MR']=='' for x in references)
        double=[x for x in rows if x['Egamma']=='54.77']
        assert len(double)==2 and len({x['parent']['energy'] for x in double})==2
        records[name]={'line_count':len(lines),'sha256':item['sha256'],'selected_rows':rows}
    actual=records['cf249alpha']['selected_rows'];adopted=records['adopted']['selected_rows']
    rr={x['Egamma']:x for x in actual if x['Egamma'] in ['333.37','388.15']}
    aa={x['Egamma']:x for x in adopted if x['Egamma'] in rr}
    ratio=float(rr['333.37']['RI'])/float(rr['388.15']['RI'])
    normratio=float(aa['333.37']['RI'])/float(aa['388.15']['RI'])
    assert abs(ratio-normratio)<.001
    reference_rows=[]
    for energy,old in c['historical_unsigned_M2_over_E1'].items():
        value=old['magnitude'];partial=sum(c['experimental_ICC_values'][energy]);model=c['model_CC_for_reference_gammas'][energy]
        reference_rows.append({'Egamma_keV':float(energy),'old_MR_magnitude_not_signed_phase':value,
            'M2_intensity_fraction_conditional':value*value/(1+value*value),
            'absolute_cross_amplitude_coefficient_conditional':2*value/(1+value*value),
            'measured_partial_ICC_central_sum':partial,'BrIcc_model_total_CC':model,
            'partial_sum_over_model_total':partial/model,
            'anomalous_ICC_not_automatically_mixing_ratio':True})
    low=[x for x in actual if x['Egamma']=='54.77' and x['parent']['energy']=='54.784'][0]
    upper=[x for x in actual if x['Egamma']=='54.77' and x['parent']['energy']=='442.892'][0]
    assert low['MR']=='1.3' and upper['MR']=='0.63'
    cc=float(low['CC']);pafter=1/(1+cc)
    result={'at':datetime.now(timezone.utc).isoformat(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'evaluated_records':records,'reference_rows':reference_rows,
       'photon_ratio_absolute_alpha_object':ratio,'photon_ratio_relative_adopted':normratio,
       'upper_388_half_life_ns':c['reported_half_life_ns'][0],
       'upper_388_mean_lifetime_ns':c['reported_half_life_ns'][0]/math.log(2),
       'conditional_333_then_54_77_photon_branch_given_lower_total_decay':pafter,
       '333_and_388_mutually_exclusive_from_this_parent':True,
       'fixed_column_parent_MR_and_normalization_controls':True,
       'both_current_reference_MR_fields_blank_not_pure_measurement':True,
       'no_SeGA_Q_P_delta_or_experimental_CI_reestimated':True,'ok':True}
    (RUN/'cm245-reference-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'rows':reference_rows,'photon_ratios':[ratio,normratio],
                     'lower54photon':pafter,'mean_lifetime_ns':result['upper_388_mean_lifetime_ns']},indent=2))


if __name__=='__main__':
    main()
