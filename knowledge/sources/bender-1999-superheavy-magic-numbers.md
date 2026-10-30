---
type: source
title: "Bender et al. 1999 - Shell structure of superheavy nuclei in self-consistent mean-field models"
aliases: [Bender 1999 superheavy shell structure, superheavy magic numbers RMF Skyrme, BEN99]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Shell structure of superheavy nuclei in self-consistent mean-field models"
authors: [M. Bender, K. Rutz, P.-G. Reinhard, J. A. Maruhn, W. Greiner]
journal: Physical Review C
year: 1999
volume: 60
issue: 3
pages: "034304"
doi: "10.1103/PhysRevC.60.034304"
canonical_source: "https://doi.org/10.1103/PhysRevC.60.034304"
citation_key: bender1999superheavy
nuclei: [208pb, 292114, 298114, 304120, 310126]
reactions: []
experiments: []
models: [relativistic-mean-field, skyrme-hartree-fock, gogny-hfb, bcs-pairing]
observables: [single-particle-energies, shell-gaps, spin-orbit-splitting, charge-density-distributions, two-proton-separation-energies]
methods: [self-consistent-mean-field, density-gradient-analysis, central-depression-evaluation]
tags: [superheavy-elements, magic-numbers, spin-orbit-quenching, island-of-stability, central-depression, Day27]
---

# Shell structure of superheavy nuclei in self-consistent mean-field models

## Bibliographic Record

PRC 60, 034304 (1999), DOI `10.1103/PhysRevC.60.034304`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Systematic investigation of shell closures in superheavy nuclei ($Z \approx 110 - 130, N \approx 170 - 200$) using self-consistent mean-field models (Skyrme forces SkM*, SLy4, SkI4; Gogny D1S; and Relativistic Mean Field NL3, NL-SH, NL-Z); analysis of spin-orbit splitting for proton $2f, 1i$ and neutron $3d, 2h, 1j$ states; calculation of radial charge and matter density profiles; evaluation of central density depression (bubble/wine-bottle effect) driven by Coulomb repulsion.
- Not covered: Fusion evaporation reaction dynamics.
- Coverage caveats: Distinguishes between model-dependent proton gap predictions ($Z=114$ vs $Z=120/126$) and the robust consensus on $N=184$.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| BEN99-1 | 超重核中巨大的质子静电斥力（$Z \sim 114 - 120$）将核内核子向表面推挤，导致自洽密度分布出现明显的中心凹陷（Central Density Depression，中心密度较饱和密度降低 $15\% - 30\%$）。 | model-result | direct | Sec. III.A, Figs. 1-2 | false |
| BEN99-2 | 由于自旋—轨道势正比于密度的空间梯度（$V_{ls} \propto \frac{1}{r} \frac{d\rho}{dr}$），中心平坦与梯度反转诱发自旋—轨道相互作用在核内核区发生严重淬灭（高-$l$ 轨道自旋—轨道劈裂减弱 $30\% - 45\%$）。 | model-result | direct | Sec. III.B, Table I | false |
| BEN99-3 | 质子幻数在不同自洽模型间发生剧烈分化：相对论平均场（RMF）由于较弱的有效质量与强相对论标量-矢量势差，普遍预言 $Z=114$ 为质子闭壳（壳隙 $\sim 1.8\text{ MeV}$）；而非相对论 Skyrme（如 SLy4）与 Gogny（D1S）则预言 $Z=120$ 或 $Z=126$ 为闭壳。 | cross-source-model-comparison | direct | Sec. IV, Figs. 6-8 | false |
| BEN99-4 | 无论何种模型，超重核的单粒子能隙（$\Delta E \sim 1.5 - 2.2\text{ MeV}$）远小于 $^{208}\text{Pb}$ 的巨闭壳能隙（$3.8 - 4.5\text{ MeV}$），导致超重核基态普遍处于弱形变软势阱中（$\beta_2 \approx 0.10 - 0.15$），不能将 $^{208}\text{Pb}$ 坚硬球形双幻核的概念直接平移至超重岛。 | author-interpretation | direct | Sec. V, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **双幻核刚性概念的跨区不可迁移性**：$^{208}\text{Pb}$ 的超大壳隙使基态高度刚硬、四极激发能量高（$E(2^+) = 4.09\text{ MeV}$）；而超重核因为库仑退局域化与自旋—轨道淬灭，壳隙严重压缩，基态表现为明显的四极/八极形状共存，不能将其假设为刚硬球形核。
2. **宏观-微观单粒子势直接平移的失败**：传统的 Woods-Saxon 或 Nilsson 唯象参数固定了自旋—轨道耦合强度与表面扩散系数，无法自洽反映由库仑斥力引起的内部密度塌缩，导致超重区单粒子能级外推产生重大系统误差。
