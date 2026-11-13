# -*- coding: utf-8 -*-
import json, hashlib

tex_path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-4.tex"
with open(tex_path, "rb") as f:
    tex_sha256 = hashlib.sha256(f.read()).hexdigest()

ledger = {
  "section_id": "3.4",
  "status": "submitted-for-parent-acceptance",
  "worker": "G88 Gemini Tiered/high; revised per T17 audit and parent feedback",
  "recorded_at": "2026-11-13T11:20:00.000000+00:00",
  "canonical_paths": {
    "tex": tex_path,
    "tex_sha256": tex_sha256
  },
  "sources": [
    {
      "source_id": "shimizu-2005-high-k-precession",
      "canonical_source": "Y. R. Shimizu, M. Matsuzaki, K. Matsuyanagi, Phys. Rev. C 72, 014306 (2005)",
      "source_page": "knowledge/sources/shimizu-2005-high-k-precession.md",
      "raw_file": "raw/papers/gpt/query/20261113-A130-precession-limits/shimizu-matsuzaki-matsuyanagi-2005-nucl-th-0412074v2.pdf",
      "raw_sha256": "6566edd91dc5765a21241ac553f599faf0037d1cadf4113edbe1d969645e97c7",
      "doi": "10.1103/PhysRevC.72.014306",
      "arxiv": "nucl-th/0412074v2",
      "actual_read_pages": "arXiv preprint PDF pp. 2–3 (Section II, Eqs.(1)–(11)), PDF pp. 5–6 (Section III B, Eqs.(32)–(39))",
      "archive_required": True
    },
    {
      "source_id": "lawrie-2020-tilted-precession-wobbling",
      "canonical_source": "E. A. Lawrie, O. Shirinda, C. M. Petrache, Phys. Rev. C 101, 034306 (2020)",
      "source_page": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
      "raw_file": "raw/papers/2020_Lawrie et al_Tilted precession and wobbling in triaxial nuclei.pdf",
      "raw_sha256": "777f935b0266fed8a9d9f2e1cc1f72995c84dd83e27ca1f5377ab2785b2ec405",
      "doi": "10.1103/PhysRevC.101.034306",
      "actual_read_pages": "PDF pp. 2–4 (Sec. II, Eqs.(1)–(16), Figs.1–4), pp. 6–8 (Sec. III, Eqs.(23)–(34), Table I, Fig.9), pp. 9–11 (Sec. IV, Figs.10–11 and Summary)",
      "archive_required": True
    },
    {
      "source_id": "frauendorf-2014-transverse-wobbling",
      "canonical_source": "S. Frauendorf, F. Dönau, Phys. Rev. C 89, 014322 (2014)",
      "source_page": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "raw_file": "raw/papers/2014_Frauendorf_Dönau_Transverse wobbling.pdf",
      "raw_sha256": "36794ee1308adc1b34206ccdbf62353d6e79b3b485979e78709fd31efe5f57e3",
      "doi": "10.1103/PhysRevC.89.014322",
      "actual_read_pages": "PDF pp. 1–2, 6–10 (Eqs.(11)–(24), frozen alignment and asymptotic B(E2) scaling)",
      "archive_required": True
    },
    {
      "source_id": "lv-2022-evidence-against-wobbling-135pr",
      "canonical_source": "B. F. Lv et al., Phys. Lett. B 827, 136840 (2022)",
      "source_page": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
      "raw_file": "raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf",
      "raw_sha256": "4b87c540bf9da5141fa88ef8f00859162cb08918d56a5da74726c7537df5e26b",
      "doi": "10.1016/j.physletb.2022.136840",
      "actual_read_pages": "PDF pp. 1–5 (lifetime measurement, B(E2) analysis and competing soft-core interpretations)",
      "archive_required": True
    },
    {
      "source_id": "petrache-2006-near-degenerate-chiral-misinterpretation",
      "canonical_source": "C. M. Petrache, G. B. Hagemann, I. Hamamoto, K. Starosta, Phys. Rev. Lett. 96, 112502 (2006)",
      "source_page": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
      "raw_file": "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf",
      "raw_sha256": "ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f",
      "doi": "10.1103/PhysRevLett.96.112502",
      "actual_read_pages": "PDF pp. 1–4 (core shape fluctuation and misinterpretation of nearly degenerate companion bands)",
      "archive_required": True
    },
    {
      "source_id": "nomura-2022-questioning-wobbling-ibfm",
      "canonical_source": "K. Nomura, C. M. Petrache, Phys. Rev. C 105, 024320 (2022)",
      "source_page": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "raw_file": "raw/papers/2022_Nomura et al_Questioning the wobbling interpretation of low-spin bands in γ -soft nuclei within the interacting b.pdf",
      "raw_sha256": "e61e3dd6fe5e67fb55543f3a136c7cce0fda98ad01f112d81d5eef70b613465f",
      "doi": "10.1103/PhysRevC.105.024320",
      "actual_read_pages": "PDF pp. 1–8 (IBFM calculations of gamma-soft odd-A nuclei reproducing low-spin bands without triaxial wobbling)",
      "archive_required": True
    },
    {
      "source_id": "lange-kumar-hamilton-1982-multipole-admixtures",
      "canonical_source": "J. Lange, K. Kumar, J. H. Hamilton, Rev. Mod. Phys. 54, 119 (1982)",
      "source_page": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
      "raw_file": "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf",
      "raw_sha256": "ed925a0577a9257903806acd209c1db707529e86a5bfd9a301a83d597bf78ffb",
      "doi": "10.1103/RevModPhys.54.119",
      "actual_read_pages": "PDF pp. 119–125 (formulation of angular distribution, DCO and multipole mixing ratio delta)",
      "archive_required": True
    },
    {
      "source_id": "book-bohr-mottelson-nuclear-structure-vol2",
      "canonical_source": "A. Bohr, B. R. Mottelson, Nuclear Structure, Vol. II: Nuclear Deformations (Benjamin, 1975; World Scientific, 1998)",
      "source_page": "knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md",
      "doi": "10.1142/3530",
      "actual_read_pages": "Vol. II Chapter 4 (high-spin rotational bands, wobbling motion, and high-K states)",
      "archive_required": True
    }
  ],
  "claims_and_derivations": [
    {
      "id": "3.4-P01",
      "kind": "definition-and-model-derivation",
      "claim": "In the strong-coupling adiabatic model for an axially symmetric shape rotor, the coordinate about the symmetry axis (3-axis) is redundant, expressed by constraint R_3 = 0 (no collective mass rotation about shape symmetry axis). This does not imply that for any arbitrary microscopic axially symmetric many-body system the cranking response or effective inertia about the symmetry axis must be zero. For physical core angular momentum R_perp = hbar (mathcalI_perp - j_perp) and dimensionless I, K, j, collective Hamiltonian is H_coll = R_perp^2 / (2 J_perp) = hbar^2 (mathcalI_perp - j_perp)^2 / (2 J_perp). Neglecting off-diagonal Coriolis mixing and absorbing constant terms gives E_K(I) - E_intr = hbar^2 [I(I+1) - K^2] / (2 J_perp) for I >= K. Bandhead spin I_bandhead = K holds in this model under allowed signature/parity conditions; observed bandhead can differ in real nuclei.",
      "sources": ["shimizu-2005-high-k-precession", "book-bohr-mottelson-nuclear-structure-vol2"],
      "locator": "Shimizu 2005 preprint PDF p. 3 Eq.(9); BM-II p. 190; T17 correction; manuscript Eqs.(3-4-high-K-H)-(3-4-high-K-spectrum)",
      "conditions": "Adiabatic strong-coupling, K > 1/2 Coriolis decoupling neglected; intrinsic state fixed; not universal to non-adiabatic or triaxial systems."
    },
    {
      "id": "3.4-P02",
      "kind": "task-local-derivation",
      "claim": "The laboratory adjacent-spin transition energy in a fixed-K band is Delta E_lab(I -> I-1) = hbar^2 I / J_perp, with the first transition above bandhead Delta E_lab(K+1 -> K) = hbar^2 (K+1) / J_perp, distinguishing from large-K precession hbar^2 K / J_perp^(eff).",
      "sources": ["shimizu-2005-high-k-precession"],
      "locator": "Shimizu 2005 preprint PDF p. 3 Eqs.(10)-(11); T17 correction; manuscript Eqs.(3-4-lab-spacing)-(3-4-first-lab-spacing)",
      "conditions": "Fixed intrinsic K; delta I = 1 laboratory transitions; ideal constant moment of inertia."
    },
    {
      "id": "3.4-P03",
      "kind": "model-relation-and-conceptual-distinction",
      "claim": "The small-amplitude wobbling frequency omega_wob in the co-rotating intrinsic frame at fixed spin I is conceptually and operationally distinct from the cross-spin energy spacing Delta E_lab in the laboratory frame. In the axially symmetric RPA framework (Shimizu et al. 2005), the two are rigorously connected by omega_wob = omega_prec - omega_rot, where omega_prec = hbar K / J_perp^(eff)(omega_prec) is the lab precession frequency and omega_rot is the frame cranking frequency. This reference-frame relation stems from axially symmetric small-amplitude RPA and does not require taking the adiabatic limit upfront; the adiabatic approximation further reduces J_perp^(eff) to static cranking inertia.",
      "sources": ["shimizu-2005-high-k-precession"],
      "locator": "Shimizu 2005 preprint PDF pp. 2-3 Eqs.(5)-(8); PDF pp. 5-6 Sec. III B Eqs.(32)-(39); T17 correction; manuscript Eq.(3-4-shimizu-connection)",
      "conditions": "Axially symmetric limit about rotation axis (J_y = J_z = J_perp) in RPA; does not imply generic triaxial TW is isomorphic to high-K precession, nor that they are disconnected."
    },
    {
      "id": "3.4-P04",
      "kind": "author-interpretation-and-model-geometry",
      "claim": "In the tilted precession (TiP) model (Lawrie et al. 2020), 3D rotation in odd-A triaxial nuclei arises from orientation competition between valence quasiparticle alignment along a preferred geometric principal axis and core rotation about the maximum-inertia axis. This tilts the stationary rotation axis into a principal plane (e.g. s-m plane). Total angular momentum precesses about this tilted direction; bands with larger tilt angles are TiP bands.",
      "sources": ["lawrie-2020-tilted-precession-wobbling"],
      "locator": "Lawrie 2020 PRC 101, 034306 pp. 2-3 Eqs.(1)-(6), Figs.1-3; p. 5 Sec. III, Eqs.(19)-(22); manuscript Sec. 3.4.2",
      "conditions": "Particle-rotor coupling framework with frozen j in comparison; model mechanism, not directly observable classical time trajectory; no universal gamma or spin boundaries."
    },
    {
      "id": "3.4-P05",
      "kind": "model-domain-and-approximation-condition",
      "claim": "Harmonic wobbling is an extreme small-amplitude approximation to 3D rotation / TiP, valid only when the transverse angular momentum components satisfy f(n, I) << 1 and the excitation energies and transition probabilities scale linearly with phonon number n. For typical transverse coupling parameters in 135Pr and 105Pd, f remains large (f1 > 0.45), meaning the strict harmonic wobbling approximation does not automatically hold.",
      "sources": ["lawrie-2020-tilted-precession-wobbling"],
      "locator": "Lawrie 2020 PRC 101, 034306 pp. 4, 6-8 Eqs.(15)-(16), (32)-(34), Table I, Fig.9; manuscript Sec. 3.4.2 & 3.4.4",
      "conditions": "Calculated within QTR model with stated parameters and frozen j; energy decrease Delta E(I) is not a unique or universal criterion for TiP or wobbling."
    },
    {
      "id": "3.4-P06",
      "kind": "quantum-geometric-distinction",
      "claim": "In a 1D coordinate x, if effective H is invariant under reflection x -> -x (V(-x) = V(x)), any reflection-odd eigenstate strictly has psi(0) = 0; this holds for any 1D reflection-symmetric potential, not only harmonic oscillators. Symmetric anharmonic terms do not destroy this node. In finite-I nuclear states, the absence of a node occurs only when reflection symmetry itself is broken (e.g. by odd-parity terms, Coriolis cross terms, or mixing with reflection-even channels) or when observing a marginalized/projected distribution. Transverse curvature differences do not break local reflection symmetry. Angular reflection, spatial parity, and signature are distinct operations.",
      "sources": ["lawrie-2020-tilted-precession-wobbling", "book-bohr-mottelson-nuclear-structure-vol2"],
      "locator": "T17 correction; parent feedback; manuscript Sec. 3.4.3",
      "conditions": "Finite-spin quantum mechanics; theoretical probability density is not directly measurable in real-time experiments; physical testing proceeds via observable energies and EM transitions."
    },
    {
      "id": "3.4-P07",
      "kind": "model-applicability-and-competing-mechanisms",
      "claim": "Small-amplitude wobbling phonon tagging requires localization in the quadratic expansion basin where higher-order terms are small. It does not require all three inertias to be distinct (high-K axisymmetric limit has local expansion), nor that j never reorients. Competing mechanisms for companion bands with smoothly varying Delta E(I) include: signature partner bands (alpha = +- 1/2), quasiparticle configuration crossings, and dynamic coupling to a gamma-soft core.",
      "sources": ["petrache-2006-near-degenerate-chiral-misinterpretation", "lv-2022-evidence-against-wobbling-135pr", "nomura-2022-questioning-wobbling-ibfm"],
      "locator": "Petrache 2006 PRL 96, 112502; Lv 2022 PLB 827, 136840; Nomura 2022 PRC 105, 024320; manuscript Sec. 3.4.4",
      "conditions": "Transitional A approx 130 nuclei with shallow triaxial minima; competing interpretations require case-by-case data analysis."
    },
    {
      "id": "3.4-P08",
      "kind": "spectroscopic-analysis-and-measurement-boundary",
      "claim": "Multi-dimensional spectroscopic criteria: (1) DCO ratio R_DCO(delta) is a rational function of two quadratics; solving it yields two real roots, a degenerate root, or no real root (excluding poles where denominator vanishes). Linear polarization P aids in parity distinction but does not guarantee unique disambiguation under experimental uncertainties. (2) delta(E2/M1) is rigorously defined as radiation emission amplitude ratio. Using charge-type magnetic operator M_S(M1) = M_mu(M1)/c (units e fm) pairs with photon factor E_gamma/(hbar c), consistent with Section 5.9; using M_mu(M1) (units mu_N) pairs with E_gamma/hbar, without extra c^2. (3) Interband B(E2) ~ 1/I and strong M1 suppression are asymptotic limits of idealized harmonic models, not universal laws. (4) Scientific confirmation relies on forward joint prediction of self-consistent models against multi-observable networks and critical falsification of competing hypotheses.",
      "sources": ["lange-kumar-hamilton-1982-multipole-admixtures", "frauendorf-2014-transverse-wobbling", "book-bohr-mottelson-nuclear-structure-vol2"],
      "locator": "Lange et al. 1982 RMP 54, 119; Frauendorf 2014 PRC 89, 014322; T17 correction; manuscript Sec. 3.4.5, Eq.(3-4-delta-def)",
      "conditions": "Oriented nuclear radiation theory; SI and conventional magnetic operator definitions."
    }
  ],
  "integration_boundary": "Only Section 3.4 Tex, section-3-4.json, research-note a130-rewrite-angular-convention-reference-20261113.md and G88/receipt.json were modified per T17 audit and parent controller directives. No other chapters, shared Bib, or git state touched."
}

with open("raw/writing/gpt/A130/latex-evidence-ledger/section-3-4.json", "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print("Successfully written revised section-3-4.json")
