#!/usr/bin/env python3
"""Source/unit audit only: no model import, state selection, solve, or fit.

Convert the reported downward E2 strength using the declared ordinary Weisskopf
unit. Lifetime and ICC are deliberately NOT arguments to the conversion.
All outputs are new files beside this script; existing files are not overwritten.
"""

from datetime import datetime, timezone
from fractions import Fraction
import csv
import hashlib
import json
import math
from pathlib import Path

from bs4 import BeautifulSoup
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
HELP = ROOT / "raw/papers/gpt/query/20261106-ba137-isomer-validation"
VOGT = ROOT / "raw/papers/gpt/query/20261106-vogt2017-ba137-rstat"
BOOK = ROOT / "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ordinary_e2_down_unit(A, radius_coefficient_fm=1.2):
    """One ordinary E2 Weisskopf unit, returned in e^2 b^2."""
    radius_fm = radius_coefficient_fm * A**(1/3)
    reference_e2fm4 = (1/(4*math.pi))*(3/5)**2*radius_fm**4
    return reference_e2fm4 / 1e4


def convert_reported_downward_strength(A, strength_Wu, quoted_margin_Wu):
    unit = ordinary_e2_down_unit(A)
    return strength_Wu*unit, quoted_margin_Wu*unit


def main():
    for name in ("unit-audit.json", "observed-strength.csv"):
        if (OUT/name).exists():
            raise FileExistsError(OUT/name)
    paths = [HELP/"manifest.json", HELP/"nndc-be2-help.html", HELP/"nndc-gamma-help.html",
             VOGT/"manifest.json", VOGT/"vogt2017-accepted.pdf", BOOK]
    before = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    manifest = json.loads((HELP/"manifest.json").read_text())
    for item in manifest["files"]:
        p = ROOT/item["path"]
        assert p.stat().st_size == item["size"] and sha(p) == item["sha256"]

    be2_html = (HELP/"nndc-be2-help.html").read_text()
    gamma_html = (HELP/"nndc-gamma-help.html").read_text()
    be2_text = " ".join(BeautifulSoup(be2_html, "html.parser").stripped_strings)
    gamma_text = " ".join(BeautifulSoup(gamma_html, "html.parser").stripped_strings)
    assert "0⁺ → 2⁺" in be2_text
    assert "B<sub>w</sub>(E2&darr;) = 0.297" in be2_html
    assert "B(M<sub>&lambda;</sub>,E<sub>&lambda;</sub>)=T<sub>&gamma;</sub>/T<sub>W</sub>" in gamma_html
    assert "partial half-life" in gamma_text

    with pymupdf.open(BOOK) as book:
        rate_page = book[400].get_text()
        assert all(s in rate_page for s in ["(3C-16)", "(3C-17)", "(3C-18)", "decay rate"])
        assert "per second" in rate_page
    with pymupdf.open(VOGT/"vogt2017-accepted.pdf") as paper:
        table = paper[13].get_text()
        assert all(s in table for s in ["137Ba", "2349.9", "589(20)", "0.46(3)"])
        assert "corrected for internal conversion" in table
        timing = paper[8].get_text()
        assert "2349.9-keV excited state" in timing and "589(20)" in timing

    coefficient = (1/(4*math.pi))*(3/5)**2*1.2**4
    assert math.isclose(5*coefficient, .297, rel_tol=1e-4)
    # SI area conversion, independently of the /1e4 in the unit function.
    one_barn_in_fm2 = 1e-28 / (1e-15)**2
    assert math.isclose(one_barn_in_fm2, 100., rel_tol=1e-15)
    assert math.isclose(one_barn_in_fm2**2, 1e4, rel_tol=1e-15)
    unit = ordinary_e2_down_unit(137)
    assert math.isclose(unit, coefficient*137**(4/3)/one_barn_in_fm2**2, rel_tol=2e-15)
    value, quoted_margin = convert_reported_downward_strength(137, .46, .03)
    assert math.isclose(value/unit, .46, rel_tol=1e-15)
    assert math.isclose(quoted_margin/unit, .03, rel_tol=1e-15)

    # Hermitian E2 RMEs have equal squared magnitudes on reversing a transition.
    arbitrary_rme_squared = Fraction(1731, 1000)
    down = arbitrary_rme_squared/20
    up = arbitrary_rme_squared/16
    assert up/down == Fraction(20, 16)
    assert (arbitrary_rme_squared/1)/(arbitrary_rme_squared/5) == 5
    # If BOTH physical B and its special 0->2 reference are multiplied by five,
    # their dimensionless ratio is unchanged. This is not the present transition.
    assert math.isclose((5*value)/(5*unit), value/unit, rel_tol=1e-15)

    # Matched radiative half-lives at fixed energy/multipolarity, alpha=0.
    # No actual 137Ba lifetime or ICC is used in these algebraic controls.
    lifetime_controls = []
    lambda_W = 3.7
    T_W = math.log(2)/lambda_W
    for strength_ratio in (.1, .5, 2., 10.):
        T_gamma = math.log(2)/(strength_ratio*lambda_W)
        correct = T_W/T_gamma
        printed = T_gamma/T_W
        assert math.isclose(correct, strength_ratio, rel_tol=1e-15)
        assert math.isclose(printed, 1/strength_ratio, rel_tol=1e-15)
        lifetime_controls.append({"B_over_BW": strength_ratio,
                                  "T_W_over_T_gamma": correct,
                                  "printed_inverse_T_gamma_over_T_W": printed})

    observation = {
        "nucleus": "137Ba", "A": 137, "Z": 56,
        "initial_two_J": 19, "final_two_J": 15,
        "spin_parity_labels": "(19/2-)_1 -> (15/2-)_1; parentheses retained from the level scheme",
        "direction": "downward, 2349.9-keV parent -> 2229.8-keV daughter",
        "B_E2_down_Wu": .46, "quoted_margin_Wu": .03,
        "one_ordinary_down_Wu_e2fm4": unit*1e4,
        "one_ordinary_down_Wu_e2b2": unit,
        "B_E2_down_e2b2": value, "quoted_margin_e2b2": quoted_margin,
        "B_definition": "abs(<15/2||T(E2)||19/2>)**2 / 20",
        "T_half_parent_ns": 589., "T_half_quoted_margin_ns": 20.,
        "T_half_parent_us": .589,
        "T_is_metadata_not_conversion_input": True,
        "source_B_already_ICC_corrected": True,
        "numeric_alpha_reported_by_paper": None,
        "alpha_assumed_or_B_rederived_from_T": False,
        "evidence_group": "Vogt2017-Ba137-2349p9-to-2229p8-E2",
        "T_and_B_are_independent_observations": False,
        "confidence_level_of_quoted_margin": None,
        "margin_conversion": "Only the reported 0.03 W.u. margin multiplied by the fixed unit; no new uncertainty estimate",
        "is_15over2_to_11over2_Rstat_first_denominator": False,
        "source_locator": "Vogt2017 accepted manuscript Table III, PDF p.14/printed p.13; timing Sec.III B/Fig.7, PDF p.9/printed p.8",
    }
    after = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    assert before == after
    result = {
        "schema": "Ba137-isomer-source-unit-audit-v1",
        "actual_checked_at": datetime.now(timezone.utc).isoformat(),
        "observation": observation,
        "ordinary_reference": {
            "formula": "BW_down(E2)=(1/(4*pi))*(3/5)^2*(1.2*A^(1/3))^4 e^2 fm^4",
            "radius_coefficient_fm": 1.2,
            "coefficient_e2fm4": coefficient,
            "one_barn_in_fm2": one_barn_in_fm2,
            "one_barn_squared_in_fm4": one_barn_in_fm2**2,
        },
        "direction_conventions": {
            "isomer_reverse_Bup_over_Bdown": 20/16,
            "isomer_reverse": "B(15/2->19/2)=(20/16) B(19/2->15/2), both in the same ordinary units",
            "special_0_to_2_reference": "5 times the ordinary downward reference; coefficient approximately 0.297",
            "special_reference_is_used_for_this_isomer": False,
            "avoid_extra_spin_factor": "Compare an already normalized downward B directly to the converted datum; do not divide by 20 again.",
        },
        "localized_documentation_findings": [
            {"source": str((HELP/"nndc-be2-help.html").relative_to(ROOT)),
             "lines": [60, 70],
             "finding": "General downward formula is explicit. The following prose specifies 0+->2+ but its 0.297 expression is labelled with a downward arrow.",
             "assessment": "0.297 is the rounded fivefold 0->2 reference; its downward-arrow label conflicts with the surrounding context, not an error in the fivefold coefficient."},
            {"source": str((HELP/"nndc-gamma-help.html").relative_to(ROOT)),
             "lines": [178, 192],
             "finding": "The page names T_gamma a partial half-life, then prints dimensionless B as T_gamma/T_W.",
             "assessment": "At fixed energy/multipolarity with matched radiative times, B/BW=T_W/T_gamma. The printed reciprocal is a hindrance ratio; the alpha=0 single-branch limit already exposes the reversal.",
             "scope": "Specific archived help expression; no assertion that ENSDF datasets or NNDC as a whole are invalid."},
        ],
        "independent_textbook_locator": {
            "path": str(BOOK.relative_to(ROOT)),
            "edition": "Bohr and Mottelson, Nuclear Structure I, first edition 1969; local World Scientific 1998 edition",
            "printed_page": 382, "PDF_page": 401,
            "equations": ["3C-16", "3C-17", "3C-18"],
            "basis": "Radiative rate proportional to E^(2L+1) B; the book's T(E2) is a rate per second, not a half-life.",
            "inspection": "Local PDF text; no textbook page reproduction written.",
        },
        "lifetime_ratio_controls": lifetime_controls,
        "parent_model_protocol_boundary": "Parent fixes primary ordinal 0/0 and an energy-only alternative before B; this sidecar neither selects states nor calculates any model strength.",
        "input_sha256": before, "inputs_unchanged": True,
        "new_model_calculation_or_refit": False,
        "reported_B_converted_using_only_A_and_Wu": True,
    }
    with (OUT/"unit-audit.json").open("x") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    columns = ["nucleus", "initial_two_J", "final_two_J", "direction",
               "B_E2_down_Wu", "quoted_margin_Wu", "one_ordinary_down_Wu_e2b2",
               "B_E2_down_e2b2", "quoted_margin_e2b2", "T_half_parent_ns",
               "T_half_quoted_margin_ns", "evidence_group",
               "T_and_B_are_independent_observations", "source_B_already_ICC_corrected"]
    with (OUT/"observed-strength.csv").open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerow({k: observation[k] for k in columns})
    print(json.dumps({
        "one_down_Wu_e2b2": unit,
        "observed_Bdown_e2b2": value,
        "quoted_margin_e2b2": quoted_margin,
        "reverse_factor": 20/16,
        "lifetime_ratio_controls": len(lifetime_controls),
        "inputs_unchanged": True, "model_calculation": False,
    }, indent=2))


if __name__ == "__main__":
    main()
