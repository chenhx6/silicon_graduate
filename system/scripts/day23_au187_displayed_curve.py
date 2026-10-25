"""Digitize a published red fit line; never treat plot ordinates as raw data counts."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from PIL import Image


def points(rgb, roi, cut):
    r, g, b = [rgb[:, :, i].astype(float) for i in range(3)]
    mask = (r > cut[0]) & (r - g > cut[1]) & (r - b > cut[1])
    mask[:roi['y'][0]] = False
    mask[roi['y'][1] + 1:] = False
    selected = []
    for x in range(roi['x'][0], roi['x'][1] + 1):
        y = np.flatnonzero(mask[:, x])
        if y.size:
            selected.append((x, float(np.median(y)), int(y.size)))
    return np.array(selected)


def fit(coords, calibration, shifts=(0, 0, 0, 0), scale=1):
    x0 = calibration['theta0_x'] + shifts[0]
    x90 = calibration['theta90_x'] + shifts[1]
    yh = calibration['y_tick_hi'] + shifts[2]
    yl = calibration['y_tick_lo'] + shifts[3]
    ih, il = calibration['intensity_hi_display_units'], calibration['intensity_lo_display_units']
    theta = np.deg2rad(90 * (coords[:, 0] - x0) / (x90 - x0))
    slope = (il - ih) / (yl - yh)
    ordinate = (ih + slope * (coords[:, 1] - yh)) * scale
    design = np.column_stack([np.ones(len(theta)), np.polynomial.legendre.legval(np.cos(theta), [0, 0, 1]),
                              np.polynomial.legendre.legval(np.cos(theta), [0, 0, 0, 0, 1])])
    betas = np.linalg.lstsq(design, ordinate, rcond=None)[0]
    residual_px = (design @ betas - ordinate) / (slope * scale)
    return {'A0_display_units': float(betas[0]), 'A2_displayed_curve': float(betas[1] / betas[0]),
            'A4_displayed_curve': float(betas[2] / betas[0]),
            'RMS_vertical_pixel': float(np.sqrt(np.mean(residual_px ** 2))),
            'max_abs_vertical_pixel': float(max(abs(residual_px)))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    img = Path(c['image'])
    assert hashlib.sha256(img.read_bytes()).hexdigest() == c['sha256']
    rgb = np.asarray(Image.open(img).convert('RGB'))
    assert [rgb.shape[1], rgb.shape[0]] == c['native_size']
    coords = points(rgb, c['ROI'], (160, 80))
    assert len(coords) > 450 and max(coords[:, 2]) <= 5
    central = fit(coords, c['manual_axis_calibration'])
    variants = []
    for cut in [(140, 60), (160, 80), (190, 110)]:
        pp = points(rgb, c['ROI'], cut)
        for step in [1, 2, 4]:
            variants.append({'threshold': cut, 'stride': step, 'fit': fit(pp[::step], c['manual_axis_calibration'])})
    for shifts in itertools.product([-1, 0, 1], repeat=4):
        variants.append({'axis_pixel_shifts': shifts, 'fit': fit(coords, c['manual_axis_calibration'], shifts)})
    envelope = {k: [min(v['fit'][k] for v in variants), max(v['fit'][k] for v in variants)]
                for k in ['A0_display_units', 'A2_displayed_curve', 'A4_displayed_curve']}
    scaled = fit(coords, c['manual_axis_calibration'], scale=10)
    unit_error = max(abs(scaled[k] - central[k]) for k in ['A2_displayed_curve', 'A4_displayed_curve'])
    # Independent extraction in pixel-row coordinates then affine axis conversion.
    raw_cal = c['manual_axis_calibration']
    theta = np.deg2rad(90 * (coords[:, 0] - raw_cal['theta0_x']) / (raw_cal['theta90_x'] - raw_cal['theta0_x']))
    design = np.column_stack([np.ones(len(theta)), np.polynomial.legendre.legval(np.cos(theta), [0, 0, 1]),
                              np.polynomial.legendre.legval(np.cos(theta), [0, 0, 0, 0, 1])])
    pixel_coef = np.linalg.lstsq(design, coords[:, 1], rcond=None)[0]
    slope = (raw_cal['intensity_lo_display_units'] - raw_cal['intensity_hi_display_units']) / (raw_cal['y_tick_lo'] - raw_cal['y_tick_hi'])
    transformed = pixel_coef * slope
    transformed[0] += raw_cal['intensity_hi_display_units'] - slope * raw_cal['y_tick_hi']
    transform_error = max(abs(transformed[1] / transformed[0] - central['A2_displayed_curve']), abs(transformed[2] / transformed[0] - central['A4_displayed_curve']))
    controls = {'frozen_native_image_hash_and_size_checked': True,
                'only_red_published_fit_path_selected': len(coords) > 450 and max(coords[:, 2]) <= 5,
                'P2P4_reconstruction_residual_subpixel_RMS': central['RMS_vertical_pixel'] < .7,
                'display_ordinate_unit_rescale_invariance': unit_error < 1e-12,
                'pixel_fit_affine_axis_conversion_matches': transform_error < 1e-12,
                'axis_threshold_and_stride_sensitivity_recorded': len(variants) == 90}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': c['scope'], 'formal_day_index': 23, 'conditions': c,
           'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'selected_curve_columns': len(coords), 'central_displayed_curve_fit': central,
           'axis_threshold_stride_sensitivity_envelope_not_CI': envelope,
           'sensitivity_variant_count': len(variants),
           'sample_native_red_coordinates': coords[::50].tolist(),
           'controls': controls, 'all_controls_pass': all(controls.values()),
           'numeric_control_errors': {'unit_rescale': unit_error, 'affine_axis_conversion': transform_error},
           'limitations': ['This is only a geometric reconstruction of a published fitted curve, not the experimental peak counts or original likelihood.',
                          'Sensitivity envelope is a declared image/axis exercise, not statistical uncertainty or a confidence interval.',
                          'Black points/error bars were not digitized or assigned Poisson errors; no delta was fitted.',
                          'Near-agreement with a model shape does not certify original normalization/calibration, producer or a global root weight.',
                          'Source Fig4.12/Table4.4 processing stages remain distinct; no new independent measurement, lifetime, physical scale, count rate or time.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'columns': len(coords), 'central': central, 'envelope_not_CI': envelope,
                      'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
