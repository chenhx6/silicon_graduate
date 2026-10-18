#!/usr/bin/env python3
"""Integrate L26's actual vector coverage, with separate declared kernel models.

Published paths are figure summaries, not event data or detector response files.
Axes and model alternatives are frozen before evaluation. No fit to Pbar is made.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import numpy as np


def parse_polyline(d: str) -> np.ndarray:
    commands = re.findall(r"[A-Za-z]", d)
    assert commands[0] == "M" and commands.count("M") == 1 and set(commands) == {"M", "L"}
    values = [float(x) for x in re.findall(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?", d)]
    assert len(values) % 2 == 0
    return np.array(values).reshape(-1, 2)


def matrix_transform(points: np.ndarray, transform: str) -> np.ndarray:
    vals = [float(x) for x in re.findall(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?", transform)]
    assert len(vals) == 6
    a, b, c, d, tx, ty = vals
    return points @ np.array([[a, b], [c, d]]) + [tx, ty]


def axis_points(page: np.ndarray, axis: dict, x_shift: tuple = (0, 0), y_shift: float = 0) -> np.ndarray:
    x0, xpi = axis["theta0_x"]+x_shift[0], axis["thetaPi_x"]+x_shift[1]
    baseline = axis["zero_y"]+y_shift
    # The arbitrary ordinate scale cancels in coverage averages; use the fixed
    # published y=1 tick for visual curve reconstruction only.
    yscale = axis["zero_y"]-axis["y1_tick_y"]
    result = np.column_stack([(page[:, 0]-x0)/(xpi-x0)*math.pi, (baseline-page[:, 1])/yscale])
    assert np.all(np.diff(result[:, 0]) >= -1e-10)
    return result


def p_and_w(theta: np.ndarray, a2: float, a4: float, beta: float) -> tuple:
    lab_x = np.cos(theta)
    x = (lab_x-beta)/(1-beta*lab_x)
    p2 = (3*x*x-1)/2
    p4 = (35*x**4-30*x*x+3)/8
    wcm = 1+a2*p2+a4*p4
    h = 1.5*a2*(1-x*x)-.625*a4*(1-x*x)*(7*x*x-1)
    jacobian = (1-beta*beta)/(1-beta*lab_x)**2
    assert np.min(wcm) > 0 and np.min(jacobian) > 0
    return h/wcm, wcm*jacobian


def integral(coverage: np.ndarray, function, bounds: tuple, coordinate: str = "theta", nodes: int = 16) -> float:
    gx, gw = np.polynomial.legendre.leggauss(nodes)
    total = 0.0
    for (left, yl), (right, yr) in zip(coverage[:-1], coverage[1:]):
        if right-left < 1e-12:
            continue  # Vertical figure steps carry zero integration measure.
        lo, hi = max(left, bounds[0]), min(right, bounds[1])
        if hi <= lo:
            continue
        slope = (yr-yl)/(right-left)
        if coordinate == "theta":
            t = (lo+hi)/2+(hi-lo)/2*gx
            y = yl+slope*(t-left)
            value = np.sum(gw*y*function(t))*(hi-lo)/2
        elif coordinate == "cos":
            xmin, xmax = math.cos(hi), math.cos(lo)
            x = (xmin+xmax)/2+(xmax-xmin)/2*gx
            t = np.arccos(x)
            y = yl+slope*(t-left)
            value = np.sum(gw*y*function(t)/np.sqrt(1-x*x))*(xmax-xmin)/2
        else:
            raise ValueError(coordinate)
        total += float(value)
    return total


def average(coverage: np.ndarray, function, bounds: tuple, weight=lambda t: np.ones_like(t), **kwargs) -> float:
    den = integral(coverage, weight, bounds, **kwargs)
    assert den > 0
    return integral(coverage, lambda t: weight(t)*function(t), bounds, **kwargs)/den


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg, contract = json.loads(args.input.read_text()), json.loads(args.contract.read_text())
    assert cfg["identity"] == "L26-FIG4-1275-COVERAGE-VECTOR-01"
    assert contract["identity"] == "L26-FIG4-PLOT-AND-DECLARED-KERNEL-CONTRACT-01"
    assert hashlib.sha256(args.input.read_bytes()).hexdigest() == contract["coverage_input_sha256"]
    svg = Path(contract["source_svg"])
    assert hashlib.sha256(svg.read_bytes()).hexdigest() == contract["source_svg_sha256"]
    root = ET.parse(svg).getroot()
    red_path = next(e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "path"
                    and hashlib.sha256(e.get("d", "").encode()).hexdigest() == contract["plotted_P_path_d_sha256"])
    red_page = matrix_transform(parse_polyline(red_path.get("d")), red_path.get("transform"))
    axis = cfg["axis_registration_page_points"]
    coverage = axis_points(np.array(cfg["points_page_xy"]), axis)
    red = axis_points(red_page, axis)
    assert np.min(coverage[:, 1]) >= -1e-13
    assert np.min(red[:, 1]) > -1e-3 and np.max(red[:, 1]) < 1
    # No silent clipping: even zeros and vertical steps are kept as published.
    full = (0.0, math.pi)
    cut = tuple(cfg["input_physics"]["theta_cut_rad"])
    red_function = lambda t: np.interp(t, red[:, 0], red[:, 1])
    models = []
    convergence_errors, coordinate_errors, scale_errors = [], [], []
    for model in contract["physics_models"]:
        polar = lambda t: p_and_w(t, model["a2"], model["a4"], model["beta"])[0]
        rate = lambda t: p_and_w(t, model["a2"], model["a4"], model["beta"])[1]
        per_bounds = {}
        for name, bounds in [("full", full), ("cut", cut)]:
            p_source = average(coverage, polar, bounds)
            p_event = average(coverage, polar, bounds, weight=rate)
            p_cos = average(coverage, polar, bounds, coordinate="cos")
            coordinate_errors.append(abs(p_source-p_cos))
            high_order = average(coverage, polar, bounds, nodes=32)
            convergence_errors.append(abs(p_source-high_order))
            scaled = coverage.copy(); scaled[:, 1] *= 7.0
            scale_errors.append(abs(p_source-average(scaled, polar, bounds)))
            p_extra_sine = average(coverage, polar, bounds, weight=np.sin)
            q = (.131+3.25e-4*1275)/(1275/511+511/(1275+511))
            per_bounds[name] = {"Pbar_source_coverage_weighted": p_source,
                                "Pbar_declared_event_weighted": p_event,
                                "Wlab_average_over_source_coverage": average(coverage, rate, bounds),
                                "C_WP_integral_over_C": integral(coverage, lambda t: rate(t)*polar(t), bounds)/integral(coverage, lambda t: np.ones_like(t), bounds),
                                "incorrect_extra_sin_theta_average": p_extra_sine,
                                "Pbar_mean_read_from_red_vector": average(coverage, red_function, bounds),
                                "A0_source_recipe_with_adopted_Q": .5*q*p_source,
                                "conditional_A0_event_model_if_holding_Q_fixed_not_a_recalibration": .5*q*p_event}
        nearest = polar(red[:, 0])
        models.append({**model, "red_vector_P_max_abs_difference": float(np.max(np.abs(nearest-red[:, 1]))),
                       "red_vector_P_RMS_difference": float(np.sqrt(np.mean((nearest-red[:, 1])**2))),
                       "averages": per_bounds,
                       "cut_relative_source_mass": integral(coverage, lambda t: np.ones_like(t), cut)/integral(coverage, lambda t: np.ones_like(t), full),
                       "cut_relative_event_yield_declared_kernel": integral(coverage, rate, cut)/integral(coverage, rate, full),
                       "Qrecipe_to_eventkernel_scale_full": per_bounds["full"]["Pbar_source_coverage_weighted"]/per_bounds["full"]["Pbar_declared_event_weighted"],
                       "transfer_boundary": "A Q calibrated under coverage-weighted Pbar changes if Pbar's kernel definition changes; keeping Q fixed is only a counterfactual diagnostic."})
    assert max(convergence_errors) < 1e-10
    assert max(coordinate_errors) < 2e-8
    assert max(scale_errors) < 1e-12
    assert abs(average(coverage, lambda t: np.ones_like(t)*.4, full)-.4) < 1e-13
    assert average(coverage, lambda t: np.zeros_like(t), full) == 0.0
    plot_full = average(coverage, red_function, full)
    plot_cut = average(coverage, red_function, cut)
    prose_full = cfg["input_physics"]["reported_Pbar_full_approx"]
    prose_cut = cfg["input_physics"]["reported_Pbar_cut_approx"]
    observed_gain = cfg["input_physics"]["reported_A0_cut"]/cfg["input_physics"]["reported_A0_full"]

    # Registration sensitivity only; this is not a confidence interval for data.
    registration = []
    physical = contract["physics_models"][0]
    for sx0, sxpi, sy in itertools.product([-1, 0, 1], repeat=3):
        transformed = axis_points(np.array(cfg["points_page_xy"]), axis, (.01*sx0, .01*sxpi), .01*sy)
        if min(transformed[:, 1]) < -1e-13:
            registration.append({"shifts_pagept": [.01*sx0, .01*sxpi, .01*sy], "status": "rejected-negative-C; not clipped"})
            continue
        pf = lambda t: p_and_w(t, physical["a2"], physical["a4"], physical["beta"])[0]
        registration.append({"shifts_pagept": [.01*sx0, .01*sxpi, .01*sy], "status": "evaluated",
                             "Pbar_full": average(transformed, pf, full), "Pbar_cut": average(transformed, pf, cut)})
    output = {"identity": contract["identity"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "contract_sha256": hashlib.sha256(args.contract.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "raw_pdf_sha256": cfg["raw_pdf_sha256"], "svg_sha256": contract["source_svg_sha256"],
              "coverage_point_count": len(coverage), "red_P_point_count": len(red),
              "axis_registration": axis, "red_path_attrs_except_d": {k:v for k,v in red_path.attrib.items() if k != "d"},
              "red_path_d_sha256": contract["plotted_P_path_d_sha256"],
              "normalized_coverage_theta_C": coverage.tolist(), "models": models,
              "source_prose_comparison": {"prose_approx_full_cut": [prose_full, prose_cut],
                                           "literal_red_curve_C_average_full_cut": [plot_full, plot_cut],
                                           "differences": [plot_full-prose_full, plot_cut-prose_cut],
                                           "literal_last_printed_half_unit_agreement": [abs(plot_full-prose_full) <= .005, abs(plot_cut-prose_cut) <= .005],
                                           "approx_word_is_not_a_precision_or_CI_specification": True,
                                           "status": "literal published-curve arithmetic not closed to prose approximations; actual kernel, selection and unrounded producer remain unknown"},
              "cut_design_not_measured_counts": {"observed_amplitude_ratio": observed_gain,
                                                  "break_even_retained_fraction_for_declared_uniform_histogram_stat_model": 1/observed_gain**2,
                                                  "warning": "Actual Compton-selected counts/background/covariance are absent; do not claim an experimental cut optimum from the drawn source curve."},
              "quadrature_16_vs32_max_abs_difference": max(convergence_errors),
              "theta_vs_cos_Jacobian_control_max_abs_difference": max(coordinate_errors),
              "overall_C_scale_control_max_abs_difference": max(scale_errors),
              "registration_sensitivity_not_CI": registration,
              "scope": "Published 56Co1238 source-coverage and P curves for22Ne1275 only, not rawdetector response or target-specific25Na selection. Source arithmetic and declared alternative kernels remain separate.",
              "joint_response_boundary": "Actual xi marginal has response-weighted <Sigma P>, generally not <Sigma><P>. A single theta coverage curve cannot restore theta-psi correlations, cut/multiplicity migration or fullCov.",
              "calibration_transfer_identity": "With true A=kappa q P_event, Q_recipe=A/(kappa P_source)=q(P_event/P_source). New weighting requires consistently transformed Q; a calibration-to-target ratio cancels only if these factors match.",
              "day_index": 16, "partial_day_indices": [17], "formal_day17_credit": False,
              "experimental_P_or_Q_remeasured": False, "all_internal_checks_passed": True}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"output": str(args.output), "coverage_points": len(coverage), "red_P_points": len(red),
                      "models": models, "coordinate_error": max(coordinate_errors),
                      "quadrature_error": max(convergence_errors), "all_internal_checks_passed": True}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
