#!/usr/bin/env python3
"""Rather arXiv v1 published-rate contrasts; not an original DSAM fit."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    a = parser.parse_args()
    d = json.loads(a.contract.read_text())
    checks = []

    def check(name, condition, **values):
        checks.append({"name": name, "passed": bool(condition), **values})

    rows = {(x["band"], x["spin"]): x for x in d["rows"]}
    contrast = []
    for spin in (14, 15, 16, 17):
        m, p = rows["main", spin], rows["partner", spin]
        rm = Fraction(p["BM1_muN2"]) / Fraction(m["BM1_muN2"])
        re = Fraction(p["BE2_e2b2"]) / Fraction(m["BE2_e2b2"])
        s = rm / re
        contrast.append({"spin": spin, "partner_over_main_BM1": float(rm),
                         "partner_over_main_BE2": float(re),
                         "same_parent_M1_E2_double_ratio": float(s),
                         "exact_same_parent_double_ratio": str(s)})
        for c_main, c_partner in ((Fraction(2), Fraction(3)),
                                  (Fraction(3, 4), Fraction(11, 7))):
            mp = Fraction(m["BM1_muN2"]) * c_main
            ep = Fraction(m["BE2_e2b2"]) * c_main
            pp = Fraction(p["BM1_muN2"]) * c_partner
            pe = Fraction(p["BE2_e2b2"]) * c_partner
            check(f"I{spin}_per_parent_rate_scale_{c_main}_{c_partner}",
                  (pp/pe)/(mp/ep) == s)
    s15 = Fraction(contrast[1]["exact_same_parent_double_ratio"])
    s17 = Fraction(contrast[3]["exact_same_parent_double_ratio"])
    double = s15 / s17
    check("spin15_to17_contrast_exact", double == Fraction(22624, 3105),
          exact=str(double), value=float(double))
    error_rows = []
    for x in d["rows"]:
        t, st = Fraction(x["tau_ps"]), Fraction(x["tau_parenthesis_if_SD_ps"])
        b, sb = Fraction(x["BM1_muN2"]), Fraction(x["BM1_parenthesis_if_SD_muN2"])
        minimum = b * st / t
        error_rows.append({"band": x["band"], "spin": x["spin"],
                           "literal_quoted_BM1_error_if_SD": float(sb),
                           "minimum_local_BM1_SD_from_independent_tau": float(minimum),
                           "extra_independent_SD_interpretation_compatible_at_centers": sb >= minimum,
                           "not_an_experimental_significance_or_CI": True})
    check("main12_displayed_SD_reductio", not error_rows[0]["extra_independent_SD_interpretation_compatible_at_centers"])
    check("main13_displayed_SD_reductio", not error_rows[1]["extra_independent_SD_interpretation_compatible_at_centers"])
    # The printed precision is preserved; no invented correction to .10(.02).
    literal = rows["partner", 18]["BE2_printed_literal"]
    check("partner18_literal_preserved", literal == "0.1(2)")
    main_min = min((x for x in d["rows"] if x["band"] == "main"), key=lambda x: Fraction(x["BM1_muN2"]))
    partner_max = max((x for x in d["rows"] if x["band"] == "partner"), key=lambda x: Fraction(x["BM1_muN2"]))
    check("printed_main_min_is15", main_min["spin"] == 15)
    check("printed_partner_max_is15", partner_max["spin"] == 15)
    mass = []
    for x in d["mass_checks"]:
        mass.append({**x, "mass_conserving_productA": x["targetA"]+x["beamA"]-x["neutrons"],
                     "closes_to_printed_product": x["targetA"]+x["beamA"]-x["neutrons"] == x["printedproductA"]})
    check("review_literal90_does_not_close106", not mass[0]["closes_to_printed_product"])
    check("primary_Rather96_closes106", mass[1]["closes_to_printed_product"])
    out = {"scope": d["analysis_scope"],
           "contract_sha256": hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "source_rows_literal": d["rows"], "spin_contrasts": contrast,
           "S15_over_S17_exact": str(double), "S15_over_S17": float(double),
           "independent_SD_reductio_rows": error_rows,
           "literal_prose_table_boundary": {"main_min_spin_from_table": main_min["spin"],
                                            "partner_max_spin_from_table": partner_max["spin"],
                                            "source_prose_spin": 17,
                                            "no_spin_or_band_labels_repaired": True},
           "mass_number_role_controls": mass,
           "actual_experimental_Cov_or_original_fit_recovered": False,
           "Lieder_primary_body_read": False,
           "checks": checks, "checks_total": len(checks),
           "checks_passed": sum(x["passed"] for x in checks),
           "all_passed": all(x["passed"] for x in checks)}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_passed": out["all_passed"], "checks": len(checks),
                      "S15_over_S17": float(double), "mass": mass,
                      "first_two_SD_reductios": error_rows[:2]}, ensure_ascii=False))
    if not out["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
