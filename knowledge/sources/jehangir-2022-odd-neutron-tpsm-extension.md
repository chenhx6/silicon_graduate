---
type: source
title: "Jehangir et al. 2022 - Extended TPSM for odd-neutron nuclei"
aliases: [Odd-neutron TPSM extension 2022, Jehangir 2022 Xe TPSM]
created: 2026-09-30
updated: 2026-09-30
status: ai-draft
review_status: unreviewed
source_type: theory-paper
reading_depth: deep-read
title_original: "Extended triaxial projected shell model approach for odd-neutron nuclei"
authors: [S. Jehangir, N. Nazir, G. H. Bhat, J. A. Sheikh, N. Rather, S. Chakraborty, R. Palit]
journal: Physical Review C
year: 2022
volume: 105
pages: 054310
doi: 10.1103/PhysRevC.105.054310
arxiv: 2203.12851v1
language: en
canonical_source: "https://arxiv.org/abs/2203.12851"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/2203-12851-tpsm-odd-neutron-xe-20260930/PDFs/Extended_triaxial_projected_shell_model_approach_for_odd-neutron_nuclei.pdf"
raw_sha256: 2c2d428aa5d82b8951d8f927bc11ccd9d30ed791fd55d488ea9cfcfb6372dea5
nuclei: [117Xe, 119Xe, 121Xe, 123Xe, 125Xe, 127Xe, 129Xe, 131Xe]
reactions: []
experiments: []
models: [triaxial-projected-shell-model, angular-momentum-projection, configuration-mixing]
observables: [level-scheme, signature-splitting, aligned-angular-momentum, dynamic-moment-of-inertia, transition-quadrupole-moment]
methods: [angular-momentum-projection, projected-configuration-mixing]
tags: [tpsm, odd-neutron, xenon-isotopes, high-spin, signature-inversion]
---

# Jehangir 等（2022）：奇中子 TPSM 基底扩展

## Bibliographic Record

S. Jehangir et al., Physical Review C 105, 054310 (2022), DOI 10.1103/PhysRevC.105.054310；arXiv 2203.12851v1。Crossref 核实题名、作者、卷和文章号；OpenAlex 将 arXiv 版本标为 green OA。本地文件来自 arXiv 官方 PDF，SHA-256 已记录在 frontmatter。

## Scope and Reading Depth

- 已深读 16 页主文，核对 Eqs. (1)–(8)、Table I，以及 Figs. 1–18 中的投影前后能带图、能谱、signature splitting、alignment、dynamic moment of inertia、transition quadrupole moments。
- 重点核对 odd-neutron 基底由 1ν/1ν+2π 扩展到 3ν 与 3ν+2π，以及 131Xe 能谱、对齐和 signature 结果。
- 未重新分析引用的 gamma spectra；未重跑投影/混合代码；未覆盖 135Ce，且 131Xe yrare band 没有实验观测。

## Summary

作者把三轴投影壳模型用于奇中子 Xe 同位素链 117–131Xe，将原有 1-quasineutron 与 1ν+2π 基底扩展到 3-quasineutron 和 3ν+2π 五准粒子态，使模型可讨论第二次 band crossing。计算与已发表 Xe 能级、signature splitting、alignment 和动态转动惯量比较，并预测若干尚未观测的 yrare/高自旋带。该工作提供 odd-neutron projected-basis 方法例子，包含 N=77 的 131Xe 同中子素；不包含 135Ce，也不是新实验。

## Active Recall Before Opening the Full Text

开全文前的预期是：奇中子 TPSM 需从三轴 Nilsson+配对准粒子态进行角动量投影；扩展的 3n/5qp 组态可能用于高自旋对齐与 band crossing。我不确定具体 Xe 同位素范围、投影核/组态混合方式、131Xe 是否有实测 yrare band、形变是计算还是沿用输入。原文核对后确认：覆盖 117–131Xe，131Xe 的 Table I 形变取自先前来源；yrast 数据可比较，但该核 yrare band 未观测，部分结果为 TPSM prediction。

## Method and Model Space

- 角动量投影算符和旋转积分见 Eqs. (2)–(3)；投影后的多准粒子态经 Hill–Wheeler 广义本征方程 Eq. (6) 混合，集体波函数见 Eq. (7)。
- Eq. (1) 的奇中子基底含 1ν、1ν+2π、3ν 和 3ν+2π 组态；新增 neutron-alignment components 是从旧 odd-neutron TPSM 扩展到高自旋的关键。
- Hamiltonian 含 quadrupole–quadrupole、monopole pairing 和 quadrupole pairing 项（Eq. (4)）；单粒子空间采用 N=3,4,5 三个主壳。作者使用 GQ=0.16GM，配对强度按质量差形式设置；电四极矩计算采用 proton/neutron effective charges 1.5e/0.5e（Eqs. (5)–(8)，PDF pp. 4–6）。
- 作者说明 Eq. (4) 的 QQ 力强度 `χ` 由 self-consistent HFB condition 联系到四极形变 `ε`（JN22-13）；这项关系是 Hamiltonian 参数化条件。本文 Table I 的 Xe 形变仍取自先前来源，不应把这一参数关系误写成本文独立的形状测量或无约束能面极小值。
- Table I 的 131Xe 参数为 ε=0.160、ε′=0.090、γ=29°；所有 Xe 形变参数采用早期文献值，不是本文独立测量或共同拟合出的形状。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JN22-1 | odd-neutron TPSM 投影基底从 1ν 与 1ν+2π 扩展到 3ν、3ν+2π 五准粒子组态。 | model-method | direct | Eq. (1), PDF p. 4 | true |
| JN22-2 | Euler-angle angular-momentum projection 后，在非正交投影态空间用 Hill–Wheeler 广义本征方程混合组态。 | model-method | direct | Eqs. (2)–(3), (6)–(7), PDF pp. 4–6 | true |
| JN22-3 | Hamiltonian 包括 QQ、monopole pairing 和 quadrupole pairing；使用 N=3,4,5 主壳、GQ=0.16GM，E2 有效电荷为 1.5e/0.5e。 | model-input | direct | Eqs. (4)–(8), PDF pp. 4–6 | true |
| JN22-4 | 系统计算覆盖奇中子 117–131Xe 同位素链，不包括 135Ce；Table I 的 131Xe 输入为 ε=0.160、ε′=0.090、γ=29°。 | model-input | direct | Abstract; Table I, PDF pp. 1, 7 | true |
| JN22-5 | TPSM 与已发表实验能谱比较；对 129Xe、131Xe，作者报告 yrast 谱总体符合较好。131Xe 数据取自论文所引既有实验。 | model-result | direct | Fig. 7 caption and discussion, PDF p. 7 | true |
| JN22-6 | 131Xe yrast signature splitting 与计算比较；对 131Xe yrare band，正文明确称尚无实验观测，相关 signature 行为是模型预测。 | model-result | direct | Figs. 12–13 and discussion, PDF pp. 10–11 | true |
| JN22-7 | 作者将 129Xe、131Xe 第一 band crossing 归因于质子对齐；119–127Xe 的第一 crossing 则归因于中子对齐。 | author-interpretation | indirect | Figs. 1–3, 14–17; Summary, PDF pp. 2–3, 10–14 | true |
| JN22-8 | Fig. 8–10 展示的投影组态振幅来自非正交基，作者明确提醒这些振幅不能当作通常意义的概率。 | model-limitation | direct | Figs. 8–10 captions, PDF pp. 8–9 | true |
| JN22-9 | 模型计算的 Qt 随 band crossing 下降，并比较 yrast/yrare 的 K 构成；这是模型可观测量，不是本文测得的绝对 lifetime 或 shape measurement。 | model-result | direct | Fig. 18 and discussion, PDF pp. 13–14 | true |
| JN22-10 | 作者提出对高自旋 excited bands 测 g-factors 作为后续判别量；当前 TPSM 对 131Xe yrare band 等结果仍需未来实验检验。 | author-interpretation | direct | Summary, PDF pp. 14–15 | true |
| JN22-11 | 该论文是理论模型比较，实验能级取自 Refs. [47]–[54] 等已发表数据；不报告新的反应、装置或 coincidence dataset。 | synthesis | direct | Figs. 4–7 captions; Summary, PDF pp. 4–8, 14 | true |
| JN22-12 | Fig. 7 的 131Xe 比较使用既有数据 Refs. [52]–[54]，其中 Ref. [53] 为 Banik et al. 2020 PRC 101, 044306；Chakraborty et al. 2023 明确说明其 `131Xe` 谱学分析重用 Banik 2020 Ref. [22] 数据，因此两文至少共享该实验谱系，不能计成两份独立 131Xe 实验确认。 | synthesis | indirect | Fig. 7 caption and Refs. [52]–[54], PDF pp. 7, 16; Chakraborty et al. 2023 Sec. II, PDF p. 2 and Ref. [22] | true |
| JN22-13 | TPSM Hamiltonian 中 QQ-force strength `χ` 按 self-consistent HFB condition 与四极形变 `ε` 关联；这是一条模型相互作用参数约束，Table I 的形变输入仍沿用既有工作。 | model-method | direct | Eq. (4), PDF p. 4; Table I, PDF p. 7 | true |
| JN22-14 | 以 Bhat et al. 2014 Eq. (3) 的近似 `γ=arctan(ε′/ε)` 约定核算 Jehangir Table I 的 `131Xe` `ε=0.160, ε′=0.090`，得 `29.36°`，与表列整数 `29°` 相符；这是模型输入的一致性检查，不是形状测量。 | synthesis | indirect | Table I, PDF p. 7; Bhat et al. 2014 Eq. (3), PDF p. 4 | true |

## 131Xe Isotone Comparison

131Xe 为 Z=54、N=77；它与 Hara Table 5 的 N=77 候选 134La、135Ce、136Pr 同中子数但质子数不同。此 TPSM paper 为同位素链 117–131Xe 的模型应用，不构成上述三核的直接模型覆盖。对 131Xe，Table I 的 gamma 参数沿用已有来源，Fig. 7 比较已发表 yrast 数据；yrare band 仍为理论预测。Fig. 7 所用数据含 Banik et al. 2020 PRC 101, 044306；Chakraborty et al. 2023 明确将其 131Xe 研究描述为对 Banik 数据的重新分析，因此至少这一实验谱系是共享的，不能把两篇理论/解释文章当作独立观测。

按 Bhat et al. 2014 Eq. (3) 给出的近似参数约定 `γ=arctan(ε′/ε)` 做独立算术核对：`arctan(0.090/0.160)=29.36°`，与 JN22 Table I 的整数值 `29°` 一致（JN22-14）。这只核对表中模型输入的内部数值关系，不从 `131Xe` 能谱推断实验形状；Bhat 文中其他核素的参数/文字不匹配仍按 BHA14-6 单独保留。

## Competing Interpretations and Limitations

- 第一 crossing 的质子/中子归因由扩展组态空间模型解释；它不是直接轨道占据测量。
- 131Xe 的实测 yrast energies/signature 可比较，但模型 gamma=29° 是输入。没有新 Coulomb-excitation、quadrupole-invariant 或其它独立形状数据。
- 131Xe yrare band、其 signature splitting、alignments 和 Qt 仍是 TPSM predictions；作者建议测 g-factors 以判断 proton/neutron 结构。
- Fig. 8–10 的振幅不能当作非正交组态的概率。此结果提醒模型选择不能只凭单个权重大小确定 configuration identity。
- 已有人审的 [[chakraborty-2023-131xe-wobbling-origin]] 认为 131Xe 负宇称 yrare sequence 的低 E2 成分更符合 signature partner、未发现 wobbling 实验信号；2022 TPSM 的能谱再现不新增实验，也不单独裁定该争议。
- JN22 Fig. 7 与 Chakraborty 2023 至少共享 Banik 2020 的 131Xe 数据谱系（JN22-12）；2023 的新分析提供对集体模式指认的反证，不等于第二次独立布居实验。

## Knowledge Impact and Learning Decision

Decision: supports angular-momentum-projected configuration mixing as an odd-neutron high-spin comparison tool and limits shape/configuration inference. It extends the basis and applies it to the N=77 isotope 131Xe, but does not cover 135Ce and does not add independent 131Xe measurements.

## Extracted Pages

- Nuclei: [[131xe]]
- Models: [[triaxial-projected-shell-model]]; angular-momentum projection is covered on that model page.
- Projects: [[a130-model-choice-card]]
