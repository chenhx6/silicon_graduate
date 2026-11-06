#!/usr/bin/env python3
"""Source-located moment constraints and alternatives, without combining data.

Retains evaluated/source-quoted margins as quoted; no confidence-level model,
new fit, averaging, or independence count. Source records remain in raw files.
"""

import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
OLD = "raw/papers/gpt/query/20261105-ba129-core-constraints"
CORE = "raw/papers/gpt/query/20261106-ba-core-E2-calibration"
RAW = "raw/papers/gpt/query/20261106-ba-spin-moment-benchmark"
TEX = "raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex"
PDF = "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf"


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def margin(value, digits):
    return float(Decimal(digits) * Decimal(10)**Decimal(value).as_tuple().exponent)


def main():
    if (OUT/"source-constraints.json").exists() or (OUT/"source-constraints.csv").exists():
        raise FileExistsError("Refusing to overwrite constraint outputs")
    benchmark = json.loads((OUT/"benchmark-results.json").read_text())
    odd = {r["odd_A"]: r["odd"]["Qs_eb"] for r in benchmark["cases"]}
    core = {r["core_A"]: r["core"]["Qs_eb"] for r in benchmark["cases"]}
    rows, sources = [], {}

    def source(path, first, last, page=None, locator=None):
        lines = (ROOT/path).read_text().splitlines()
        excerpt = "\n".join(lines[first-1:last])
        sources[path] = sha(path)
        return {"path": path, "line_first": first, "line_last": last,
                "pdf_page": page, "locator": locator}, excerpt

    def add(a, state, observable, value, error, unit, src, role, *, model=None,
            theory=None, keys=(), alternative=None, approximate=False, dependency=None):
        rows.append({
            "id": f"constraint-{len(rows)+1:02d}", "A": a, "nucleus": f"{a}Ba",
            "state": state, "observable": observable,
            "experimental_or_evaluated_value": value, "quoted_margin": error, "unit": unit,
            "source_theory_value": theory, "fixed_model_value": model,
            "model_minus_data": model-value if model is not None else None,
            "difference_over_quoted_margin": (model-value)/error if model is not None and error else None,
            "margin_multiple_is_not_a_statistical_test": True,
            "model_uncertainty": None, "confidence_level": None,
            "approximate": approximate, "source": src, "source_keys": list(keys),
            "role": role, "alternative": alternative, "dependency": dependency,
        })

    # The only Ba negative-parity 11/2 row in the paper's EM comparison tables.
    src, text = source(TEX, 962, 993, 9, "Nomura2017 Table VI, 11/2_1- row; arXiv v2")
    assert "${11/2}^-_1$ & +1.13 & +0.98(8) & -1.161  & -1.001(15)" in text
    add(135, "11/2_1-", "Qs", .98, .08, "e b", src,
        "additional EM benchmark; not one of the E2 moment anchors named in the source",
        model=odd[135], theory=1.13, keys=("Nomura2017 reference 39: NNDC",),
        dependency="Hamiltonian strengths were energy-adjusted; comparison is conditional on those inputs. NNDC reference is not a second measurement.")
    add(135, "11/2_1-", "magnetic_moment", -1.001, .015, "mu_N", src,
        "tabulated constraint retained; magnetic operator calibration outside the frozen E2 contract",
        theory=-1.161,
        dependency="The source table prints mu_N^2 in its moment header; physical magnetic moments have units mu_N. No M1 strengths inferred.")

    # Current archived adopted objects; evaluation dates are not retrieval dates.
    for a, first, last, page in [(135, 107, 122, 1), (137, 60, 76, 1)]:
        path = f"{RAW}/nndc{a}-adopted-text.ens"
        src, text = source(path, first, last, page, "Adopted lowest 11/2- level")
        q = re.search(r"MOME2=([+-]?\d+\.\d+)\s+(\d+)", text)
        assert q
        add(a, "11/2_1-", "Qs", float(q[1]), margin(q[1], q[2]), "e b", src,
            "source-named neutron-charge calibration target state; calibration consistency, not a holdout"
            if a == 137 else "evaluated comparison; preserve separately from the paper's +0.98(8)",
            model=odd[a], keys=("1983Mu12", "1989Ra17"),
            dependency="135Ba and 137Ba share source keys; covariance and reference-moment dependence are not quantified.")
        if a == 137:
            mu = re.search(r"MOMM1=([+-]?\d+\.\d+)\s+(\d+)", text)
            add(a, "11/2_1-", "magnetic_moment", float(mu[1]), margin(mu[1], mu[2]), "mu_N", src,
                "tabulated evaluated constraint; not calculated under this E2-only benchmark",
                keys=("1983Mu12", "1989Ra17"))
            assert "Q|?-0.05 (1976Fu06)" in text
            alt_src, _ = source(path, 69, 69, 1, "Evaluator explicitly notes conflicting older Q")
            add(a, "11/2_1-", "Qs", -.05, None, "e b", alt_src,
                "conflicting historical alternative, not selected adopted datum",
                model=odd[a], keys=("1976Fu06",), approximate=True,
                alternative="about -0.05; evaluator says adopted +0.78(9) disagrees")
        level = text.splitlines()[0]
        time_value, time_unit = level[39:49].split()
        time_error = level[49:55].strip()
        add(a, "11/2_1-", "T1/2", float(time_value), margin(time_value, time_error),
            {"H": "hour", "M": "minute"}[time_unit], src,
            "M4 isomer lifetime; outside the rank-2 single-negative-parity-space benchmark",
            dependency="Evaluated BM4 and lifetime are related summaries, not independent E2 observations.")
        b = re.search(r"BM4W=(\d+\.\d+)\s+(\d+)", text)
        assert b
        gamma_src, _ = source(path, 118 if a == 135 else 71, 122 if a == 135 else 76,
                              6 if a == 135 else 4, "M4 decay to 3/2+ ground state")
        add(a, "11/2_1- -> 3/2_1+", "B(M4)", float(b[1]), margin(b[1], b[2]), "W.u.",
            gamma_src, "rank-4 parity-changing constraint, outside this E2/M1 model space",
            dependency="Same evaluated decay/lifetime lineage; no inference of E2 strength.")

    # Additional directly tabulated first-2+ moments already in the parent archive.
    src, text = source(f"{OLD}/nndc130-adopted-text.ens", 43, 54, 1, "First 2+ moment and reorientation alternatives")
    for value, error, key, label in [
        (-1.02, .16, "1989Bu07", "constructive; adopted displayed value"),
        (-.09, .16, "1989Bu07", "destructive"),
        (-.33, .24, "1974Ne15", "other historical method value"),
        (+.37, .18, "1973ToXW", "destructive historical alternative"),
        (-1.10, .34, "1967Si03", "other historical method value"),
    ]:
        assert key in text
        add(130, "2_1+", "Qs", value, error, "e b", src,
            "additional core EM benchmark; no branch selected to improve model agreement",
            model=core[130], keys=(key,), alternative=label,
            dependency="1989Bu07 also supplies the B(E2) charge calibration; branch solutions are not independent observations.")
    src, text = source(f"{CORE}/nndc134-coulomb-text.ens", 13, 19, 1, "First 2+ Coulomb-excitation Q alternatives")
    assert "Q=-0.26 {I8} or +0.15 {I8} (1989Bu07)" in text
    for value in (-.26, .15):
        add(134, "2_1+", "Qs", value, .08, "e b", src,
            "additional core EM benchmark; preserve both source alternatives",
            model=core[134], keys=("1989Bu07",), alternative="two listed solutions",
            dependency="Same source contributes to the selected B(E2) calibration; unknown covariance.")
    src, text = source(f"{CORE}/nndc136-adopted-text.ens", 51, 61, 1, "First 2+ Q reorientation alternatives")
    for value, error, keys, label in [
        (-.19, .06, ("1986BaZJ", "1986Ro15"), "constructive"),
        (+.07, .07, ("1986BaZJ", "1986Ro15"), "destructive"),
        (+.01, .05, ("1984Be20",), "constructive"),
        (+.25, .05, ("1984Be20",), "destructive"),
        (-.19, .17, ("1972Ke16",), "constructive"),
        (+.02, .18, ("1972Ke16",), "destructive"),
    ]:
        assert all(key in text for key in keys)
        add(136, "2_1+", "Qs", value, error, "e b", src,
            "source-named chi_E calibration target state; source does not identify its numerical target/branch",
            model=core[136], keys=keys, alternative=label,
            dependency="Shared Coulomb-excitation provenance with the first-2+ B(E2) calibration; keep interference solutions separate.")

    anchor_src, _ = source(TEX, 549, 582, 4, "Eqs. (7)-(8) and E2 calibration paragraph")
    record = {
        "schema": "source-located-static-moment-constraints-v1",
        "actual_generated_at": datetime.now(timezone.utc).isoformat(),
        "primary_source": {"pdf": PDF, "sha256": sha(PDF), "calibration_locator": anchor_src},
        "calibration_quote_boundary": "Nomura names 136Ba 2_1+ and 137Ba 11/2_1- and quotes chi_E=.35, e_n=.125 e b, but does not give their numerical experimental/calculated moments there.",
        "sources_sha256": sources, "constraints": rows,
        "coverage": {
            "odd_129_131_133_Qs": "Model predictions only in this bounded source check; no experimental numbers invented and no claim of exhaustive absence.",
            "core_128_132_Qs": "No numerical Q found in the checked first-2+ adopted/Coulomb blocks.",
            "Nomura_other_EM_tables": "Other negative-parity 11/2 rows concern Xe/La/Cs, not additional Ba-chain observations.",
        },
        "version_boundary": {
            "135Ba": "Paper Table VI gives +0.98(8); archived adopted gives +0.96(8). Retain both, do not average or count as independent.",
            "137Ba_evaluation": "NDS 108,2173 (2007), cutoff 1-Oct-2006; later update/header annotations retained in raw.",
            "135Ba_evaluation": "NDS 109,517 (2008), cutoff 22-Jan-2008; later header annotations retained in raw.",
            "136Ba_evaluation": "NDS 152,331 (2018), cutoff 1-Apr-2018; not asserted to be the exact NNDC snapshot used in 2017.",
        },
        "units": {"Qs": "physical spectroscopic e b; signs retained",
                  "magnetic_moment": "mu_N, not the squared unit printed in the paper's moment header",
                  "B(M4)": "W.u.; outside the current E2 operator scope"},
        "constraints_are_not_an_independent_data_count": True,
        "no_error_distributions_or_model_uncertainties_invented": True,
    }
    with (OUT/"source-constraints.json").open("x") as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write("\n")
    flattened = [{
        **{k: row[k] for k in ("id", "nucleus", "state", "observable",
                              "experimental_or_evaluated_value", "quoted_margin", "unit",
                              "source_theory_value", "fixed_model_value", "model_minus_data",
                              "difference_over_quoted_margin", "role", "alternative")},
        "source_path": row["source"]["path"],
        "source_first_line": row["source"]["line_first"],
        "source_last_line": row["source"]["line_last"],
        "source_pdf_page": row["source"]["pdf_page"],
        "source_keys": ";".join(row["source_keys"]),
    } for row in rows]
    with (OUT/"source-constraints.csv").open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(flattened[0]))
        writer.writeheader()
        writer.writerows(flattened)
    print(json.dumps({"rows": len(rows), "Qs_rows_including_alternatives":
                      sum(r["observable"] == "Qs" for r in rows)}, indent=2))


if __name__ == "__main__":
    main()
