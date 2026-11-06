#!/usr/bin/env python3
"""Extract the frozen five-isotope evaluation and retain method alternatives.

No fit, averaging of published alternatives, or confidence interval is performed.
"""
import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import re

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
OLD = ROOT / "raw/papers/gpt/query/20261105-ba129-core-constraints"
RAW = ROOT / "raw/papers/gpt/query/20261106-ba-core-E2-calibration"
RATE = 1.2239e13
MASSES = (128, 130, 132, 134, 136)
PDF_GAMMA_PAGES = {128: 5, 130: 3, 132: 6, 134: 5, 136: 7}
COULOMB_IDS = {130: "130056007", 132: "132056010",
               134: "134056008", 136: "136056012"}
B_UP = {130: ("1.163", "11"), 132: ("0.86", "6"),
        134: ("0.679", "11"), 136: ("0.407", "7")}
SOURCE_KEYS = {
    128: ["2000Pe20", "2000Pe19", "1998Pe17"],
    130: ["1989Bu07"],
    132: ["1985Bu01", "2001Ra27"],
    134: ["1972Ke16", "1977Kl05", "1989Bu07"],
    136: ["1984Be20", "1986Ro15", "1972Ke16"],
}
SOURCE_KEY_NOTES = {
    128: "General adopted lifetime comment names RDDS 2000Pe20/2000Pe19 and DSA 1998Pe17; it does not give a row-specific weighting decomposition.",
    130: "Adopted/Coulomb value is the evaluation's average of two 1989Bu07 interference solutions.",
    132: "1985Bu01 two-sign alternatives; 2001Ra27 recommendation adopted by this ENSDF evaluation.",
    134: "Evaluation's stated weighted average retained literally; not re-estimated from the listed measurements.",
    136: "Evaluation's stated weighted average retained literally; other methods and interference branches retained separately.",
}
T_DEPENDENCY = {
    128: "Selected half-life is the input; Bdown and the source BE2W are not extra observations.",
    130: "Adopted T=41.8(12) ps combines RDDS 43.2(5) ps and 40.7(4) ps derived from the selected Coulomb Bup. Do not count T and Bup as independent.",
    132: "Adopted half-life is derived from Coulomb B(E2); it is not an independent lifetime constraint.",
    134: "Specific first-2+ comment overrides general (n,n'gamma) lifetime provenance: this T is derived from Coulomb B(E2).",
    136: "Specific first-2+ comment overrides general DSAM provenance: evaluator derives this T from B(E2) and adopted gamma properties.",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


def number(value, digits="", unit=None):
    value, digits = value.strip(), digits.strip()
    margin = float(Decimal(digits) * Decimal(10) ** Decimal(value).as_tuple().exponent) if digits else None
    return {"value": float(value), "value_literal": value,
            "uncertainty_digits_literal": digits or None,
            "quoted_margin": margin, "unit": unit,
            "confidence_level": None, "error_distribution": None}


def b_from_half(t_ps, eg_kev, alpha):
    if alpha is None:
        raise ValueError("Missing ICC cannot be replaced with zero")
    return math.log(2) / (RATE * t_ps * 1e-12 * (eg_kev / 1000) ** 5 * (1 + alpha))


def write_csv(path, records):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def parse_state(a):
    folder = OLD if a in (128, 130) else RAW
    path = folder / f"nndc{a}-adopted-text.ens"
    lines = path.read_text().splitlines()
    levels = [(i, line) for i, line in enumerate(lines)
              if line[5:9] == "  L "]
    candidates = [(i, line) for i, line in levels if line[21:39].strip() == "2+"]
    start, level = min(candidates, key=lambda item: float(item[1][9:19]))
    end = next((i for i, _ in levels if i > start), len(lines))
    block = lines[start:end]
    gammas = [(i + start, line) for i, line in enumerate(block)
              if line[5:9] == "  G "]
    assert len(gammas) == 1, (a, "single listed gamma branch required")
    gi, gamma = gammas[0]
    assert gamma[31:41].strip() == "E2"
    assert float(gamma[21:29]) == 100
    lower = [line for _, line in levels if float(line[9:19]) < float(level[9:19])]
    assert len(lower) == 1 and lower[0][21:39].strip() == "0+"
    assert float(lower[0][9:19]) == 0
    t, t_unit = level[39:49].split()
    assert t_unit == "PS"
    energy = number(level[9:19], level[19:21], "keV")
    eg = number(gamma[9:19], gamma[19:21], "keV")
    half = number(t, level[49:55], "ps")
    alpha = number(gamma[55:62], gamma[62:64], "dimensionless")
    assert alpha["value"] > 0 and alpha["quoted_margin"] is None
    header = "\n".join(lines[:5])
    cutoff = re.search(r"CUT=([^$]+)", header).group(1).strip()
    citation = re.search(r"CIT=([^$]+)", header).group(1).strip()
    author = re.search(r"AUT=([^$]+)", header).group(1).strip()
    stamp = re.search(r"(\d{6})\s*$", lines[1]).group(1)
    wu = next((re.search(r"BE2W=([0-9.]+)\s+(\d+)", s)
               for s in block if "BE2W=" in s), None)
    photon_fraction = 1 / (1 + alpha["value"])
    result = {
        "nucleus": f"{a}Ba", "A": a, "Z": 56, "N": a - 56,
        "state_label": "2_1+", "initial_spin": 2, "final_spin": 0,
        "initial_parity": "+", "final_parity": "+",
        "level_energy": energy, "gamma_energy": eg,
        "half_life": half, "half_life_dependency": T_DEPENDENCY[a],
        "gamma": {
            "multipolarity": "E2", "relative_photon_intensity_literal": gamma[21:29].strip(),
            "relative_intensity_error_literal": gamma[29:31].strip() or None,
            "listed_outgoing_gamma_count": len(gammas),
            "listed_total_transition_branch_fraction": 1.0,
            "branch_basis": "First excited state; only listed decay is pure E2 to 0+ ground state. No uncertainty on branch completeness inferred.",
            "alpha_total": alpha, "photon_fraction_for_total_decay": photon_fraction,
            "icc_margin_not_reported": True,
        },
        "source_wu": {"value": float(wu.group(1)), "literal": wu.group(0),
                      "quoted_margin": number(wu.group(1), wu.group(2))["quoted_margin"],
                      "direction": "2+ -> 0+", "unit": "W.u.",
                      "selected_as_separate_datum": False,
                      "dependency": "Same level decay summary; no independent W.u. observation counted."} if wu else None,
        "source": {
            "adopted_dataset_id": f"{a}056001", "adopted_path": rel(path),
            "adopted_sha256": sha(path), "level_line": start + 1,
            "gamma_line": gi + 1, "block_last_line": end,
            "literal_level_record": level, "literal_gamma_record": gamma,
            "first_2plus_block": [{"line": start + i + 1, "text": s}
                                 for i, s in enumerate(block)],
            "adopted_pdf": rel(folder / f"nndc{a}-adopted.pdf"),
            "level_pdf_page": 1, "gamma_pdf_page": PDF_GAMMA_PAGES[a],
            "record_stamp": stamp, "literature_cutoff": cutoff,
            "evaluation_citation": citation, "evaluators": author,
            "underlying_source_keys": SOURCE_KEYS[a],
            "source_key_scope": SOURCE_KEY_NOTES[a],
            "all_source_quantities_are_evaluated_summaries": True,
        },
        "calibration_block_id": f"{a}Ba-first2-E2",
        "include_selected_strength_once": True,
        "joint_covariance_with_other_isotopes": None,
        "confidence_interval": None,
    }
    if a == 128:
        value = b_from_half(half["value"], eg["value"], alpha["value"])
        margin_t = value * half["quoted_margin"] / half["value"]
        margin_e = 5 * value * eg["quoted_margin"] / eg["value"]
        result["selected_strength"] = {
            "input_quantity": "T1/2", "input_literal": f'{t} {level[49:55].strip()} ps',
            "B_down_e2b2": value, "B_up_e2b2": 5 * value,
            "B_down_margin_e2b2": margin_t,
            "margin_kind": "First-order propagation of quoted T margin only, holding Egamma, ICC and rate constant fixed",
            "gamma_energy_margin_contribution_e2b2": margin_e,
            "complete_strength_uncertainty": None,
            "conversion": "ln(2)/(T_seconds*C_E2*Egamma_MeV^5*(1+alpha_total)); Bup=5*Bdown",
            "why_not_wu_as_input": "The adopted decay table gives a rounded 72(7) W.u., not a direct absolute Bup. Retain it but use the explicitly requested T/Egamma/ICC formula.",
        }
    else:
        value_literal, digits = B_UP[a]
        folder = OLD if a == 130 else RAW
        cp = folder / f"nndc{a}-coulomb-text.ens"
        clines = cp.read_text().splitlines()
        matches = [(n, s) for n, s in enumerate(clines, 1)
                   if re.search(rf"BE2={re.escape(value_literal)}\s+{digits}(?:\s|[$])", s)]
        assert len(matches) == 1
        n, literal = matches[0]
        direct = number(value_literal, digits, "e^2 b^2")
        result["selected_strength"] = {
            "input_quantity": "B(E2;0+ -> 2+) from Coulomb-excitation evaluation",
            "input_literal": f"{value_literal} {digits}",
            "B_up_e2b2": direct["value"], "B_up_quoted_margin_e2b2": direct["quoted_margin"],
            "B_down_e2b2": direct["value"] / 5,
            "B_down_margin_e2b2": direct["quoted_margin"] / 5,
            "margin_kind": "Source quoted Bup margin divided by 5; no confidence-level reinterpretation",
            "conversion": "Bdown=Bup/(2*Ji+1)=Bup/5 for Ji=2 -> Jf=0",
        }
        cstart = max(i for i, s in enumerate(clines[:n])
                     if s[5:9] == "  L ")
        cend = next((i for i, s in enumerate(clines)
                     if i > cstart and s[5:9] == "  L "), len(clines))
        result["source"].update(
            coulomb_dataset_id=COULOMB_IDS[a], coulomb_path=rel(cp),
            coulomb_sha256=sha(cp), coulomb_Bup_line=n,
            coulomb_literal_Bup_record=literal,
            coulomb_first2_block=[{"line": i + 1, "text": clines[i]}
                                  for i in range(cstart, cend)],
            direction_verified_by_pdf=(
                rel(RAW / "nndc134-coulomb.pdf") + " p.1: B(E2) upward arrow"
                if a == 134 else result["source"]["adopted_pdf"] + " p.1: B(E2) upward arrow"
            ),
        )
    return result


def alternatives():
    """Literal method-summary alternatives, explicitly excluded from baseline."""
    data = []

    def add(a, value, digits, key, role, lines, condition="", quantity="Bup"):
        item = number(value, digits, "e^2 b^2" if quantity == "Bup" else "ps")
        base = OLD if a == 130 else RAW
        name = "adopted" if a == 130 and quantity == "T1/2" and key == "2000St07" else "coulomb"
        p = base / f"nndc{a}-{name}-text.ens"
        raw_lines = p.read_text().splitlines()
        lo, hi = lines
        excerpt = [{"line": i, "text": raw_lines[i - 1]} for i in range(lo, hi + 1)]
        assert value in "\n".join(x["text"] for x in excerpt)
        data.append({
            "alternative_id": f"{a}Ba-alt-{sum(x['A']==a for x in data)+1:02}",
            "A": a, "quantity": quantity,
            "value": item["value"], "quoted_margin": item["quoted_margin"],
            "value_literal": value, "uncertainty_digits_literal": digits,
            "unit": item["unit"], "source_keys": key.split(";"),
            "role": role, "condition": condition,
            "source_path": rel(p), "source_lines": list(range(lo, hi + 1)),
            "source_excerpt": excerpt,
            "B_down_e2b2": item["value"] / 5 if quantity == "Bup" else None,
            "B_down_margin_e2b2": item["quoted_margin"] / 5 if quantity == "Bup" else None,
            "conversion": "Bup/5" if quantity == "Bup" else "kept as half-life alternative; not selected or added as another B observation",
            "include_in_selected_calibration": False, "confidence_interval": None,
            "same_publication_branches_not_independent": True,
        })

    add(130, "1.167", "11", "1989Bu07", "interference branch", (20, 21), "constructive")
    add(130, "1.159", "12", "1989Bu07", "interference branch", (20, 21), "destructive")
    add(130, "1.21", "38", "1973ToXW", "historical method value", (21, 22), "destructive")
    add(130, "1.36", "14", "1967Si03", "historical method value", (22, 22))
    add(130, "0.75", "18", "1958Fa01", "historical method value", (22, 22))
    add(130, "43.2", "5", "2000St07", "RDDS component of adopted lifetime", (55, 56),
        "Summary-only provenance; no Stuch retrieval in this task", "T1/2")
    add(130, "40.7", "4", "1989Bu07", "lifetime derived from selected Coulomb Bup", (17, 27),
        "Dependent on selected Bup; not an independent measurement", "T1/2")
    add(132, "0.821", "16", "1985Bu01", "matrix-element-sign branch", (15, 17),
        "product of four matrix elements negative")
    add(132, "0.897", "16", "1985Bu01", "matrix-element-sign branch", (15, 17),
        "product of four matrix elements positive")
    add(132, "0.73", "18", "1958Fa01", "historical method value", (17, 17))
    add(134, "0.672", "16", "1972Ke16", "listed component of adopted average", (17, 19))
    add(134, "0.700", "15", "1977Kl05", "listed component of adopted average", (17, 19))
    add(134, "0.665", "5", "1989Bu07", "listed component of adopted average", (17, 19))
    add(136, "0.399", "3", "1984Be20", "listed component of adopted average", (50, 54),
        "outside-parentheses convention: constructive")
    add(136, "0.419", "4", "1986Ro15", "listed component of adopted average", (50, 54),
        "constructive")
    add(136, "0.418", "11", "1972Ke16", "listed component and constructive branch", (50, 54),
        "Repeated in source's Others list; count once")
    add(136, "0.46", "4", "2002Ra21", "other Coulomb-excitation method value", (51, 54),
        "Inverse-kinematics method, source description lines30–34")
    add(136, "0.417", "4", "1986BaZJ;1986Ro15", "interference branch", (52, 54),
        "destructive; same study lineage as 0.419(4)")
    add(136, "0.388", "10", "1985Bu01", "interference branch", (52, 54),
        "constructive; taking Q=-0.19(17) as source specifies")
    add(136, "0.400", "10", "1985Bu01", "interference branch", (52, 54),
        "destructive; taking Q=-0.19(17) as source specifies")
    add(136, "0.417", "12", "1972Ke16", "interference branch", (53, 54), "destructive")
    add(136, "0.53", "16", "1963Al31", "historical method value", (54, 54))
    add(136, "2.2", "3", "1973Fi15", "other lifetime method", (48, 49),
        "DSAM: source method description lines9–10; not the adopted B-derived lifetime", "T1/2")
    return data


def main():
    manifests = [json.loads((folder / "manifest.json").read_text())
                 for folder in (OLD, RAW)]
    records = {item["path"]: item for m in manifests for item in m["files"]}
    used = []
    for a in MASSES:
        folder = OLD if a in (128, 130) else RAW
        roles = ["adopted"] + (["coulomb"] if a != 128 else [])
        for role in roles:
            wire = folder / f"nndc{a}-{role}.response.html"
            text = folder / f"nndc{a}-{role}-text.ens"
            pres = BeautifulSoup(wire.read_bytes(), "html.parser").find_all("pre")
            assert len(pres) == 1
            assert pres[0].get_text().encode("utf-8") == text.read_bytes()
            for p in (wire, text):
                assert sha(p) == records[rel(p)]["sha256"], rel(p)
                used.append({"path": rel(p), "sha256": sha(p),
                             "size": p.stat().st_size, "reused": folder == OLD})
        p = folder / f"nndc{a}-adopted.pdf"
        assert p.read_bytes().startswith(b"%PDF")
        assert sha(p) == records[rel(p)]["sha256"]
        used.append({"path": rel(p), "sha256": sha(p),
                     "size": p.stat().st_size, "reused": folder == OLD})
    p = RAW / "nndc134-coulomb.pdf"
    assert sha(p) == records[rel(p)]["sha256"]
    used.append({"path": rel(p), "sha256": sha(p), "size": p.stat().st_size, "reused": False})
    rows = [parse_state(a) for a in MASSES]
    alt = alternatives()
    assert math.isclose(rows[0]["selected_strength"]["B_down_e2b2"], 0.27652516113300324, rel_tol=1e-12)
    assert [round(r["selected_strength"]["B_down_e2b2"], 4) for r in rows[1:]] == [0.2326, 0.172, 0.1358, 0.0814]
    result = {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "task_label": "20261106-ba-core-E2-calibration",
        "kind": "evaluation-based calibration inputs with explicitly derived directions",
        "selection_policy": "One first-2+ E2 strength per even Ba isotope. Prefer explicit absolute Coulomb Bup; 128Ba uses the requested half-life/rate conversion.",
        "rate_contract": {
            "C_E2": RATE, "provenance": "Parent/task-declared rate coefficient",
            "rate_equation": "lambda_gamma[E2,s^-1]=C_E2*Egamma[MeV]^5*Bdown[e^2 b^2]",
            "single_branch_equation": "Bdown=ln(2)/(T1/2[s]*(1+alpha_total)*C_E2*Egamma[MeV]^5)",
            "general_photon_branch_equation": "b_gamma_j=I_gamma_j/sum_k(I_gamma_k*(1+alpha_k)); Bdown_j=ln(2)*b_gamma_j/(T1/2*C_E2*Egamma_j^5) for a pure E2 branch",
            "direction_identity": "Bup(0->2)=5*Bdown(2->0)",
            "missing_ICC_policy": "null and stop required for rate derivation; never replace with zero",
        },
        "error_contract": {
            "source_quoted_margins_not_confidence_intervals": True,
            "unreported_ICC_uncertainties_remain_null": True,
            "128_B_margin_is_T_only_linearized_not_complete": True,
            "cross_isotope_covariance": None,
            "same_measurement_derivatives_not_independent": True,
        },
        "selected_rows": rows, "alternatives": alt,
        "shared_selected_source_keys": {
            "1989Bu07": [130, 134], "1972Ke16": [134, 136],
            "interpretation": "Shared source identifiers are dependence warnings; neither correlation values nor event overlap are inferred.",
        },
        "inputs": used,
        "analysis_script": rel(Path(__file__).resolve()),
        "analysis_script_sha256": sha(Path(__file__).resolve()),
        "no_primary_paper_download_needed": True,
        "new_measurement": False, "model_fit_performed": False,
        "row_count_is_not_a_claim_of_statistical_independence": True,
    }
    (OUT / "ba-core-E2.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    flat = []
    for row in rows:
        s, src = row["selected_strength"], row["source"]
        flat.append({
            "nucleus": row["nucleus"], "state": row["state_label"],
            "Ex_keV": row["level_energy"]["value"],
            "Ex_literal": row["level_energy"]["value_literal"],
            "Ex_error_digits": row["level_energy"]["uncertainty_digits_literal"],
            "Ex_margin_keV": row["level_energy"]["quoted_margin"],
            "Egamma_keV": row["gamma_energy"]["value"],
            "Egamma_literal": row["gamma_energy"]["value_literal"],
            "Egamma_error_digits": row["gamma_energy"]["uncertainty_digits_literal"],
            "Egamma_margin_keV": row["gamma_energy"]["quoted_margin"],
            "T_half_ps": row["half_life"]["value"],
            "T_half_literal": row["half_life"]["value_literal"],
            "T_half_error_digits": row["half_life"]["uncertainty_digits_literal"],
            "T_half_margin_ps": row["half_life"]["quoted_margin"],
            "alpha_total": row["gamma"]["alpha_total"]["value"],
            "alpha_literal": row["gamma"]["alpha_total"]["value_literal"],
            "alpha_error": None,
            "selected_input": s["input_quantity"], "selected_input_literal": s["input_literal"],
            "B_up_e2b2": s["B_up_e2b2"],
            "B_down_e2b2": s["B_down_e2b2"],
            "B_down_margin_e2b2": s["B_down_margin_e2b2"],
            "margin_kind": s["margin_kind"],
            "direction": "2_1+ -> 0_1+",
            "source_dataset_id": src["adopted_dataset_id"],
            "record_stamp": src["record_stamp"],
            "literature_cutoff": src["literature_cutoff"],
            "adopted_path": src["adopted_path"],
            "level_line": src["level_line"], "gamma_line": src["gamma_line"],
            "source_keys": ";".join(src["underlying_source_keys"]),
            "calibration_block_id": row["calibration_block_id"],
            "confidence_interval": None,
        })
    write_csv(OUT / "ba-core-E2.csv", flat)
    write_csv(OUT / "alternatives.csv", [
        {k: ";".join(map(str, v)) if isinstance(v, list) else v
         for k, v in item.items() if k not in ("source_excerpt",)}
        for item in alt
    ])
    print(json.dumps({"selected": [{"nucleus": r["nucleus"], **r["selected_strength"]} for r in rows],
                      "alternative_count": len(alt), "input_count": len(used)}, indent=2))


if __name__ == "__main__":
    main()
