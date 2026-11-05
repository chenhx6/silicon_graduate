#!/usr/bin/env python3
"""Local 129Ba ENSDF inventory. All writes are confined to this script directory.

Run from any directory: python3 -B /workspace/wiki/tmp/ba129-lifetime-readiness/extract_holdout.py
No network, reference retrieval, repository mutation, or B(XL) recomputation.
"""
import csv
import hashlib
import io
import json
import math
import re
import subprocess
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path("/workspace/wiki")
OUT = ROOT / "tmp/ba129-lifetime-readiness"
BASE = "raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/"
INPUTS = {
    "R": (BASE + "nndc-129ba-129056013-201408-09194d4feed3.ens",
          "09194d4feed3bbda013c551ce5ba9ecf55a25799e8c46ec22f23685df1c1ef19"),
    "A": (BASE + "nndc-129ba-129056001-201408-15d8e353eb23.ens",
          "15d8e353eb23d55847dc0d0127591fd2fb23e6da63ae98146747aecb233f65f6"),
    "S": ("knowledge/sources/nndc-2014-129ba-365-coefficient-records.md",
          "ee15d30b0bc9b0a35d2c54f32f4f2bb054aa29fd2e36c36fe5de478608623e6b"),
    "C": ("raw/papers/2024_Chakraborty et al_Exploring the possibility of wobbling motion in Ba 129.pdf",
          "d5729de577067f8afeab771afb51328989772c68962a938d553bccb50f0c0808"),
}
BANDS = {"A": 1, "D": 2, "B": 3, "C": 4}
TARGETS = {"365": ("643.6", "364.7"), "521": ("1318.4", "521.0"),
           "671": ("2146.3", "670.8")}
EXPECTED_LEVELS = {
    "182.04", "278.81", "643.6", "797.4", "883.43", "1210.0",
    "1318.4", "1475.4", "1545.3", "1845.0", "2146.3", "2281.2",
    "2336.7", "2599.6", "3094.2", "3179.4", "3430.6",
}


def write(name, text):
    path = OUT / name
    assert OUT.resolve() == OUT and path.resolve().parent == OUT
    path.write_text(text, encoding="utf-8")


def number(text):
    return float(text) if text.strip() else None


def uncertainty(value, digits):
    """ENSDF uncertainty in last quoted digits. Unknown/qualifier stays null."""
    if not value or not digits or not digits.isdigit():
        return None
    return float(Decimal(digits) * Decimal(10) ** Decimal(value).as_tuple().exponent)


def precision(value):
    return float(Decimal(10) ** Decimal(value).as_tuple().exponent)


def level_id(energy):
    # Task-local ID, not an official ENSDF level identifier.
    return "129Ba_Ex" + energy.replace(".", "p") + "keV"


def parse(text, alias):
    levels, unplaced = [], []
    current_level = current_gamma = None
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.ljust(80)
        record = {"line": lineno, "locator": f"{alias}:{lineno}", "raw": raw}
        if line[5:8] == "  L":
            record.update({
                "E": line[9:19].strip(), "DE": line[19:21].strip(),
                "J": line[21:39].strip(), "T": line[39:49].strip(),
                "DT": line[49:55].strip(), "band": line[76:77].strip(),
                "gammas": [], "continuations": [],
            })
            levels.append(record)
            current_level, current_gamma = record, None
        elif line[5:8] == "  G":
            record.update({name: line[start:end].strip() for name, start, end in [
                ("E", 9, 19), ("DE", 19, 21), ("RI", 21, 29), ("DRI", 29, 31),
                ("M", 31, 41), ("MR", 41, 49), ("DMR", 49, 55),
                ("CC", 55, 62), ("DCC", 62, 64), ("TI", 64, 74),
            ]})
            record["continuations"] = []
            if current_level is None:
                unplaced.append(record)
            else:
                current_level["gammas"].append(record)
            current_gamma = record
        elif line[7] == "G" and current_gamma is not None:
            current_gamma["continuations"].append(record)
        elif line[7] == "L" and current_level is not None:
            current_level["continuations"].append(record)
    return levels, unplaced


def explicit_final(gamma):
    for row in gamma["continuations"]:
        match = re.search(r"\bFL=([\d.]+)", row["raw"])
        if match:
            return match[1], row["locator"]
    return None


def resolve_final(parent, rg, ag, reaction, adopted):
    for gamma in [ag, rg]:
        explicit = explicit_final(gamma)
        if explicit:
            energy, locator = explicit
            assert energy in adopted
            return adopted[energy], "explicit_FL@" + locator
    target = float(parent["E"]) - float(rg["E"])
    candidates = [l for l in reaction
                  if float(l["E"]) < float(parent["E"])
                  and abs(float(l["E"]) - target) <= 1.0]
    basis = "unique_reaction_level_within_1keV"
    if len(candidates) > 1 and any(m in ag["M"] for m in ["M1", "E2"]):
        parent_parity = "-" if "-" in parent["J"] else "+"
        candidates = [l for l in candidates if parent_parity in l["J"]]
        basis += "_after_same_parity_constraint_from_recorded_multipolarity"
    assert len(candidates) == 1, (parent["E"], rg["E"], [c["E"] for c in candidates])
    final = candidates[0]
    if final["E"] == "8.4":
        return adopted["8.42"], "unique_reaction_level_within_1keV;8.4_to_adopted_8.42"
    return adopted[final["E"]], basis


def ic_status(gamma):
    mixed = "M1+E2" in gamma["M"]
    if not gamma["CC"]:
        return "missing_CC;delta0.5_global_rule_if_calculated" if mixed else "missing_CC"
    if mixed and not gamma["MR"]:
        return "evaluated_CC_assumed_delta0.5_not_measured_delta"
    if gamma["M"] in {"E1", "E2"}:
        return "evaluated_CC_pure_multipole_no_mixing_delta"
    return "evaluated_CC_multipole_identity_requires_review"


def write_csv(name, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    write(name, stream.getvalue())


def main():
    assert OUT.resolve() == OUT
    OUT.mkdir(parents=True, exist_ok=True)
    content, sources = {}, {}
    for alias, (rel, expected) in INPUTS.items():
        data = (ROOT / rel).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        assert digest == expected, f"Input changed; review before rerun: {rel}"
        content[alias] = data
        sources[alias] = {"path": rel, "bytes": len(data), "sha256": digest}
    rlevels, runplaced = parse(content["R"].decode(), "R")
    alevels, aunplaced = parse(content["A"].decode(), "A")
    adopted = {l["E"]: l for l in alevels}
    chosen = [l for l in rlevels if l["band"] in BANDS and float(l["E"]) <= 3430.6]
    assert {l["E"] for l in chosen} == EXPECTED_LEVELS
    assert len(content["R"].splitlines()) == 555
    assert len(content["A"].splitlines()) == 934
    assert len(chosen) == 17

    level_rows, branch_rows, excerpts = [], [], []
    j_differences, m_differences, target_rows = [], [], []
    rescaling_residuals = []
    for rl in chosen:
        al = adopted[rl["E"]]
        assert rl["band"] == al["band"]
        assert rl["DE"] == al["DE"]
        assert (rl["T"], rl["DT"]) == (al["T"], al["DT"])
        assert len(rl["gammas"]) == len(al["gammas"])
        paper_band = None if rl["E"] == "182.04" else BANDS[rl["band"]]
        paper_role = "common_9/2_base_below_plotted_sequences" if paper_band is None else "plotted_band_member"
        if rl["J"] != al["J"]:
            j_differences.append({"energy_keV": rl["E"], "reaction": rl["J"],
                                  "adopted": al["J"], "locators": [rl["locator"], al["locator"]]})
        native_t = native_dt = mean_tau = mean_dtau = tau_ps = None
        unit, refs, method = "", "", "not_reported_in_checked_objects"
        if rl["T"]:
            value, unit = rl["T"].split()
            native_t, native_dt = number(value), uncertainty(value, rl["DT"])
            mean_tau, mean_dtau = native_t / math.log(2), native_dt / math.log(2)
            tau_ps = mean_tau * {"PS": 1, "NS": 1000}[unit]
            if unit == "PS":
                refs, method = "2000St07", "RDDS_DDCM;R:10-11,38-39;A:30"
            else:
                refs, method = "2013Ka27;1992By03", "evaluated_weighted_gamma_t;R:81-82;A:113-114"
        level_rows.append({
            "level_id": level_id(rl["E"]), "energy_keV_raw": rl["E"],
            "energy_uncertainty_keV": uncertainty(rl["E"], rl["DE"]),
            "Jpi_reaction_raw": rl["J"], "Jpi_adopted_raw": al["J"],
            "ENSDF_band": rl["band"], "Chakraborty2024_band": paper_band,
            "Chakraborty2024_role": paper_role,
            "T1_2_raw": rl["T"], "DT_raw": rl["DT"],
            "T1_2_value": native_t, "T1_2_uncertainty": native_dt, "time_unit": unit,
            "mean_tau_derived": mean_tau, "mean_tau_uncertainty_derived": mean_dtau,
            "mean_tau_ps_derived": tau_ps,
            "mean_tau_ps_uncertainty_derived": None if mean_dtau is None else mean_dtau * {"PS": 1, "NS": 1000}[unit],
            "lifetime_primary_keys": refs, "lifetime_method_and_locator": method,
            "reaction_locator": rl["locator"], "adopted_locator": al["locator"],
            "registered_outgoing_gamma_count": len(rl["gammas"]),
        })
        a_gammas = {g["E"]: g for g in al["gammas"]}
        assert set(a_gammas) == {g["E"] for g in rl["gammas"]}
        max_ri = max(number(g["RI"]) for g in rl["gammas"])
        sum_ri = sum(number(g["RI"]) for g in rl["gammas"])
        refg = max(rl["gammas"], key=lambda g: number(g["RI"]))
        for rg in rl["gammas"]:
            ag = a_gammas[rg["E"]]
            assert not rg["MR"] and not ag["MR"]
            assert not rg["TI"] and not ag["TI"]
            expected_ri = 100 * number(rg["RI"]) / max_ri
            residual = abs(number(ag["RI"]) - expected_ri)
            assert residual <= 0.5 * precision(ag["RI"]) + 1e-10
            rescaling_residuals.append(residual)
            if rg["M"] != ag["M"]:
                m_differences.append({"parent_keV": rl["E"], "gamma_keV": rg["E"],
                                      "reaction": rg["M"], "adopted": ag["M"],
                                      "locators": [rg["locator"], ag["locator"]]})
            final, final_basis = resolve_final(rl, rg, ag, rlevels, adopted)
            b_records = [row for row in ag["continuations"] if row["raw"][5] == "B"]
            same_parity_model = rl["E"] != "182.04"
            branch_rows.append({
                "parent_level_id": level_id(rl["E"]), "parent_energy_keV": rl["E"],
                "parent_Jpi_adopted": al["J"], "ENSDF_band": rl["band"],
                "Chakraborty2024_band": paper_band,
                "gamma_energy_keV_raw": rg["E"], "gamma_uncertainty_keV": uncertainty(rg["E"], rg["DE"]),
                "final_level_id": level_id(final["E"]), "final_energy_keV": final["E"],
                "final_Jpi_adopted": final["J"], "final_assignment_basis": final_basis,
                "energy_closure_residual_keV": round(float(rl["E"]) - float(final["E"]) - float(rg["E"]), 9),
                "RI_reaction_raw": rg["RI"], "DRI_reaction_raw": rg["DRI"],
                "RI_reaction_uncertainty": uncertainty(rg["RI"], rg["DRI"]),
                "RI_adopted_raw": ag["RI"], "DRI_adopted_raw": ag["DRI"],
                "RI_adopted_uncertainty": uncertainty(ag["RI"], ag["DRI"]),
                "photon_fraction_among_listed_branches_only": round(number(rg["RI"]) / sum_ri, 10),
                "photon_ratio_reference_gamma_keV": refg["E"],
                "photon_ratio_to_reference": round(number(rg["RI"]) / max_ri, 10),
                "derived_fraction_ratio_uncertainty": None,
                "multipolarity_reaction_raw": rg["M"], "multipolarity_adopted_raw": ag["M"],
                "MR_reaction_raw": rg["MR"], "MR_adopted_raw": ag["MR"],
                "CC_reaction_raw": rg["CC"], "DCC_reaction_raw": rg["DCC"],
                "CC_reaction_quoted_uncertainty": uncertainty(rg["CC"], rg["DCC"]),
                "CC_adopted_raw": ag["CC"], "DCC_adopted_raw": ag["DCC"],
                "CC_adopted_quoted_uncertainty": uncertainty(ag["CC"], ag["DCC"]),
                "IC_status_reaction": ic_status(rg), "IC_status_adopted": ic_status(ag),
                "RI_primary_key": "1992By03", "RI_measurement_publication_year": 1992,
                "evaluation_year": 2014, "reaction_locator": rg["locator"],
                "adopted_locator": ag["locator"],
                "evaluated_B_record_not_independent": " | ".join(r["raw"].strip() for r in b_records),
                "evaluated_B_locator": ";".join(r["locator"] for r in b_records),
                "EM_holdout_category": "conditional_photon_ratio" if same_parity_model and len(rl["gammas"]) > 1
                                      else "E1_isomer_outside_negative_parity_model" if not same_parity_model
                                      else "single_branch_no_nontrivial_photon_ratio",
            })
        for label, (parent, gamma) in TARGETS.items():
            if parent == rl["E"]:
                tg = next(g for g in branch_rows if g["parent_energy_keV"] == parent
                          and g["gamma_energy_keV_raw"] == gamma)
                assert not rl["T"] and not al["T"]
                crossover = {"365": "461.6", "521": "674.8", "671": "827.9"}[label]
                crossover_record = next(g for g in rl["gammas"] if g["E"] == crossover)
                target_rows.append({
                    "rounded_gamma_label_keV": label, "actual_gamma_energy_keV": gamma,
                    "parent_level_id": level_id(parent), "parent_energy_keV": parent,
                    "Jpi_reaction": rl["J"], "Jpi_adopted": al["J"],
                    "final_energy_keV": tg["final_energy_keV"],
                    "T1_2": None, "mean_tau": None, "absolute_B_readiness": "blocked_missing_parent_lifetime",
                    "RI_reaction": tg["RI_reaction_raw"],
                    "RI_reaction_uncertainty": tg["RI_reaction_uncertainty"],
                    "CC_adopted": number(tg["CC_adopted_raw"]),
                    "IC_status_adopted": tg["IC_status_adopted"],
                    "same_parent_crossover_gamma_keV": crossover,
                    "photon_RI_link_to_crossover_ratio": number(tg["RI_reaction_raw"]) / number(crossover_record["RI"]),
                    "photon_ratio_uncertainty": None,
                    "locators": [rl["locator"], al["locator"], tg["reaction_locator"], tg["adopted_locator"]],
                })
        for alias, level in [("R", rl), ("A", al)]:
            excerpts.append(f"\n{alias} parent {rl['E']} keV\n")
            records = [level] + level["continuations"]
            for g in level["gammas"]:
                records += [g] + g["continuations"]
            excerpts += [f"{row['locator']}\t{row['raw']}\n" for row in sorted(records, key=lambda r: r["line"])]

    assert len(branch_rows) == 33
    assert sum(bool(l["T1_2_raw"]) for l in level_rows) == 3
    assert [l["energy_keV_raw"] for l in level_rows if l["time_unit"] == "PS"] == ["797.4", "1475.4"]
    assert len(target_rows) == 3
    assert any(g["E"] == "365.0" for g in runplaced)

    pdf_text = subprocess.run(
        ["pdftotext", "-layout", str(ROOT / INPUTS["C"][0]), "-"],
        check=True, capture_output=True, text=True).stdout
    pages = [p for p in pdf_text.split("\f") if p.strip()]
    assert len(pages) == 5
    numbered_pdf = "".join(
        f"\nPDF page {i}; journal page 024324-{i}\n" +
        "".join(f"C:P{i}:L{j:03d} {line}\n" for j, line in enumerate(page.splitlines(), 1))
        for i, page in enumerate(pages, 1))
    write("chakraborty2024-extracted.txt", numbered_pdf)
    write("ensdf-selected-records.txt", "".join(excerpts))
    write_csv("levels.csv", level_rows)
    write_csv("branches.csv", branch_rows)

    # A worked example only: every alpha in this denominator is present in A.
    worked = [b for b in branch_rows if b["parent_energy_keV"] == "797.4"]
    assert all(b["CC_adopted_raw"] for b in worked)
    denominator = sum(number(b["RI_reaction_raw"]) * (1 + number(b["CC_adopted_raw"])) for b in worked)
    g518 = next(b for b in worked if b["gamma_energy_keV_raw"] == "518.6")
    worked_example = {
        "parent_keV": 797.4, "target_gamma_keV": 518.6,
        "status": "calculated_conditional_example_not_an_independent_measurement",
        "assumptions": ["only_listed_decay_channels", "ENSDF_assumed_delta0.5_for_153.8_keV_CC",
                        "pure_E2_518.6_keV_CC_from_adopted_object"],
        "sum_RI_times_1_plus_alpha": denominator,
        "photon_fraction_among_listed_photons": g518["photon_fraction_among_listed_branches_only"],
        "photon_probability_per_parent_decay": 100 / denominator,
        "total_gamma_plus_IC_branch_probability": 100 * (1 + number(g518["CC_adopted_raw"])) / denominator,
        "uncertainties": None,
    }
    # Check source stability again after extraction; do not rewrite any input.
    assert all(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest
               for rel, digest in INPUTS.values())
    manifest = {
        "schema": "ba129-em-holdout-readiness-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "local_source_audit;conditional_model_holdouts;primary_RDDS_audit_pending",
        "input_sources_read_and_hashed": sources,
        "locator_convention": "R/A/S: original 1-based file lines including leading blank; C:Pn:Lnnn: extracted PDF page lines",
        "evaluation": {"year": 2014, "version": "201408/14NDS", "cutoff": "2014-05-31",
                       "locators": ["R:2-4", "A:2-4"]},
        "scope": {"selection": "ENSDF bands A/B/C/D through the 27/2 states shown in Chakraborty2024 Fig.1",
                  "level_count": 17, "branch_count": 33, "ENSDF_to_paper_band": BANDS,
                  "band_mapping_exception": "182.04 keV 9/2- is ENSDF B but is the common base drawn below the four sequences; paper band 3 is plotted from 13/2; its paper band field is null",
                  "band_crosswalk_locator": "C:P2 Fig.1; visually inspected local crop",
                  "other_negative_parity_and_higher_spin_states": "outside_this_inventory",
                  "level_id": "task-local identifier based on adopted excitation energy; not an official ENSDF ID",
                  "all_registered_branches_included": True, "branch_completeness_experimentally_established": False},
        "source_lineage": [
            {"key": "1992By03", "year": 1992, "reference": "A. Byrne et al., Nucl. Phys. A 548, 131",
             "observables": "selected E_gamma and RI; single A2/DCO layer",
             "locators": ["R:5-7,19-26,33", "A:11-13", "C:P5 ref.[25]"]},
            {"key": "2000St07", "year": 2000, "reference": "O. Stuch et al., Phys. Rev. C 61, 044325",
             "observables": "797.4 and 1475.4 keV T1/2 as encoded by ENSDF; RDDS/DDCM",
             "primary_body_read_here": False, "locators": ["R:10-11,38-39", "A:30", "C:P5 ref.[30]"]},
            {"key": "2013Ka27", "year": 2013, "reference": "J. Kaur et al., Phys. Rev. C 87, 064312",
             "observables": "182 keV isomer gamma(t)/TDPAD; evaluated T1/2 also uses 1992By03",
             "locators": ["R:12-18,79-83", "A:108-114", "C:P5 ref.[31]"]},
            {"key": "1977Gi02;1978Gi04", "years": [1977, 1978],
             "reference": "J. Gizon et al., Nucl. Phys. A 277, 464 (1977); J. Gizon et al., Phys. Rev. C 17, 596 (1978)",
             "observables": "paired A2/A4; polarization respectively; not selected RI source",
             "locators": ["R:8-9,19-32", "C:P5 refs.[26-27]"]},
            {"key": "Chakraborty2024", "year": 2024,
             "reference": "S. Chakraborty et al., Phys. Rev. C 110, 024324",
             "observables": "reanalysis/band interpretation; no new T1/2 or RI measurements supplied",
             "locators": ["C:P2 Fig.1 and text", "C:P3", "C:P4"]},
        ],
        "parent_task_context_not_read_or_verified_here": {
            "path": "raw/papers/gpt/query/20261105-ba129-model-readiness/gizon1977-main.pdf",
            "parent_reported_sha256": "017e979cea49b19daecc5394a5ca90e460ad0cb2c1a60edaf510e3b7dc446795",
            "parent_report": "p466 Table1: 365 coefficient errors (.05,.05); 461.8 errors (.04,.06); both A4 positive; 55-degree single-spectrum intensity is not integrated branching",
            "use": "context only; not used to replace ENSDF coefficients or RI; no primary PDF read by this subtask",
        },
        "field_contract": {
            "csv_empty_cell_and_json_null": "not reported/not computed; never zero",
            "T_field": "T1/2, not mean lifetime; native ENSDF PS/NS units retained",
            "tau": "mean_tau = T1/2 / ln(2); uncertainty divided by ln(2); ps conversion explicit",
            "RI": "relative photon intensity, not absolute decay probability or reduced B(XL)",
            "ratio_errors": "not computed: common normalization, efficiency and fit covariance unavailable",
            "CC": "total internal-conversion coefficient alpha; blank does not mean zero; quoted DCC not an independently measured delta",
            "multipole_mixing": "f_E2 = delta^2/(1+delta^2) within one mixed radiative transition, not a parent branching fraction",
            "rate_denominator": "D=sum_j RI_j*(1+alpha_j), only if all relevant channels are accounted for",
            "total_branch": "b_i=RI_i*(1+alpha_i)/D",
            "photon_probability": "p_gamma_i=RI_i/D",
            "photon_rate": "lambda_gamma_i=p_gamma_i/mean_tau; M1/E2 split then uses 1/(1+delta^2),delta^2/(1+delta^2)",
        },
        "targets_365_521_671": target_rows,
        "reaction_adopted_Jpi_differences": j_differences,
        "reaction_adopted_multipolarity_differences": m_differences,
        "conditional_probability_example": worked_example,
        "holdout_rules": [
            "Freeze energy-fit Hamiltonian, state/band mapping and independently chosen EM operators before looking at validation outcomes.",
            "Two PS lifetimes can validate total decay rates conditionally on complete modeled EM channels; no other PS lifetimes supplied here.",
            "Use within-parent photon RI ratios as empirical EM holdouts, with multipolarity/efficiency/covariance boundaries retained.",
            "182.04-keV isomer is E1 to 7/2+; only usable when the model contains that positive-parity state and an E1 operator.",
            "No absolute B for 365/521/671 without their own parent lifetimes; do not borrow 797.4/1475.4 lifetimes.",
            "Evaluated BE2W/BE1W, T1/2 and branch-derived rates are dependent representations, not extra independent observations.",
            "Reaction/adopted RI are the same 1992 lineage with normalization changes; 2024 reanalysis is not a new experiment.",
            "Do not treat model-selected delta, assumed delta0.5 CC, or 1977 55-degree singles intensities as independent integrated-branch data.",
        ],
        "checks": {
            "four_input_hashes_match_and_unchanged_after_extraction": True,
            "ENSDF_line_counts": {"R": 555, "A": 934},
            "17_levels_and_33_gammas_crossmatched": True,
            "photon_ratio_algebraic_degrees_of_freedom_not_independent_observation_count": 16,
            "adopted_mixed_CC_assuming_delta0p5_count": 10,
            "adopted_missing_CC_count": 18,
            "all_selected_MR_and_TI_fields_blank_in_both_objects": True,
            "all_adopted_RI_are_max100_rescalings_within_last_digit_rounding": True,
            "max_adopted_RI_rescaling_absolute_rounding_residual": max(rescaling_residuals),
            "three_lifetimes_agree_between_objects": True,
            "three_target_parent_T_fields_blank_in_both_objects": True,
            "final_levels_explicit_FL_or_energy_match_within_1keV_plus_recorded_multipolarity_if_needed": True,
            "unplaced_365.0_keV_R63_excluded": True,
            "PDF_text_pages_checked": 5,
            "outside_output_writes_by_script": False,
            "network_or_get_paper_or_git_mutations_or_subagents": False,
        },
        "outputs": ["levels.csv", "branches.csv", "holdout_manifest.json", "audit.md",
                    "ensdf-selected-records.txt", "chakraborty2024-extracted.txt",
                    "chakraborty2024-fig1.png", "extract_holdout.py"],
    }
    write("holdout_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "levels": len(level_rows), "branches": len(branch_rows),
        "lifetime_levels_keV": [l["energy_keV_raw"] for l in level_rows if l["T1_2_raw"]],
        "Jpi_differences": len(j_differences), "multipolarity_differences": m_differences,
        "conditional_probability_example": worked_example,
        "input_hashes_unchanged": True, "output_dir": str(OUT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
