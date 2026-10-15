#!/usr/bin/env python3
"""Selected real 67Ga ENSDF fields and a conditional strength consistency check.

The original source lifetimes and strengths remain evaluated fit/derived
records, not new measurements. Blank CC, unknown covariance and unobserved
channels are never silently replaced with zero. Zero-IC cases are explicit
mathematical controls, not an experimental L4 replay.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

import numpy as np
from scipy.constants import c, e, epsilon_0, hbar

from day14_ensdf_crosswalk import number, uncertainty


def records(path):
    lines = path.read_text().splitlines()
    levels, gammas = [], []
    level, gamma = None, None
    for n, raw in enumerate(lines, 1):
        line = raw.ljust(80)
        if line[:5].strip() != "67GA":
            continue
        if line[5:7] == "  " and line[7] == "L":
            level = dict(line=n, energy_keV=number(line[9:19]),
                         energy_text=line[9:19].strip(),
                         sigma_energy_keV=uncertainty(line[9:19], line[19:21]),
                         Jpi=line[21:39].strip(), half_life_text=line[39:49].strip(),
                         half_life_error_digits=line[49:55].strip(), raw=raw,
                         comments=[])
            levels.append(level)
            gamma = None
        elif line[5:7] == "  " and line[7] == "G":
            if level is None:
                raise AssertionError("gamma without parent level")
            gamma = dict(line=n, parent_energy_keV=level["energy_keV"],
                         parent_line=level["line"], energy_keV=number(line[9:19]),
                         energy_text=line[9:19].strip(),
                         sigma_energy_keV=uncertainty(line[9:19], line[19:21]),
                         RI=number(line[21:29]),
                         sigma_RI=uncertainty(line[21:29], line[29:31]),
                         multipolarity=line[31:41].strip(),
                         mixing_ratio_text=line[41:49].strip(),
                         mixing_ratio=number(line[41:49]),
                         mixing_ratio_error_digits=line[49:55].strip(),
                         sigma_mixing_ratio=uncertainty(line[41:49], line[49:55]),
                         CC=number(line[55:62]), flag=line[76:77].strip(),
                         raw=raw, comments=[])
            gammas.append(gamma)
        elif line[7] == "G" and gamma is not None:
            gamma["comments"].append(dict(line=n, text=raw))
        elif line[7] == "L" and level is not None:
            level["comments"].append(dict(line=n, text=raw))
    return lines, levels, gammas


def select_level(levels, energy):
    matches = [x for x in levels if x["energy_keV"] is not None and
               abs(x["energy_keV"]-energy) < 1]
    if len(matches) != 1:
        raise AssertionError("selected level is not unique")
    return matches[0]


def level_gammas(gammas, level):
    return [x for x in gammas if x["parent_line"] == level["line"]]


def half_life_ps(level):
    match = re.fullmatch(r"([\d.]+)\s+(PS|NS)", level["half_life_text"])
    if not match:
        raise ValueError("missing or nonnumeric selected half-life")
    scale = {"PS": 1., "NS": 1000.}[match[2]]
    return float(match[1])*scale, uncertainty(
        match[1], level["half_life_error_digits"])*scale


def dco(gamma):
    for row in gamma["comments"]:
        match = re.search(r"DCO=([\d.]+)\s+\{I(\d+)\}", row["text"])
        if match:
            return dict(value=float(match[1]), quoted_error=uncertainty(
                match[1],match[2]), line=row["line"], raw=row["text"])
    return None


def rate_coefficient_and_WU(A):
    hc = hbar*c/e/1e6*1e15  # MeV fm
    hb = hbar/e/1e6        # MeV s
    coulomb = e*e/(4*math.pi*epsilon_0)/e/1e6*1e15  # MeV fm
    coefficient = 8*math.pi*3/(2*15**2)*coulomb/(hb*hc**5)
    weisskopf = (3/5)**2/(4*math.pi)*(1.2*A**(1/3))**4
    return coefficient, weisskopf


def conditional_strength(E_MeV, T_half_ps, photon_ratio, cc_strong, cc_weak,
                         delta, *, complete_inventory_assumed):
    if cc_strong is None or cc_weak is None or not complete_inventory_assumed:
        raise ValueError("CC and complete inventory required; blank is not zero")
    if E_MeV <= 0 or T_half_ps <= 0 or min(photon_ratio, cc_strong, cc_weak) < 0:
        raise ValueError("positive energy/time and nonnegative rate ledger required")
    coefficient, wu = rate_coefficient_and_WU(67)
    total_rate = math.log(2)/(T_half_ps*1e-12)
    denominator = 1+cc_strong+photon_ratio*(1+cc_weak)
    gamma_rate = total_rate/denominator
    E2_rate = gamma_rate/(1+delta*delta)  # declared E2/M3 gamma truncation
    b = E2_rate/(coefficient*E_MeV**5)
    return dict(total_rate_s=total_rate, gamma958_rate_s=gamma_rate,
                E2_gamma_rate_s=E2_rate, rate_ledger_denominator=denominator,
                B_E2_e2fm4=b, B_E2_WU=b/wu)


def audit(paths, receipts):
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    selected = {}
    for label, path in paths.items():
        lines, levels, gammas = records(path)
        check(label+"_real_object_identity", "67GA" in lines[1] and
              "200512" in lines[1] and "05NDS" in lines[1])
        check(label+"_downloaded_text_hash_matches_receipt",
              hashlib.sha256(path.read_bytes()).hexdigest() == receipts[label]["text_sha256"])
        parent = select_level(levels, 3031.7)
        gs = level_gammas(gammas, parent)
        strong = [x for x in gs if 957 < x["energy_keV"] < 959]
        check(label+"_one_same_parent_958_line", len(strong) == 1 and
              parent["Jpi"] == "13/2+")
        selected[label] = dict(parent=parent, gammas=gs, strong958=strong[0],
                               header=lines[:26], lines_total=len(lines))
        if label == "adopted":
            selected[label]["daughter2074"] = select_level(levels, 2073.755)
            selected[label]["daughter2862"] = select_level(levels, 2862.45)
            selected[label]["feeder3578"] = select_level(levels, 3577.95)
            selected[label]["feeder3856"] = select_level(levels, 3855.99)
            selected[label]["daughter2074_gammas"] = level_gammas(
                gammas,selected[label]["daughter2074"])
        if label == "ni58":
            d = select_level(levels,2073.2)
            selected[label]["daughter2074"] = d
            selected[label]["daughter2074_gammas"] = level_gammas(gammas,d)
    a, f, al, ni = (selected[x] for x in ("adopted", "fe12c", "alpha", "ni58"))
    g = a["strong958"]
    check("evaluated_E2_optional_M3_and_finite_quoted_delta_retained",
          g["multipolarity"] == "E2(+M3)" and
          g["mixing_ratio_text"] == "-0.00" and
          np.isclose(g["sigma_mixing_ratio"], .01))
    check("source_blank_CC_retained_as_missing", g["CC"] is None)
    check("Fe_multipolarity_and_MR_are_transferred_not_second_measurement",
          any("M,MR" in s and "From adopted gammas" in s for s in f["header"]))
    check("adopted_flagD_and_alpha_flagA_retain_lineage",
          any("FLAG=DQ" in x["text"] for x in g["comments"]) and
          al["strong958"]["flag"] == "A")
    check("alpha_primary_metadata1978Al32_and_RDM_method_retained",
          "1978AL32" in al["header"][1] and
          any("T(R)" in s and "1978Al32" in s for s in al["header"]))
    check("Fe_global_RI_normalizer_is359plus1202",
          any("I|g(359)+I|g(1202)=100" in s for s in f["header"]))
    check("same_line_has_different_RI_normalizations",
          np.isclose(f["strong958"]["RI"], 58.2) and np.isclose(g["RI"], 100))
    check("Ni1999data_identified_without_adding_independent_MR",
          "1999DA10" in ni["header"][1] and
          ni["strong958"]["mixing_ratio"] is None)
    weak = [x for x in a["gammas"] if 168 < x["energy_keV"] < 170]
    check("weak168p8_branch_not_silently_dropped", len(weak) == 1 and
          np.isclose(weak[0]["RI"], .2) and np.isclose(weak[0]["sigma_RI"], .1))
    weak = weak[0]
    check("weak_MR_and_conversion_stay_unclassified_missing",
          weak["multipolarity"] == "" and weak["CC"] is None)
    check("weak_and_strong_Ni_RIs_match_adopted_values",
          any(np.isclose(x["energy_keV"],168.8) and np.isclose(x["RI"],.2)
              for x in ni["gammas"]) and np.isclose(ni["strong958"]["RI"],100))
    a554 = [x for x in a["daughter2074_gammas"] if 553 < x["energy_keV"] < 556][0]
    n554 = [x for x in ni["daughter2074_gammas"] if 553 < x["energy_keV"] < 556][0]
    n871 = [x for x in ni["daughter2074_gammas"] if 870 < x["energy_keV"] < 873][0]
    d958,d554,d871 = dco(ni["strong958"]),dco(n554),dco(n871)
    check("same_reported_DCO_does_not_uniquely_label_E2", g["multipolarity"] ==
          "E2(+M3)" and a554["multipolarity"] == "E1(+M2)" and
          np.isclose(d958["value"],1.45) and np.isclose(d554["value"],1.45))
    check("same_parent_two_E1_lines_can_have_different_reported_DCO",
          np.isclose(d871["value"],.77) and n554["parent_line"] == n871["parent_line"])
    thalf, dt = half_life_ps(a["parent"])
    tau, dtau = thalf/math.log(2), dt/math.log(2)
    check("selected_half_life_and_mean_not_confused", np.isclose(thalf,4.5) and
          np.isclose(dt,.4) and np.isclose(tau,6.4921276840003355))
    long_lifetimes = {}
    for key in ["feeder3578", "feeder3856"]:
        t, err = half_life_ps(a[key])
        long_lifetimes[key] = dict(T_half_ps=t, quoted_error_ps=err,
                                   mean_tau_ps=t/math.log(2))
    check("nanosecond_and_picosecond_feeders_use_their_own_parents",
          np.isclose(long_lifetimes["feeder3578"]["T_half_ps"],160) and
          np.isclose(long_lifetimes["feeder3856"]["T_half_ps"],11) and
          long_lifetimes["feeder3856"]["mean_tau_ps"] > tau)
    coefficient, wu = rate_coefficient_and_WU(67)
    check("CODATA_E2_coefficient_matches_existing_Wiki_unit_reconstruction",
          np.isclose(coefficient,1.2251867220e9,rtol=5e-11))
    E, ratio = g["energy_keV"]/1000, weak["RI"]/g["RI"]
    control = conditional_strength(E, thalf, ratio, 0., 0., 0.,
                                   complete_inventory_assumed=True)
    pure_only = conditional_strength(E, thalf, 0., 0., 0., 0.,
                                     complete_inventory_assumed=True)
    source_be2 = [x for x in g["comments"] if "BE2W=" in x["text"]]
    check("source_evaluated_strength_marker_retained", len(source_be2) == 1 and
          "BE2W=9.6 9" in source_be2[0]["text"])
    check("conditional_zeroIC_two_gamma_rounding_matches_reported9p6",
          round(control["B_E2_WU"],1) == 9.6)
    check("weak_branch_reduces_conditional_rate_not_strengthens_it",
          control["B_E2_WU"] < pure_only["B_E2_WU"] and
          np.isclose(control["B_E2_WU"]*(1+ratio),pure_only["B_E2_WU"]))
    wrong_tau = control["B_E2_WU"]/math.log(2)
    check("half_life_as_mean_gives_a_material_factor_error", wrong_tau > 13 and
          np.isclose(wrong_tau/control["B_E2_WU"],1/math.log(2)))
    missing_blocked = False
    try:
        conditional_strength(E, thalf, ratio, g["CC"], weak["CC"],0.,
                             complete_inventory_assumed=True)
    except ValueError:
        missing_blocked = True
    check("actual_missing_CC_blocks_an_unqualified_absolute_strength", missing_blocked)
    controls = []
    for ccweak in [0., 1., 100.]:
        controls.append(dict(cc_weak_chosen=ccweak, **conditional_strength(
            E,thalf,ratio,0.,ccweak,0.,complete_inventory_assumed=True)))
    check("tiny_photon_branch_need_not_mean_tiny_total_rate", controls[-1][
        "B_E2_WU"] < .9*controls[0]["B_E2_WU"])
    critical_ccweak = (1+ratio)*(1/.9-1)/ratio
    critical = conditional_strength(E,thalf,ratio,0.,critical_ccweak,0.,
                                    complete_inventory_assumed=True)
    check("chosen_conversion_10percent_boundary_is_algebraically_correct",
          np.isclose(critical["B_E2_WU"],.9*control["B_E2_WU"]))
    mixing = []
    for delta in [0.,.01,.02]:
        mixing.append(dict(delta_chosen=delta, M3_gamma_fraction=delta**2/(1+delta**2),
                           **conditional_strength(E,thalf,ratio,0.,0.,delta,
                                                  complete_inventory_assumed=True)))
    check("quoted_delta_scale_is_not_exact_zero_or_hard_confidence_bound",
          np.isclose(mixing[1]["M3_gamma_fraction"],.0000999900009999))
    check("E2_M3_rate_fractions_sum_one_and_rate_is_phase_insensitive", all(
        np.isclose(1/(1+x["delta_chosen"]**2)+x["M3_gamma_fraction"],1)
        for x in mixing))
    closure = dict(strong958_E_parent_minus_daughter_minus_gamma_keV=
                   a["parent"]["energy_keV"]-a["daughter2074"]["energy_keV"]-g["energy_keV"],
                   weak168p8_E_parent_minus_daughter_minus_gamma_keV=
                   a["parent"]["energy_keV"]-a["daughter2862"]["energy_keV"]-weak["energy_keV"])
    check("mixed_dataset_energy_central_residuals_are_not_forced_to_zero",
          np.isclose(closure["strong958_E_parent_minus_daughter_minus_gamma_keV"],.005) and
          np.isclose(closure["weak168p8_E_parent_minus_daughter_minus_gamma_keV"],.52))
    dr_independent = ratio*math.sqrt((weak["sigma_RI"]/weak["RI"])**2+
                                   (g["sigma_RI"]/g["RI"])**2)
    rel_sigma = math.sqrt((dt/thalf)**2+(5*g["sigma_energy_keV"]/g["energy_keV"])**2+
                         (dr_independent/(1+ratio))**2)
    return dict(kind="L3 selected evaluated-data crosswalk plus L2 conditional rate consistency",
                selected_source_records=selected, half_life_input_ps=thalf,
                mean_tau_ps=tau, transformed_quoted_time_error_ps=dtau,
                separate_feeder_lifetimes=long_lifetimes,
                E2_rate_coefficient_s_MeV_e2fm4=coefficient, Weisskopf_unit_e2fm4=wu,
                conditional_two_observed_gamma_zeroIC=control,
                conditional_single_gamma_zeroIC=pure_only,
                wrong_half_life_as_tau_control_B_E2_WU=wrong_tau,
                independent_marginal_approximation=dict(
                    photon_ratio=ratio, sigma_ratio=dr_independent,
                    sigma_B_E2_WU=control["B_E2_WU"]*rel_sigma,
                    actual_source_joint_covariance=None),
                chosen_weak_conversion_controls=controls,
                chosen_ccweak_for10percent_change=critical_ccweak,
                chosen_mixing_sensitivity_not_confidence_bounds=mixing,
                central_energy_closures_only=closure,
                source_DCO_counter_example=dict(
                    DCO958_E2=d958,DCO554_E1=d554,DCO871_same_parent_E1=d871,
                    exact_gate_geometry_and_reference_not_supplied=True,
                    not_a_causal_assignment_to_spin_change_alone=True),
                boundaries=[
                    "The NDS evaluation and its adopted/reaction objects are reused records, not additional independent experiments.",
                    "Quoted delta error0.01 preserves finite uncertainty; E2(+M3) and missing higher/weak-line inputs are not exact-zero evidence.",
                    "The4.5ps input is parent half-life; the two feeders have different mean lifetimes and cannot replace it.",
                    "ZeroIC and a complete two-gamma ledger are explicit controls. Source blank CC, complete unseen channels and actual covariance are unknown.",
                    "Evaluated BE2W9.6(9) is retained; conditional numerical agreement is not a new strength measurement or reconstruction of evaluator code.",
                    "The mixing-fraction controls use an E2/M3 gamma truncation; phase/sign and angular interference require the source convention and full response.",
                    "Missing primary papers, actual angular/line-shape data, stopping/feeding, response and fitCov keep experimental L4 not-ready.",
                    "Day14 remains active; Day15 remains an uncredited partial preview; no Day16 card is opened."],
                checks=checks, checks_passed=len(checks))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--ni-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    receipts = {x["label"]:x for x in json.loads(args.receipt.read_text())}
    receipts["ni58"] = json.loads(args.ni_receipt.read_text())
    paths = {label:args.directory/(label+".ens") for label in receipts}
    result = audit(paths,receipts)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(checks_passed=result["checks_passed"],
                          all_checks_true=all(result["checks"].values()),
                          output=str(args.output))))


if __name__ == "__main__":
    main()
