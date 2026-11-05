"""Read-only algebra probe of the exact parent-computed 129Ba model parameters.

Run with python3 -B; JSON is printed to stdout. There is no fit, source-data
reanalysis, reaction calculation, or physical certification. Source modules
are imported from the shared workspace and their hashes are recorded. The
parent's fixed 11/2 anchor and the reviewer's alternative 9/2 placement are
evaluated and labelled separately.
"""
import sys
sys.dont_write_bytecode = True

import hashlib
import json
import os
from dataclasses import asdict, replace
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
import paired_single_j_rotor as rotor
import paired_single_j_transfer as transfer
import paired_single_j_em as em


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


PARENT_FIT = (
    "outputs/l4/20261105-ba129-model-readiness/"
    "model-fit-free-inertias-C120/energy-calibration.json"
)
FILES = [
    PARENT_FIT,
    "system/scripts/analysis/paired_single_j_rotor.py",
    "system/scripts/analysis/paired_single_j_transfer.py",
    "system/scripts/analysis/paired_single_j_em.py",
    "raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf",
    "raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartII.pdf",
    "raw/papers/gpt/query/20261105-ba129-model-readiness/bucurescu1998-main.pdf",
]
hashes_before = {path: digest(path) for path in FILES}
parent_fit = json.loads((ROOT / PARENT_FIT).read_text())
best = parent_fit["best"]
parameters = best["model_parameters"]
if parent_fit["model_sha256"] != hashes_before[
    "system/scripts/analysis/paired_single_j_rotor.py"
]:
    raise RuntimeError("Parent fit used a different rotor module; reconcile before replay.")
p = rotor.PairedRotorParameters(
    parameters["two_j"], parameters["C_MeV"], parameters["gamma_deg"],
    tuple(parameters["inertias_hbar2_per_MeV"]),
    parameters["lambda_F_MeV"], parameters["Delta_MeV"],
)
anchor_11 = next(
    row for row in best["energy_comparison"]
    if row["twice_I"] == 11 and row["model_ordinal_assumed"] == 0
    and row["model_relative_energy_keV"] == 0
    and row["observed_relative_energy_keV"] == 0
)
reference_9 = next(
    row for row in best["energy_comparison"]
    if row["twice_I"] == 9 and row["model_ordinal_assumed"] == 0
)
dual = replace(
    p, gamma_deg=60 - p.gamma_deg, lambda_F_MeV=-p.lambda_F_MeV,
    inertias_hbar2_per_MeV=(
        p.inertias_hbar2_per_MeV[0],
        p.inertias_hbar2_per_MeV[2],
        p.inertias_hbar2_per_MeV[1],
    ),
)
q = expm(-1j * np.pi / 2 * rotor._spin_matrices(11)[0])
sp = rotor.single_particle_spectrum(11, p.C_MeV, p.gamma_deg)
sd = rotor.single_particle_spectrum(11, dual.C_MeV, dual.gamma_deg)
result = {
    "kind": "model-algebra-audit",
    "input_boundary": (
        "Exact parameters read from the parent energy-calibration.json. "
        "RMS: parent computation, not independently refitted; not user-supplied data."
    ),
    "parent_fit_path": PARENT_FIT,
    "parent_parameter_locator": "/best/model_parameters",
    "parent_RMS_locator": "/best/RMS_residual_keV_excluding_anchor",
    "parent_computed_energy_RMS_keV_excluding_anchor":
        best["RMS_residual_keV_excluding_anchor"],
    "parameters": asdict(p),
    "dual_parameters": asdict(dual),
    "sp_pair_energies_MeV": sp.kramers_pair_energies_MeV.tolist(),
    "sp_negation_residual_MeV": float(np.max(abs(
        sd.hamiltonian_MeV + q @ sp.hamiltonian_MeV @ q.conj().T
    ))),
    "spin_checks": [],
}
original, reflected = {}, {}
for two_I in (9, 11, 13, 15, 17, 19):
    a = original[two_I] = rotor.solve(two_I, p)
    b = reflected[two_I] = rotor.solve(two_I, dual)
    wi = expm(-1j * np.pi / 2 * rotor._spin_matrices(two_I)[0]).conj()
    w = np.kron(wi, q)
    result["spin_checks"].append({
        "two_I": two_I,
        "spectrum_max_difference_keV": float(
            np.max(abs(a.eigenvalues_MeV - b.eigenvalues_MeV)) * 1000
        ),
        "H_covariance_error_MeV": float(np.max(abs(
            b.hamiltonian_product_MeV
            - w @ a.hamiltonian_product_MeV @ w.conj().T
        ))),
        "minimum_eigenvalue_spacing_MeV": float(np.min(np.diff(a.eigenvalues_MeV))),
    })

s = original[11]
a, b = transfer.strengths(s), transfer.strengths(reflected[11])
parent_ex = (
    s.eigenvalues_MeV - s.eigenvalues_MeV[0] + anchor_11["energy_keV"] / 1000
)
# This alternative zero was introduced by this reviewer, not by the parent fit.
reviewer_ex = (
    s.eigenvalues_MeV - original[9].eigenvalues_MeV[0]
    + reference_9["energy_keV"] / 1000
)
windows = {}
for name, ex, anchor, origin, formula in (
    (
        "parent_fixed_11over2",
        parent_ex, anchor_11,
        "Parent fit: fixed first 11/2− at Ex=278.81 keV.",
        "Ex_n = E_n(11/2) - E_0(11/2) + 0.27881 MeV",
    ),
    (
        "reviewer_alternative_9over2",
        reviewer_ex, reference_9,
        "Reviewer-only illustrative placement: fixed first 9/2− at Ex=182.04 keV.",
        "Ex_n = E_n(11/2) - E_0(9/2) + 0.18204 MeV",
    ),
):
    mask = (ex >= 0) & (ex < 2.0)
    windows[name] = {
        "origin": origin,
        "formula": formula,
        "anchor_level_id": anchor["level_id"],
        "anchor_Ex_keV": anchor["energy_keV"],
        "energy_window_MeV": "[0, 2)",
        "states": int(mask.sum()),
        "state_indices_zero_based": np.flatnonzero(mask).tolist(),
        "original_removal_fraction": float(
            a.removal_strengths[mask].sum() / a.removal_sum
        ),
        "dual_removal_fraction": float(
            b.removal_strengths[mask].sum() / b.removal_sum
        ),
    }
result["transfer"] = {
    "complete_I_equals_j_spectrum_size": len(s.eigenvalues_MeV),
    "removal_sum": a.removal_sum,
    "addition_sum": a.addition_sum,
    "dual_removal_sum": b.removal_sum,
    "dual_addition_sum": b.addition_sum,
    "sum_rule_error": max(a.sum_rule_error, b.sum_rule_error),
    "removal_vs_dual_addition_max_error": float(np.max(abs(
        a.removal_strengths - b.addition_strengths
    ))),
    "addition_vs_dual_removal_max_error": float(np.max(abs(
        a.addition_strengths - b.removal_strengths
    ))),
    "windows": windows,
    "parent_minus_reviewer_energy_placement_keV": float(
        (parent_ex[0] - reviewer_ex[0]) * 1000
    ),
    "first_six_states": [{
        "index_zero_based": i,
        "energy_above_first_11over2_keV": float(
            (s.eigenvalues_MeV[i] - s.eigenvalues_MeV[0]) * 1000
        ),
        "parent_fixed_11over2_Ex_keV": float(parent_ex[i] * 1000),
        "reviewer_alternative_9over2_Ex_keV": float(reviewer_ex[i] * 1000),
        "removal": float(a.removal_strengths[i]),
        "dual_removal": float(b.removal_strengths[i]),
        "removal_over_first": float(a.removal_strengths[i] / a.removal_strengths[0]),
        "dual_removal_over_first": float(b.removal_strengths[i] / b.removal_strengths[0]),
    } for i in range(6)],
}
result["unit_EM_checks"] = []
for ii, ff in ((11, 9), (13, 11), (15, 11), (15, 13), (11, 11)):
    x = em.unit_em(original[ii], original[ff])
    y = em.unit_em(reflected[ii], reflected[ff])
    item = {
        "two_Ii": ii, "two_If": ff,
        "unit_E2_B_max_difference": float(np.max(abs(
            x.collective_quadrupole.unit_B - y.collective_quadrupole.unit_B
        ))),
        "unit_j_B_max_difference": float(np.max(abs(
            x.particle_j.unit_B - y.particle_j.unit_B
        ))),
        "relative_E2_j_interference_sign_reversal_error": float(np.max(abs(
            x.collective_quadrupole.rme * x.particle_j.rme.conj()
            + y.collective_quadrupole.rme * y.particle_j.rme.conj()
        ))),
    }
    if ii == ff:
        item["diagonal_Q_sign_reversal_error"] = float(np.max(abs(
            np.diag(x.collective_quadrupole.rme) + np.diag(y.collective_quadrupole.rme)
        )))
        item["diagonal_j_invariance_error"] = float(np.max(abs(
            np.diag(x.particle_j.rme) - np.diag(y.particle_j.rme)
        )))
    result["unit_EM_checks"].append(item)

# Size of the discarded coupling, not a full-Hamiltonian energy correction.
vectors = s.single_particle.eigenvectors
u = (vectors * s.u) @ vectors.conj().T
v = (vectors * s.v) @ vectors.conj().T
uf, vf = np.kron(np.eye(12), u), np.kron(np.eye(12), v)
body = list(rotor._spin_matrices(11))
body[1] *= -1
hr = np.zeros((144, 144), complex)
for ik, jk, inertia in zip(
    body, rotor._spin_matrices(11), p.inertias_hbar2_per_MeV,
):
    R = np.kron(ik, np.eye(12)) - np.kron(np.eye(12), jk)
    hr += R @ R / (2 * inertia)
coupling = s.product_embedding.conj().T @ (
    -uf @ hr @ vf + vf @ hr @ uf
) @ s.product_embedding
result["discarded_Nambu_coupling"] = {
    "two_I": 11,
    "block_spectral_norm_MeV": float(np.linalg.norm(coupling, 2)),
    "first_six_positive_state_coupling_norms_MeV":
        np.linalg.norm(coupling @ s.eigenvectors[:, :6], axis=0).tolist(),
    "interpretation": "Nonzero residuals, not predicted eigenvalue shifts or error bars.",
}
result["sha256"] = hashes_before
result["inputs_unchanged_during_probe"] = all(
    digest(path) == value for path, value in hashes_before.items()
)
result["boundaries"] = [
    "Only the declared positive-energy approximation is checked for isospectrality.",
    "No full Nambu fit, number/gap equation, or DWBA/IBFM operator replay.",
    "The current EM module returns unit tensors, not calibrated B(E2), B(M1), moments or delta.",
    "State matching by energy index is justified here only by nondegenerate spectra.",
]
print(json.dumps(result, indent=2, allow_nan=False))
