---
type: source
title: "Piekarewicz 2004 - Unmasking the nuclear matter equation of state"
aliases: [Piekarewicz 2004 soft monopole mode, soft ISGMR neutron skin, PIE04]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Unmasking the nuclear matter equation of state"
authors: [J. Piekarewicz]
journal: Physical Review C
year: 2004
volume: 69
issue: 4
pages: "041301(R)"
doi: "10.1103/PhysRevC.69.041301"
canonical_source: "https://doi.org/10.1103/PhysRevC.69.041301"
citation_key: piekarewicz2004unmasking
nuclei: [90zr, 116sn, 120sn, 132sn, 140sn, 208pb]
reactions: []
experiments: []
models: [relativistic-mean-field, relativistic-rpa, NL3, FSUGold]
observables: [ISGMR-strength-distribution, soft-monopole-energy, incompressibility-K_A, symmetry-incompressibility-K_tau]
methods: [RRPA-constrained-monopole, leptodermous-expansion, transition-density-decomposition]
tags: [giant-monopole-resonance, soft-monopole, neutron-skin, incompressibility, K_tau, equation-of-state, Day27]
---

# Unmasking the nuclear matter equation of state

## Bibliographic Record

PRC 69, 041301(R) (2004), DOI `10.1103/PhysRevC.69.041301`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Fully self-consistent Relativistic Random Phase Approximation (RRPA) calculations of the Isoscalar Giant Monopole Resonance (ISGMR) in neutron-rich nuclei, with particular focus on the tin isotopic chain ($^{116}\text{Sn} \to ^{140}\text{Sn}$) and $^{208}\text{Pb}$; discovery and characterization of the low-energy "soft monopole mode" at $E_x \sim 8 - 10\text{ MeV}$; evaluation of the nuclear incompressibility $K_A$ using constrained sum rules ($m_1/m_0$ and $\sqrt{m_1/m_{-1}}$); formal demonstration of the breakdown of the macroscopic leptodermous expansion for $K_A$ in the presence of the soft mode; determination of the true symmetry incompressibility $K_\tau$.
- Not covered: Heavy-ion collision flow observables.
- Coverage caveats: Focuses on the decoupling of skin compression from core breathing.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| PIE04-1 | 在极富中子核（如 $^{132}\text{Sn} \to ^{140}\text{Sn}$）中，自洽相对论 RPA 计算发现，除了位于 $E_x \sim 15\text{ MeV}$ 的经典主 ISGMR 呼吸峰外，在低激发能区（$E_x \sim 8.5 - 10.5\text{ MeV}$）涌现出一个显著的**软单极呼吸模式（Soft Monopole Mode）**，携带高达 $12\% - 18\%$ 的单极 EWSR。 | model-result | direct | Sec. II, Fig. 1 | false |
| PIE04-2 | 径向跃迁密度分析表明，软单极模式对应于中子皮与等旋对称核芯之间的径向反相伸缩振荡（外层中子皮径向膨胀时内层核芯被轻微压缩），与主呼吸模（全核整体同相压缩）具有完全不同的物理机制。 | model-result | direct | Sec. III, Fig. 2 | false |
| PIE04-3 | 若无视该软模式的存在，直接套用宏观液滴薄皮展开公式（Leptodermous Expansion）计算整体质心能量，低能软模式会将表观质心拉低逾 $1.0\text{ MeV}$，导致提取出的对称不可压缩系数 $K_\tau$ 发生虚假发散（从真实的 $-500\text{ MeV}$ 暴跌至 $-800\text{ MeV}$ 以下）。 | model-result | direct | Sec. IV, Fig. 3, Table I | false |
| PIE04-4 | 确立了只有在微观上将软单极中子皮模式与主核芯呼吸模解耦后，由稳定核（$^{208}\text{Pb}$）约束的核物质不可压缩性 $K_\infty \approx 230 - 240\text{ MeV}$ 与 $K_\tau \approx -500 \pm 50\text{ MeV}$ 才能在极富中子滴线区保持普适自洽。 | author-interpretation | direct | Sec. V, Conclusions | false |

## Cross-Mass-Region Transferability Significance

1. **宏观液滴不可压缩性展开式的跨同位旋失效**：证明液滴薄层展开公式 $K_A(A, Z)$ 隐含假定原子核为均匀流体，在存在可压缩中子皮的极端富中子核中彻底失效。
2. **软单极模式作为中子皮径向压缩率的敏感探针**：确立了 $E_x \sim 9\text{ MeV}$ 的软单极强度是直接探测中子星地壳中非均匀中子物质压缩率的理想微观窗口。
