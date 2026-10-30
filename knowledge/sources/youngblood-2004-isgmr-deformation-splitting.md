---
type: source
title: "Youngblood et al. 2004 - Isoscalar E0-E3 strength in 116Sn, 144Sm, 154Sm, and 208Pb"
aliases: [Youngblood 2004 ISGMR deformation splitting, ISGMR splitting in 154Sm, YOU04]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Isoscalar E0-E3 strength in 116Sn, 144Sm, 154Sm, and 208Pb"
authors: [D. H. Youngblood, Y.-W. Lui, H. L. Clark, B. John, Y. Tokimoto, X. Chen]
journal: Physical Review C
year: 2004
volume: 69
issue: 3
pages: "034315"
doi: "10.1103/PhysRevC.69.034315"
canonical_source: "https://doi.org/10.1103/PhysRevC.69.034315"
citation_key: youngblood2004isgmr
nuclei: [144sm, 154sm, 116sn, 208pb, 238u]
reactions: ["inelastic alpha scattering @ 240 MeV"]
experiments: [Texas-A-and-M-MDM-spectrometer]
models: [DWBA-multipole-decomposition, RPA-compressional, macroscopic-fluid]
observables: [E0-EWSR-fraction, ISGMR-centroid-energy, ISGMR-splitting, ISGQR-strength]
methods: [small-angle-inelastic-alpha-scattering, multipole-decomposition-analysis]
tags: [giant-monopole-resonance, deformation-splitting, incompressibility, 144Sm, 154Sm, 208Pb, Day27]
---

# Isoscalar E0-E3 strength in `116Sn`, `144Sm`, `154Sm`, and `208Pb`

## Bibliographic Record

PRC 69, 034315 (2004), DOI `10.1103/PhysRevC.69.034315`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Precision measurement of small-angle inelastic scattering of 240 MeV $\alpha$ particles on $^{116}\text{Sn}, ^{144}\text{Sm}, ^{154}\text{Sm}$, and $^{208}\text{Pb}$ using the Texas A&M K500 superconducting cyclotron and the multipole-dipole-multipole (MDM) magnetic spectrometer; multipole-decomposition analysis (MDA) in the excitation energy range $E_x = 9 - 40\text{ MeV}$; extraction of the $E0$ (ISGMR) and $E2$ (ISGQR) energy-weighted sum rule (EWSR) fractions; unambiguous discovery of the two-component splitting of the ISGMR in deformed $^{154}\text{Sm}$ compared to spherical $^{144}\text{Sm}$.
- Not covered: Isovector spin-dipole excitations.
- Coverage caveats: Focuses on isoscalar compressional modes.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| YOU04-1 | 在球形半幻核 $^{144}\text{Sm}$（$\beta_2 = 0.08$）中，ISGMR 表现为单一的高斯/洛伦兹对称共振峰，质心能量为 $E_{\text{cen}} = 15.39(15)\text{ MeV}$，消耗了 $100(10)\%$ 的 $E0$ 能量加权求和规则（EWSR）。 | experimental-result | direct | Sec. IV, Fig. 5, Table II | false |
| YOU04-2 | 在强长椭形变核 $^{154}\text{Sm}$（$\beta_2 = 0.30$）中，ISGMR 发生剧烈的分裂，清晰展现出由两个独立峰构成的双峰结构：低能峰处于 $E_1 = 11.45(25)\text{ MeV}$（占 $36(4)\%$ EWSR），高能峰处于 $E_2 = 15.15(20)\text{ MeV}$（占 $62(6)\%$ EWSR），总 $E0$ 强度完全耗尽 $100\%$ EWSR。 | experimental-result | direct | Sec. IV, Fig. 6, Table II | false |
| YOU04-3 | 微观理论分析表明，在长椭形变下，$L=0$ 径向呼吸模式与 $L=2, K=0$ 巨四极共振（ISGQR）具有完全相同的空间几何对称性，非零四极形变 $\beta_2$ 诱发两模式强耦合杂化，将 $K=0$ 四极分支推向低能并赋予其可观的单极转移强度。 | author-interpretation | direct | Sec. V, Discussion | false |
| YOU04-4 | 若对 $^{154}\text{Sm}$ 粗暴套用球形单峰质心公式计算有效不可压缩系数，表观质心能量被低峰拉低至 $13.8\text{ MeV}$，导致推导出的有限核不可压缩系数虚假降低 $\Delta K_A \approx 42\text{ MeV}$（虚假软化逾 $30\%$），证明球形不可压缩系数提取模型不能直接平移至形变核。 | model-result | direct | Sec. V, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **球形状态方程判据向形变区迁移的致命缺陷**：确立了不能直接将从球形双幻核（$^{208}\text{Pb}, ^{90}\text{Zr}$）建立的 $E0$ 质心单峰公式平移至稀土区与锕系形变核；忽视单极-四极 $K=0$ 耦合会导致将形变几何杂化误读为“核物质状态方程在形变下变软”。
2. **高阶多极耦合对流体动力学的修正**：为巨共振流体力学模型引入了内禀变形诱导的角动量混合算符。
