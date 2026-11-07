---
type: source
title: "Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism"
aliases: [Xu 2004 Superheavy High-Spin Isomers, Xu 2004 PRL]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism"
authors: [F. R. Xu, E. G. Zhao, R. Wyss, P. M. Walker]
journal: Physical Review Letters
year: 2004
volume: 92
pages: 252501
doi: 10.1103/PhysRevLett.92.252501
language: en
canonical_source: doi:10.1103/PhysRevLett.92.252501
citation_key:
raw_file: "raw/papers/isomer/isomer_application/superheavy_nuclei/2004_Xu et al_Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism.pdf"
raw_sha256: 9e6cdfecc0bdf71547cc8eddc7d69489fab8e0361d63ad87bd64a2aea39a413c
archive_required: true
nuclei: [250fm, 254no, 256fm, 266hs, 270ds]
reactions: []
experiments: []
models: [configuration-constrained-pes, woods-saxon-universal, lipkin-nogami-pairing, strutinsky-shell-correction, specialization-energy]
observables: [excitation-energy, fission-barrier-height, alpha-decay-q-value, partial-fission-half-life]
methods: [multidimension-deformation-minimization, blocked-quasiparticle-tracking]
tags: [superheavy-nuclei, high-k-isomer, fission-barrier, specialization-energy, k-conservation, stability-enhancement]
---

# Xu 等（2004）：高自旋同核异能性增强超重核稳定性

## Bibliographic Record

The theoretical paper was published in *Physical Review Letters* 92, 252501 (2004), received 29 November 2003, published 25 June 2004 (DOI: 10.1103/PhysRevLett.92.252501). The 4-page PDF is preserved at `raw/papers/isomer/isomer_application/superheavy_nuclei/2004_Xu et al_Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism.pdf` with SHA-256 `9e6cdfecc0bdf71547cc8eddc7d69489fab8e0361d63ad87bd64a2aea39a413c` (174,665 bytes). `archive_required: true` is preserved.

## Scope and Reading Depth

The 4-page article was read in full, including configuration-constrained potential-energy surface (PES) formulations, Figs. 1–2 (calculated 2-quasineutron and 2-quasiproton excitation energies), Fig. 3 (decay schemes in $^{270}\text{Ds} \to {}^{266}\text{Hs}$), Fig. 4 (fission barrier of $^{256}\text{Fm}$ $7^-$ isomer), and Fig. 5 (triaxial $(\beta_2, \gamma)$ PES trajectory).

## Summary

Xu et al. demonstrated through configuration-constrained PES calculations that high-$K$ multi-quasiparticle (multi-QP) states systematically occur at low excitation energies ($E_x \sim 1.0–1.5\text{ MeV}$) in deformed, axially symmetric even-even superheavy nuclei with $Z \ge 100$. Unlike conventional quantum systems where excited states are less stable than the ground state, high-$K$ multi-QP isomers in superheavy nuclei exhibit **enhanced stability** against both spontaneous fission and $\alpha$ decay:
1. **Fission Barrier Elevation & Superfluidity Reduction**: The blocking of unpaired nucleons reduces pairing correlations (decreasing the superfluid gap $\Delta$), which increases the collective mass inertia $B_{\text{eff}} \propto \Delta^{-2}$. Furthermore, when configuration quantum numbers (like $K^\pi$) are conserved along the deformation path, the system incurs a substantial "specialization energy", elevating the fission barrier height and width (e.g. in $^{256}\text{Fm}$, the calculated $7^-$ fission barrier is higher than the ground-state barrier, accounting for the 3-orders-of-magnitude hindrance of the experimental partial fission half-life of $0.8\text{ ms}$). Nonaxial $\gamma$ deformation lowers both barriers by $\sim 2.5\text{ MeV}$, but preserves the relative specialization elevation.
2. **Alpha Decay Suppression**: Reduced pair density at the Fermi surface inhibits $\alpha$-particle preformation, while the centrifugal barrier and reduced $Q_\alpha$ for transitions to excited daughter isomers further lengthen $\alpha$ lifetimes.
3. **Isomeric Predictions in $^{254}\text{No}$ and $^{270}\text{Ds}$**: In $^{270}_{110}\text{Ds}$, low-lying $9^-$ ($1.39\text{ MeV}$), $10^-$ ($1.26\text{ MeV}$), and $\pi 10^-$ ($1.07\text{ MeV}$) isomers reproduce the observed $6.0\text{ ms}$ isomeric $\alpha$ decay to $^{266}\text{Hs}$. In $^{254}\text{No}$, the $8^-$ two-quasineutron configuration $\nu\{7/2^+[613] \otimes 9/2^-[734]\}$ was calculated at $1.12\text{ MeV}$, and the two-quasiproton configuration $\pi\{7/2^-[514] \otimes 9/2^+[624]\}$ was calculated at $1.48\text{ MeV}$.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| XU04-1 | Configuration-constrained PES calculations reveal that low-lying high-$K$ two-quasiparticle states ($K^\pi = 7^-, 8^-, 9^-, 10^-$) systematically exist at $E_x \sim 1.0–1.5\text{ MeV}$ in deformed even-even nuclei with $Z \ge 100$. | model-calculation | direct | PDF p. 1–2, Abstract, Figs. 1–2 | false |
| XU04-2 | High-$K$ multi-quasiparticle isomers enhance superheavy nucleus stability by simultaneously decreasing the probability of spontaneous fission (via specialization energy barrier elevation and pairing-reduced collective inertia) and $\alpha$ decay (via pair-density blocking and centrifugal inhibition). | author-interpretation | direct | PDF p. 1, 3, text col. 1 | false |
| XU04-3 | In $^{270}\text{Ds}$, calculated $9^-$ ($1.39\text{ MeV}$), $10^-$ ($1.26\text{ MeV}$), and $\pi 10^-$ ($1.07\text{ MeV}$) two-quasiparticle states quantitatively match the observed isomeric $\alpha$ decay ($E_\alpha = 10.95, 11.15, 12.15\text{ MeV}$, $T_{1/2} = 6.0\text{ ms}$). | model-calculation | direct | PDF p. 2–3, Fig. 3 | false |
| XU04-4 | In $^{256}\text{Fm}$, the configuration-constrained fission barrier of the $7^-$ isomer ($\pi 7/2^-[514] \otimes \pi 7/2^+[633]$) exhibits enhanced barrier height and width relative to the ground state, explaining the observed $T_{1/2}(\text{SF}) = 0.8\text{ ms}$ (hindered by a factor of $\sim 300$ relative to unhindered estimate). | model-calculation | direct | PDF p. 3–4, Figs. 4–5 | false |
## Competing Interpretations and Limitations

### Intrinsic Decay Stabilization vs Heavy-Ion Reaction Yields
A fundamental physical nuance must be distinguished between the **intrinsic half-life stabilization** of an isomer and its **formation cross section in heavy-ion reactions**:
1. **Intrinsic Lifetime Stabilization**: Xu 2004 correctly shows that once a nucleus is in a cold, low-energy high-$K$ isomeric state, tunneling into the fission channel or $\alpha$ emission is strongly hindered by the specialization barrier and pairing blocking, provided $K$ is conserved during the tunneling process.
2. **Heavy-Ion Fusion Formation**:
   The synthesis cross section of a superheavy evaporation residue in complete fusion is:
   $$\sigma_{\text{ER}}(E_{\text{c.m.}}) = \frac{\pi}{k^2} \sum_{J=0}^{J_{\text{max}}} (2J+1) T(E_{\text{c.m.}}, J) P_{\text{CN}}(E_{\text{c.m.}}, J) W_{\text{surv}}(E^*, J)$$
   - Formation and decay are governed by distinct stages: cold-state stability against spontaneous fission does not alone determine the reaction capture cross section $\sigma_{\text{cap}}(J)$, compound-nucleus formation probability $P_{\text{CN}}(J)$, or survival probability $W_{\text{surv}}(J)$ during particle evaporation.
   - In the hot compound nucleus, pairing correlations are weakened and level densities are high, while rotational energy modifies the effective fission barrier across the spin distribution. Fission competition during statistical de-excitation governs the overall survival probability.
   - Feeding into a specific isomeric state depends on the spin distribution of the evaporation residues and the branching ratios $b_{\text{iso}}(J)$ during the final $\gamma$-ray cascades near the yrast line.
   - **Conclusion**: Enhanced intrinsic half-life of a cold high-$K$ isomer does not directly translate into an increased formation cross section in heavy-ion reactions; the observed yield reflects the full convolution of entrance-channel dynamics, compound-nucleus survival, and yrast feeding branches.
3. **K Conservation in Fission Models**: If the nucleus undergoes dynamic shape evolution involving triaxiality ($\gamma \ne 0$) or Coriolis mixing along the fission path, the $K$ projection is partially destroyed, allowing the nucleus to circumvent the specialization barrier by tunneling through non-$K$-conserving paths.

## Source Self-Audit

- Audit date: 2026-11-07 by Codex research agent (self-audit, not human-reviewed).
- Consistency check: confirmed that calculated energies for $^{270}\text{Ds}$ ($1.39, 1.26, 1.07\text{ MeV}$), $^{254}\text{No}$ ($1.12, 1.48\text{ MeV}$), and $^{256}\text{Fm}$ ($1.01\text{ MeV}$) match PDF text and Figs. 1–3.
- Distinction confirmed: theoretical model calculation based on Woods-Saxon PES, not experimental synthesis.

## Extracted Pages

- PDF p. 1 (252501-1): Motivation; definition of configuration-constrained PES; pairing via Lipkin-Nogami; abstract.
- PDF p. 2 (252501-2): Fig. 1 2-quasineutron excitation energy systematics; Fig. 2 2-quasiproton systematics; analysis of $^{270}\text{Ds} \to {}^{266}\text{Hs}$ decay events.
- PDF p. 3 (252501-3): Fig. 3 decay scheme for $^{270}\text{Ds}$; Fig. 4 calculated fission barrier of $^{256}\text{Fm}$ $7^-$ isomer; discussion of $^{254}\text{No}$ and $^{250}\text{Fm}$ configurations.
- PDF p. 4 (252501-4): Fig. 5 triaxial $(\beta_2, \gamma)$ PES trajectory for $^{256}\text{Fm}$; conclusions, acknowledgments, and references (1–23).
