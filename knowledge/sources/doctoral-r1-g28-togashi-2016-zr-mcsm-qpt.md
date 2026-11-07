---
type: source
title: 'Togashi等 2016: Zr同位素形状相变与Type-II壳演化MCSM计算（PRL）'
aliases: [Togashi 2016 PRL Zr QPT, 'arXiv:1606.09056', PRL 117 172502]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Quantum Phase Transition in the Shape of Zr isotopes
authors: [Tomoaki Togashi, Yusuke Tsunoda, Takaharu Otsuka, Noritaka Shimizu]
journal: Physical Review Letters
year: 2016
volume: 117
pages: '172502'
doi: 10.1103/PhysRevLett.117.172502
arxiv: 1606.09056v2
canonical_source: https://doi.org/10.1103/PhysRevLett.117.172502
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G28/togashi-2016-zr-qpt.pdf
raw_sha256: f43431ebad67addfbefb521eed14c43f152fe5221ccc0d995d69a3d5aaa7b3e9
raw_storage_status: fully-archived-local
archive_required: true
nuclei: [90zr, 92zr, 94zr, 96zr, 98zr, 100zr, 102zr, 104zr, 106zr, 108zr, 110zr]
reactions: []
experiments: []
models: [mcsm, jun45, snbg3, vmu, t-plot, type-ii-shell-evolution]
observables: [energy-level, b-e2, deformation-beta2, occupation-number, espe]
methods: [monte-carlo-shell-model, constrained-hartree-fock-pes, angular-momentum-parity-projection]
tags: [shape-coexistence, quantum-phase-transition, type-ii-shell-evolution, mcsm, a100, zr-isotopes]
---

# Togashi等：Zr同位素形状相变与Type-II壳演化MCSM计算

## Bibliographic Record

- 题名：Quantum Phase Transition in the Shape of Zr isotopes
- 作者：Tomoaki Togashi, Yusuke Tsunoda, Takaharu Otsuka, Noritaka Shimizu
- 期刊：*Physical Review Letters* **117**, 172502 (2016)
- DOI：[10.1103/PhysRevLett.117.172502](https://doi.org/10.1103/PhysRevLett.117.172502)
- arXiv 预印本：[arXiv:1606.09056v2](https://arxiv.org/abs/1606.09056) [nucl-th] (5 Aug 2016)
- 本地底本：`raw/papers/gpt/query/20261108-foundations-G28/togashi-2016-zr-qpt.pdf`（5 页，SHA-256：`f43431ebad67addfbefb521eed14c43f152fe5221ccc0d995d69a3d5aaa7b3e9`）

## Scope and Reading Depth

### Covered scope

- 全文 5 页、公式、Table I、Figs. 1–4 及参考文献。
- 模型空间定义：8 质子轨道（$0f_{5/2}, 1p_{3/2}, 1p_{1/2}, 0g_{9/2}, 0g_{7/2}, 1d_{5/2}, 1d_{3/2}, 2s_{1/2}$）与 8 中子轨道（$0g_{9/2}, 0g_{7/2}, 1d_{5/2}, 1d_{3/2}, 2s_{1/2}, 0h_{11/2}, 1f_{7/2}, 2p_{3/2}$），不对轨道占据数做截断（Table I，PDF p.1）。
- 哈密顿量构建与微调记录：JUN45（$0g_{9/2}$ 及以下）、SNBG3（$T=1$）、VMU（其余有效相互作用）。明确记录作者对 $T=1$ 中心力（除 $1f_{7/2}, 2p_{3/2}$ 外）缩放 0.75 倍，并利用 $^{90-96}\text{Zr}$ 的 $2_1^+, 4_1^+$ 和 $^{94-100}\text{Zr}$ 的 $0_2^+$ 能级对 $0g_{9/2}$ 及以上的 $T=1$ 两体矩阵元进行了微调（PDF p.2）。
- 能级演化与形变跳变：$E(2_1^+)$ 在 $N=60$ 的下降，以及理论计算得到的 $B(E2)$ 趋势（Fig. 1，PDF p.2）。
- T-plot 势能面投影：$^{98}\text{Zr}(0_1^+)$ 为球形分布，$^{98}\text{Zr}(0_2^+)$ 呈长椭分布（$Q_0 \sim 350\text{ fm}^2$），$^{100}\text{Zr}(0_1^+)$ 呈长椭分布（Fig. 2，PDF p.3）。
- 轨道占据数与中子 ESPE 宽度变化：$\pi 0g_{9/2}$ 质子占据数在 $^{98}\text{Zr}(0_1^+)$ 为 0.4，在 $^{98}\text{Zr}(0_2^+)$ 为 3.5，在长椭态中为 3.5–5.5；中子 ESPE（$2s_{1/2}$ 至 $0g_{7/2}$）分布宽度从 $^{98}\text{Zr}(0_1^+)$ 的 $4\text{ MeV}$ 缩窄至长椭态的 $2\text{ MeV}$ 范围内（Fig. 3，PDF p.4）。
- $\pi 0g_{9/2} - \nu 0g_{7/2}$ 与 $\pi 0g_{9/2} - \nu 0h_{11/2}$ 相互作用中中心力与张量力的相干与相消性质（PDF p.4）。
- $^{100}\text{Zr}$ 与 $^{110}\text{Zr}$ 的理论能级图与计算 $B(E2)$ 值（Fig. 4，PDF p.4）。

### Not covered

- 未运行作者的 MCSM 源码，未复算基矢重叠积分与投影方差。
- 未核验作者引用的外部实验数据文献（如 Browne 2015、Raman 2001 等 100Zr 外部数据），不将图 1c 中的实验引用点升级为独立已核事实。

### Coverage caveats

- MCSM 采用量子蒙特卡洛与变分法选取投影 Slater 行列式基矢，属于变分近似选基对角化，非全组态空间完全严格对角化。
- 哈密顿量在选定参数后固定用于全链计算，但并非无拟合：$^{94-100}\text{Zr}$ 的 $0_2^+$ 能级已用于微调 $T=1$ 两体矩阵元。
- Fig. 3a 所示的质子轨道占据数是多体波函数投影期望值，属于模型输出，并非实测占据数。
- Fig. 4a 中标注在红色带内箭头旁的数字（如 73、101、42、59、83、118 等）为 MCSM 计算的 $B(E2)$ 预测值（单位 W.u.），非作者测量的实验值。

## Paper Question and Scientific Motivation

- 论文关注 Zr 同位素在 $N=60$ 附近出现的快速形状改变（$E(2_1^+)$ 下降约 6 倍），探讨其微观机制是否可由 Type-II 壳演化解释，并在有限核中考察其是否呈现量子相变（QPT）特征（PDF p.1）。

## Method and Design Logic

- 计算采用先进蒙特卡洛壳模型（MCSM），结合角动量与宇称投影。
- 模型空间包含 8 个质子轨道与 8 个中子轨道，无粒子数截断（Table I）。
- 相互作用综合 JUN45、SNBG3 与 VMU，有效电荷设为固定值 $(e_p, e_n) = (1.3e, 0.6e)$。
- 采用 T-plot 方法：将每个优化基矢的内禀四极矩 $(Q_0, Q_2)$ 投影在约束 Hartree-Fock 势能面上，圆圈面积表示该基矢与本征态的重叠权重（PDF p.2）。

## Key Evidence and Reasoning Chain

1. **能谱计算结果**：计算得到的 $E(2_1^+)$ 在 $N=60$ 显著下降，$R_{4/2}$ 接近转动极限（PDF p.2, Fig. 1a）。
2. **基态与激发态波函数形状**：T-plot 显示 $^{98}\text{Zr}(0_1^+)$ 集中在球形区域，而 $^{98}\text{Zr}(0_2^+)$ 呈长椭形变（$Q_0 \sim 350\text{ fm}^2$）；$^{100}\text{Zr}(0_1^+)$ 呈长椭形变，原球动态对应于计算出的高激发 $0_4^+$ 态（PDF p.3, Fig. 2）。
3. **模型占据数与单极漂移**：从球形 $^{98}\text{Zr}(0_1^+)$ 到长椭 $^{98}\text{Zr}(0_2^+)$，计算的 $\pi 0g_{9/2}$ 占据数从 0.4 增至 3.5；在 $^{100,110}\text{Zr}$ 长椭态中达到 3.5–5.5（PDF p.4, Fig. 3a）。
4. **中心力与张量力的协同与竞争**：中子 ESPE 中从 $2s_{1/2}$ 到 $0g_{7/2}$ 的能量范围从球态的 $4\text{ MeV}$ 压缩到长椭态的 $2\text{ MeV}$ 以内（PDF p.4, Fig. 3b）。对于 $0g_{9/2}-0g_{7/2}$，张量力与中心力相干（coherent），使 $\nu 0g_{7/2}$ 下拉约 $2\text{ MeV}$；对于 $0g_{9/2}-0h_{11/2}$，张量力与中心力相消（destructive），净效应仍为弱下拉（PDF p.4）。
5. **相变与组态差异**：作者指出球态与长椭态涉及较多核子的粒子-空穴重排，导致两态混合受抑，从而在能态相交时呈现出跳变特征（PDF p.4）。

## Summary

Togashi 等（2016）利用大空间 MCSM 计算了 $N=50-70$ 的 Zr 同位素。计算采用 8 质子+8 中子无截断模型空间，基于 JUN45、SNBG3 与 VMU 构建哈密顿量，并利用轻核 $2_1^+, 4_1^+$ 及 $^{94-100}\text{Zr}$ 的 $0_2^+$ 进行微调后固定。计算展示了 $N=60$ 处 $E(2_1^+)$ 的下降与长椭基态的出现。作者将这一突变解释为 Type-II 壳演化效应：跨次壳质子占据 $\pi 0g_{9/2}$ 触发中心力与张量力的单极效应，使中子 ESPE 展宽由 $4\text{ MeV}$ 缩窄至 $2\text{ MeV}$ 以内，增强了四极形变驱动能力；两态间显著的组态差异抑制了混合，呈现出快速的能态交叉。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TOG16-1 | MCSM 采用 8 质子+8 中子模型空间（Table I），不对轨道占据数做截断。 | computational-boundary | direct | PDF p.1, Table I | false |
| TOG16-2 | 哈密顿量利用 $^{90-96}\text{Zr}$ 的 $2_1^+, 4_1^+$ 及 $^{94-100}\text{Zr}$ 的 $0_2^+$ 能级对 $0g_{9/2}$ 及以上的 $T=1$ 两体矩阵元进行微调后固定。 | computational-setup | direct | PDF p.2, col. 1 | false |
| TOG16-3 | 计算的 $E(2_1^+)$ 在 $N=60$ 较 $N=58$ 下降约 6 倍，理论预测的 $^{100}\text{Zr}$ 带内 $B(E2; 2_1^+ \to 0_1^+)$ 值为 $73\text{ W.u.}$。 | model-result | direct | PDF p.2, Fig. 1; p.4, Fig. 4a | false |
| TOG16-4 | T-plot 显示 $^{98}\text{Zr}(0_1^+)$ 为球形分布，$^{98}\text{Zr}(0_2^+)$ 为长椭分布（$Q_0 \sim 350\text{ fm}^2$），$^{100}\text{Zr}(0_1^+)$ 变为长椭基态。 | model-result | direct | PDF p.3, Fig. 2 | false |
| TOG16-5 | 计算的 $\pi 0g_{9/2}$ 占据数在 $^{98}\text{Zr}(0_1^+)$ 为 0.4，在 $^{98}\text{Zr}(0_2^+)$ 为 3.5，在长椭态中为 3.5–5.5。 | model-result | direct | PDF p.4, Fig. 3a | false |
| TOG16-6 | 中子 ESPE（$2s_{1/2}$ 至 $0g_{7/2}$）范围在 $^{98}\text{Zr}(0_1^+)$ 为 $4\text{ MeV}$，在长椭态中压缩至 $2\text{ MeV}$ 以内；$0g_{9/2}-0g_{7/2}$ 处中心力与张量力相干下拉约 $2\text{ MeV}$，$0g_{9/2}-0h_{11/2}$ 处两者相消。 | theoretical-mechanism | direct | PDF p.4, col. 1, Fig. 3b | false |
| TOG16-7 | 作者将 $N=60$ 处的突变解释为 Type-II 壳演化所致的能级交叉，组态差异导致两态混合受抑，呈现有限核量子相变特征。 | author-interpretation | direct | PDF p.3 col. 2; p.4 col. 1 | false |

## Nuclear Structure Information

- 核素范围：$^{90}\text{Zr}$ 至 $^{110}\text{Zr}$（偶偶核）。
- 重点结构：$^{98}\text{Zr}$（球形基态 $0_1^+$ 与长椭 $0_2^+$ 共存）；$^{100}\text{Zr}$（长椭基态 $0_1^+$ 与高激发球形候选态 $0_4^+$）。

## Authors' Interpretation

- 作者将 $N=60$ 处的快速形状改变归因于 Type-II 壳演化与四极相互作用的互促，认为跨壳粒子-空穴激发改变了局部单粒子能级，从而有利于形变产生。
- 作者认为两组态之间涉及较多核子的激发重组，使得相互混合较小，形成陡峭的相变行为。

## Model Results

- 有效电荷设为固定值 $(e_p, e_n) = (1.3e, 0.6e)$。
- 理论计算给出的 $^{100}\text{Zr}$ 带内跃迁强度为 $B(E2; 2_1^+ \to 0_1^+) = 73\text{ W.u.}$、$B(E2; 4_1^+ \to 2_1^+) = 101\text{ W.u.}$（Fig. 4a 理论值）。

## Competing Interpretations and Limitations

- 对比模型：作者在 Fig. 1d 与 Fig. 2 中指出现有 IBM、HFB 与 FRDM 模型在 Zr 同位素链中大多呈现较为平缓的形变演化。
- 局限性：哈密顿量微调包含了 $^{94-100}\text{Zr}$ 的 $0_2^+$ 能级，非纯粹第一性无参预报；MCSM 轨道占据数为多体期望值，非实验实测单粒子谱因子。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | MCSM 计算表明质子占据 $\pi 0g_{9/2}$ 可通过中心力与张量力改变中子 ESPE 展宽，为形变提供有利条件。 | PDF pp.1–4, Figs. 1–3 | unreviewed |
| AR-2 | Assumptions and dependencies | 依赖微调后的固定有效哈密顿量与固定有效电荷 $(1.3e, 0.6e)$。 | PDF p.2, col. 1 | unreviewed |
| AR-3 | Transfer conditions | 适用于次壳闭合邻近存在高 $j$ 独特宇称轨道的核区（如 Sr, Zr）。 | PDF p.4, col. 2 | unreviewed |
| AR-4 | Failure conditions | 若没有次壳阻挡或 Fermi 面处于大单粒子能隙深处无法激发，该壳演化机制的突变特征将减弱或消失。 | PDF p.4, col. 2 | unreviewed |
| AR-5 | Reverse/falsification test | 检验理论预言的高激发残余球态（如 $^{100}\text{Zr}$ 的 $0_4^+$ 态）是否存在。 | PDF p.2, Fig. 1b; p.4, Fig. 4a | unreviewed |
| AR-6 | Research-question decision | 作为 A≈100 Zr 同位素形状演化微观理论计算的关键参考条目。 | TOG16-1–7 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 建立了 Togashi 2016 MCSM 计算关于 Zr 突变的原始证据与参数约束记录。
- Effect of this source: supports & theoretical-input-contract。
- Reason: 澄清了微调数据集范围（含 94–100Zr 0_2+）及 ESPE 展宽变化的字面事实。
- Persistence decision: persistent source for [[doctoral-r1-g28-a100-shell-shape-20261108]]。
- Review state: unreviewed.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[doctoral-r1-g28-singh-2018-98zr-lifetimes]] | 理论预报 $^{98}\text{Zr}$ 基态小 $B(E2)$ 与长椭 $0_2^+$，为 Singh 2018 实验所对比。 |
| foundational-background | [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]] | 本文为 Otsuka 2023 讨论 Type-II 壳演化与核自组织的主要范例之一。 |

## Human Review Triage

### P0
none identified.

### P1
none identified.

### P2/P3
- P2: 区分图 4a 的理论计算 $B(E2)$ 预测值与实验测量值；区分模型计算占据数与实验实测光谱因子。

## Extracted Pages

- Nuclei: `90zr`, `92zr`, `94zr`, `96zr`, `98zr`, `100zr`, `110zr`
- Concepts: `type-ii-shell-evolution`, `quantum-phase-transition`, `t-plot`, `effective-single-particle-energy`
- Models: `mcsm`, `jun45`, `snbg3`, `vmu`

## Non-source Notes and Follow-up

- 专属于 G28 独立研究任务。
