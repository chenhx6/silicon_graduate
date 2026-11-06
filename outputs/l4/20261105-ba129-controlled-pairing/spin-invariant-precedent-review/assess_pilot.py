"""Read-only pilot assessment: stored-number arithmetic, not a model rerun.

Writes derived assessment products beside this file. Does not import the
model, refit, diagonalize, or edit the parent contract or result.
"""
import sys
sys.dont_write_bytecode = True
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path

ROOT = Path("/workspace/wiki")
OUT = Path(__file__).resolve().parent
BASE = ROOT / "outputs/l4/20261105-ba129-controlled-pairing"
PILOT = BASE / "spin-invariant-probe/chain-core-only-v1.json"
CONTRACT = BASE / "spin-invariant-chain-contract.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    result = json.loads(PILOT.read_text())
    contract = json.loads(CONTRACT.read_text())
    inputs = {str(PILOT.relative_to(ROOT)):sha(PILOT),
              str(CONTRACT.relative_to(ROOT)):sha(CONTRACT)}
    assert inputs[str(CONTRACT.relative_to(ROOT))] == result["contract_sha256"]
    assert sha(ROOT/contract["source"]) == contract["source_sha256"]
    inputs[contract["source"]] = contract["source_sha256"]
    for name, digest in result["producer_sha256"].items():
        assert sha(ROOT/name) == digest
        inputs[name] = digest
    assert [x["case"] for x in result["cases"]] == contract["cases"]
    rows = []
    closure_residuals = []
    for case in result["cases"]:
        spec = case["case"]
        odd = case["odd_core_operator_only"]
        core = case["core"]["full_moments"]
        full = odd["full_moments"]
        n5 = next(x for x in odd["restricted_prescriptions"] if x["count_requested"] == 5)
        all_jp = next(x for x in odd["restricted_prescriptions"] if x["count_requested"] is None)
        q2 = full["q2_scalar"]
        closure_error = sum(x["q2_contribution"] for x in odd["quadratic_spin_channels"].values()) - q2
        closure_residuals.append(abs(closure_error))
        assert abs(closure_error) < 1e-8
        assert abs(full["ratio_signed"] - full["q3_scalar_signed"]/q2**1.5) < 1e-12
        assert abs(full["gamma_folded_deg"]
                   - math.degrees(math.acos(abs(full["ratio_signed"])))/3) < 1e-10
        q2_fraction = n5["q2_with_scalar_normalization"]/q2
        channel_fraction = all_jp["q2_with_scalar_normalization"]/q2
        saturation = n5["q2_with_scalar_normalization"]/all_jp["q2_with_scalar_normalization"]
        beta_ratio = n5["beta_proxy_over_full_invariant_scale"]
        beta_coefficient = beta_ratio**2/q2_fraction
        assert abs(beta_coefficient - 17.5) < 1e-10
        assert abs(case["sqrt_q2_odd_over_core"] - math.sqrt(q2/core["q2_scalar"])) < 1e-12
        assert abs(q2_fraction - n5["retained_fraction_of_full_q2"]) < 1e-12
        rows.append({
            "odd_A":spec["odd_A"], "core_A":spec["core_A"], "two_J":spec["two_J_state"],
            "state_ordinal":spec["state_ordinal"],
            "full_q2_unit_core_charge":q2, "full_signed_cubic_ratio":full["ratio_signed"],
            "full_folded_gamma_deg":full["gamma_folded_deg"],
            "full_signed_equivalent_gamma_deg":full["gamma_rigid_equivalent_signed_deg"],
            "proxy_n5_gamma_deg":n5["gamma_proxy_deg"],
            "proxy_all_Jplus2_gamma_deg":all_jp["gamma_proxy_deg"],
            "full_minus_n5_gamma_deg":full["gamma_folded_deg"]-n5["gamma_proxy_deg"],
            "n5_minus_all_Jplus2_gamma_deg":n5["gamma_proxy_deg"]-all_jp["gamma_proxy_deg"],
            "n5_Jplus2_fraction_of_full_q2":q2_fraction,
            "all_Jplus2_fraction_of_full_q2":channel_fraction,
            "n5_saturation_within_Jplus2":saturation,
            "beta_proxy_over_full_scale":beta_ratio,
            "beta_ratio_squared_over_fraction":beta_coefficient,
            "P_core_R0_all_zero_spin_states":case["P_core_R0"],
            "P_core_ground_R0":case["P_core_ground_R0"],
            "sqrt_q2_odd_over_core":case["sqrt_q2_odd_over_core"],
            "q2_odd_over_core":q2/core["q2_scalar"],
            "core_folded_gamma_deg":core["gamma_folded_deg"],
            "quadratic_closure_residual_abs":abs(closure_error),
        })
    c135 = next(x for x in rows if x["odd_A"] == 135)
    receipt = {
        "checked_at_actual_host_utc":datetime.now(timezone.utc).isoformat(),
        "scope":result["scope"],
        "verification_kind":"hash, contract identity and stored-number arithmetic only; no independent diagonalization",
        "input_sha256":inputs,
        "contract_status":contract["status"],
        "case_parameters_match_contract":True,
        "stored_quadratic_closure_max_abs_error":max(closure_residuals),
        "independent_cubic_closure_not_attached_in_this_pilot_JSON":True,
        "gamma_full_folded_span_deg":max(x["full_folded_gamma_deg"] for x in rows)-min(x["full_folded_gamma_deg"] for x in rows),
        "gamma_proxy_n5_span_deg":max(x["proxy_n5_gamma_deg"] for x in rows)-min(x["proxy_n5_gamma_deg"] for x in rows),
        "maximum_abs_n5_to_all_Jplus2_gamma_change_deg":max(abs(x["n5_minus_all_Jplus2_gamma_deg"]) for x in rows),
        "maximum_full_minus_n5_gamma_difference_deg":max(x["full_minus_n5_gamma_deg"] for x in rows),
        "n5_saturation_within_Jplus2_range":[min(x["n5_saturation_within_Jplus2"] for x in rows),max(x["n5_saturation_within_Jplus2"] for x in rows)],
        "n5_fraction_of_full_q2_range":[min(x["n5_Jplus2_fraction_of_full_q2"] for x in rows),max(x["n5_Jplus2_fraction_of_full_q2"] for x in rows)],
        "q2_A137_over_A129_at_eB1":rows[-1]["full_q2_unit_core_charge"]/rows[0]["full_q2_unit_core_charge"],
        "A135_q2_odd_core_reduction_fraction":1-c135["q2_odd_over_core"],
        "beta_ratio_is_algebraic_reexpression_of_quadratic_channel_fraction":True,
        "notes":[
            "Full means complete within the declared model space.",
            "A137 P_core_R0 is 0.726660438, outside the approximate 0.77-0.81 range in the task summary.",
            "P_core_R0 includes excited R=0 core states; P_core_ground_R0 is separate.",
            "Near-unity odd/core ratio does not imply isotope-independent total charge collectivity.",
            "The full-E2 eF=0.125 case and source Fig13 replay are not assessed here.",
        ],
        "rows":rows,
    }
    changed=[name for name,digest in inputs.items() if sha(ROOT/name)!=digest]
    assert not changed
    receipt["input_hashes_unchanged_at_end"] = True
    (OUT/"pilot-checks.json").write_text(json.dumps(receipt,indent=2)+"\n")
    buffer=io.StringIO(newline="")
    writer=csv.DictWriter(buffer,fieldnames=list(rows[0]))
    writer.writeheader();writer.writerows(rows)
    (OUT/"pilot-summary.csv").write_text(buffer.getvalue())
    print(json.dumps({k:v for k,v in receipt.items() if k not in ("rows","input_sha256")},indent=2))


if __name__ == "__main__":
    main()
