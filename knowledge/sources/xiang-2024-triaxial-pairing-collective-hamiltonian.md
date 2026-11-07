---
type: source
title: "Xiang 等 2024：128Xe 的三轴形状—配对集体 Hamiltonian"
aliases: [Xiang 2024 TPCH, 128Xe triaxial pairing collective Hamiltonian]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: read
title_original: "Coupling of shape and pairing vibrations in a collective Hamiltonian based on nuclear energy density functionals. II. Low-energy excitation spectra of triaxial nuclei"
authors: [J. Xiang, Z. P. Li, T. Nikšić, D. Vretenar, W. H. Long, X. Y. Wu]
journal: Physical Review C
year: 2024
volume: "109"
pages: "044319"
doi: 10.1103/PhysRevC.109.044319
arxiv: 2312.01791v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.109.044319
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g41-pairing-shape/xiang-2023-collective-hamiltonian-triaxial-pairing-128xe-arxiv2312.01791v1.pdf
raw_sha256: bc2c7be79c87445bcd14c105971f8c3020cbc2744e9a44575bd77741c8b2a5ba
raw_storage_status: archived-local
archive_required: true
nuclei: [128xe]
reactions: []
experiments: []
models: [triaxial-pairing-collective-hamiltonian, pc-pk1, atdhfb-cranking]
observables: [excitation-energy, be2, rho2-e0]
methods: [constrained-cdft, collective-quantization, zero-point-energy]
tags: [doctoral-foundations, pairing-vibration, triaxiality, gamma-softness]
---

# 配对与形状共同运动，并不等于只有一个“配对修正”

## Bibliographic Record

出版题名、卷年和 DOI 由归档 Crossref JSON 核实；实际阅读底本为
`2312.01791v1`，**11 个物理页**，页边标记 2023-12-04，内部 Dated 为
2023-12-07。出版记录为 2024-04-16。不声称已与出版版逐式比对。

## Scope and Reading Depth

- Completed reading_depth: read。
- Covered scope: pp. 1–7 正文主线、Figs. 1–8、Table I、Eqs. (1)–(26)；
  另定向核对 Appendix 的 cranking 近似、质量和 ZPE 表达式。
- Not covered: 附录全部代数独立重推、原生产代码、连续网格收敛、理论误差、
  参考实验的独立重新评价，以及最终出版版是否修改了预印本的排印问题。
- Worker G41 初稿经总控缩减重建；未采纳的阈值和机制归因不是本文结果。

## Paper Question and Scientific Motivation

作者把已有的四极—配对框架扩展到三轴形状，考察
\((\beta,\gamma,\alpha)\) 对 128Xe 低能谱和跃迁的影响。
本篇的 \(\alpha=\langle\hat P\rangle\) 是所定义配对算符的期望，
不是以 MeV 为单位的单一 BCS 能隙，也不是配对规范角。
完整集体坐标还含三个 Euler 角；不能把它称为六个振动坐标。

## Method and Design Logic

PC-PK1 粒子—空穴道、BCS 加可分离配对道给出约束参考态。
六个振动质量函数构成含 β 几何因子的三阶矩阵，三条转动惯量用 IB 公式，
振动质量用 ATDHFB cranking 矩公式。模型包含形状—配对质量交叉项，
不能将带间偏差归因于“原文没有这些交叉项”。
配对强度相对于所引原参数上调 6%，不是无经验输入的从头计算。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| X24-1 | 动力学坐标为 β、γ、α 和空间 Euler 角；振动质量含 \(B_{\beta\gamma},B_{\beta\alpha},B_{\gamma\alpha}\)，配对坐标不是规范角。 | model-result | direct | p. 2, Eqs. (1)–(6) | false |
| X24-2 | 转动惯量采用 IB；振动质量采用 cranking；Appendix 明确舍去时间奇相互作用矩阵 E₁。它不等于完整 TV 响应。 | model-result | direct | p. 2, Eqs. (7)–(12); pp. 7–8, Eqs. (23)–(44) | false |
| X24-3 | 本计算使用 \(G=-771.68\ \mathrm{MeV\,fm^3}\)，相对所引原配对参数上调 6%。 | model-result | direct | p. 3, Sec. III 首段 | false |
| X24-4 | 相比仅含 β、γ 的结果，加入动态配对总体压缩低能谱；0₂、0₃ 的模型结构与 E0 强度分配交换。 | model-result | direct | pp. 3–6, Figs. 4–7 及正文解释 | false |
| X24-5 | 对同一 TPCH，加入 ZPE 是另一项比较：极小点向较大 α 移动，谱向较高能量扩展；作者报告所列能量增加约 18%–50%。 | model-result | direct | pp. 6–7, Fig. 8, Table I | false |
| X24-6 | Table I 中 2₁⁺ 的 W/O、W/ZPE、实验列为 0.202、0.247、0.443 MeV；2γ⁺ 对应 0.770、0.940、0.970 MeV。改善与残余偏差同时存在。 | model-result | direct | p. 7, Table I | false |
| X24-7 | 作者把部分 γ 带到基态带 E2 的减弱联系于增强惯量导致的基态带压缩，并提出未来配对转动可能改善；这是作者的待检验解释。 | author-interpretation | direct | p. 5 末段至 p. 6 首段 | false |

## Summary

“加入动态配对压缩谱”与“扣除 ZPE 扩展谱”是不同的模型操作。
不能把它们压成一种不带条件的配对效应，也不能从仍然偏低的
\(E(2_1^+)\) 唯一判定缺少哪个时间奇项。
本文提供一个具体的共同自由度应用，同时表明已有三轴—配对联合研究，
仅提出这类模型不构成本任务的新颖性。

## Competing Interpretations and Limitations

本文没有给出实核惯量张量的直接测量。谱与跃迁比较仍依赖 EDF、配对、
集体空间、cranking、ZPE 和状态映射。
配对振动坐标的软性不能直接当作粒子数规范旋转的零频惯量。
E0 强度还取决于波函数的节点、重叠及半径算符，不是单一 gap 量尺。
Fig. 6 所谓二维 projections 实际固定第三坐标在峰值，并非对其积分的边缘分布；
比较图形时须保留这一条件。

## 原件排印与初稿纠错

- p. 3 Eq. (19) 的预印本印成 \(1/(2I)\)，标准约化跃迁定义的分母为
  \(2I+1\)。本任务标记为底本排印/约定边界，没有凭此推断作者程序采用了错误定义，
  也没有静默修改原始 PDF。正式引用前需查出版版或勘误。
- Eq. (14) 印为 \( \tfrac14\mathrm{Tr}[M_{(3)}^{-1}M_{(2)}]\)，
  不采用 worker 初稿的 \(M_{(1)}^{-1}M_{(2)}\)。
- Fig. 7 caption 明确图中数字是 E2 的 W.u.。初稿把其中 0.03/11.6 等
  当成精确 \(\rho^2(E0)\times10^{-3}\)，此读取已撤回；E0 的依据是 Fig. 5(b)
  和正文的定性分配变化，不保留伪造的精确值。
- “E(2₁⁺)偏低证明忽略 TV 导致惯量过大”不是作者在该处建立的因果结论，
  本任务不采纳。配对塌缩必产生刚体流、固定转移/E0 分类阈值等也不来自本篇。

## Knowledge Impact and Learning Decision

与 [[nomura-2021-pairing-triaxial-vibrations-gamma-soft]] 形成方法比较：
静态能面映射到 IBM，与具有显式坐标质量矩阵的 TPCH 是不同建模合同。
Nomura 页原有 40% 惯量及模型空间限制已经存在，本轮不把重读当成新发现。
跨区迁移与竞争解释进入
[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。

## Agent Self-audit Triage

P0：身份、原件哈希、Table I 三列和模型近似已回原件；
Eq. (19) 的底本问题隔离，未冒称修正了作者计算。
P1：不从压谱唯一归因 TV；图中 E2/E0、条件截面/边缘分布、α/gap/规范角
分别处理。生产代码、Cov 及最终版变更未恢复。
P2/P3：citation key 未与已生成 BibTeX 唯一匹配，保持空值。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
