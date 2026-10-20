#!/usr/bin/env python3
"""Printed Fe58 phase graph and parameter-input audit, not GOSIA replay."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def edge(a, b):
    return tuple(sorted((a, b)))


def canonical_signs(vertices, tree, chords, signs):
    phases = {vertices[0]: 1}
    while len(phases) < len(vertices):
        before = len(phases)
        for a, b in tree:
            if a in phases and b not in phases:
                phases[b] = phases[a] * signs[edge(a, b)]
            elif b in phases and a not in phases:
                phases[a] = phases[b] * signs[edge(a, b)]
        if before == len(phases):
            raise ValueError("Disconnected declared tree")
    return tuple(signs[edge(a, b)] * phases[a] * phases[b] for a, b in chords)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    a = parser.parse_args()
    d = json.loads(a.contract.read_text())
    checks, graphs = [], {}

    def check(name, condition, **values):
        checks.append({"name": name, "passed": bool(condition), **values})

    for isotope in ("56", "58"):
        g = d["graph" + isotope]
        vertices, tree, chords = g["vertices"], g["tree_edges"], g["chord_edges"]
        edges = tree + chords
        classes = {}
        for pattern in itertools.product((-1, 1), repeat=len(edges)):
            signs = {edge(*e): s for e, s in zip(edges, pattern)}
            canonical = canonical_signs(vertices, tree, chords, signs)
            classes[canonical] = classes.get(canonical, 0) + 1
        expected_classes = 2 ** (len(edges) - len(vertices) + 1)
        orbit_size = 2 ** (len(vertices) - 1)
        check(f"Fe{isotope}_cycle_rank_classes", len(classes) == expected_classes,
              vertices=len(vertices), edges=len(edges), cycle_rank=len(chords),
              classes=len(classes))
        check(f"Fe{isotope}_all_orbits_exact", set(classes.values()) == {orbit_size},
              orbit_size=orbit_size, all_edge_patterns=2 ** len(edges))
        all_gauge_ok = True
        for pattern in itertools.product((-1, 1), repeat=len(chords)):
            signs = {edge(*e): 1 for e in tree}
            signs.update({edge(*e): s for e, s in zip(chords, pattern)})
            for eta in itertools.product((-1, 1), repeat=len(vertices) - 1):
                phases = dict(zip(vertices, (1,) + eta))
                changed = {edge(x, y): s * phases[x] * phases[y]
                           for (x, y), s in signs.items()}
                all_gauge_ok &= canonical_signs(vertices, tree, chords, changed) == pattern
        check(f"Fe{isotope}_vertex_rephasing_preserves_class", all_gauge_ok)
        graphs[isotope] = {"vertices": len(vertices), "edges": len(edges),
                           "cycle_rank": len(chords), "classes": len(classes),
                           "orbit_size": orbit_size,
                           "printed_subset_only": True}
    # A closed path visits every vertex an even number of times, so its edge
    # product is invariant. This is the printed real-phase P3 example.
    triangle_ok, mixed_ratio_ok = True, True
    for eta in itertools.product((-1, 1), repeat=3):
        m01, m12, m20 = (0.351, -0.271, 0.078)
        product = m01 * m12 * m20
        changed = (eta[0]*eta[1]*m01) * (eta[1]*eta[2]*m12) * (eta[2]*eta[0]*m20)
        triangle_ok &= math.isclose(product, changed, rel_tol=1e-15)
        # Same-transition E2/M1 relative sign is invariant to state rephasing.
        e2, m1 = eta[0]*eta[1]*0.271, eta[0]*eta[1]*(-0.5)
        mixed_ratio_ok &= math.isclose(e2/m1, 0.271/(-0.5), rel_tol=1e-15)
    check("P3_state_phase_invariant", triangle_ok)
    check("same_transition_multipole_ratio_state_phase_invariant", mixed_ratio_ok)
    wu = (1/(4*math.pi)) * (3/5) ** 2 * (1.2 * 58 ** (1/3)) ** 4
    table = []
    for x in d["TableVII_4to2"]:
        b = float(x["RME_eb"]) ** 2 / 9 * 10000 / wu
        residual = b - float(x["B_WU"])
        check("TableVII_unit_center_" + x["sign"], abs(residual) < 0.51,
              B_WU_calculated=b, printed_B_WU=x["B_WU"], residual=residual)
        table.append({**x, "B_WU_from_printed_RME": b,
                      "not_independent_measurement_or_CI": True})
    yields = []
    for x in d["TableII"]:
        raw_ratio = x["counts"] / x["reference_counts"]
        factor = float(x["yield"]) / raw_ratio
        check(f"yield_correction_is_not_rawratio_{x['A']}_{x['label']}", abs(factor - 1) > 0.2)
        yields.append({**x, "raw_count_ratio": raw_ratio,
                       "combined_relative_efficiency_angular_factor": factor,
                       "not_absolute_efficiency": True})
    qs = []
    for x in d["Qs"]:
        spin = x["I"]
        c = math.sqrt(16*math.pi/5) * math.sqrt(spin*(2*spin-1)/((2*spin+1)*(spin+1)*(2*spin+3)))
        qs.append({**x, "printedEq2_diagonal_RME_eb": float(x["Qs_eb"]) / c,
                   "state_phase_cannot_change_diagonal_sign": True,
                   "not_Qt_or_sidefeeding_Qs": True})
    out = {"scope": d["scope"],
           "contract_sha256": hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "graphs": graphs, "TableVII_conversion": table,
           "yield_chart_controls": yields, "spectroscopic_Q_to_diagonal_RME": qs,
           "original_Gosia_fit_executed": False,
           "reported_fit_independence": d["shared_constraint_boundary"],
           "checks": checks, "checks_total": len(checks),
           "checks_passed": sum(x["passed"] for x in checks),
           "all_passed": all(x["passed"] for x in checks)}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_passed": out["all_passed"], "checks": len(checks),
                      "graphs": graphs, "yield_controls": yields, "diagonal": qs}))
    if not out["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
