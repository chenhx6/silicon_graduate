---
type: source
title: "Roy et al. 2011 - Systematics of antimagnetic rotation in even-even Cd isotopes"
aliases: [Roy 2011 110Cd antimagnetic rotation, Roy 2011 PLB Cd systematics]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: experiment-and-theory
reading_depth: deep-read
title_original: "Systematics of antimagnetic rotation in even–even Cd isotopes"
authors: [Santosh Roy, S. Chattopadhyay, Pradip Datta, S. Pal, S. Bhattacharya, R. K. Bhowmik, A. Goswami, H. C. Jain, R. Kumar, S. Muralithar, D. Negi, R. Palit, R. P. Singh]
journal: "Physics Letters B"
year: 2011
volume: 694
pages: "322-326"
doi: "10.1016/j.physletb.2010.10.018"
citation_key: Roy_2011_PLB
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-10-28
canonical_source: "Roy et al., Phys. Lett. B 694, 322 (2011)"
raw_file: "raw/papers/gpt/day26-20261028/roy-2011-cd110-systematics-plb.pdf"
raw_sha256: "2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a"
nuclei: [110Cd, 106Cd, 108Cd]
reactions: [96Zr-18O-4n]
experiments: [INGA, DSAM-lineshape]
models: [classical-particle-plus-rotor, AMR-plus-core-rotation, two-shears]
observables: [level-lifetime, BE2, dynamic-moment-of-inertia, alignment]
methods: [DSAM, lineshape-analysis, gamma-gamma-coincidence]
tags: [110Cd, antimagnetic-rotation, DSAM, shears-mechanism, even-even-Cd]
---

# Systematics of antimagnetic rotation in even–even Cd isotopes

## Bibliographic Record

- S. Roy *et al.*, *Phys. Lett. B* **694**, 322–326 (2011), DOI `10.1016/j.physletb.2010.10.018`.
- 规范文件：`raw/papers/gpt/day26-20261028/roy-2011-cd110-systematics-plb.pdf`（5 页，SHA-256 `2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a`）。

## Scope and Reading Depth

- 全文 5 页精读（pp. 322–326）：实验测量（`96Zr(18O, 4n)110Cd` 反应，70 MeV，INGA 阵列 18 叶 clover 探测器，LINESHAPE 寿命分析）、Table 1 寿命与 B(E2) 提取、经典两粒子加转子模型公式（Eqs. 1–6）、`106,108,110Cd` 系统学对比与总结。
- 局限与未覆盖：阻止本领（stopping power）系统误差未计入拟合误差（原文注明可能达 20%）；高自旋 26+ 及以上仅得到顶层有效寿命。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RO11-1 | 测得 110Cd 准基态能带 16+ 至 24+ 态平均寿命分别为 tau = 0.36(3)、0.23(3)、0.17(3)、0.21(7) 和 0.27(7) ps；对应带内 E2 跃迁强度呈现自旋上升下的稳步平缓下降：B(E2) = 0.14(1)、0.12(2)、0.11(2)、0.09(3) 和 0.06(2) (eb)^2。 | experimental-fact | direct | p.324, Table 1 | true |
| RO11-2 | 与邻近偶偶核 106,108Cd 的“纯反磁转动”（核心惯量 Im=0）不同，110Cd 的高自旋反磁转动由对称双剪刀机制与核心集体转动共同驱动，核心转动惯量拟合为 Im = 19.5 MeV^-1 hbar^2（约半刚体转子值）。 | model-interpretation | direct | pp.325-326, Fig. 4 | true |
| RO11-3 | 核心转动与双剪刀闭合的耦合自然解释了 110Cd 在 hbar omega = 0.65–0.72 MeV 处出现的 8 hbar 顺对齐增益，以及 B(E2) 未发生骤降而是在 0.06–0.14 (eb)^2 维持平缓过渡平台的实验事实。 | model-result | direct | pp.325-326, text and Fig. 4(b) | true |
| RO11-4 | 测得的 1075、1224、1323、1314 keV 跃迁能量与能级差严格对应于 NNDC ENSDF 数据集 110048001 中的 Band B；导出的动态惯量跃迁比 J^(2)/B(E2) 落在 116–341 hbar^2 MeV^-1 (e^2 b^2)^-1，远高于常规集体转动核（15–40）。 | derived-observable | direct | Table 1; ENSDF 110048001 | true |

## Summary

Roy et al. (2011) 报告了 110Cd 高自旋能级的多探测器 DSAM 线形寿命分析与反磁转动系统学研究。实验确立了 16+ 至 24+ 能级的寿命与递减的 B(E2) 跃迁几率，并通过经典粒子加转子模型证明：110Cd 属于双剪刀反磁转动与核心集体转动耦合的典型案例，成功解释了其转动惯量大、顺对齐增益显著以及 B(E2) 平缓过渡的独特性质。

## Competing Interpretations and Limitations

- 实验提取的能级寿命直接依赖阻止本领数据库，存在约 20% 的系统不确定度包络。
- 经典的粒子加转子模型中，粒子-空穴排斥互作用参数 V_pinu ~ 1.2 MeV 与空穴-空穴互作用参数 V_pipi ~ 0–0.2 MeV 属于唯象参数，未包含三维微观自洽平均场形变自适应涨落。
- 跃迁能量接近的 1323 与 1314 keV 线形存在重叠，需借助门控矩阵解耦，高自旋端有效侧馈寿命存在模型假设。

## Model Dependence

模型采用两对称剪刀闭合几何 I = j_p + 2 j_h cos(theta)，其中质子空穴 pi(g9/2)^-2 构成剪刀双叶，两对准中子 nu(h11/2)^2 对齐于转动轴。电四极跃迁几率正比于 sin^4(theta)。核心集体转动对频率的贡献由 omega = omega_rot - omega_sh 给出。

## Knowledge Impact and Learning Decision

- Effect: `supports` [[antimagnetic-rotation]]、[[shears-mechanism]] 与 [[octupole-mr-amr-evidence-gradient]]；为 110Cd 提供第一手实验寿命与 B(E2) 原始依据。
- Review state: Codex self-audited; not `human-reviewed`.

## Extracted Pages

- Concepts/notes: [[antimagnetic-rotation]], [[shears-mechanism]], [[octupole-mr-amr-evidence-gradient]].

## Sources

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

Codex source self-audit; all new claims retain `needs_review: true`.
