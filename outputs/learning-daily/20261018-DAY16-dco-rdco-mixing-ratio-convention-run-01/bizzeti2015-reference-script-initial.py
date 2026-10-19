#!/usr/bin/env python3
"""B15 literal-sign, finite-geometry ambiguity and printed-table audit.

Source axes and operational table values remain separate; no raw events fit.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import sympy as sp

from day16_co60_conditional_stokes import operators, LINEAR_BASIS


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def weighted_mean(values, sigma):
    weights = 1/(sigma*sigma)
    mean = float(weights@values/weights.sum())
    error = float(1/math.sqrt(weights.sum()))
    chi2 = float(np.sum(((values-mean)/sigma)**2))
    return {"mean": mean, "standard_error_if_independent": error, "chi2": chi2,
            "reduced_chi2_df5": chi2/5}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "B15-SIGN-FINITEANGLE-REFERENCE-AUDIT-01"
    assert sha(Path(cfg["raw"])) == cfg["raw_sha256"]
    a0, a2, phi = sp.symbols("a0 a2 phi", real=True)
    fit = a0+a2*sp.cos(2*phi)
    endpoint = sp.simplify((fit.subs(phi, sp.pi/2)-fit.subs(phi, 0))
                          /(fit.subs(phi, sp.pi/2)+fit.subs(phi, 0)))
    assert endpoint == -a2/a0
    # Compare literal Eq.(1)'s electric-axis term with the declared pure E2
    # intensity coefficients; not the Pd state or a fitted reference density.
    x, psi = sp.symbols("x psi", real=True)
    aa2, aa4 = sp.symbols("aa2 aa4", real=True)
    w = 1+aa2*sp.legendre(2, x)+aa4*sp.legendre(4, x)
    hb = (-sp.Rational(3, 2)*aa2+sp.Rational(5, 8)*aa4*(7*x*x-1))*(1-x*x)
    hj = (sp.Rational(3, 2)*aa2-sp.Rational(5, 8)*aa4*(7*x*x-1))*(1-x*x)
    assert sp.simplify(hb+hj) == 0
    assert sp.trigsimp(w+hb*sp.cos(2*psi)-(w+hj*sp.cos(2*(psi+sp.pi/2)))) == 0
    pure = {aa2: sp.Rational(5, 7), aa4: -sp.Rational(12, 7)}
    wm, hbm, hjm = [sp.factor(v.subs(pure)) for v in [w, hb, hj]]
    assert sp.simplify(hbm/wm) == -1 and sp.simplify(hjm/wm) == 1
    # Independent classical m=0 electric quadrupole radiation is meridional.
    theta = sp.symbols("theta", real=True)
    n = sp.Matrix([sp.sin(theta), 0, sp.cos(theta)])
    et = sp.Matrix([sp.cos(theta), 0, -sp.sin(theta)])
    ep = sp.Matrix([0, 1, 0])
    moment = sp.diag(-sp.Rational(1, 2), -sp.Rational(1, 2), 1)
    field = moment*n-n*(n.dot(moment*n))
    assert sp.trigsimp(field.dot(n)) == 0 and field.dot(ep) == 0
    classical_I = sp.factor(sp.trigsimp(field.dot(field)))
    assert sp.trigsimp(classical_I-sp.Rational(9, 4)*sp.sin(theta)**2*sp.cos(theta)**2) == 0
    numeric = []
    for degree in [30., 60., 120.]:
        op = operators(4, 0, (("E", 2, 1.),), math.radians(degree), 0., "native")
        v = op[:, 0, 2]
        rho = LINEAR_BASIS@np.outer(v, v.conj())@LINEAR_BASIS.conj().T
        degreeP = float((rho[0, 0]-rho[1, 1]).real/np.trace(rho).real)
        assert abs(degreeP-1) < 1e-12
        numeric.append({"theta_deg": degree, "helicity_E2_m0_Pparallel": degreeP,
                        "literal_B15_Eq1_2_P_if_same_axes": -1.})
    # Appendix B's printed sine projects onto the outgoing instead of incoming
    # direction. It cannot be paired with the stated cosine for generic angles.
    nr1 = sp.Matrix([1, 0, 0])
    nr12 = sp.Matrix([sp.cos(phi), sp.sin(phi), 0])
    direction = sp.Matrix([sp.sin(phi)*sp.sin(theta), -sp.cos(phi)*sp.sin(theta), sp.cos(theta)])
    projected = sp.trigsimp(nr1.cross(nr12).dot(direction))
    assert sp.trigsimp(projected-sp.sin(phi)*sp.cos(theta)) == 0
    norm_defect = sp.trigsimp(sp.cos(phi)**2+projected**2-1)
    assert sp.trigsimp(norm_defect+sp.sin(phi)**2*sp.sin(theta)**2) == 0
    # Full geometry degeneracy condition, stronger than energy-order validity.
    t, half, q = sp.symbols("t half q", real=True)
    c1, c2 = sp.cos(t+half), sp.cos(sp.pi-t+half)
    assert sp.trigsimp(sp.expand_trig((1-c1)*(1-c2)-(sp.sin(t)+sp.sin(half))**2)) == 0
    critical = []
    for isotope, energy in cfg["energies_keV"].items():
        for alpha in cfg["angles_alpha_deg"]:
            sine = 511/energy-math.sin(math.radians(alpha/2))
            angles = []
            if 0 < sine <= 1:
                base = math.degrees(math.asin(sine))
                angles = [base+alpha/2, 180-base+alpha/2]
                for a in angles:
                    b = 180+alpha-a
                    assert abs((1-math.cos(math.radians(a)))*(1-math.cos(math.radians(b)))-(511/energy)**2) < 1e-12
            critical.append({"isotope_or_source": isotope, "E_keV": energy, "alpha_deg": alpha,
                "real_solution": bool(angles), "critical_angles_deg": angles,
                "critical_cosines": [math.cos(math.radians(a)) for a in angles]})
    assert not any(v["real_solution"] for v in critical if v["isotope_or_source"] == "108Pd")
    tables = {}
    for isotope, values in cfg["tables"].items():
        data = np.array(values["As_P_A_sigmaA"])
        ratios = data[:, 0]/data[:, 1]
        quoted = weighted_mean(data[:, 2], data[:, 3])
        ratio_errors = values["sigma_As_printed"]/abs(data[:, 1])
        replay = weighted_mean(ratios, ratio_errors)
        wrong_center_ratios = data[:, 0]/np.array(values["P_center_Table2"])
        tables[isotope] = {"As_over_eventweighted_P": ratios.tolist(),
            "reported_A_minus_replayed_ratio": (data[:, 2]-ratios).tolist(),
            "quoted_A_weightedmean_if_independent": quoted,
            "rounded_As_P_replay_if_P_fixed_and_rows_independent": replay,
            "wrong_centerP_instead_of_eventweightedP_control": wrong_center_ratios.tolist(),
            "source_average": values["source_mean"], "source_error": values["source_error"],
            "shared_Pmodel_reference_Cov_or_cut_component_recovered": False}
        assert abs(quoted["mean"]-values["source_mean"]) < .002
        assert abs(quoted["standard_error_if_independent"]-values["source_error"]) < .001
    centers = np.deg2rad([18., 54., 90., 126., 162.])
    design = np.column_stack([np.ones(5), np.cos(2*centers)])
    ratio_fits = []
    for index, row in enumerate(cfg["table5_raw_MCratios"]):
        beta, *_ = np.linalg.lstsq(design, np.array(row), rcond=None)
        ratio_fits.append({"counter": index+3, "unweighted_rounded_bin_A": float(beta[1]/beta[0]),
            "source_A": cfg["table5_A_printed"][index],
            "original_bin_counts_Cov_or_fitweights_known": False})
    average_beta, *_ = np.linalg.lstsq(design, np.array(cfg["table5_average_bins"]), rcond=None)
    sinc = math.sin(math.pi/5)/(math.pi/5)
    result = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "source_sha256": cfg["raw_sha256"],
        "literal_Eq9_Eq10_endpoint_asymmetry": str(endpoint),
        "literal_operational_plus_fit_sign_does_not_match_same_zero_endpoint_definition": True,
        "conditional_pure_E2_axis_probe": {"intensity_W": str(wm), "B15_literal_cos2coefficient": str(hbm),
            "Jones_meridional_cos2coefficient": str(hjm), "axis_rotation_pi_over2_reconciles_formulas": True,
            "classical_quadrupole_transverse_field_squared": str(classical_I), "helicity_controls": numeric,
            "actual_Pd_P_or_source_producer_repaired": False},
        "AppendixB_literal_sine_probe": {"outgoing_projection": str(projected),
            "cos_sin_pair_norm_defect": str(norm_defect),
            "cos_only_harmonic_can_still_use_cos2_equals2cos_squared_minus1": True,
            "actual_angle_producer_certified_or_repaired": False},
        "full_geometry_critical_angle_rows": critical,
        "Tables3_4_replays": tables, "Table5_unweighted_MC_bin_diagnostics": ratio_fits,
        "Table5_average_bins_unweighted_A": float(average_beta[1]/average_beta[0]),
        "Table5_average_A_source": cfg["table5_average_A_printed"],
        "bin36deg_cos2_attenuation": sinc,
        "no_tracking_over_tracking_A_ratio_from_source": cfg["table5_average_A_printed"]/.484,
        "literal_smearing_units_100keV": {"FWHM_mm": cfg["smearing"]["printed_b_mm_sqrt_keV"]/10,
            "sigma_mm": cfg["smearing"]["printed_b_mm_sqrt_keV"]/10/cfg["smearing"]["FWHM_to_sigma"],
            "actual_producer_units_or_measured_resolution_certified": False},
        "figure5_axis_micrometers_vs_text15millimeters_boundary": True,
        "full_new_GOSIA_response_or_experimental_fit": False}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: result[key] for key in ["literal_Eq9_Eq10_endpoint_asymmetry", "full_geometry_critical_angle_rows",
        "Tables3_4_replays", "Table5_average_bins_unweighted_A", "Table5_average_A_source",
        "bin36deg_cos2_attenuation", "no_tracking_over_tracking_A_ratio_from_source"]}, indent=2))


if __name__ == "__main__":
    main()
