# -*- coding: utf-8 -*-
import json, hashlib

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

files_to_hash = {
    "sec_3_4_tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-4.tex",
    "ledger_json": "raw/writing/gpt/A130/latex-evidence-ledger/section-3-4.json",
    "research_note": "knowledge/research-notes/a130-rewrite-angular-convention-reference-20261113.md",
    "runtime_receipt": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/runtime-receipt.json",
    "parent_runtime_check": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/parent-runtime-check.json"
}

hashes = {k: {"path": v, "sha256": sha256_file(v)} for k, v in files_to_hash.items()}

receipt = {
  "task_id": "G88",
  "section": "3.4",
  "status": "completed-post-t17-refinement-submitted-for-parent-acceptance",
  "timestamp": "2026-11-13T11:25:00.000000+00:00",
  "t17_audit_integration": {
    "audit_reference": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/T17/ (correction.tex and report.json)",
    "audit_status": "accepted-and-integrated",
    "dimensional_correction": "H_coll = R_perp^2 / (2 J_perp) = hbar^2 (mathcalI_perp - j_perp)^2 / (2 J_perp) with R_perp having action units and mathcalI, j being dimensionless; removed redundant hbar^2 multiplying R_perp^2 / (2 J_perp).",
    "axial_symmetry_clarification": "Shape redundancy constraint R_3 = 0 expresses absence of independent collective shape rotation, which does not imply microscopic J_parallel must be zero for arbitrary many-body systems.",
    "energy_spacing_distinction": "Distinguished exact fixed-K bandhead spacing hbar^2 (K+1) / J_perp from large-K precession frequency hbar^2 K / J_perp^(eff).",
    "rpa_frame_and_adiabatic_condition": "omega_wob = omega_prec - omega_rot is the axially symmetric small-amplitude RPA frame relation; replacing dynamic frequency-dependent effective inertia with static cranking inertia requires the adiabatic condition.",
    "center_node_in_reflection_symmetric_potential": "Clarified that in any 1D reflection-symmetric potential V(-x) = V(x), any reflection-odd eigenstate has psi(0) = 0, which is not unique to harmonic potentials; symmetric anharmonic terms (like x^4) do not eliminate the center node. Absence of a node occurs only when reflection symmetry itself is broken, or when observing a marginalized/projected distribution.",
    "m1_charge_type_operator_pairing": "Synchronized with Section 5.9: charge-type operator M_S(M1) = M_mu(M1)/c (units e fm) pairs with photon momentum factor E_gamma/(hbar c); conventional magnetic moment operator M_mu pairs with E_gamma/hbar, without extraneous c^2 factor."
  },
  "modified_paths": [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-4.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-3-4.json",
    "knowledge/research-notes/a130-rewrite-angular-convention-reference-20261113.md",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/runtime-receipt.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json"
  ],
  "file_hashes": hashes
}

with open("outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json", "w", encoding="utf-8") as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print("Successfully written updated outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json")
