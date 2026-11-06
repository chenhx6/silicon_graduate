#!/usr/bin/env python3
"""Three new interior points on the supplemental fixed-Lambda,A Gamma path."""
import os
for _variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                  "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_variable] = "1"

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from single_j_ibfm import IBFMParameters, CoreParameters, BosonCore, IBFMKernel
from quadrupole_scalar_invariants import (
    direct_from_spectrum, reduced_table_from_spectrum, reduced_invariants,
)
from run_controls import proxy_summary, scalar_summary, real, write_csv


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protocol_file = OUT / "gamma-path-protocol.json"
    p = json.loads(protocol_file.read_text())
    initial = json.loads((OUT / "protocol.json").read_text())
    original = json.loads((OUT / "controls.json").read_text())
    assert sha(OUT / "protocol.json") == p["initial_protocol_immutable_sha256"]
    assert sha(OUT / "controls.json") == p["initial_controls_sha256"]
    for rel, h in p["input_sha256"].items():
        assert sha(ROOT / rel) == h, rel
    params = IBFMParameters(**p["primary_parameters"])
    eB = original["calibration"]["eB"]
    em = initial["electromagnetic_operator"]
    core = BosonCore(CoreParameters(**initial["frozen_even_core"]))
    rv, rvec = np.linalg.eigh(core.bosons.L2.toarray())
    rlabels = np.rint((np.sqrt(np.maximum(0, 1 + 4 * rv)) - 1) / 2).astype(int)
    old = {c["label"]: c for c in original["cases"]}
    summaries, details, vectors = [], [], []
    energy_replay = []
    first_indices = None
    for s in p["path"]["s"]:
        kernel = IBFMKernel(replace(params, Gamma0=.6 * s))
        sol = kernel.solve(two_M=1)
        same = sol.indices_for_J(11)
        i = int(same[0])
        if first_indices is None:
            first_indices = sol.basis.full_indices
        else:
            assert np.array_equal(first_indices, sol.basis.full_indices)
        vectors.append(sol.vectors[:, same])
        gap = float(sol.energies[same[1]] - sol.energies[i])
        if s in (0, 1):
            label = p["endpoint_reuse"][str(s)]
            label = label.split(":")[-1]
            c = old[label]
            assert abs(float(sol.energies[i]) - c["state"]["energy_MeV"]) < 1e-11
            assert abs(gap - c["state"]["same_J_next_gap_MeV"]) < 1e-11
            assert i == c["state"]["state_index"]
            energy_replay.append({"s": s, "reused_case": label,
                                  "energy_difference": float(sol.energies[i]) - c["state"]["energy_MeV"],
                                  "gap_difference": gap - c["state"]["same_J_next_gap_MeV"],
                                  "role": "Identical-H eigenvector replay for overlap only; existing scalar results reused"})
        else:
            operator = kernel.e2(eB, em["eF_eb"], em["chi_E2"])
            direct = direct_from_spectrum(sol, operator, i,
                                          representation_label="135Ba fixed-Lambda,A Gamma path")
            table = reduced_table_from_spectrum(sol, operator,
                                                representation_label="135Ba fixed-Lambda,A Gamma path")
            closure = reduced_invariants(table, i)
            assert closure.complete and not closure.missing_entries
            delta2 = closure.invariants.q2 - direct.q2
            delta3 = closure.invariants.q3 - direct.q3
            assert max(abs(delta2), abs(delta3)) < 1e-9
            static = float(abs(table.rme[i, i])**2 / 12)
            proxy5, proxy_all = (proxy_summary(table, i, n) for n in (5, None))
            for proxy in (proxy5, proxy_all):
                proxy["fraction_of_full_q2"] = proxy["q2_scalar_contribution_e2b2"] / direct.q2
            full_psi = np.zeros(kernel.dimension, complex)
            full_psi[sol.basis.full_indices] = sol.vectors[:, i]
            product = full_psi.reshape(core.bosons.dimension, params.two_j + 1)
            transformed = rvec.conj().T @ product
            probability = {str(r): float(np.sum(abs(transformed[rlabels == r])**2))
                           for r in sorted(set(rlabels))}
            assert abs(sum(probability.values()) - 1) < 1e-10
            nd = real(np.vdot(product, core.bosons.n_d @ product))
            sectors = [{"two_Ja": int(a), "two_Jb": int(b), "q3_e3b3": real(v)}
                       for (a, b), v in sorted(closure.cubic_by_two_J_pair.items())]
            pos = sum(x["q3_e3b3"] for x in sectors if x["q3_e3b3"] > 0)
            neg = sum(x["q3_e3b3"] for x in sectors if x["q3_e3b3"] < 0)
            assert abs(pos + neg - direct.q3) < 1e-10
            c = {
                "label": f"Gamma_s{s:g}", "Gamma0": .6 * s, "Lambda0": 1., "A0": -.9,
                "state": {"same_J_ordinal": 0, "state_index": i,
                          "energy_MeV": float(sol.energies[i]),
                          "same_J_next_gap_MeV": gap},
                "full_direct": scalar_summary(direct),
                "full_6j": {"q2_e2b2": closure.invariants.q2, "q3_e3b3": closure.invariants.q3},
                "closure": {"complete": True, "delta_q2": delta2, "delta_q3": delta3,
                            "reciprocity_residual": closure.reciprocity_residual},
                "proxy5": proxy5, "proxy_all": proxy_all,
                "same_J": {"static_q2_e2b2": static,
                           "other_same_J_q2_e2b2": float(closure.quadratic_by_two_J[11] - static),
                           "static_fraction": static / direct.q2,
                           "other_same_J_fraction": float((closure.quadratic_by_two_J[11] - static) / direct.q2)},
                "core": {"P_R": probability, "n_d_expectation": nd},
                "signed_cubic_spin_pairs": sectors,
                "cubic": {"positive_spin_pair_sum_e3b3": pos, "negative_spin_pair_sum_e3b3": neg,
                          "initial_triple_e3b3": real(closure.cubic_by_state_pair[
                              (table.multiplets[i].label, table.multiplets[i].label)])},
            }
            details.append(c)
        summary = {
            "s": s, "Gamma0": .6 * s, "Lambda0": 1., "A0": -.9,
            "new_scalar_point": s not in (0, 1), "source_case": c["label"],
            "same_J_ordinal": 0, "state_index": i, "same_J_gap_MeV": gap,
            "q2_e2b2": c["full_direct"]["q2_e2b2"], "q3_e3b3": c["full_direct"]["q3_e3b3"],
            "full_signed_ratio": c["full_direct"]["signed_ratio"],
            "full_folded_angle_deg": c["full_direct"]["folded_angle_deg"],
            "proxy5_raw_ratio": c["proxy5"]["raw_ratio"], "proxy_all_raw_ratio": c["proxy_all"]["raw_ratio"],
            "proxy_all_angle_deg": c["proxy_all"]["angle_deg"],
            "proxy_all_status": c["proxy_all"]["angle_status"],
            "q2_static_fraction": c["same_J"]["static_fraction"],
            "q2_other_same_J_fraction": c["same_J"]["other_same_J_fraction"],
            "P_core_R0": c["core"]["P_R"]["0"], "P_core_R2": c["core"]["P_R"]["2"],
            "nd": c["core"]["n_d_expectation"],
            "complete_6j_closure": c["closure"]["complete"],
            "delta_q2": c["closure"]["delta_q2"], "delta_q3": c["closure"]["delta_q3"],
            "q3_positive_sectors": c["cubic"]["positive_spin_pair_sum_e3b3"],
            "q3_negative_sectors": c["cubic"]["negative_spin_pair_sum_e3b3"],
        }
        summaries.append(summary)
        print(json.dumps(summary), flush=True)
    adjacent, matrices = [], []
    for index in range(4):
        mat = abs(vectors[index].conj().T @ vectors[index + 1])**2
        matrices.append(mat)
        forward, backward = int(np.argmax(mat[0, :])), int(np.argmax(mat[:, 0]))
        top = np.argsort(mat[0])[::-1][:2]
        adjacent.append({
            "left_s": p["path"]["s"][index], "right_s": p["path"]["s"][index + 1],
            "lowest_to_lowest_fidelity": float(mat[0, 0]),
            "left_lowest_best_right_same_J_ordinal": forward,
            "right_lowest_best_left_same_J_ordinal": backward,
            "top_two_right_matches": [{"ordinal": int(j), "fidelity": float(mat[0, j])} for j in top],
        })
    forward_ranks, backward_ranks = [0], [0]
    for mat in matrices:
        forward_ranks.append(int(np.argmax(mat[forward_ranks[-1], :])))
    for mat in reversed(matrices):
        backward_ranks.append(int(np.argmax(mat[:, backward_ranks[-1]])))
    backward_ranks.reverse()
    continuity = {
        "forward_tracked_same_J_ordinals": forward_ranks,
        "backward_tracked_same_J_ordinals": backward_ranks,
        "lowest_preserved_both_directions_on_sample": all(x == 0 for x in forward_ranks + backward_ranks),
        "minimum_sampled_gap_MeV": min(x["same_J_gap_MeV"] for x in summaries),
        "minimum_adjacent_lowest_fidelity": min(x["lowest_to_lowest_fidelity"] for x in adjacent),
        "scope": "Five sampled points, not a proof about all continuous parameter values or a critical point fit",
    }
    assert sha(OUT / "protocol.json") == p["initial_protocol_immutable_sha256"]
    assert sha(OUT / "controls.json") == p["initial_controls_sha256"]
    for rel, h in p["input_sha256"].items():
        assert sha(ROOT / rel) == h, rel
    result = {
        "schema": "135Ba-fixed-Lambda-A-Gamma-path-results-v1",
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "supplement_protocol_sha256": sha(protocol_file),
        "driver_sha256": sha(Path(__file__)),
        "reused_helper_sha256": sha(OUT / "run_controls.py"),
        "initial_protocol_sha256": p["initial_protocol_immutable_sha256"],
        "initial_controls_sha256": p["initial_controls_sha256"],
        "fixed_E2": {"eB": eB, "eF": em["eF_eb"], "chi_E2": em["chi_E2"]},
        "points": summaries, "new_point_details": details,
        "adjacent_overlaps": adjacent, "continuity": continuity,
        "endpoint_eigenvector_replay_checks": energy_replay,
        "new_scalar_point_count": len(details),
        "no_refit": True, "broader_grids_run": False,
    }
    with (OUT / "gamma-path.json").open("x") as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write("\n")
    write_csv(OUT / "gamma-path-summary.csv", summaries)
    print("CONTINUITY", json.dumps(continuity), flush=True)


if __name__ == "__main__":
    main()
