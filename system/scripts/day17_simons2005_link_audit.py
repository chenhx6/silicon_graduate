#!/usr/bin/env python3
"""SIM05 typed photon branches: conditional ratios, not a polarization refit."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path = RUN / 'simons2005-link-contract.json'
    contract = json.loads(path.read_text())
    links = [dict(zip(contract['link_columns'], row)) for row in contract['links']]
    for row in links:
        row['central_over_printed_sigma_abs_descriptive_only'] = abs(row['P']) / row['sigma_P']
        row['missing_Q_a_counts_covariance_precludes_independent_P_replay'] = True
    ratios = []
    for values in contract['sameparent_rows']:
        row = dict(zip(contract['sameparent_columns'], values))
        ein, eout, iin, iout = (row[k] for k in ('Ein', 'Eout', 'Iin', 'Iout'))
        base = (iin / iout) * (eout / ein)**3
        # Unknown intensity correlation spans [-1,1]; E fixed in this diagnostic.
        u, v = row['sigmaIin']/iin, row['sigmaIout']/iout
        row.update({
            'conditional_pure_M1_Bin_over_Bout': base,
            'intensity_only_local_sigma_range_unknown_rho': [base*abs(u-v), base*(u+v)],
            'full_ratio': 'base*(1+delta_out^2)/(1+delta_in^2)',
            'not_actual_CI_or_Fig6_recovery': True,
        })
        # Overall normalization cancels; photon widths carry no extra ICC factor.
        assert math.isclose(base, (7.3*iin/(7.3*iout))*(eout/ein)**3)
        for din, dout in [(0., 0.), (.3, -.7), (-1.2, .4)]:
            by_components = ((iin/(1+din*din))/(iout/(1+dout*dout)))*(eout/ein)**3
            assert math.isclose(by_components, base*(1+dout*dout)/(1+din*din))
        ratios.append(row)
    result = {
        'at': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'links': links, 'sameparent_ratios': ratios,
        'caption_151_vs_Table_I151_53_4_and_I409_100_retained': True,
        'four_links_all_negative_central_but_no_joint_sign_test': True,
        'scale_and_M1_component_controls': True,
        'no_actual_Q_counts_delta_or_experimental_CI_invented': True,
        'ok': True,
    }
    (RUN/'simons2005-link-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'link_ratios': [x['central_over_printed_sigma_abs_descriptive_only'] for x in links],
                      'pure_M1_controls': [x['conditional_pure_M1_Bin_over_Bout'] for x in ratios], 'ok': True}))


if __name__ == '__main__':
    main()
