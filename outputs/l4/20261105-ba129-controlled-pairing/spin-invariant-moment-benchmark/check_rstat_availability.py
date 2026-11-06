#!/usr/bin/env python3
"""Bounded 135/137Ba R_stat^(1) denominator audit; creates new extension files only.

No Hamiltonian solve or fit. Static-v1 files are hash-checked and never written.
The parent CSV supplies explicitly labelled model predictions, not measurements.
"""

import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
RAW_STATIC = ROOT / "raw/papers/gpt/query/20261106-ba-spin-moment-benchmark"
RAW_REACTION = ROOT / "raw/papers/gpt/query/20261106-ba-rstat-readiness"
PARENT = ROOT / (
    "outputs/l4/20261105-ba129-controlled-pairing/"
    "spin-invariant-precedent-review/focused-sidecar/calibrated-observable-candidates.csv"
)
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from paired_single_j_em import clebsch_gordan


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def levels(path):
    lines = path.read_text().splitlines()
    starts = [i for i, line in enumerate(lines) if line[5:9] == "  L "]
    blocks = []
    for n, start in enumerate(starts):
        end = starts[n+1] if n+1 < len(starts) else len(lines)
        line = lines[start]
        blocks.append({
            "line": start+1, "last_line": end, "energy_keV": float(line[9:19]),
            "Jpi": line[21:39].strip(), "T_half_field": line[39:49].strip() or None,
            "text": lines[start:end],
        })
    return blocks, lines


def main():
    if (OUT/"rstat-readiness.json").exists() or (OUT/"rstat-readiness.csv").exists():
        raise FileExistsError("Refusing to overwrite extension outputs")
    old = json.loads((OUT/"checks.json").read_text())
    static_hashes = dict(old["output_files_sha256"])
    static_hashes["checks.json"] = sha(OUT/"checks.json")
    for name, expected in static_hashes.items():
        assert sha(OUT/name) == expected, name
    with PARENT.open() as stream:
        parent = {int(row["odd_A"]): row for row in csv.DictReader(stream)}
    files = [PARENT]
    parsed = {}
    for mass in (135, 137):
        for role, base, name in [
            ("adopted", RAW_STATIC, f"nndc{mass}-adopted-text.ens"),
            ("reaction", RAW_REACTION, f"nndc{mass}-reaction-text.ens"),
        ]:
            path = base/name
            parsed[mass, role] = levels(path)
            files.append(path)
    input_hashes = {str(p.relative_to(ROOT)): sha(p) for p in files}

    # Independent angular normalization and detailed-balance direction.
    cg2 = clebsch_gordan(11, 11, 4, 0, 11, 11)**2
    assert math.isclose(cg2, 55/91, rel_tol=2e-15)
    coefficient = 1/((16*math.pi/5)*cg2)
    assert math.isclose(coefficient, 91/(176*math.pi), rel_tol=2e-15)
    test_rme_squared = 1.731
    bup, bdown = test_rme_squared/12, test_rme_squared/16
    assert math.isclose(bup, (16/12)*bdown, rel_tol=1e-15)

    adopted_135 = [x for x in parsed[135, "adopted"][0] if "15/2-" in x["Jpi"]]
    reaction_135 = [x for x in parsed[135, "reaction"][0] if "15/2-" in x["Jpi"]]
    assert len(adopted_135) == len(reaction_135) == 1
    a135, r135 = adopted_135[0], reaction_135[0]
    assert a135["energy_keV"] == r135["energy_keV"] == 950.5
    assert a135["Jpi"] == "(15/2-)" and r135["Jpi"] == "15/2-"
    assert a135["T_half_field"] is None and r135["T_half_field"] is None
    gamma = next(line for line in a135["text"] if line[5:9] == "  G ")
    assert float(gamma[9:19]) == 682.3 and float(gamma[21:29]) == 100
    assert gamma[31:41].strip() == "Q" and not gamma[55:62].strip()
    assert not any("CC=" in line or "BE2" in line for line in a135["text"]+r135["text"])
    lower = [x for x in parsed[135, "adopted"][0] if x["Jpi"] == "11/2-"][0]
    topology_residual = a135["energy_keV"] - 682.3 - lower["energy_keV"]
    assert abs(topology_residual) < .03 and lower["energy_keV"] == 268.218
    for role in ("adopted", "reaction"):
        assert not any("15/2" in x["Jpi"] for x in parsed[137, role][0])
    assert "T{-1/2}<10 ns" in parsed[137, "reaction"][1][6]
    assert "1385.7" in parsed[137, "reaction"][1][6]

    rows = []
    for mass in (135, 137):
        row = parent[mass]
        diagonal_strength = coefficient*float(row["Qs_model_eb"])**2
        assert math.isclose(diagonal_strength, float(row["static_strength_e2b2"]), rel_tol=2e-13)
        model_bup = float(row["all_Jplus2_strength_e2b2"])*float(row["first_Jplus2_fraction_of_channel"])
        ratio = diagonal_strength/model_bup
        assert math.isclose(ratio, float(row["R_static_to_first_Jplus2"]), rel_tol=2e-13)
        rows.append({
            "A": mass, "initial_state": "11/2_1-", "target_model_state": "(15/2-)_1",
            "model_Rstat_first": ratio, "model_diagonal_strength_e2b2": diagonal_strength,
            "model_Bup_11to15_e2b2": model_bup,
            "model_Bdown_15to11_e2b2": (12/16)*model_bup,
            "experimental_Bdown_e2b2": None, "experimental_Bup_e2b2": None,
            "experimental_Rstat_first": None,
            "target_mapping": "tentative 950.5-keV (15/2-) -> 268.218-keV 11/2-"
                              if mass == 135 else "no assigned 15/2 level in either checked dataset",
            "denominator_ready": False,
            "blocking_inputs": "15/2 parent half-life; ICC; absolute branch/purity completeness; tentative assignment"
                               if mass == 135 else "assigned lowest 15/2- and matching decay; absolute E2 strength",
            "static_role": "additional EM comparison; model overpredicts paper/adopted central Q"
                           if mass == 135 else "137Ba static Q is a source-named eF calibration target",
        })
    for name, expected in static_hashes.items():
        assert sha(OUT/name) == expected, name
    assert all(sha(ROOT/p) == h for p, h in input_hashes.items())
    result = {
        "schema": "bounded-Ba135-Ba137-Rstat-first-readiness-v1",
        "actual_checked_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Two adopted objects plus their two originating high-spin reaction objects; no exhaustive literature search.",
        "definition": "R_stat^(1)=(|R_11,11|^2/12)/B(E2;11/2_1- -> 15/2_1-)",
        "normalization": {
            "CG_stretched_squared": cg2,
            "static_strength_from_Qs": "Sdiag=91/(176*pi)*Qs^2, Qs in e b",
            "reverse_direction": "Bup(11/2->15/2)=(16/12)*Bdown(15/2->11/2)",
            "ratio_from_decay_strength": "R_stat^(1)=273/(704*pi)*Qs^2/Bdown",
            "E2_rate": "Bdown=ln(2)*I_gamma_target*fE2/[T_half(parent)*C_E2*Egamma_MeV^5*sum_k I_gamma_k*(1+alpha_k)]",
            "rate_conditions": "Requires complete decay accounting; fE2=1 only for a justified pure E2 branch; missing ICC is not zero.",
            "static_sign": "Qs is retained signed separately; this squared ratio cannot test its sign.",
        },
        "cases": rows,
        "135Ba_evidence": {
            "adopted_level_lines": [202, 206], "reaction_level_lines": [53, 57],
            "adopted_spin": "(15/2-)", "reaction_spin": "15/2-",
            "gamma_keV": 682.3, "RI_photon": 100., "multipolarity_literal": "Q",
            "DCO": 1.18, "DCO_quoted_margin": .03, "ICC": None, "parent_T_half": None,
            "lower_11over2_T_half": "28.7 h, belongs to the daughter isomer, not the 15/2 parent",
            "energy_closure_residual_keV": topology_residual,
            "older_gamma_energy_keV": 682.7,
            "source_keys": ["2006Ch51", "2007ChZZ", "1987Dr13"],
            "lineage": "RI and DCO include 2007ChZZ private communication; Q identifies quadrupole order. E2 interpretation is conditional on the adopted tentative negative-parity assignment.",
        },
        "137Ba_exclusions": [
            {"state_keV": 2047.4, "reaction_state_keV": 2047.2, "Jpi": None,
             "gamma_keV": 1385.7, "daughter_keV": 661.659,
             "T_half": "<10 ns, reaction general comment for this line",
             "reason": "Unassigned state and unclassified multipolarity; no validated 15/2 mapping or absolute B(E2)",
             "adopted_lines": [147, 150], "reaction_lines": [7, 25, 26]},
            {"state_keV": 2349.1, "Jpi": "(17/2-)", "daughter_keV": 2229.5,
             "daughter_Jpi": "(13/2-)", "gamma_keV": 120.2, "T_half_us": .59,
             "T_half_margin_us": .10, "ICC_total": 1.004, "ICC_margin": .017,
             "B_E2_Wu": .45, "B_E2_margin_Wu": .08, "adopted_lines": [192, 200],
             "reason": "Measured E2 belongs to a different spin pair; cannot substitute in R_stat^(1)"},
            {"state_keV": 1797.67, "Jpi": "7/2-", "adopted_lines": [106, 111],
             "reason": "E2 to 11/2- belongs to J-2 rather than the requested J+2 sector"},
        ],
        "independence": "A future measured denominator would add EM information; 137Ba's static numerator remains calibration-linked. Do not construct the denominator from core B(E2), model strengths, or the 11/2 isomer lifetime and call it an experimental holdout.",
        "static_v1_sha256": static_hashes, "static_v1_unchanged": True,
        "input_sha256": input_hashes,
        "normalization_checks_passed": True, "model_or_operator_refit": False,
        "verdict": "Neither experimental R_stat^(1) is determined by the bounded checked source set.",
    }
    with (OUT/"rstat-readiness.json").open("x") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    with (OUT/"rstat-readiness.csv").open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"cases": rows, "static_v1_unchanged": True,
                      "normalization_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
