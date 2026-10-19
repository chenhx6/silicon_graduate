#!/usr/bin/env python3
"""Query ROOT on actual published graph values under declared error contracts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import ctypes
import openpyxl
import ROOT as R

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def deviance(data, model):
    return 2*sum(m-d+d*math.log(d/m) if d else m for d, m in zip(data, model))


def main():
    cp = RUN / 'fougeres2023-graph-root-contract.json'
    c = json.loads(cp.read_text())
    p = ROOT / c['xlsx']
    assert sha(p) == c['xlsx_sha256']
    assert R.gROOT.GetVersion() == '6.40.04'
    sheet = openpyxl.load_workbook(p, read_only=True, data_only=True)[c['sheet']]
    rows = []
    for i, row in enumerate(sheet.iter_rows(min_row=3, values_only=True), 3):
        if row[10] is not None:
            rows.append({'excel_row': i, 'values': [float(row[k]) for k in [10, 11, 14, 15]]})
    old = json.loads((RUN / 'fougeres2023-exercise-result.json').read_text())
    assert rows == next(x['actual_rows'] for x in old['profiles'] if x['state_label'] == '7785')
    assert len(rows) == 25
    x, model, data, errors = map(list, zip(*(row['values'] for row in rows)))
    norm = sum(data)/sum(model)
    cases = []
    kept = []
    for i, mode in enumerate(['fallback error, original display model',
                              'zero model variance, original display model',
                              'fallback error, normalized display model',
                              'zero model variance, normalized display model',
                              'stored original variance, then actual Scale']):
        o = R.TH1D(f'graph_o{i}', '', len(rows), 0, len(rows))
        h = R.TH1D(f'graph_m{i}', '', len(rows), 0, len(rows))
        kept += [o, h]
        multiplier = norm if 'normalized' in mode else 1.0
        for b, (d, m, e) in enumerate(zip(data, model, errors), 1):
            o.SetBinContent(b, d)
            o.SetBinError(b, e)
            h.SetBinContent(b, m*multiplier)
        if mode.startswith('zero'):
            h.Sumw2()
            for b in range(1, len(rows)+1):
                h.SetBinError(b, 0.0)
        if mode.startswith('stored original'):
            h.Sumw2()
            h.Scale(norm)
            multiplier = norm
        options = {opt: float(o.Chi2Test(h, opt)) for opt in
                   ['LL CHI2', 'CHI2', 'UU CHI2', 'UW CHI2', 'WW CHI2', 'LL CHI2/NDF']}
        chi, ndf, igood = ctypes.c_double(), ctypes.c_int(), ctypes.c_int()
        pv = float(o.Chi2TestX(h, chi, ndf, igood, 'LL'))
        assert options['LL CHI2'] == options['CHI2'] == chi.value
        cases.append({'mode': mode, 'model_multiplier': multiplier, 'options': options,
                      'Chi2TestX': {'chi2': chi.value, 'ndf': ndf.value, 'igood': igood.value,
                                   'returned_p_value_not_interpreted_as_experimental': pv},
                      'model_sumw2_buffer_length': h.GetSumw2N(),
                      'model_error_squared_sum': sum(h.GetBinError(b)**2 for b in range(1, len(rows)+1)),
                      'boundary': 'declared numerical contract on graph values; actual template variance unknown'})
    normalized = [m*norm for m in model]
    pearson = sum((d-m)**2/m for d, m in zip(data, normalized))
    assert abs(cases[1]['options']['UW CHI2']-pearson) < 1e-9
    assert abs(cases[3]['options']['UW CHI2']-pearson) < 1e-9
    assert abs(cases[0]['options']['CHI2']-cases[1]['options']['CHI2']) > 1.0
    assert abs(cases[4]['model_error_squared_sum']-norm*norm*sum(model)) < 1e-9
    assert abs(cases[4]['options']['UW CHI2']-cases[0]['options']['UW CHI2']) < 1e-9
    out = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'actual_rows': rows, 'n': len(rows),
           'source_model_display_sum': sum(model), 'source_data_display_sum': sum(data),
           'same_display_domain_integral_multiplier': norm,
           'fixed_model_Pearson_original_display': sum((d-m)**2/m for d, m in zip(data, model)),
           'fixed_model_Pearson_normalized_display': pearson,
           'fixed_model_deviance_original_display': deviance(data, model),
           'fixed_model_deviance_normalized_display': deviance(data, normalized),
           'native_cases': cases, 'published_SI_grid_minimum_for_reference_only': c['SI_minimum'],
           'all_25_display_points_preserved_no_window_search': True,
           'consistent_scale_variance_control_passed': True,
           'error_contract_does_not_identify_actual_MC_variance': True,
           'original_paper_statistic_fit_tau_or_CI_not_replayed': True, 'ok': True}
    (RUN / 'fougeres2023-graph-root-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'actual_rows'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
