---
type: source
title: "Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism"
aliases: [Xu 2004 Superheavy High-Spin Isomers, Xu 2004 PRL]
created: 2026-11-07
updated: 2026-11-08
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

2026-11-08 R3总控再次回读四页。PDF3明确区分256Fm7⁻总半衰期70ns
与裂变部分半衰期0.8ms；无阻碍对照2.5μs给约320倍，不能将0.8ms当总寿命。
文中确实有Fig.4–5。固定组态PES是理论计算，作者提醒实际裂变未必保持该组态。
本文未计算B∝Δ⁻²的普适动力学律，也未由测得γ寿命唯一反演裂变稳定性。

## Summary

作者用组态约束Woods–Saxon/Strutinsky势能面及Lipkin–Nogami配对研究
形变超重核中的低能多准粒子态。论文提出高K组态可能抑制γ、α及裂变的相关通路，
结合当时已知事件讨论稳定性增强；不是逐核所有衰变率的实验认证。
配对减弱影响α预形成，固定组态路径给裂变势垒增加；实际动力学可改变组态。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| XU04-1 | 所算区域存在低能高K两准粒子候选，能量随核素与组态变化；不能把1–1.5MeV设为所有候选范围。 | model-calculation | direct | PDF1–2, Figs.1–2 | false |
| XU04-2 | 固定组态、配对与α预形成等用于解释受抑通路；没有本文推出的普适B∝Δ⁻²动力学定律。 | author-interpretation-with-boundary | direct | PDF1–3 | false |
| XU04-3 | 270Ds的9−/10−中子候选为1.39/1.26MeV，质子10−为1.07MeV；用α能量比较候选组态，不是算出了观测6ms的绝对寿命。 | model-versus-adopted-data | direct | PDF2–3, Fig.3 | false |
| XU04-4 | 256Fm7−固定组态路径势垒高且宽；转引总半衰期70ns、裂变部分0.8ms及无阻碍对照2.5μs。 | model-and-cited-experiment-distinguished | direct | PDF3–4, Figs.4–5 | false |
| XU04-5 | 该例非轴向PES相对轴向降低基态/异能态势垒2.4/2.6MeV。 | model-calculation | direct | PDF3, Fig.5 | false |

## Competing Interpretations and Limitations

### Intrinsic Decay Stabilization vs Heavy-Ion Reaction Yields
A fundamental physical nuance must be distinguished between the **intrinsic half-life stabilization** of an isomer and its **formation cross section in heavy-ion reactions**:
1. **Intrinsic Lifetime Stabilization**: The calculations illustrate stabilization for specified configurations and paths; this is not a universal lifetime theorem for every high-K state.
2. **Heavy-Ion Fusion Formation**:
   The synthesis cross section of a superheavy evaporation residue in complete fusion is:
   $$\sigma_{\text{ER}}(E_{\text{c.m.}}) = \frac{\pi}{k^2} \sum_{J=0}^{J_{\text{max}}} (2J+1) T(E_{\text{c.m.}}, J) P_{\text{CN}}(E_{\text{c.m.}}, J) W_{\text{surv}}(E^*, J)$$
   - Formation and decay are governed by distinct stages: cold-state stability against spontaneous fission does not alone determine the reaction capture cross section $\sigma_{\text{cap}}(J)$, compound-nucleus formation probability $P_{\text{CN}}(J)$, or survival probability $W_{\text{surv}}(J)$ during particle evaporation.
   - In the hot compound nucleus, pairing correlations are weakened and level densities are high, while rotational energy modifies the effective fission barrier across the spin distribution. Fission competition during statistical de-excitation governs the overall survival probability.
   - Feeding into a specific isomeric state depends on the spin distribution of the evaporation residues and the branching ratios $b_{\text{iso}}(J)$ during the final $\gamma$-ray cascades near the yrast line.
   - **Conclusion**: Enhanced intrinsic half-life of a cold high-$K$ isomer does not directly translate into an increased formation cross section in heavy-ion reactions; the observed yield reflects the full convolution of entrance-channel dynamics, compound-nucleus survival, and yrast feeding branches.
3. **Configuration Conservation**: The paper explicitly notes that actual fission can involve more complex dynamics without fixed configuration. Triaxiality permits K mixing but does not alone determine its strength or a unique alternative tunneling rate. The stage-factorized reaction formula above is a cross-source comparison with [[zagrebaev-2001-superheavy-synthesis-survival]], not a new result of Xu2004.

## Source Self-Audit

- Audit dates: 2026-11-07 initial agent record; 2026-11-08 parent primary-text correction, not human-reviewed.
- Consistency check: confirmed that calculated energies for $^{270}\text{Ds}$ ($1.39, 1.26, 1.07\text{ MeV}$), $^{254}\text{No}$ ($1.12, 1.48\text{ MeV}$), and $^{256}\text{Fm}$ ($1.1\text{ MeV}$) are model values discussed in the PDF; the 1.01MeV value belongs to 250Fm, not 256Fm.
- Distinction confirmed: theoretical model calculation based on Woods-Saxon PES, not experimental synthesis.

## Extracted Pages

- PDF p. 1 (252501-1): Motivation; definition of configuration-constrained PES; pairing via Lipkin-Nogami; abstract.
- PDF p. 2 (252501-2): Fig. 1 2-quasineutron excitation energy systematics; Fig. 2 2-quasiproton systematics; analysis of $^{270}\text{Ds} \to {}^{266}\text{Hs}$ decay events.
- PDF p. 3 (252501-3): Fig. 3 decay scheme for $^{270}\text{Ds}$; Fig. 4 calculated fission barrier of $^{256}\text{Fm}$ $7^-$ isomer; discussion of $^{254}\text{No}$ and $^{250}\text{Fm}$ configurations.
- PDF p. 4 (252501-4): Fig. 5 triaxial $(\beta_2, \gamma)$ PES trajectory for $^{256}\text{Fm}$; conclusions, acknowledgments, and references (1–23).
