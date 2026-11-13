# -*- coding: utf-8 -*-
import json, hashlib

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

files_to_hash = {
    "sec_3_7_tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-7.tex",
    "ledger_json": "raw/writing/gpt/A130/latex-evidence-ledger/section-3-7.json",
    "research_note": "knowledge/research-notes/a130-rewrite-parity-chirality-and-e1-limits-20261113.md",
    "bib_file": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/new-references-3-7.bib"
}

hashes = {k: {"path": v, "sha256": sha256_file(v)} for k, v in files_to_hash.items()}

receipt = {
  "task_id": "G88",
  "section": "3.7",
  "status": "completed-round2-refinement-submitted-for-parent-acceptance",
  "timestamp": "2026-11-13T12:10:00.000000+00:00",
  "modified_paths": [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-7.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-3-7.json",
    "knowledge/research-notes/a130-rewrite-parity-chirality-and-e1-limits-20261113.md",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/new-references-3-7.bib",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/section-3-7-receipt.json"
  ],
  "items_mapping": {
    "37-1": "Corrected Clebsch-Gordan prefactor to exactly 12/5 = (3/(4pi)) / (5/(16pi)) in eq:3-7-D0-Q0-ratio. Added full mathematical explanation in research note showing that the 8/5 factor in literature arises only after substituting simplified K=0 CG coefficients where CG1^2 / CG2^2 = 2(2I-1)/[3(I-1)], canceling 3 into 8/5[(2I-1)/(I-1)]. Verified exact rational control: I=2 gives 24/5, I=3 gives 4.",
    "37-2": "Corrected operator algebra: for integer spin I (even fermion number), T^2 = +1 and R_y(pi)^2 = +1; for half-integer spin I (odd fermion number), T^2 = -1 and R_y(pi)^2 = -1; in both cases C^2 = T^2 R_y(pi)^2 = (-1)^(4I) = +1. Clarified C does not enforce Kramers degeneracy, but does not rule out degeneracies from other symmetries.",
    "37-3": "Clarified that invariance of the scalar triple product chi_geom under orthogonal spatial reflection proves that this handedness is not a parity-odd order parameter, but does not imply the entire oriented state or three-vector configuration is reflection invariant. Stated T alone also flips chi_geom, and C = T R_y(pi) is the standard convenient body-fixed chiral operation, not the unique possible sign-reversing transformation.",
    "37-4": "Defined q3 = -sqrt(7/2) <(Q2 x Q2)_2 . Q2> strictly as a rank-0 cubic scalar invariant in charge-length units e^3 fm^6, not energy or octupole. Removed overstrong 'strict dynamical decoupling' claims, noting q3 can evolve dynamically in coupled states through wave function changes.",
    "37-5": "Distinguished Bucher et al. (2017) Coulomb excitation direct measurement of E3 RME (0.65(+14/-20) e b^(3/2)) and B(E3) (48(+21/-29) W.u.) with asymmetric errors from the E1 matrix elements that largely rely on prior lifetime/branching ratio data.",
    "37-6": "Framed D0 = D0^macro + D0^micro as a phenomenological liquid-drop + shell decomposition convention, noting terms do not universally have opposite signs. Clarified the SCCM calculation specifically compares proton and neutron dipole contributions (neutron high-j low-K occupancy cancellation). Noted strong E3 does not alone prove a rigid static pear, preserving dynamic octupole vibration alternatives."
  },
  "equation_checks": {
    "clebsch_gordan_prefactor": "(3/(4pi)) / (5/(16pi)) = 12/5. For K=0, (12/5) * [2(2I-1)/(3(I-1))] = (8/5) * [(2I-1)/(I-1)]. Evaluates to 24/5 at I=2, 4 at I=3.",
    "chirality_squared": "C^2 = T^2 R_y(pi)^2 = (-1)^(2I) (-1)^(2I) = (-1)^(4I) = +1 for both integer and half-integer I.",
    "axial_vector_reflection_det": "det(M_axial) = (-1)(-1)(+1) = +1, preserving chi_geom under spatial orthogonal reflection."
  },
  "file_hashes": hashes
}

with open("outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/section-3-7-receipt.json", "w", encoding="utf-8") as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print("Successfully written updated section-3-7-receipt.json")
