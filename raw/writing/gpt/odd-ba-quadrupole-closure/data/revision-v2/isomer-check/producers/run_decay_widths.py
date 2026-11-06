#!/usr/bin/env python3
"""E2-radiative upper lifetime bounds for the declared model decay schemes."""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

from datetime import datetime, timezone
import csv
import hashlib
import json
import math
from pathlib import Path

from run_benchmark import (
    OUT, ROOT, IBFMParameters, IBFMKernel, CoreParameters, BosonCore,
    calibrate_core_e2, transition_rme, sha, real,
)


def main():
    started = datetime.now(timezone.utc).isoformat()
    base = json.loads((OUT / "protocol.json").read_text())
    contract = json.loads((OUT / "decay-width-protocol.json").read_text())
    assert sha(OUT / "protocol.json") == contract["base_protocol_sha256"]
    assert sha(OUT / "results.json") == contract["base_results_sha256"]
    for path, digest in base["input_sha256"].items():
        assert sha(ROOT / path) == digest, path
    p = IBFMParameters(**base["parameters"])
    k = IBFMKernel(p)
    s = k.solve()
    anchor = int(s.indices_for_J(11)[0])
    parents = [int(x) for x in s.indices_for_J(19)[:2]]
    ordinal = {}
    for spin in set(s.two_J.tolist()):
        for n, index in enumerate(s.indices_for_J(spin)):
            ordinal[int(index)] = n
    core = BosonCore(CoreParameters(p.n_b, p.eps_d, p.kappa, p.chi))
    cs = core.solve()
    c0, c2 = (int(cs.indices_for_J(j)[0]) for j in (0, 4))
    old = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/linear-calibration.json"
    settings = [
        {"root_id": "primary", "chi_E": .35, "eF_eb": .125},
        {"root_id": "core_only_control", "chi_E": .35, "eF_eb": 0.},
        *json.loads(old.read_text())["roots"],
    ]
    coeff = contract["rate_coefficient"]["value"]
    rows, branches = [], []
    for operator in settings:
        calibration = calibrate_core_e2(
            core, cs, c0, c2, chi_prime=operator["chi_E"],
            target_B_0_to_2=base["core_Bup_target_e2b2"])
        tensor = k.e2(calibration.eB, operator["eF_eb"], operator["chi_E"])
        for i in parents:
            local = []
            for f, energy in enumerate(s.energies):
                tj = int(s.two_J[f])
                if abs(tj - 19) > 4 or 19 + tj < 4 or energy >= s.energies[i]:
                    continue
                egamma = float(s.energies[i] - energy)
                rme = transition_rme(s, tensor, i, f)
                b = float(abs(rme)**2 / 20)
                rate = coeff * egamma**5 * b
                local.append({
                    "operator": operator["root_id"],
                    "initial_two_J": 19, "initial_ordinal": ordinal[i],
                    "final_two_J": tj, "final_ordinal": ordinal[f],
                    "initial_relative_MeV": float(s.energies[i] - s.energies[anchor]),
                    "final_relative_MeV": float(energy - s.energies[anchor]),
                    "photon_model_MeV": egamma, "signed_RME_eb": real(rme),
                    "Bdown_e2b2": b, "E2_gamma_rate_s_inverse": rate,
                })
            total = sum(r["E2_gamma_rate_s_inverse"] for r in local)
            for r in local:
                r["conditional_E2_only_radiative_fraction"] = (
                    r["E2_gamma_rate_s_inverse"] / total if total else None)
            local.sort(key=lambda r: r["E2_gamma_rate_s_inverse"], reverse=True)
            bound = math.log(2) * 1e9 / total if total > 0 else None
            row = {
                "operator": operator["root_id"], "initial_ordinal": ordinal[i],
                "eB_eb": calibration.eB, "eF_eb": operator["eF_eb"],
                "chi_E": operator["chi_E"], "open_E2_branch_count": len(local),
                "sum_E2_gamma_rate_s_inverse": total,
                "model_scheme_half_life_upper_bound_ns": bound,
                "observed589ns_over_model_upper_bound": 589. / bound if bound else None,
                "dominant_final_two_J": local[0]["final_two_J"] if local else None,
                "dominant_final_ordinal": local[0]["final_ordinal"] if local else None,
                "dominant_photon_model_MeV": local[0]["photon_model_MeV"] if local else None,
                "dominant_E2_only_radiative_fraction": (
                    local[0]["conditional_E2_only_radiative_fraction"] if local else None),
            }
            rows.append(row)
            branches.extend(local)
    for path, digest in base["input_sha256"].items():
        assert sha(ROOT / path) == digest, path
    result = {
        "schema": "137Ba-model-E2-decay-completeness-v1",
        "started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_sha256": sha(OUT / "decay-width-protocol.json"),
        "producer_sha256": sha(__file__), "rate_coefficient": contract["rate_coefficient"],
        "rows": rows, "branches": branches,
        "conditions": contract["conditions"],
        "model_widths_are_not_measured_widths": True,
        "no_missing_ICC_or_nonE2_rate_assumed_zero_for_total_lifetime_prediction": True,
        "meaning_of_last_flag": "Only E2-radiative widths are included, hence an upper bound; no complete lifetime prediction is claimed.",
    }
    with (OUT / "decay-width-results.json").open("x") as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write("\n")
    with (OUT / "decay-width-summary.csv").open("x", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for r in rows:
        print(r["operator"], r["initial_ordinal"] + 1,
              "half_life_upper_ns", r["model_scheme_half_life_upper_bound_ns"],
              "obs_over_bound", r["observed589ns_over_model_upper_bound"],
              "dominant_J", f"{r['dominant_final_two_J']}/2",
              "rank", r["dominant_final_ordinal"] + 1)


if __name__ == "__main__":
    main()
