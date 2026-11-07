---
type: research-ledger
title: "Ledger of Primary Sources, Page Ranges, and Evidence Verification Across Six Mass Regions"
task: "Six-Region Triaxial/Collective Synthesis, Counterexamples, and Cross-Region Transfer"
created: 2026-11-07
updated: 2026-11-07
worker: "R5"
location: "outputs/l3/20261107-isomer-cross-region/six-regions/"
status: complete
---

# Ledger of Primary Sources, Page Ranges, and Evidence Verification Across Six Mass Regions

## 1. Overview and Verification Summary

This ledger documents the audit trail, bibliographic identifiers, local artifact paths, exact page ranges, SHA-256 integrity hashes, and verified physical findings for primary benchmark publications and counterexamples across the six nuclear mass regions ($A \approx 60, 80, 100, 130, 160, 190$).

All newly acquired items are cataloged in `raw/papers/gpt/query/20261107-six-region-transfer/manifest.json`. No existing source pages, synthesis notes, system files, or BibTeX baselines have been modified.

---

## 2. Six-Region Primary Evidence Audit Matrix

### 2.1 Region $A \approx 60$: Proposed Chirality in $^{60}\text{Ni}$
- **Citation**: J. Peng and Q. B. Chen, "Possible chiral doublets in $^{60}$Ni", *Physics Letters B* **793** (2019) 303–307.
- **DOI**: `10.1016/j.physletb.2019.04.065` | **arXiv**: `1904.12100v1`
- **Source Note**: `knowledge/sources/peng-2019-possible-chiral-doublets-60ni.md` (Newly created, `archive_required: true`)
- **Local Artifact**: `raw/papers/gpt/query/20261107-six-region-transfer/arxiv-1904-12100/source/Ni60.tex`
- **Raw SHA-256**: `835bbcd55b8d3df189955c5e9cf07933896aa5e98871302f5e77d235f6632360`
- **Tar Artifact SHA-256**: `c412378f7c6360e09bb49f6513eae187b859b4337e64a55df4639cf54198a77d` (857,538 bytes)
- **Exact Page / Text Locators**:
  - pp. 303–304 (`Ni60.tex` lines 74–82, 231–245): 4-quasiparticle configuration $\pi(1f_{7/2})^{-1}(2p_{3/2})^1 \otimes \nu(1g_{9/2})^1(1f_{5/2})^{-1}$; constrained TAC-CDFT gives bandhead $\beta=0.27, \gamma=19^\circ$; PRM adopts $\beta=0.27, \gamma=22^\circ$, $\mathcal{J}_0=9.0\ \hbar^2/\text{MeV}$, $\xi=0.98$.
  - pp. 304–305 (`Ni60.tex` lines 310–335, Fig. 2): Root-mean-square angular momentum projections along $s, i, l$ axes demonstrating 3D aplanar orientation.
  - pp. 305–306 (`Ni60.tex` lines 340–395, Fig. 4): Azimuthal plots $\mathcal{P}(\theta, \varphi)$ proving planar rotation at $I=9-11\hbar$, chiral vibration at $I=12\hbar$, static chirality at $I=13-14\hbar$ with two symmetric off-plane peaks at $\varphi \approx \pm 60^\circ$, and secondary vibration at $I=15\hbar$.
- **Audit Verdict**: Peng & Chen 2019 is a multi-j PRM and constrained TAC-CDFT theoretical candidate, not an experimental confirmation of static chirality. The theoretical calculation indicates that 4-quasiparticle cross-shell intruder excitation provides an open model pathway for aplanar rotation in A ≈ 60, but empirical validation remains an open experimental question; theory predictions must not be represented as confirmed physical observations.

### 2.2 Region $A \approx 80$: Candidate Chiral-Wobbler in $^{74}\text{Br}$
- **Citation**: R. J. Guo et al., "Evidence for Chiral Wobbler in Nuclei", *Physical Review Letters* **132**, 092501 (2024); S. Frauendorf, "First evidence for chiral wobbling of triaxial nuclei", *Nuclear Science and Techniques* **35**, 123 (2024).
- **DOI**: `10.1103/PhysRevLett.132.092501` and `10.1007/s41365-024-01478-2`
- **Source Note**: `knowledge/sources/guo-2024-chiral-wobbler-74br.md` (Existing, re-read and audited)
- **Local Artifacts**:
  - `raw/papers/2024_Guo et al_Evidence for Chiral Wobbler in Nuclei.pdf` (SHA-256: `1783B784C3843E15DE39406182613757F9C3B928A2791E45A7D650F117EA4333`)
  - `raw/papers/2024_Frauendorf_First evidence for chiral wobbling of triaxial nuclei.pdf` (SHA-256: verified local copy)
- **Exact Page Locators**:
  - PRL pp. 1–3: Level scheme of $^{74}\text{Br}$ showing three positive-parity bands (B1, B2, B3) with $\pi g_{9/2} \otimes \nu g_{9/2}$; reaction $^{58}\text{Ni}(^{19}\text{F}, 2p1n)^{74}\text{Br}$ at 74 MeV.
  - PRL pp. 3–4, Table I: DSAM lifetimes for states in Band 3 yielding enhanced $B(E2)$ values connecting to Band 1, with mixing ratios $\delta$ varying by spin. (Note: fourth band B4 is predicted by TPSM, not identified in experiment).
  - NST review pp. 1–3: S. Frauendorf's theoretical discussion on the coexistence of chiral rotation and wobbling motion.
- **Audit Verdict**: Disproves the regional assertion that $A \approx 80$ wobbling is "forbidden / extremely weak", establishing a candidate chiral-wobbler.

### 2.3 Region $A \approx 100$: Transverse Wobbling in $^{105}\text{Pd}$
- **Citation**: J. Timár et al., "Experimental Evidence for Transverse Wobbling in $^{105}$Pd", *Physical Review Letters* **122**, 062501 (2019).
- **DOI**: `10.1103/PhysRevLett.122.062501`
- **Source Note**: `knowledge/sources/timar-2019-transverse-wobbling-105pd.md` (Existing, re-read and audited)
- **Local Artifact**: `raw/papers/2019_Timár et al_Experimental Evidence for Transverse Wobbling in Pd 105.pdf`
- **Raw SHA-256**: `3948CF32712A400AA8DF0AEE489EBEBD89DF7480508BDDC60156A359ED322909`
- **Exact Page Locators**:
  - PRL pp. 1–2: Reaction $^{96}\text{Zr}(^{13}\text{C}, 4n)^{105}\text{Pd}$ at 55 MeV, EUROBALL IV array; negative-parity bands A and B based on $\nu h_{11/2}$.
  - PRL pp. 2–3, Table I: DCO ratios and linear polarization asymmetry establishing $|\delta| \gg 1$ ($E2$ dominance) for $\Delta I = 1$ Band B $\to$ Band A transitions.
  - PRL pp. 3–4, Fig. 2: Wobbling energy $E_{\text{wob}}(I)$ decreasing from 610 keV at $17/2^-$ to 430 keV at $23/2^-$, confirming transverse wobbling signature.
- **Audit Verdict**: Disproves the blanket assertion that $A \approx 100$ wobbling is "strictly forbidden".

### 2.4 Region $A \approx 130$: Two-Phonon Wobbling Dispute in $^{135}\text{Pr}$
- **Citation**:
  1. Discovery claim: N. Sensharma et al., "Two-phonon wobbling in $^{135}$Pr", *Physics Letters B* **792** (2019) 170–174.
  2. Counter-evidence: B. F. Lv et al., "Evidence against the wobbling nature of low-spin bands in $^{135}$Pr", *Physics Letters B* **824** (2022) 136840.
- **DOIs**: `10.1016/j.physletb.2019.03.039` and `10.1016/j.physletb.2021.136840`
- **Source Notes**: `knowledge/sources/sensharma-2019-two-phonon-wobbling-135pr.md` and `knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md` (Both re-read and cross-checked)
- **Local Artifacts**:
  - `raw/papers/2019_Sensharma et al_Two-phonon wobbling in 135Pr.pdf`
  - `raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf`
- **Exact Page Locators**:
  - Sensharma PLB pp. 171–173, Table 1, Figs. 1–3: Observed TW2 $\to$ TW1 transitions at 450.2, 550.5, 517.1 keV; claimed large $|\delta|$ from DCO-like ratios and harmonic energy scaling $E_{\text{wob}}(n_\omega=2) \approx 2 E_{\text{wob}}(n_\omega=1)$.
  - Lv PLB 824 pp. 2–4, Table 1: High-statistics JUROGAM II polarimetry and angular correlation ratios extract multipole mixing ratios with $|\delta| < 1$:
    - 747.3 keV: $P = 0.04^{+0.08}_{-0.13}, R_{\text{ac}} = 0.37(4), \delta = -0.47^{+0.09}_{-0.22}$
    - 813.2 keV: $P = -0.03^{+0.05}_{-0.12}, R_{\text{ac}} = 0.48(6), \delta = -0.37^{+0.10}_{-0.14}$
    - 755.1 keV: $P = -0.07^{+0.09}_{-0.10}, R_{\text{ac}} = 0.50(6), \delta = -0.31^{+0.10}_{-0.13}$
    - 450.2 keV: $R_{\text{ac}} = 0.49(4), \delta = -0.38(9)$
  - Result: Dominant $M1$ character ($M1$ fraction $1/(1+\delta^2) \approx 80-87\%$), providing experimental counter-evidence against the wobbling phonon interpretation.
- **Audit Verdict**: Refutation is based on experimental multipole mixing ratios ($M1$ dominance) measured with the JUROGAM II array in PLB 824 (2022) 136840. The previous invented citation 'PRL 128, 242503' and uniform delta <= 0.15 / 98% M1 assertions are completely absent and formally retracted; the actual experimental data feature transition-dependent asymmetric error bars (e.g. delta(747.3) = -0.47(+0.09/-0.22)).

### 2.5 Region $A \approx 160$: Dual Deformation Regimes in Rare-Earth Odd-Odd Nuclei
- **Citation**:
  1. Normal-deformed odd-odd: Z.-H. Zhang, "Investigation of the two-quasiparticle bands in the doubly-odd nucleus $^{166}$Ta using a particle-number conserving cranked shell model", *Sci. China PMA* **59**, 682012 (2016) [`1606.00573`].
  2. TSD wobbler benchmark: S. W. Ødegård et al., *Phys. Rev. Lett.* **86**, 5866 (2001); D. R. Jensen et al., *Phys. Rev. Lett.* **89**, 142503 (2002).
- **Source Notes**:
  - `knowledge/sources/zhang-2016-two-quasiparticle-bands-166ta.md` (Newly created, `archive_required: true`)
  - `knowledge/sources/odegard-2001-evidence-wobbling-163lu.md` (Existing)
  - `knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md` (Existing)
- **Local Artifacts**:
  - `raw/papers/gpt/query/20261107-six-region-transfer/arxiv-1606-00573/source/166Ta.tex` (SHA-256: `81fb0e20b64b6bfb770636b0c9eef3ae6648103d5c2112d749bcac34f0b09e88`)
  - `raw/papers/2001_Ødegård et al_Evidence for the Wobbling Mode in Nuclei.pdf`
  - `raw/papers/2002_Jensen et al_Evidence for Second-Phonon Nuclear Wobbling.pdf`
- **Exact Page Locators**:
  - Zhang SCPMA pp. 1–8 (`166Ta.tex` lines 60–75, 230–310): PNC-CSM adopts $\varepsilon_2 = 0.192, \varepsilon_4 = -0.0045$, and **assumes axial symmetry** ($\gamma = 0^\circ$). Reproduces moments of inertia and alignments without refitting, consistent with axial prolate geometry. Chirality is absent in normal deformation.
  - Ødegård PRL pp. 5866–5869 & Jensen PRL pp. 142503-1–4: Triaxial superdeformed minimum ($\varepsilon_2 \approx 0.38, \gamma \approx 20^\circ$) hosts verified 1-phonon and 2-phonon wobbling in $^{163}\text{Lu}$. No chiral doublet bands have been reported in odd-odd TSD bands.
- **Audit Verdict**: Zhang 2016 adopts an axially symmetric deformed core (gamma = 0 deg) as an input model assumption of the PNC-CSM Hamiltonian (Eq. eq:H_CSM). The reproduction of experimental moments of inertia under this axial assumption demonstrates that axial geometry suffices to describe observed normal-deformed sequences, but an axial model assumption cannot be used as empirical proof to exclude triaxiality across the entire A ≈ 160 region or in normal-deformed states. Chirality in odd-odd systems under high-spin TSD conditions remains experimentally unobserved.

### 2.6 Region $A \approx 190$: $^{187}\text{Au}$ Dispute & Oblate Chirality in $^{194-200}\text{Tl}$
- **Citation**:
  1. Wobbling claim: N. Sensharma et al., "Longitudinal Wobbling Motion in $^{187}$Au", *Phys. Rev. Lett.* **124**, 052501 (2020).
  2. Wobbling counter-evidence: S. Guo et al., "Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei", *Phys. Lett. B* **828**, 137010 (2022).
  3. Oblate chirality across isotopes: S. Jehangir et al., "High-Spin Doublet Band Structures in odd-odd $^{194-200}$Tl isotopes", *Eur. Phys. J. A* **56**, 206 (2020) [`2007.12347`].
- **DOIs**: `10.1103/PhysRevLett.124.052501`, `10.1016/j.physletb.2022.137010`, `10.1140/epja/s10050-020-00206-9`
- **Source Notes**:
  - `knowledge/sources/jehangir-2020-high-spin-doublet-bands-194-200tl.md` (Newly created, `archive_required: true`)
  - `knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md` (Existing, re-read)
  - `knowledge/sources/guo-2022-low-spin-wobbling-187au.md` (Existing, re-read)
- **Local Artifacts**:
  - `raw/papers/gpt/query/20261107-six-region-transfer/arxiv-2007-12347/source/194_200Tl_v21.tex` (SHA-256: `8b1cb723cdd74da061061156e81cf4627051c6696f4d22edabbd5e8b27cdbf14`)
  - `raw/papers/2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf`
  - `raw/papers/2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei3.pdf`
- **Exact Page Locators**:
  - Sensharma PRL pp. 1–5: Longitudinal wobbler claim based on increasing $E_{\text{wob}}(I)$ in $^{187}\text{Au}$.
  - Guo PLB pp. 1–6: Demonstration of dual-root ambiguity in $\delta$; small-$|\delta|$ solution ($M1$) explains the data as tilted axis precession.
  - Jehangir EPJA pp. 1–9 (`194_200Tl_v21.tex` Section 2, Eq. (2), Table Tab:Tcr, Figs. 1–10): Active, uncommented Table Tab:Tcr in author TeX source yields explicit triaxial parameters: beta = 0.178, gamma = 30 deg for 194Tl; beta = 0.168, gamma = 29 deg for 196Tl; beta = 0.157, gamma = 31 deg for 198Tl; beta = 0.157, gamma = 34 deg for 200Tl (commented-out table versions are explicitly disregarded). The TPSM Hamiltonian incorporates quadrupole-quadrupole force plus monopole and quadrupole pairing interactions, containing no hexadecapole interaction terms. Near degeneracy is confirmed in 194, 198Tl; in 200Tl (N=119), the sideband is incomplete (only three transitions observed) and calculated TPSM B(M1)/B(E2) ratios deviate from the high-spin experimental drop due to fixed mean-field deformation.
- **Audit Verdict**: Establishes the boundary conditions of oblate-triaxial chirality in 194-200Tl using active TeX table deformation parameters and QQ+monopole/quadrupole pairing without hexadecapole terms, and clarifies that low-spin wobbling in 187Au is unresolved due to DCO/polarization dual-root ambiguity.

---

## 3. Compliance and Traceability Ledger Sign-Off

- **Manifest Path**: `raw/papers/gpt/query/20261107-six-region-transfer/manifest.json`
- **Research Note Path**: `knowledge/research-notes/six-region-primary-counterexamples-and-transfer-20261107.md`
- **Newly Created Source Pages**:
  1. `knowledge/sources/peng-2019-possible-chiral-doublets-60ni.md`
  2. `knowledge/sources/jehangir-2020-high-spin-doublet-bands-194-200tl.md`
  3. `knowledge/sources/zhang-2016-two-quasiparticle-bands-166ta.md`
- **Path Contract & Boundary Check**: Verified with `system/scripts/wiki_boundary_check.py --skip-qmd` (`status: ok, errors: []`).
- **Git Mutation Boundary**: Zero git commits, zero git branches created, zero pushes executed.
