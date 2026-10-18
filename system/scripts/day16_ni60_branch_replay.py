#!/usr/bin/env python3
"""Read the actual SDK's private Ni60 level object and audit pair probabilities.

This checks one source-model cascade. It is not an experimental response fit.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import shlex
import subprocess
from zoneinfo import ZoneInfo

from scipy.stats import binomtest

from day16_ni60_reference_audit import source_levels


CPP = r'''#include <iostream>
#include <iomanip>
#include "G4NuclearLevelData.hh"
#include "G4LevelManager.hh"
#include "G4NucLevel.hh"
#include "G4Version.hh"
int main(int argc, char** argv) {
  if (argc != 2) return 2;
  auto* data = G4NuclearLevelData::GetInstance();
  if (!data->AddPrivateData(28, 60, argv[1])) return 3;
  const auto* manager = data->GetLevelManager(28, 60);
  if (!manager) return 4;
  std::cout << std::setprecision(17)
            << "{\"SDK\":" << G4VERSION_NUMBER << ",\"levels\":[";
  bool first = true;
  for (std::size_t i : {1, 4}) {
    if (!first) std::cout << ",";
    first = false;
    const auto* level = manager->GetLevel(i);
    std::cout << "{\"level\":" << i << ",\"transitions\":[";
    for (std::size_t j = 0; j < level->NumberOfTransitions(); ++j) {
      if (j) std::cout << ",";
      std::cout << "{\"daughter\":" << level->FinalExcitationIndex(j)
                << ",\"cdf\":" << level->GammaCumProbability(j)
                << ",\"gamma_probability\":" << level->GammaProbability(j) << "}";
    }
    std::cout << "]}";
  }
  std::cout << "]}\n";
}
'''


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> dict:
    p = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"command": command, "exit_code": p.returncode,
            "stdout": p.stdout, "stderr": p.stderr}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--rdm", type=Path, required=True)
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--geant4-config", default="/opt/geant4/11.4.2/bin/geant4-config")
    args = parser.parse_args()
    args.build_dir.mkdir(parents=True, exist_ok=True)
    source_hash, rdm_hash = digest(args.source), digest(args.rdm)
    cpp = args.build_dir / "ni60-level-object.cc"
    cpp.write_text(CPP)
    binary = args.build_dir / "ni60-level-object"
    flags = [subprocess.check_output([args.geant4_config, option], text=True)
             for option in ["--cflags", "--libs"]]
    command = ["g++", *shlex.split(flags[0]), str(cpp), "-o", str(binary),
               *shlex.split(flags[1]), "-Wl,-rpath,/opt/geant4/11.4.2/lib"]
    compiled = run(command)
    assert compiled["exit_code"] == 0, compiled
    executed = run([str(binary.resolve()), str(args.source.resolve())])
    assert executed["exit_code"] == 0, executed
    loaded = json.loads([s for s in executed["stdout"].splitlines() if s.startswith('{"SDK"')][-1])
    assert loaded["SDK"] == 1142
    actual = {row["level"]: row["transitions"] for row in loaded["levels"]}
    rows = source_levels(args.source)
    upper = rows[4]["transitions"]
    norm = sum(row["relative_intensity"] * (1 + row["CC"]) for row in upper)
    cdf, checks = 0., []
    for typed, obj in zip(upper, actual[4], strict=True):
        weight = typed["relative_intensity"] * (1 + typed["CC"]) / norm
        cdf += weight
        assert typed["daughter"] == obj["daughter"]
        error = max(abs(cdf - obj["cdf"]), abs(1 / (1 + typed["CC"]) - obj["gamma_probability"]))
        assert error < 2e-7
        checks.append({"daughter": typed["daughter"], "total_branch_weight": weight,
                       "calculated_cdf": cdf, "SDK_max_abs_difference": error})
    beta_rows = []
    in_ground = False
    for raw in args.rdm.read_text().splitlines():
        parts = raw.split()
        if not parts or parts[0].startswith("#"):
            continue
        if parts[0] == "P":
            in_ground = parts[1] == "0"
        elif in_ground and parts[0] == "BetaMinus" and len(parts) > 3:
            beta_rows.append(parts)
    feeding = [row for row in beta_rows if row[1] == "2505.753"]
    assert len(feeding) == 1
    fraction = float(feeding[0][3]) / 100
    first = next(row for row in upper if row["daughter"] == 1)
    last = rows[1]["transitions"][0]
    assert last["daughter"] == 0
    typed_p = fraction * first["relative_intensity"] / norm / (1 + last["CC"])
    previous = 0.
    for row in actual[4]:
        if row["daughter"] == 1:
            loaded_p = fraction * (row["cdf"] - previous) * row["gamma_probability"]
            break
        previous = row["cdf"]
    else:
        raise AssertionError("Missing first transition")
    loaded_p *= actual[1][0]["gamma_probability"]
    assert abs(typed_p - loaded_p) < 2e-7
    bad_p = fraction * first["relative_intensity"] / sum(v["relative_intensity"] for v in upper)
    bad_p /= (1 + first["CC"]) * (1 + last["CC"])
    comparisons = []
    for label, k in [("corr", 99840), ("iso", 99845)]:
        n = 100000
        se = math.sqrt(loaded_p * (1 - loaded_p) / n)
        comparisons.append({"label": label, "N": n, "pairs": k,
            "expected_pairs": n * loaded_p, "fixed_p_SE": se,
            "z_fixed_p": (k / n - loaded_p) / se,
            "exact_binomial_two_sided_pvalue": binomtest(k, n, loaded_p).pvalue})
    result = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": digest(Path(__file__)), "source_sha256": source_hash,
        "RDM_sha256": rdm_hash, "helper_source_sha256": digest(cpp),
        "helper_binary_sha256": digest(binary), "compile": compiled, "execute": executed,
        "actual_level_object": loaded, "branch_checks": checks,
        "ground_beta_fraction": fraction, "sum_Igamma_times_one_plus_CC": norm,
        "pair_probability_typed_model": typed_p, "pair_probability_actual_SDK_object": loaded_p,
        "wrong_gamma_only_normalization_control": bad_p,
        "wrong_minus_correct_probability": bad_p - typed_p,
        "MC_comparisons_same_model_only": comparisons,
        "independent_experimental_validation": False, "input_joint_covariance_known": False,
        "boundary": "Ground-state Co60 only; same source model and selected truth windows. No actual array Q/phase/transport certification.",
        "original_inputs_unchanged": digest(args.source) == source_hash and digest(args.rdm) == rdm_hash}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in ["pair_probability_typed_model", "pair_probability_actual_SDK_object",
        "wrong_minus_correct_probability", "MC_comparisons_same_model_only", "original_inputs_unchanged"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
