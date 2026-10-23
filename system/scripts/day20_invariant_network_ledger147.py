"""Central-value ledger for a J=0 -> J=2 E2 network.

This transforms explicitly transcribed source values, not experimental events.
Unlisted matrix elements remain symbolic; no CI or convergence certification.
Conventions: q2=a.T a, q3=-sqrt(7/10)*a.T D a (Henderson Eq. 7-10).
Input a and symmetric D are real RMEs in eb, in a single phase convention.
"""

import argparse
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def ledger(data):
    a = [Decimal(x["central_eb"]) for x in data["ground_to_two"]]
    n = len(a)
    entries = {}
    for row in data["two_to_two"]:
        i, j = sorted((row["i"] - 1, row["j"] - 1))
        if not (0 <= i <= j < n) or (i, j) in entries:
            raise ValueError("Invalid or duplicate matrix element")
        entries[i, j] = Decimal(row["central_eb"])
    k = -math.sqrt(7 / 10)
    q2 = sum(x*x for x in a)
    known = sum((1 if i == j else 2)*a[i]*d*a[j]
                for (i, j), d in entries.items())
    missing = [{"i": i+1, "j": j+1,
                "coefficient_eb2_in_q3": k*float((1 if i == j else 2)*a[i]*a[j])}
               for i in range(n) for j in range(i, n) if (i, j) not in entries]
    prefixes = []
    for m in range(1, n+1):
        unknown = [x for x in missing if x["i"] <= m and x["j"] <= m]
        s2 = sum(x*x for x in a[:m])
        s3 = sum((1 if i == j else 2)*a[i]*d*a[j]
                 for (i, j), d in entries.items() if i < m and j < m)
        item = {"n_two_states": m, "q2_eb2": str(s2),
                "known_q3_term_eb3": k*float(s3),
                "unlisted_terms": unknown,
                "complete_within_this_prefix": not unknown}
        if not unknown:
            ratio = k*float(s3) / float(s2)**1.5
            item["truncated_moment_ratio"] = ratio
            item["effective_angle_deg_if_ratio_in_domain"] = (
                math.degrees(math.acos(ratio))/3 if abs(ratio) <= 1 else None)
        prefixes.append(item)
    # Independent floating matrix calculation of the listed contribution only.
    # Zeros here are a computational mask, never values assigned to missing RMEs.
    matrix = np.zeros((n, n))
    for (i, j), d in entries.items():
        matrix[i, j] = matrix[j, i] = float(d)
    vector = np.array(a, dtype=float)
    comparison = float(vector @ matrix @ vector)
    # Passive state rephasing must preserve every listed loop product.
    phases = np.array([(-1)**i for i in range(n)])
    rephased = float((phases*vector) @ (phases[:, None]*matrix*phases) @ (phases*vector))
    return {
        "scope": "Literal central-value transformation; no experimental uncertainty propagation",
        "q2_six_state_eb2": str(q2),
        "first_state_fraction_of_listed_q2": float(a[0]**2/q2),
        "known_aDa_eb3": str(known), "known_q3_term_eb3": k*float(known),
        "unknown_in_selected_network": missing,
        "outside_selected_network": "Additional q2 strength and q3 paths are unspecified, not zero",
        "q3_expression": "known_q3_term + sum(coefficient_eb2_in_q3 * D_ij_eb) + outside-network paths",
        "prefixes": prefixes,
        "numerical_diagnostics": {
            "decimal_vs_numpy_aDa_absolute_difference_eb3": abs(float(known)-comparison),
            "passive_rephasing_absolute_difference_eb3": abs(rephased-comparison)},
        "not_inferred": ["Full experimental q2 or q3", "Original fit covariance or CI",
                         "Missing-element bounds", "Actual gamma softness or a rigidity verdict"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    result = ledger(json.loads(raw))
    result["input_sha256"] = hashlib.sha256(raw).hexdigest()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with args.output.open("x") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
