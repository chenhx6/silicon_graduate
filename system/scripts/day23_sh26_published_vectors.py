"""Read published vector primitives; do not confuse a plot diagnostic with original chi2."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pymupdf


def polyline(drawing):
    assert all(item[0] == 'l' for item in drawing['items'])
    return np.array([tuple(drawing['items'][0][1])] + [tuple(item[2]) for item in drawing['items']])


def diagnostic(point_y, curve_y, halfbar):
    residuals = (point_y - curve_y) / halfbar
    return float(residuals @ residuals), residuals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    pdf = Path(cfg['source_pdf'])
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == cfg['sha256']
    doc = pymupdf.open(pdf); page = doc[cfg['page_index']]; drawings = page.get_drawings()
    targets = []; caps_checked = 0; center_errors = []; invariant_errors = []
    for panel in cfg['panels']:
        roi = pymupdf.Rect(panel['inset_roi']); markers = []
        for i, drawing in enumerate(drawings):
            rect = drawing['rect']; center = (rect.tl + rect.br) / 2
            if (drawing['type'] == 'fs' and drawing.get('fill') == (0., 0., 0.)
                    and len(drawing['items']) == 8 and abs(rect.width - rect.height) < .01
                    and 3.4 < rect.width < 3.6 and center in roi):
                markers.append((i, center))
        markers.sort(key=lambda item: item[1].x)
        points = []
        for index, center in markers:
            stems = []
            for i, drawing in enumerate(drawings):
                rect = drawing['rect']
                if (drawing['type'] == 's' and drawing.get('color') == (0., 0., 0.)
                        and len(drawing['items']) == 1 and rect.width < 1e-4
                        and abs(rect.x0 - center.x) < 1e-3 and rect.tl in roi and rect.br in roi):
                    stems.append((i, rect))
            assert len(stems) == 1
            stem_index, rect = stems[0]; cap_indices = []
            for endpoint in [rect.y0, rect.y1]:
                matches = []
                for i, drawing in enumerate(drawings):
                    rr = drawing['rect']
                    if (drawing.get('color') == (0., 0., 0.) and len(drawing['items']) == 1
                            and rr.height < 1e-4 and 5.8 < rr.width < 5.95
                            and abs((rr.x0 + rr.x1)/2 - center.x) < 1e-3
                            and abs(rr.y0 - endpoint) < 1e-3):
                        matches.append(i)
                assert len(matches) == 1
                cap_indices.append(matches[0]); caps_checked += 1
            error = abs((rect.y0 + rect.y1)/2 - center.y); center_errors.append(error)
            points.append({'marker_path_index': index, 'center_pdfpoints': list(center),
                           'stem_path_index': stem_index, 'stem_y_pdfpoints': [rect.y0, rect.y1],
                           'cap_path_indices': cap_indices, 'plotted_halfbar_pdfpoints_not_experimental_sigma': rect.height/2,
                           'marker_stem_midpoint_residual_pdfpoints': error})
        assert len(points) == 7
        px = np.array([p['center_pdfpoints'][0] for p in points])
        py = np.array([p['center_pdfpoints'][1] for p in points])
        bars = np.array([p['plotted_halfbar_pdfpoints_not_experimental_sigma'] for p in points])
        response = {}; profile = polyline(drawings[panel['profile_path_index']])
        axis = panel['profile_axis_calibration']
        for name in ['red', 'blue']:
            path = polyline(drawings[panel[name + '_path_index']])
            assert np.all(np.diff(path[:, 0]) >= 0) and np.all(np.diff(profile[:, 0]) >= 0)
            curve_y = np.interp(px, path[:, 0], path[:, 1])
            value, residuals = diagnostic(py, curve_y, bars)
            transformed, _ = diagnostic(2.7 * py + 10, 2.7 * curve_y + 10, 2.7 * bars)
            invariant_errors.append(abs(transformed - value))
            delta = panel['published_delta_' + name]
            x = axis['phi0_x'] + axis['one_radian_pdfpoints'] * math.atan(delta)
            y = float(np.interp(x, profile[:, 0], profile[:, 1]))
            log_chi = axis['log_low'] + (y - axis['y_low']) * (axis['log_high'] - axis['log_low']) / (axis['y_high'] - axis['y_low'])
            response[name] = {'published_delta_label': delta, 'curve_path_index': panel[name + '_path_index'],
                              'curve_y_at_points_pdfpoints': curve_y.tolist(),
                              'D_diagonal_plotted_halfbars_not_original_chi2': value,
                              'residuals_in_plotted_halfbars': residuals.tolist(),
                              'author_profile_readout_at_printed_delta': {'log10chi_label': log_chi, 'chi_label': 10**log_chi},
                              'polyline_vertex_count': len(path)}
        targets.append({'printed_energy_keV': panel['printed_energy_keV'], 'points': points, 'responses': response,
                        'direction_agreement_only': response['red']['D_diagonal_plotted_halfbars_not_original_chi2'] < response['blue']['D_diagonal_plotted_halfbars_not_original_chi2'],
                        'numerical_closure': 'not reproduced: declared D and author chi-profile readouts have different values; original objective/response/normalization/sample input absent'})
    controls = {'raw_hash_and_vector_source_checked': True,
                'seven_circle_markers_with_underlying_stems_each_panel': all(len(t['points']) == 7 for t in targets),
                'two_caps_verified_per_stem': caps_checked == 42,
                'stem_midpoints_coincide_with_markers': max(center_errors) < 1e-4,
                'positive_plotted_halfbars': all(p['plotted_halfbar_pdfpoints_not_experimental_sigma'] > 0 for t in targets for p in t['points']),
                'diagnostic_invariant_under_affine_intensity_units': max(invariant_errors) < 1e-7,
                'missing_original_chi_closure_retained': all(t['numerical_closure'].startswith('not reproduced') for t in targets)}
    controls = {k: bool(v) for k, v in controls.items()}
    output = {'scope': cfg['scope'], 'formal_day_index': 23, 'conditions': cfg,
              'contract_sha256': hashlib.sha256(args.contract.read_bytes()).hexdigest(),
              'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'targets': targets, 'controls': controls, 'all_controls_pass': all(controls.values()),
              'numeric_control_errors': {'max_marker_stem_midpoint_pdfpoints': max(center_errors), 'max_affine_D_difference': max(invariant_errors)},
              'limitations': ['D uses the extra convention that published halfbars act as independent one-sigma errors; that convention is not a recovered original likelihood.',
                             'Author chi-profile readings are geometric readouts from the published fixed-sigma/I=.2 figure, not newly fitted experimental values.',
                             'Direction agreement does not make the values close, certify the objective or supply the original producer.',
                             'No p-values, confidence intervals, new delta or equal-depth premise; source conditional large-root support is retained.',
                             'Printed746.3/811.6/754.2 labels are preserved; publication lineage/event ledger still required.']}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': output['all_controls_pass'], 'numeric_controls': output['numeric_control_errors'],
                      'readouts': [{'energy': t['printed_energy_keV'], 'redD': t['responses']['red']['D_diagonal_plotted_halfbars_not_original_chi2'],
                                    'blueD': t['responses']['blue']['D_diagonal_plotted_halfbars_not_original_chi2'],
                                    'author_readouts': {n: t['responses'][n]['author_profile_readout_at_printed_delta'] for n in ['red', 'blue']}} for t in targets]}))
    raise SystemExit(0 if output['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
