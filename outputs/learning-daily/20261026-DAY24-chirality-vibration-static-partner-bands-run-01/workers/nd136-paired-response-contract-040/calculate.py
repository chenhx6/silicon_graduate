"""Actual four-line continuous sensitivity; no counts, covariance or fit supplied."""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = HERE.parent / "nd136-holdout-design-033" / "conditional-ratios.json"
prior = json.loads(SOURCE.read_text(encoding="utf-8"))
pair = prior["primary_comparison"]
order = ["out20", "in20", "out21", "in21"]
lines = []
for spin in (20, 21):
    for role in ("out", "in"):
        row = pair[f"R{spin}"][role]
        lines.append({"id": f"{role}{spin}", "parent": pair[f"R{spin}"]["parent"],
                      "E_gamma_keV": row[0], "I_gamma_printed": row[1],
                      "printed_parenthetical_error": row[2], "error_coverage": None,
                      "assignment": row[3], "endpoint": row[4],
                      "uncertainty_not_used_for_CI": True})
energy = [row["E_gamma_keV"] for row in lines]
a20 = math.log(energy[0] / energy[1])
a21 = math.log(energy[2] / energy[3])
J = [[1, -1, 0, 0], [0, 0, 1, -1], [-1, 1, 1, -1]]
result = {
    "kind": "actual-input-continuous-response-sensitivity-not-new-experiment-or-fit",
    "source_values_from": str(SOURCE.relative_to(ROOT)),
    "source_sha256": prior["source_sha256"],
    "canonical_source": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
    "canonical_claims": ["TH19-D25P-001", "TH19-D25P-005", "TH19-D25P-006"],
    "source_locator": "physical PDF94–95 Table5.1; PDF97 footnote b; PDF77 Fig5.6",
    "source_status": "reuse of verified 028/033 line ledger and canonical; no new full-thesis reading",
    "line_order": order, "lines": lines,
    "nominal_conditional_arithmetic": {
        "R20": pair["R20"]["nominal_ratio"],
        "R21": pair["R21"]["nominal_ratio"],
        "D_R21_over_R20": pair["nominal_R21_over_R20"],
        "not_significance_or_fitted_target": True},
    "multiplicative_response_convention": {
        "f_l": "epsilon_true(E_l)/epsilon_used(E_l)",
        "g_l": "line-specific residual selection/acceptance after any used gate corrections",
        "corrected_numerator": "q_l*f_l*g_l+b_l",
        "b_l": "signed residual additive net-area bias in corrected numerator units, not a universal efficiency",
        "q_l": "N_parent*tau_parent*C_E2*E_l^5*B_l in ideal matched photon-yield interpretation",
        "I_hat_l": "100*(q_l*f_l*g_l+b_l)/Q_hat_373p7",
        "eta_l": "b_l/(q_l*f_l*g_l), requiring positive net numerator for logarithms",
        "rho_l": "ln(f_l)+ln(g_l)+ln(1+eta_l)",
        "log_Rhat_minus_log_Rtrue": "rho_out-rho_in",
        "log_Dhat_minus_log_Dtrue": "-rho_out20+rho_in20+rho_out21-rho_in21"},
    "joint_log_response_jacobian": {
        "outputs": ["lnR20", "lnR21", "lnD"], "matrix": J,
        "covariance_propagation": "Sigma_y = J Sigma_rho J^T for the declared log-residual vector; use full joint primitive Jacobian for correlated count/calibration/gate/background inputs",
        "three_outputs_rank": 2,
        "third_output_is_difference_not_third_independent_constraint": True,
        "one_common_mode": [1, 1, 1, 1],
        "within_parent_common_modes": [[1, 1, 0, 0], [0, 0, 1, 1]],
        "actual_Sigma_rho": None},
    "declared_submodel_only": {
        "f_E": "(E/E_star)^s with one common s and arbitrary common E_star",
        "d_log_Rhat_over_Rtrue_d_s": {"R20": a20, "R21": a21},
        "d_log_Dhat_over_Dtrue_d_s": a21-a20,
        "scope": "exact log response to a common power-law tilt, holding line assignments, energies and other response terms fixed",
        "not_complete_systematics": "Small contrast sensitivity or a large slope required by some hypothetical target cannot exclude general efficiency curvature, line-specific gates or additive background",
        "fitted_s": None},
    "minimum_future_joint_reanalysis_fields": [
        "immutable source/run/line/parent/daughter/assignment and energy-calibration identities, with actual uncertainties/Cov",
        "per-line spectrum/projection and exact gate combination, gate role/width, weighting, event reuse, exposure, detector mask, addback/cuts and angular/conditional acceptance",
        "gross peak areas, fit/ROI model, sideband/background/contaminant components, subtraction/transport coefficients and their joint covariance or likelihood",
        "used efficiency and correction convention, calibration parameter values and full parameter Cov, shared run/detector modes and four-energy Jacobian or full four-energy Cov",
        "line-specific gate/acceptance response parameters or corrections and their cross-line/cross-calibration covariance or joint likelihood",
        "373.7-keV normalizer identity and exact sharing/transformation; retain reference covariance if reconstructing normalized intensities, or provide pre-normalization corrected four yields",
        "full four-line corrected-yield covariance and its relation to primitive covariance (to avoid double counting), including cross-parent entries; distribution/coverage/constraints for printed errors",
        "producer/version, fitted nuisance restrictions, control-data provenance and uncertainty-model validation/coverage; missing fields stay unknown"],
    "not_required_for_these_same_parent_same_E2_ratios": ["measured tau20 or tau21", "tau20 equals tau21", "complete totalBR", "absolute B scale"],
    "not_derived": ["actual CI", "significance", "counts", "numerical covariance", "model fit", "absolute B", "totalBR", "phase", "mode exclusion", "general systematic-error exclusion"],
    "same_day24_only_day25_uncredited_preview": True,
}
# Exact coefficient identities check signs/cancellation, not experimental validity.
assert all(sum(row) == 0 for row in J)
assert all(J[2][k] == J[1][k]-J[0][k] for k in range(4))
assert all(sum(row[k]*mode[k] for k in range(4)) == 0
           for row in J for mode in ([1, 1, 0, 0], [0, 0, 1, 1]))
(HERE / "response-contract.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"R20_tilt_coefficient": a20, "R21_tilt_coefficient": a21,
                  "double_ratio_tilt_coefficient": a21-a20,
                  "coefficient_identities": "verified; not an experimental test"}, indent=2))
