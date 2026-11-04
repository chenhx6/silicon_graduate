---
name: chirality-and-wobbling-atomic-nuclei
description: "C. M. Petrache (ed.), Chirality and Wobbling in Atomic Nuclei (CRC Press, 2025): advanced theoretical and experimental spectroscopy manual for nuclear chirality, wobbling phonons, tilted axis precession, MχD, and multi-quasiparticle triaxial dynamics."
---

<!-- argument-hint: [topic, framework, nucleus, or chapter number] -->

# Chirality and Wobbling in Atomic Nuclei (C. M. Petrache, ed., CRC Press 2025)

**Editor**: Costel Marian Petrache | **Publisher**: CRC Press / Taylor & Francis Group (2025) | **PDF Pages**: 339 | **Chapters**: 17
**Source PDF**: `raw/books/Chirality and Wobbling in Atomic Nuclei.pdf` (SHA-256 `787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2`)

This project-local skill turns the definitive 2025 CRC monograph *Chirality and Wobbling in Atomic Nuclei* into an active research tool, expert reasoning guide, and experimental arbitration manual for low-energy nuclear structure and high-spin $\gamma$ spectroscopy.

## How to Use This Skill

- **General Consultation**: Ask about `wobbling vs TiP`, `chiral selection rules`, `MχD classification`, `dual-root arbitration`, `harmonic limit`, or `instanton tunneling`.
- **Nucleus-Specific Triage**: Query candidate nuclei ($^{135}\text{Pr}$, $^{135}\text{Nd}$, $^{134}\text{Pr}$, $^{131,133}\text{Ce}$, $^{103,105}\text{Pd}$, $^{128}\text{Cs}$, $^{187}\text{Au}$, $^{78}\text{Br}$).
- **Chapter-Specific Investigation**: Call `ch01` through `ch17` to inspect specific theoretical models (Frauendorf, Meng, Tanabe, Lawrie, Grodner, Raduta, Zhao, Sheikh, Chen, Brant, Zhang).
- **Experimental Method Arbitration**: Cross-check in-beam directional distributions ($a_2, a_4$), DCO/ADO ratios, Clover linear polarimetry ($P$), internal conversion coefficients, and picosecond lifetimes (DSAM/RDDS).

---

## Core Frameworks and Mental Models

1. **The Three-Axis Orthogonal Geometry of Nuclear Chirality (Chs. 1, 3, 16)**:
   Nuclear chirality originates from three mutually perpendicular angular momentum vectors in the triaxially deformed intrinsic frame ($\gamma \a30^\circ$):
   - High-$j$ valence particle aligns with the short axis ($s$);
   - High-$j$ valence hole aligns with the long axis ($l$);
   - Collective core rotates around the intermediate axis of maximum moment of inertia ($m$).
   The resulting aplanar vector product $\vec{J}_{\text{tot}} = \vec{j}_p + \vec{j}_n + \vec{R}_{\text{core}}$ breaks time-reversal-rotational symmetry $\mathcal{T}\mathcal{R}_y(\pi)$, forming degenerate left- and right-handed partner bands restored by quantum instanton tunneling.

2. **Koike-Starosta-Hamamoto (KSH) Electromagnetic Selection Rules (Chs. 1, 3, 7)**:
   A candidate pair of bands is confirmed as a genuine chiral doublet if and only if:
   - **100% In-Phase $S_{M1}(I)$ Staggering**: The ratio $[B(M1; I \to I-1)/B(E2; I \to I-2)] / [B(M1; I-1 \to I-2)/B(E2; I-1 \to I-3)]$ must stagger synchronously with identical phase in both partner bands;
   - **Intra-Band $B(E2)$ Congruence**: Intra-band $B(E2)$ values match within $<15\%$;
   - **Interband $\Delta I = 0$ $M1$ Vanishing Minimum**: The interband transition rate $B(M1; B \to A, \Delta I=0)$ drops to a deep minimum ($<0.05\ \mu_N^2$) at the chiral degeneracy spin;
   - **Grodner $g$-Factor Equality**: Measured gyromagnetic factors must satisfy $g_1(I) \equiv g_2(I)$, excluding planar signature partners.

3. **Wobbling Motion vs Tilted Precession (TiP) Arbitration (Chs. 2, 5, 6)**:
   - **Wobbling Motion (TW/LW)**: Semiclassical precession around a principal axis; requires **collective interband $E2$ transitions** ($B(E2)_{\text{inter}}/B(E2)_{\text{intra}} \sim 0.2 - 0.5$) with large mixing ratio ($|\delta| \gg 1$) and positive linear polarization asymmetry ($P > 0$);
   - **Tilted Precession (TiP) / Signature Partner**: Planar or tilted rotation; connecting interband transitions are **$M1$-dominated** ($|\delta| < 0.5, f_{M1} > 75\%$) with negative linear polarization asymmetry ($P < 0$) and weak interband $E2$ strength ($B(E2)_{\text{inter}}/B(E2)_{\text{intra}} < 0.1$).
   - *Crucial Lesson*: Directional angular distributions alone ($a_2$) suffer from mathematical quadratic dual-root degeneracy ($\Delta\chi^2 = 0$); linear polarimetry or internal conversion is mandatory to eliminate Hypothesis-Driven Root Selection (HDRS).

4. **Multiple Chiral Doublets ($M\chi D$) Classification (Chs. 3, 16)**:
   Multiple pairs of chiral doublet bands in the same nucleus fall into three distinct physical classes:
   - **Type I (Multi-Configuration)**: Different quasiparticle configurations (e.g. $^{133}\text{Ce}$ positive-parity 3-qp vs negative-parity 3-qp bands);
   - **Type II (Shape Coexistence)**: Same quasiparticle configuration occupying different triaxial deformation minima ($\gamma \approx 20^\circ$ vs $\gamma \approx -40^\circ$);
   - **Type III (Chiral Phonons)**: Same quasiparticle configuration and deformation, representing ground-state and multi-phonon chiral vibrational tunneling excitations (e.g. $^{103}\text{Rh}$).

5. **Top-on-Top Algebraic Rotor and D2 Symmetry (Ch. 4)**:
   Tanabe's algebraic formulation using double Holstein-Primakoff boson expansions restores the exact $D_2$ four-group invariance of the asymmetric core, correcting the historical axis permutation error in Bohr-Mottelson Eq. (4-282) and demonstrating that microscopic Coriolis Anti-Pairing (CAP) modifies the effective hydrodynamic inertia tensor.

6. **Chiral-Octupole Dual Symmetry Breaking (Chs. 3, 12, 15)**:
   Simultaneous coexistence of triaxial quadrupole ($\beta_2, \gamma$) and reflection-asymmetric octupole ($\beta_3$) deformations creates a 4-band supermultiplet: **Chiral-Parity Quartets**. Characterized by two intertwined pairs of chiral doublets connected by a dense network of strongly enhanced cross-parity $E1$ transitions ($B(E1)/B(E2) \sim 10^{-4}\ \text{fm}^{-2}$).

---

## Chapter Index

| # | Author & Topic | Core Physical Deliverable |
|---|---|---|
| [ch01](chapters/ch01-petrache-history-and-perspectives.md) | C. M. Petrache: History & Horizons | 25-year chiral roadmap, 4 mass islands, KSH criteria, AGATA/GRETA |
| [ch02](chapters/ch02-frauendorf-wobbling-theory.md) | S. Frauendorf: Wobbling Theory | Intermediate-axis separatrix, TW vs LW vs FM, harmonic approximation |
| [ch03](chapters/ch03-meng-wang-nuclear-chirality.md) | J. Meng & Y. P. Wang: Chirality & M$\chi$D | 3D-TAC, aplanar orientations, M$\chi$D classifications, instanton path |
| [ch04](chapters/ch04-tanabe-top-on-top-algebraic.md) | K. Tanabe: Top-on-Top Model | HP boson expansion, $D_2$ symmetry restoration, BM-II (4-282) correction |
| [ch05](chapters/ch05-guo-lv-experimental-controversies.md) | S. Guo & B. F. Lv: Experimental In-Beam | DCO/P-DCO pitfalls, $^{135}\text{Pr}$ linear polarimetry falsification |
| [ch06](chapters/ch06-lawrie-tip-vs-wobbling.md) | E. A. Lawrie: TiP vs Wobbling | Tilted precession boundary, Table 6.1 model taxonomy, $^{135}\text{Pr}$ TiP |
| [ch07](chapters/ch07-grodner-cs-chiral-transitions-gfactor.md) | E. Grodner: $^{126,128}\text{Cs}$ Benchmarks | RDDS lifetimes, $g_1 \equiv g_2$ equality theorem, non-coplanar proof |
| [ch08](chapters/ch08-raduta-semiclassical-gcsm.md) | A. A. Raduta: Coherent States & GCSM | Semiclassical phase space, Bargmann Dyson bosons, GCSM projection |
| [ch09](chapters/ch09-zhao-tdcdft-chiral-precession.md) | P. W. Zhao: TD-CDFT Dynamics | Time-dependent relativistic mean field, non-linear chiral tunneling |
| [ch10](chapters/ch10-chen-cdft-prm-wobbling.md) | Q. B. Chen: CDFT-PRM & Fermi Surface | Particle-rotor model, Fermi level placement, $^{135}\text{Pr}/^{133}\text{La}$ |
| [ch11](chapters/ch11-petrache-ibfm-mixing-ratios.md) | C. M. Petrache & S. Brant: IBFM Formalism | Interacting boson-fermion model, numerical $\delta(E2/M1)$ in odd-$A$ |
| [ch12](chapters/ch12-sheikh-tpsm-wobbling-chirality.md) | J. A. Sheikh: TPSM Triaxial Projection | 3D angular momentum projection, chiral-octupole quartets |

## Supporting Reference Files

- [glossary.md](glossary.md) — Comprehensive technical terminology (English/Chinese).
- [patterns.md](patterns.md) — 6 reusable diagnostic patterns for spectroscopy data analysis.
- [cheatsheet.md](cheatsheet.md) — Fast-check decision trees, formulas, and experimental arbitration tables.

---

## Scope & Limits

This skill covers the physical models, experimental criteria, and controversies of nuclear chirality and wobbling. For fundamental quantum mechanics of the unified model, refer to `bohr-mottelson-nuclear-structure`; for two-state mixing and $N_p N_n$ systematics, refer to `casten-nuclear-structure`; for in-beam DAQ, Clover polarimetry, and pulse processing, refer to `in-beam-gamma-spectroscopy`.
