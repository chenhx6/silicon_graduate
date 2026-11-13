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
  "status": "completed-round2-refinement-submitted-for-parent-acceptance",
  "timestamp": "2026-11-13T12:20:00.000000+00:00",
  "modified_paths": [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-4.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-3-4.json",
    "knowledge/research-notes/a130-rewrite-angular-convention-reference-20261113.md",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/runtime-receipt.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json"
  ],
  "items_mapping": {
    "34-1": "Corrected wobbling frequency formula units: for dimensionless I and physical J, frequency is omega_wob = sqrt[(hbar I/J_y - omega_rot)(hbar I/J_z - omega_rot)] and energy is hbar omega_wob = sqrt[(hbar^2 I/J_y - hbar omega_rot)(hbar^2 I/J_z - hbar omega_rot)], avoiding mixing frequency and energy dimensions. Referenced canonical Section 3.2.",
    "34-2": "Separated parameter evolution along a spin sequence from actual time evolution. Removed comparison of rearrangement rate with oscillation period. Formulated isolated stable small-amplitude normal modes, referencing Section 3.6 for coupled harmonic RPA modes.",
    "34-3": "Clarified that level energies and relative branching ratios alone do not yield absolute transition strengths; stated conditional lack of absolute data (lifetimes or Coulomb excitation/absolute RME) rather than asserting lifetimes as a universal prerequisite.",
    "34-4": "Clarified that 1/I is an asymptotic large-I limit with fixed parameters, not universal across all spin domains. Explicitly stated that M1 strength is not universally quenched even in frozen alignment, depending on magnetic operator structure, g factors, and microscopic core polarization (Frauendorf 2014 QTR limitations).",
    "34-5": "Broadened theoretical model criteria: judgment can rely on self-consistent effective phenomenological models (IBFM, PRM) as well as microscopic frameworks. Stated that linear polarization P gives complementary electric/magnetic character, not direct level parity, and same-event DCO/P are not automatically statistically independent.",
    "34-6": "Designated E_gamma/(hbar c) as the photon wave number k = q = E_gamma/(hbar c). Preserved T17 finite-K, R units, axial gauge redundancy R_3 = 0, and RPA frame relation omega_wob = omega_prec - omega_rot. In 1D reflection-symmetric potentials, clarified that symmetric anharmonicity alone does not remove the central node of odd eigenstates; finite-spin projected/marginalized distributions require specific definitions."
  },
  "file_hashes": hashes
}

with open("outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json", "w", encoding="utf-8") as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print("Successfully written updated outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/receipt.json (round 2)")
