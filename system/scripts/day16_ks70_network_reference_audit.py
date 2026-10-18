#!/usr/bin/env python3
"""Audit the printed KS70 network and the two roles of the 1505-keV line.

Inputs are published, corrected coefficients, not coincidence events. The
inverse returns algebraic roots and quoted-margin sets, never a confidence fit.
The D96 coefficient primitive is reused under the previously proved KS70 map;
this is not an independent producer implementation or a new delta measurement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_d96_eq4_erratum_audit import coefficient, direct_density
from day16_kf89_w178_gate_audit import finite_delta, intersection, preimage, roots, value


PURE = (("E", 2, 1.0),)


def mixed(delta: float | None) -> tuple:
    return PURE if delta is None else (("M", 1, 1.0), ("E", 2, delta))


def role_coeff(role: str, parts: tuple, rank: int) -> float:
    if role == "target-first":  # 1505 then 658: 3 -> 2 -> 0.
        return (coefficient(3, 2, parts, rank, 0, rank, False)
                * coefficient(2, 0, PURE, 0, rank, rank, False))
    if role == "target-second":  # 764 then 1505: 5 -> 3 -> 2.
        return (coefficient(5, 3, PURE, rank, 0, rank, False)
                * coefficient(3, 2, parts, 0, rank, rank, False))
    raise ValueError(role)


def matrix(role: str, rank: int) -> np.ndarray:
    a = role_coeff(role, mixed(0.0), rank)
    c = role_coeff(role, PURE, rank)
    b = role_coeff(role, mixed(1.0), rank) - (a + c) / 2
    return np.array([[a, b], [b, c]])


def paths_between(first: dict, second: dict, transitions: list) -> list[list[int]]:
    def walk(node: str, used: list[int]) -> list[list[int]]:
        if node == second["parent"]:
            return [used + [second["id"]]]
        found = []
        for gamma in transitions:
            if gamma["parent"] == node and gamma["id"] not in used:
                found += walk(gamma["daughter"], used + [gamma["id"]])
        return found

    return walk(first["daughter"], [first["id"]])


def photon_check(forms: dict) -> float:
    errors = []
    mode = {"q1": 0, "q2": 0, "psi1_deg": 0.0, "psi2_deg": 0.0}
    for role, spins in [("target-first", (3, 2, 0)), ("target-second", (5, 3, 2))]:
        pop = np.ones(2 * spins[0] + 1) / (2 * spins[0] + 1)
        for delta in [0.0, -0.55, 1.0, None]:
            parts = mixed(delta)
            first, second = (parts, PURE) if role == "target-first" else (PURE, parts)
            alpha = math.pi / 2 if delta is None else math.atan(delta)
            for angle in [0.0, 53.0, 90.0, 135.0, 180.0]:
                x = math.cos(math.radians(angle))
                harmonic = [np.polynomial.legendre.legval(x, [0.0] * k + [1.0])
                            for k in [0, 2, 4]]
                expected = sum(h * value(forms[role][k], alpha)
                               for h, k in zip(harmonic, [0, 2, 4]))
                actual = 16 * math.pi**2 * direct_density(
                    spins, first, second, pop, [0.0, angle, 0.0], mode)
                errors.append(abs(actual - expected))
    assert max(errors) < 1e-12
    return max(errors)


def inverse_dataset(rows: dict, forms: dict) -> dict:
    sets = []
    out = {}
    for role, observed in rows.items():
        role_results = {}
        for rank, label in [(2, "A22"), (4, "A44")]:
            central, margin = observed[label]
            a = forms[role][rank]
            allowed = preimage(a, np.eye(2), central - margin, central + margin)
            sets.append(allowed)
            other = "target-second" if role == "target-first" else "target-first"
            candidates = []
            for alpha in roots(a - central * np.eye(2)):
                assert abs(value(a, alpha) - central) < 1e-12
                candidates.append({"delta_KS_D96": finite_delta(alpha),
                                   "atan_delta_deg": math.degrees(alpha),
                                   "other_role_A22": value(forms[other][2], alpha),
                                   "other_role_A44": value(forms[other][4], alpha)})
            role_results[label] = {"printed": observed[label], "central_roots": candidates,
                                   "quoted_margin_atan_delta_deg_sets": allowed}
        out[role] = role_results
    joint = sets[0]
    for allowed in sets[1:]:
        joint = intersection(joint, allowed)
    out["all_four_quoted_margin_intersection_atan_delta_deg"] = joint
    out["confidence_level"] = None
    out["meaning"] = "literal marginal boxes; no likelihood or full covariance recovered"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "DAY16-KS70-NETWORK-1505-ROLE-REFERENCE-01"
    transitions = cfg["transitions"]
    byid = {gamma["id"]: gamma for gamma in transitions}
    energy = {level["id"]: level["energy_keV_fig5"] for level in cfg["levels"]}
    energy_residuals = []
    for gamma in transitions:
        assert energy[gamma["parent"]] > energy[gamma["daughter"]]
        # The enlarged original confirms non-closing printed energies around
        # L2162. Preserve them; topology comes from arrows/indices/spins, not
        # a fitted level-energy correction or a fabricated energy uncertainty.
        energy_residuals.append({
            "gamma_id": gamma["id"],
            "Eparent_minus_Edaughter_minus_Egamma_keV":
                energy[gamma["parent"]] - energy[gamma["daughter"]]
                - gamma["fig5_energy_keV"],
        })
    edges = []
    for row in cfg["tableI_cells"]:
        a, b = byid[row["target"]], byid[row["gate"]]
        paths = paths_between(a, b, transitions) or paths_between(b, a, transitions)
        assert paths, row
        edges.append({"target": a["id"], "gate": b["id"], "allowed_paths": paths,
                      "multiple_paths": len(paths) > 1,
                      "path_weights_supplied": len(paths) == 1,
                      "gate885_only_anisotropy": row["gate"] == 10})
    unordered = {tuple(sorted((r["target"], r["gate"]))) for r in cfg["tableI_cells"]}
    forms = {role: {k: matrix(role, k) for k in [0, 2, 4]}
             for role in ["target-first", "target-second"]}
    for role in forms:
        assert np.max(abs(forms[role][0] - np.eye(2))) < 1e-12
        # Rank four in this truncation has neither M1 nor M1-E2 interference.
        assert np.max(abs(forms[role][4][0])) < 1e-12
    selected = {}
    for label, table in [("indirect_TableI", cfg["tableI_cells"]),
                         ("direct_TableII", cfg["tableII_direct"])]:
        rows = {}
        for first, second, role in [(14, 3, "target-first"), (8, 14, "target-second")]:
            found = [r for r in table if {r.get("first", r.get("target")),
                                         r.get("second", r.get("gate"))} == {first, second}]
            assert len(found) == 1
            row = found[0]
            rows[role] = {k: row[k if label.startswith("direct") else k + "_printed"]
                          for k in ["A22", "A44"]}
        selected[label] = inverse_dataset(rows, forms)
    report = {
        "identity": cfg["identity"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_raw_sha256": cfg["raw_sha256"],
        "topology": {"levels": len(energy), "transitions": len(transitions),
                     "mixed_transitions": [r["id"] for r in transitions if r["multipoles"] == "M1/E2"],
                     "TableI_directed_gate_cells": len(edges),
                     "TableI_unordered_energy_pairs": len(unordered),
                     "TableII_rows": len(cfg["tableII_direct"]),
                     "author_abstract_correlations": 25,
                     "counting_boundary": "Our explicit table-cell/pair count is not equated with the author's unspecified count or independent experiments.",
                     "drawing_energy_residuals": energy_residuals,
                     "drawing_energy_uncertainties_known": False,
                     "edges": edges},
        "forms_KS70_same_D96_basis": {role: {str(k): m.tolist() for k, m in v.items()}
                                      for role, v in forms.items()},
        "shared_primitive_photon_contraction_error": photon_check(forms),
        "inverse": selected,
        "at_author_summary_delta_comparison_only": {
            role: {str(k): value(m, math.atan(cfg["source_summary_delta_1505"][0]))
                   for k, m in v.items()} for role, v in forms.items()},
        "direct_indirect_1505_658_A22_difference": -0.471 - (-0.403),
        "direct_indirect_1505_658_quoted_margin_boxes_overlap":
            max(-0.471 - 0.010, -0.403 - 0.014) <= min(-0.471 + 0.010, -0.403 + 0.014),
        "experimental_covariance_known": False,
        "new_delta_measurement": False,
        "all_internal_checks_passed": True,
    }
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: report[k] for k in ["forms_KS70_same_D96_basis", "inverse",
                      "at_author_summary_delta_comparison_only",
                      "direct_indirect_1505_658_A22_difference"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
