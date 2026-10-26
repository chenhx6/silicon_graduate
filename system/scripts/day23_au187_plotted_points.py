"""Extract plotted AD point centers; pixel extents never become statistical errors."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import label


def extract(rgb, panel, settings, threshold):
    result = []
    x0, y0, x1, y1 = panel['frame']
    guard = settings['frame_guard_pixels']
    for seed in panel['seeds_xy']:
        sx, sy = seed
        left = max(x0 + guard + 1, sx - settings['local_window_halfwidth'])
        right = min(x1 - guard, sx + settings['local_window_halfwidth'] + 1)
        top = max(y0 + guard + 1, sy - settings['local_window_halfheight'])
        bottom = min(y1 - guard, sy + settings['local_window_halfheight'] + 1)
        mask = np.max(rgb[top:bottom, left:right], axis=2) < threshold
        components, count = label(mask)
        assert count
        coords = np.argwhere(mask)
        nearest = coords[np.argmin((coords[:, 1] + left - sx)**2 + (coords[:, 0] + top - sy)**2)]
        chosen = components[tuple(nearest)]
        yy, xx = np.where(components == chosen)
        xx = xx + left; yy = yy + top
        cx, cy = float(np.mean(xx)), float(np.mean(yy))
        axis = panel['axis']
        theta = 90 * (cx - axis['x0']) / (axis['x90'] - axis['x0'])
        ordinate = axis['ihi'] + (cy - axis['yhi']) * (axis['ilo'] - axis['ihi']) / (axis['ylo'] - axis['yhi'])
        result.append({'seed_xy': seed, 'center_xy': [cx, cy],
                       'nominal_theta_degrees': theta, 'nominal_display_ordinate': ordinate,
                       'printed_ordinate_multiplier': axis['printed_scale'],
                       'selected_dark_pixels': int(len(xx)),
                       'visible_component_bbox_not_errorbar': [int(min(xx)), int(min(yy)), int(max(xx)), int(max(yy))],
                       'frame_clipped_window': bool(left > sx - settings['local_window_halfwidth'] or right < sx + settings['local_window_halfwidth'] + 1)})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--overlay', type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    original = Path(cfg['image'])
    if not original.exists():
        import pymupdf
        rebuild = cfg['reconstruct_image_if_missing']
        raw_pdf = Path(rebuild['source_pdf'])
        assert hashlib.sha256(raw_pdf.read_bytes()).hexdigest() == rebuild['source_sha256']
        doc = pymupdf.open(raw_pdf)
        assert any(row[0] == rebuild['image_xref'] for row in doc[rebuild['pdf_page_index']].get_images(full=True))
        extracted = doc.extract_image(rebuild['image_xref'])
        assert hashlib.sha256(extracted['image']).hexdigest() == cfg['sha256']
        original.parent.mkdir(parents=True, exist_ok=True)
        original.write_bytes(extracted['image'])
    assert hashlib.sha256(original.read_bytes()).hexdigest() == cfg['sha256']
    img = Image.open(original).convert('RGB')
    assert list(img.size) == cfg['native_size']
    rgb = np.asarray(img)
    results = []
    overlay = img.copy(); draw = ImageDraw.Draw(overlay)
    shifts = []; seed_distances = []
    for panel in cfg['panels']:
        variants = [extract(rgb, panel, cfg['segmentation'], threshold)
                    for threshold in cfg['segmentation']['dark_thresholds']]
        central = variants[1]
        sensitivity = []
        for i, row in enumerate(central):
            xy = np.array([v[i]['center_xy'] for v in variants])
            sensitivity.append({'x_pixel_range': [float(min(xy[:, 0])), float(max(xy[:, 0]))],
                                'y_pixel_range': [float(min(xy[:, 1])), float(max(xy[:, 1]))]})
            shifts.append(float(np.max(np.ptp(xy, axis=0))))
            seed_distances.append(float(np.linalg.norm(np.array(row['center_xy']) - row['seed_xy'])))
            x, y = row['center_xy']; draw.ellipse([x-7, y-7, x+7, y+7], outline=(255, 0, 255), width=1)
            draw.line([x-3, y, x+3, y], fill=(0, 180, 0), width=1)
            draw.line([x, y-3, x, y+3], fill=(0, 180, 0), width=1)
        results.append({'energy_keV': panel['energy_keV'], 'points': central,
                        'threshold_pixel_envelope_not_CI': sensitivity,
                        'errorbar_readiness': 'unresolved from this extraction; most bars are hidden by filled markers, component extent is not sigma'})
    args.overlay.parent.mkdir(parents=True, exist_ok=True); overlay.save(args.overlay)
    controls = {'native_image_hash_and_dimensions': True,
                'seven_dark_point_components_per_target': all(len(r['points']) == 7 for r in results),
                'centers_near_predeclared_visual_seeds': max(seed_distances) < 3,
                'threshold_stability_under_two_pixels': max(shifts) < 2,
                'ordered_plot_angles': all(all(a['center_xy'][0] < b['center_xy'][0] for a, b in zip(r['points'], r['points'][1:])) for r in results)}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'conditions': cfg,
           'contract_sha256': hashlib.sha256(args.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'targets': results, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'max_threshold_pixel_span': max(shifts), 'max_center_seed_distance_pixels': max(seed_distances),
           'overlay_for_visual_review': str(args.overlay),
           'limitations': ['Published I_gamma plot ordinates are not original net peak counts or event totals.',
                          'Nominal intensity transforms inherit rounded printed axis labels, especially panel b.',
                          'The last plotted marker is clipped near the 90-degree frame; its centroid is not an exact detector-angle calibration.',
                          'No experimental sigma, Poisson assignment, covariance, weighted likelihood, chi-square or delta was reconstructed.',
                          'No fit was run; this is a reduced plotted-vector readiness artifact, not an additional independent measurement.',
                          'The image segmentation and threshold checks do not certify original gate/efficiency/normalization or response.']}
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'threshold_span': max(shifts), 'max_seed_distance': max(seed_distances),
                      'targets': [{'energy': r['energy_keV'], 'centers': [p['center_xy'] for p in r['points']]} for r in results]}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
