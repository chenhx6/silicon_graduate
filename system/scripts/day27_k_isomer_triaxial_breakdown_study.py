#!/usr/bin/env python3
"""Audit K-isomer branches and radiative lifetime conventions without shape fits."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import datetime
from fractions import Fraction
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01"
ARCHIVE = RUN / "scientific-corrections-046/superseded-k-artifacts.json"
REVIEW = ROOT / "knowledge/sources/walker-dracoulis-2001-exotic-isomers.md"


def spin_value(value):
    result = Fraction(str(value))
    if result < 0 or (2 * result).denominator != 1:
        raise ValueError("spin must be a nonnegative integer or half-integer")
    return result


def electromagnetic_selection(ji, pi_i, jf, pi_f, kind, order):
    """Real photon selection rules for parity eigenstates, before K hindrance."""
    ji, jf = spin_value(ji), spin_value(jf)
    if pi_i not in (-1, 1) or pi_f not in (-1, 1):
        raise ValueError("parity must be +1 or -1")
    if kind not in ("E", "M") or type(order) is not int or order < 1:
        raise ValueError("real photons require E/M and an integer multipole order >= 1")
    angular = abs(ji - jf) <= order <= ji + jf
    operator_parity = (-1) ** (order if kind == "E" else order + 1)
    parity = pi_i * pi_f == operator_parity
    return {"triangle_allowed": bool(angular), "parity_allowed": parity,
            "allowed": bool(angular and parity), "operator_parity": operator_parity}


def nominal_forbiddenness(ki, kf, order):
    difference = abs(Fraction(str(ki)) - Fraction(str(kf)))
    if difference.denominator != 1:
        raise ValueError("the nominal K difference must be integral for this photon")
    return int(difference) - order


def radiative_partial_half_life(
    lifetime_s, branch_fraction, *, branch_convention,
    alpha=None, component_photon_fraction=1.0, lifetime_kind="half-life",
):
    """Return component-specific T_gamma, with an explicit branch convention.

    total-transition: branch includes photons and conversion electrons;
    absolute-photon: branch is absolute photons per parent decay, not a
    relative peak intensity. Alpha must then be absent to prevent double use.
    """
    numbers = [lifetime_s, branch_fraction, component_photon_fraction]
    if not all(math.isfinite(x) for x in numbers):
        raise ValueError("lifetime, branch and component fraction must be finite")
    if lifetime_s <= 0 or not 0 < branch_fraction <= 1 or not 0 < component_photon_fraction <= 1:
        raise ValueError("positive lifetime and fractions in (0, 1] are required")
    if lifetime_kind == "mean-lifetime":
        half_life = math.log(2) * lifetime_s
    elif lifetime_kind == "half-life":
        half_life = lifetime_s
    else:
        raise ValueError("lifetime_kind must distinguish half-life from mean-lifetime")
    if branch_convention == "total-transition":
        if alpha is None or not math.isfinite(alpha) or alpha < 0:
            raise ValueError("a nonnegative effective total conversion coefficient is required")
        return half_life * (1 + alpha) / (branch_fraction * component_photon_fraction)
    if branch_convention == "absolute-photon":
        if alpha is not None:
            raise ValueError("absolute photon probabilities already include conversion loss")
        return half_life / (branch_fraction * component_photon_fraction)
    raise ValueError("relative gamma intensities cannot substitute for an absolute branch")


def weisskopf_half_life_seconds(a, energy_keV, kind, order):
    """Walker--Dracoulis Table II, printed99, only its four tabulated modes."""
    table = {("E", 1): (6.76e-6, 3, -2 / 3),
             ("M", 1): (2.20e-5, 3, 0),
             ("E", 2): (9.52e6, 5, -4 / 3),
             ("M", 2): (3.10e7, 5, -2 / 3)}
    if a <= 0 or energy_keV <= 0 or not math.isfinite(energy_keV):
        raise ValueError("positive mass and photon energy in keV are required")
    if (kind, order) not in table:
        raise ValueError("this source Table II does not tabulate the requested multipole")
    coefficient, power, a_power = table[(kind, order)]
    return coefficient * energy_keV ** (-power) * a ** a_power


def reduced_hindrance(t_gamma_s, t_weisskopf_s, nu):
    if not all(math.isfinite(x) for x in [t_gamma_s, t_weisskopf_s, nu]):
        raise ValueError("hindrance inputs must be finite")
    if t_gamma_s <= 0 or t_weisskopf_s <= 0 or nu <= 0:
        raise ValueError("positive partial half-lives and positive K forbiddenness are required")
    total = t_gamma_s / t_weisskopf_s
    return {"F": total, "f_nu": total ** (1 / nu)}


def parse_spin_parity(value):
    if not re.fullmatch(r"(?:\d+|\d+/2)[+-]", value):
        raise ValueError("unrecognized spin-parity input")
    return spin_value(value[:-1]), 1 if value[-1] == "+" else -1


def rejected(call):
    try:
        call()
    except ValueError:
        return True
    return False


def run_study(output=None):
    archive = json.loads(ARCHIVE.read_text())
    rows = []
    for nucleus, d in archive["legacy_inputs"].items():
        # I=K is a historical bandhead assumption, not a verified assignment.
        ji, pi_i = parse_spin_parity(d["K_pi"])
        match = re.match(r"([EM])(\d+) to ([0-9/]+[+-])", d["decay_mode"])
        if match is None:
            raise ValueError(f"cannot audit legacy branch: {nucleus}")
        kind, order = match.group(1), int(match.group(2))
        jf, pi_f = parse_spin_parity(match.group(3))
        selection = electromagnetic_selection(ji, pi_i, jf, pi_f, kind, order)
        alternatives = [f"{mode}{lam}" for lam in range(1, 4) for mode in ["E", "M"]
                        if electromagnetic_selection(ji, pi_i, jf, pi_f, mode, lam)["allowed"]]
        rows.append({"nucleus": nucleus, "input_status": "legacy-unverified",
                     "claimed_branch": d["decay_mode"], "selection": selection,
                     "other_kinematically_allowed_modes_up_to_L3": alternatives,
                     "alternatives_are_not_observed_assignments": True,
                     "can_extract_experimental_f_nu": False,
                     "missing_inputs": ["branch-specific primary locator", "E_gamma and uncertainty",
                         "absolute photon probability or total branch plus alpha",
                         "component fraction if mixed", "radiative Weisskopf convention"],
                     "shape_inference": None})

    source = REVIEW.read_text(encoding="utf-8-sig")
    raw_name = re.search(r'^raw_file: "([^"]+)"', source, re.MULTILINE).group(1)
    raw_hash = hashlib.sha256((ROOT / raw_name).read_bytes()).hexdigest()
    expected_hash = re.search(r'^raw_sha256: "([^"]+)"', source, re.MULTILINE).group(1)
    if raw_hash.lower() != expected_hash.lower():
        raise ValueError("review raw hash mismatch")

    # Synthetic event-rate calculation is independent of the half-life recipe.
    total_rate = math.log(2) / 10
    branch_rate = total_rate * 0.25
    photon_rate = branch_rate / 4
    rate_based_tgamma = math.log(2) / photon_rate
    total_based = radiative_partial_half_life(10, 0.25, branch_convention="total-transition", alpha=3)
    photon_based = radiative_partial_half_life(10, 0.0625, branch_convention="absolute-photon")
    component_based = radiative_partial_half_life(
        10, 0.25, branch_convention="total-transition", alpha=3, component_photon_fraction=0.4)
    correct_hf = electromagnetic_selection(16, 1, 13, -1, "E", 3)
    invalid = [r["nucleus"] for r in rows if not r["selection"]["allowed"]]
    checks = {
        "six_legacy_E2_parity_failures_detected": len(invalid) == 6,
        "review_Hf_E3_allowed_nu5": correct_hf["allowed"] and nominal_forbiddenness(16, 8, 3) == 5,
        "primary_Hf_M4_allowed_nu4": electromagnetic_selection(16, 1, 12, -1, "M", 4)["allowed"]
            and nominal_forbiddenness(16, 8, 4) == 4,
        "primary_Hf_E5_allowed_nu3": electromagnetic_selection(16, 1, 11, -1, "E", 5)["allowed"]
            and nominal_forbiddenness(16, 8, 5) == 3,
        "same_parity_E2_control": electromagnetic_selection(10, 1, 8, 1, "E", 2)["allowed"],
        "zero_to_zero_dipole_excluded": not electromagnetic_selection(0, 1, 0, -1, "E", 1)["allowed"],
        "real_photon_E0_rejected": rejected(lambda: electromagnetic_selection(0, 1, 0, 1, "E", 0)),
        "event_rate_vs_two_branch_conventions": math.isclose(total_based, rate_based_tgamma)
            and math.isclose(photon_based, rate_based_tgamma),
        "component_fraction_control": math.isclose(component_based, 400),
        "mean_lifetime_control": math.isclose(radiative_partial_half_life(
            10 / math.log(2), 0.0625, branch_convention="absolute-photon", lifetime_kind="mean-lifetime"), 160),
        "double_conversion_rejected": rejected(lambda: radiative_partial_half_life(
            10, 0.0625, branch_convention="absolute-photon", alpha=3)),
        "relative_intensity_rejected": rejected(lambda: radiative_partial_half_life(
            10, 0.25, branch_convention="relative-to-326keV")),
        "missing_conversion_rejected": rejected(lambda: radiative_partial_half_life(
            10, 0.25, branch_convention="total-transition")),
        "zero_branch_rejected": rejected(lambda: radiative_partial_half_life(
            10, 0, branch_convention="absolute-photon")),
        "nu_zero_rejected": rejected(lambda: reduced_hindrance(100, 1, 0)),
        "E2_energy_scaling_keV": math.isclose(
            weisskopf_half_life_seconds(178, 200, "E", 2) /
            weisskopf_half_life_seconds(178, 100, "E", 2), 1 / 32),
        "unsupported_table_E3_not_invented": rejected(lambda: weisskopf_half_life_seconds(178, 13, "E", 3)),
    }
    if not all(checks.values()):
        raise ArithmeticError(f"physical branch checks failed: {checks}")
    primary_manifest = ROOT / "outputs/literature-acquisition/20261030-day27-smith2003-hf178.json"
    primary = json.loads(primary_manifest.read_text())
    primary_hash = hashlib.sha256((ROOT / primary["staged_file"]).read_bytes()).hexdigest()
    if primary_hash != primary["sha256"]:
        raise ValueError("primary manuscript staging hash mismatch")
    reported_branches = [
        {"branch": "16+ -> 13-", "mode": "E3", "energy_keV": 12.7,
         "nu": 5, "reported_f_nu": 66, "reported_f_nu_error": 1,
         "relative_I_gamma_percent": None,
         "evidence_kind": "adopted converted branch; gamma not directly detected"},
        {"branch": "16+ -> 12-", "mode": "M4", "energy_keV": 309.5,
         "nu": 4, "reported_f_nu": 72, "reported_f_nu_error": 2,
         "relative_I_gamma_percent": 0.015,
         "evidence_kind": "direct weak gamma coincidence with prior assignment constraints"},
        {"branch": "16+ -> 11-", "mode": "E5", "energy_keV": 587.0,
         "nu": 3, "reported_f_nu": 165, "reported_f_nu_error": 5,
         "relative_I_gamma_percent": 0.0062,
         "evidence_kind": "direct weak gamma coincidence with prior assignment constraints"},
    ]
    for branch in reported_branches:
        branch.update({
            "source_claim": "SM03-D27-2/3/4/5",
            "source_locator": "manuscript PDF5/printed3 Table I; PDF6-7 hindrance discussion",
            "independently_extracted_hindrance": False,
            "relative_intensity_normalizer": "325.5-keV gamma = 100; not absolute branch",
            "absolute_branch_probability": None,
            "radiative_partial_half_life_s": None,
        })
    results = {
        "schema_version": 2,
        "observed_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "investigation": "K-isomer parity, multipolarity and radiative partial lifetime audit",
        "scientific_status": "six invalid branches rejected; isotope shape/lifetime-collapse claims withdrawn",
        "review_source": {"knowledge": REVIEW.relative_to(ROOT).as_posix(), "raw_file": raw_name,
            "raw_sha256": raw_hash, "reading_scope": "PDF7/16-18, printed89/98-100, Fig3/Sec3.3/TableII"},
        "review_Hf_reference": {"branch": "16+ -> 13-", "mode": "E3", "E_gamma_keV_rounded": 13,
            "delta_K": 8, "nu": 5, "reported_f_nu": 66,
            "reported_not_independently_extracted": True, "radiative_partial_half_life_s": None},
        "primary_source": {"knowledge": "knowledge/sources/smith-2003-hf178-isomer-gamma-decay.md",
            "doi": "10.1103/PhysRevC.68.031302", "manuscript_sha256": primary_hash,
            "reading_scope": primary["reading_scope"]},
        "primary_reported_Hf_branches": reported_branches,
        "legacy_input_audit": rows,
        "invalid_legacy_nuclei": invalid,
        "synthetic_normalization_control": {"input_status": "synthetic-no-isotope-measurement",
            "T_level_half_life_s": 10, "b_total": 0.25, "alpha_effective": 3,
            "b_gamma_absolute": 0.0625, "T_gamma_s_from_event_rates": rate_based_tgamma,
            "T_gamma_s_from_total_branch": total_based, "T_gamma_s_from_photon_probability": photon_based,
            "component_fraction": 0.4, "component_T_gamma_s": component_based},
        "legacy_hindrance_ratio_arithmetic": {"status": "conditional-only-not-measured-lifetime-ratio",
            "assumed_f_reference": 60.5, "assumed_f_target": 3.44, "assumed_nu": 6,
            "ratio": (60.5 / 3.44) ** 6,
            "reason": "actual partial lifetimes also depend on branch energies, multipolarities and Weisskopf estimates"},
        "checks": checks, "no_shape_classifier_or_tunneling_fit": True,
        "no_new_experimental_confidence_or_curriculum_credit": True,
    }
    output = output or RUN / "continuation-studies/k-isomer-triaxial/k_isomer_branch_audit_corrected.json"
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "invalid_legacy_nuclei": invalid,
                      "review_Hf_branch": results["review_Hf_reference"],
                      "synthetic_Tgamma_seconds": total_based, "checks": checks}, indent=2))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    run_study(parser.parse_args().output)
