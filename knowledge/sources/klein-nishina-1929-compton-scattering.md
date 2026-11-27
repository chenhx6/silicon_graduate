---
type: source
title: "Klein & Nishina 1929 - Compton scattering from free electrons in Dirac theory"
aliases: [Klein Nishina 1929 Compton formula]
created: 2026-09-20
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: historical-theory-paper
reading_depth: deep-read
title_original: "Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynamik von Dirac"
authors: [O. Klein, Y. Nishina]
journal: "Zeitschrift für Physik"
year: 1929
citation_key: klein_1929_Ueber
volume: 52
pages: "853-868"
canonical_source: "Klein & Nishina, Z. Phys. 52, 853 (1929)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf"
raw_sha256: "5020b8c9480606b29a96496412219cb3f985ba3f522223d5bf016c407565a40d"
nuclei: []
reactions: []
experiments: []
models: [Dirac-electron, relativistic-Compton-scattering]
observables: [Compton-cross-section, photon-energy-shift, scattering-angle]
methods: [Compton-polarimetry, Klein-Nishina-response]
tags: [Compton, Klein-Nishina, Dirac, historical-theory, detector-response]
---

# Compton scattering from free electrons in Dirac theory

## Bibliographic Record

- O. Klein and Y. Nishina, *Zeitschrift für Physik* **52**, 853–868 (1929).
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf`。
- 16-page German historical theory PDF; OCR was visually spot-checked for equations and section flow. The paper calculates intensity, not the later polarization treatment promised in its conclusion.

## Scope and Reading Depth

- Full paper read: introduction, Dirac Hamiltonian/eigenfunctions, plane-wave perturbation, scattering amplitude, energy-angle dependence, negative-energy/spin terms and comparison with older Dirac–Gordon formulas.
- Not covered: Nishina's subsequent polarization paper and modern detector-response simulations.

## Key Results and Method Boundary

- Dirac relativistic electron dynamics predicts the Compton scattering intensity with corrections of order `hν/(mc²)` relative to older formulas; the result becomes important for hard γ rays.
- The calculation tracks free-electron initial/final spin states and energy/momentum conservation, yielding the angular/energy response later known as the Klein–Nishina cross section.
- The paper explicitly restricts itself to scattering intensity; polarization is deferred to a subsequent work. Modern polarimeter formulas must therefore pair this source with Fagg/Hanna and detector-specific response papers.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KN29-1 | Dirac relativistic quantum dynamics changes the Compton intensity/energy-angle response relative to older Dirac–Gordon formulas. | formalism | direct | PDF pp.853–868, introduction and derivation | true |
| KN29-2 | The source derives a free-electron scattering response used as the theoretical basis for later Klein–Nishina polarimeter calculations. | formalism | direct | PDF pp.853–868 | true |
| KN29-3 | Polarization is not calculated in this paper; it is explicitly deferred to subsequent work. | limitation | direct | PDF p.853 | false |

## Summary

Klein–Nishina 1929 is the relativistic scattering foundation underlying Compton polarimetry. It is a historical response theory source, not a nuclear-structure or polarization-calibration experiment.

## Competing Interpretations and Limitations

The paper's OCR/notation and historical units require care; polarization, finite detector geometry, multiple scattering and background are outside its scope. Do not quote its free-electron response as a complete modern detector sensitivity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KN29-AR-1 | Theory chain | Dirac equation → spin-resolved scattering amplitude → relativistic Compton intensity. | PDF pp.854–868 | self-checking |
| KN29-AR-2 | Transfer condition | Use only as free-electron cross-section layer; detector `Q/R`, geometry and polarization require later sources. | Scope/limitation | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and the historical response lineage.
- Persistence: link to Simpson, Bass and Garcia-Raffi detector pages; preserve polarization-not-in-this-paper boundary.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KN29-P0-1`: do not conflate the free-electron intensity formula with detector-specific polarization sensitivity.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_start": 1, "pdf_end": 2, "sections": "题头、引言及§1狄拉克波动方程开头"}
- {"pdf_start": 3, "pdf_end": 6, "sections": "§1续，§2自由电子本征函数、简并和归一化，§3开头"}
- {"pdf_start": 7, "pdf_end": 10, "sections": "§3平面单色场的一阶解，§4散射场、康普顿运动学及静止初态"}
- {"pdf_start": 11, "pdf_end": 16, "sections": "§4续，矩阵约化、自旋态处理、散射强度、旧理论比较及积分散射系数"}
- 本次获取的具体覆盖：逐页读完实页1–16的所供文本，包括引言、四节推导、末页散射系数讨论和脚注。公式覆盖限于可辨文本及编号。未查看扫描图像或复算推导。所供文本未见编号图、表或图表题注。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 作者从自由电子的狄拉克本征态出发，对入射平面单色场保留场振幅一阶，并由式(34)和(35)实施康普顿动量与能量守恒。后续强度计算取初始电子静止，末态计入两种独立自旋解。 | 理论推导 | source-reported | PDF 实页3–4（印刷855–856），式(4)–(9)；实页7（859），式(22)–(24)；实页10（862），式(34)–(39)；实页12–14（864–866），末态说明及式(51)–(52)。 | true |
| A21-2 | 式(59)给出线偏振入射的方向强度。对入射电场方向取平均得到非偏振入射的式(60)。作者指出这些结果与电子初始磁化无关，并为椭圆偏振入射保留了区别。两式的完整因子和符号须查实页15，椭圆偏振讨论续至实页16。 | 理论结果 | source-reported | PDF 实页15–16（印刷867–868），式(59)–(60)及跨页末段。 | true |
| A21-3 | 相对旧 Dirac–Gordon 强度式，修正对入射光量子能量与电子静能的比值为二阶。作者预计硬γ区差异显著，并指出当时该区实验不足以裁决。末页比较因子的精确排式须查实页16。 | 理论比较与作者判断 | source-reported | PDF 实页1（印刷853）的题下说明，实页2（854）的引言末段，实页16（868）式(59)–(60)的比较段。 | true |
| A21-4 | 本文给出散射强度随方向和波长的关系。作者在引言明确把出射辐射的偏振问题留给 Nishina 的后续论文，并在推导与末页脚注再次指向该文。 | 范围声明 | source-reported | PDF 实页1（印刷853）引言末段及脚注，实页12（864）式(44)后的正文及脚注，实页16（868）首段及脚注。 | true |

与 Wiki 的归档路径及 SHA-256 一致。建议接受既有同版记录的正文通读范围，在修订阶次和定位后沿用定性结论。整式转录及旧条目所述目视抽查仍待图像核验。

- 把 Wiki 的 Dirac–Gordon 差异从 hν/(mc²) 改为 [hν/(mc²)]²。实页1的文字直接支持二阶，实页16的旧理论比较式需作图像核对。用式(34)–(35)、式(59)–(60)替换 KN29-1 和 KN29-2 的整篇宽定位。
- 把偏振后续工作的首处定位改为 PDF 实页1（印刷853）引言，补记实页12和16脚注。区分入射偏振对强度的影响与出射偏振的计算。
- 分列物理页和印刷页。实页16的页眉被抽成858，按连续页序与同版书目应记868。题名与姓氏以规范拼写著录，受理前如需核字形，查实页1题头及末页页眉。
- 抽文漏出实页2的式(1)、实页5和6的式(13)及(18)、实页8的场叠加和电流密度两个显示式。实页4式(8)–(9)矩阵缺项，实页12式(44)字符残损，实页15式(58)及实页16的积分散射系数无法可靠转录。引用这些公式时按对应物理页查原图。
