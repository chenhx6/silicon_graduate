---
type: project
title: "30天后核结构论文 prospectus"
aliases: [post-30-day paper prospectus, nuclear-structure paper queue]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
project_stage: post-30-day-prospectus
confidentiality: private
nuclei: [131xe, 135pr, 135nd, 144ba, 146ba]
tags: [paper-prospectus, nuclear-structure, evidence-gate, l3, l4-readiness]
---

# 30天后核结构论文 prospectus

## Agent active summary

本页把30天学习计划中已经形成的证据地图压缩为五个可投稿研究候选。它们是研究队列，不是已完成稿件；每个候选都必须重新经过 `system/paper-evidence-gate.md`，补齐 source identity、locator、独立性、反证和适用条件。

## Research Question

在现有 Wiki 的实验谱学、混合比、偏振、寿命、形变和响应合同基础上，哪几条路线最可能在30天后形成有证据边界的期刊稿件？选择标准是：问题明确、已有 primary source、存在竞争解释、可写出 falsifier，并且缺失输入不会被模型或 toy 计算掩盖。

## Current Hypotheses

- P1 `135Pr` 最可能先形成方法学论文，因为支持链与反方链的差异已经落在可定义的观测量和响应合同上。
- P2 `131Xe` 最可能先形成对象身份/可识别性论文，因为当前主要增量是撤回过度解释并明确缺失 companion observables。
- P3/P4 需要更多真实绝对强度、寿命或多态 E3 输入；P5已有真实表格falsifier，但外部方法学新颖性仍需核查。

## Evidence Available

现有证据来自 `knowledge/sources/` 的直接论文、评估数据和方法原件，已在各 candidate 的 project/synthesis/source 页按 locator 分层。论文 prospectus 只汇总这些入口，不把 project、日报或 toy 工件当作新的独立实验。

## Candidate Queue

| 优先级 | 候选题目 | 研究核心 | 当前状态 | 最小新增输入 |
|---|---|---|---|---|
| P1 | `135Pr` common-response evidence audit | 统一 Matta–Lv–Sensharma 的 `δ` 分支、`P/A`、`R_ac`、取向和谱系，检验 wobbling/chirality/TiP 排序 | L3 paper blueprint；既有证据冲突清楚，缺共同 response/Cov | 逐角净峰、sideband、`a(E)`/`Q(E)`、polarization counts、gate acceptance、联合 `Σ` |
| P2 | `131Xe` low-spin identity and branch boundary | 2020/2023 逐态对象交叉、795-keV宇称版本、RDCO双根和同母态强度可识别性 | L3 milestone；对象和缺口已固化，未裁决宇称/模式 | 1983 AD原件或逐线 raw/response、794.8-keV独立宇称判据、882偏振/AD和partner寿命 |
| P3 | `135Nd/134Pr` partner-resolved absolute EM benchmark | 绝对 `B(E2)`/`B(M1)`、寿命、crossing、γ-softness 与手征/混合竞争解释 | L3/L4 candidate；多条寿命证据已有，矩阵和共同协方差未闭合 | 同一 state mapping 下的完整 EM 矩阵、寿命 producer、feeding/systematic covariance |
| P4 | Cross-mass octupole evidence ladder | 直接 E3、E1 网络、交替宇称和 PES 形变之间的证据等级与静态/动态边界 | synthesis/data-map candidate；144/146Ba和220Rn/224Ra已有锚点 | 逐条 primary locator、统一跃迁方向/单位、分支归一、共同系统误差和更多多态 E3 |
| P5 | P-ADO shared-alignment null falsifier | 用Zobel 1983同一跃迁十行真实表格检验跨reaction共享`σ/J`的可识别性 | 有真实表格结果；方法学新颖性和外部文献差异仍需审计 | projectile-family分层、原始Cov/coverage或feeding-aware公开输入 |
| P6 | `131Ce/133Ce` collective-mode identifiability boundary | 用 state identity、连接线 `δ`/偏振、寿命、绝对 EM strengths 和 model sensitivity 区分 signature/configuration、γ-soft、wobbling、chirality 与 shape coexistence | L3 decision-boundary candidate；已有谱系矩阵但缺目标核 companion observables | Bands 1–7 的逐线 `δ`/偏振、partner-resolved lifetime/`B(E2)`/`B(M1)`、HD–ND linking 和统一 covariance |

## Candidate 1: 135Pr

已有 `knowledge/projects/135pr-wobbling-controversy.md`、
`knowledge/research-notes/135pr-mixing-branch-input-contract.md` 将三条证据链分开：
Matta 的大 `|δ|` 与 `A`、Lv 的独立 `P-R_ac` 小 `|δ|`、Sensharma 2026 对旧
角分布在固定 `σ/I=.2` 下的条件 χ² 偏好。最重要的独立性结论是支持链论文和
Sensharma 新分析共享 Gammasphere 谱系，而 Lv 是独立 counter chain；不能按论文
数量加权。

2026 accepted-record 的 Chen et al. Bayesian inertia paper 增加了一个理论竞争层：
公开 abstract 只确认 CQPC、Metropolis–Hastings MCMC、energy-only constraints 和固定
电磁输入的条件预测；原始 manuscript、likelihood、priors、posterior samples、固定
EM 输入及 competing-model evidence 尚未获得。它可以作为 P1 的 model-conditioning
control，不能被写成对 Matta/Lv/Sensharma 的共同 response 重析，也不能把
within-model posterior stability 当作 wobbling 机制的模型间排他证据。对应 source
边界见 [[chen-2026-bayesian-inertia-wobbling-135pr]] `CH26-B1`–`CH26-B7`。

可投稿的最低主张是：公开观测存在分支冲突，分支排序依赖 response、取向、门、
背景和协方差；在这些输入未公开前，不能宣称统一 raw 重析已完成。若获得真实
输入，主分析应预先冻结 state identity、branch parameterization、nuisance profile
和 holdout companion。falsifier 是所有候选分支的 profiled prediction set 与数据
不相交；否则保留“不能唯一选根”。

`knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md`
进一步冻结了三条核心线（747、813、450 keV）、`ξ=arctan(δ)` 分支参数、逐实验
nuisance 和 Lv `747.3-keV P–R_ac` leave-EM-out holdout。它是 future-input
analysis contract，不代表当前已有 raw counts、response 或联合协方差。

Lv et al. 2025 adds a same-lineage `135Nd` extension
([[135nd-2025-tipped-precession-same-lineage-extension]]): a new `17/2−_3` state,
band T and `B(E2,752)/B(E2,908)=2.0(5)`. It strengthens the transition-identity
and relative-E2 layer for P3, while leaving the independent-lifetime, absolute-strength
and covariance gates open.

### 2026 model-frontier controls

Recent 2026 theory papers expand the competing-model space that a future `135Pr` or
`131Ce/133Ce` audit must consider:

| Primary record | Model-level result | Evidence boundary |
|---|---|---|
| Zhang, Qi & Wang, *Phys. Rev. C* **114**, 044312 (2026), DOI `10.1103/64zl-b9br` | Particle-rotor calculations propose coexistence of pseudospin-partner bands and a wobbling excitation for a `π(g7/2,d5/2)` configuration | Accepted/published abstract-level model evidence; no new experiment or `135Pr` response |
| Chen et al., *Phys. Rev. C* **114**, 014324 (2026), DOI `10.1103/f2zp-rb6f` | Core-quasiparticle calculations find γ-soft cores support longitudinal wobbling, while rigid triaxial cores can support low-spin transverse wobbling; interband `B(E2)out` is proposed as a discriminator | Model prediction and proposed observable; does not measure γ softness or settle an experimental branch |
| Wang, Chen & Li, *Phys. Rev. C* **113**, L061301 (2026), DOI `10.1103/14kh-p5g3` | Five-dimensional collective-Hamiltonian calculations for `122–128Xe` reproduce selected energy/staggering and `B(E2)` systematics, then interpret odd-spin γ-band geometry as wobbling-like | Theory–data comparison remains model-conditioned; calculated geometry is not a direct angular-momentum measurement |
| Chen et al., *Phys. Rev. C* **114**, 014336 (2026), DOI `10.1103/jlfb-m2qd` | Octupole core-quasiparticle calculations predict transverse-to-longitudinal wobbling evolution with spin and configuration-dependent critical spin | Model-only configuration study; useful as a competing forward model, not as an experimental octupole-wobbling observation |

These records revise the future model comparison layer: a branch audit should include
signature/pseudospin partners, γ-soft longitudinal wobbling and octupole
configuration-driven mode changes where the state identity and observables permit.
They do not relax the P1/P6 evidence gate; model geometry, predicted `B(E2)out` or
critical spin cannot replace measured response, lifetime, polarization, absolute
strength and an independent holdout.

对 Chen 2026 的安全跟进是一个 matched-input、leave-EM-out predictive test：用相同
公开能量数据和声明的竞争模型预测预先指定的一个 interband E2 fraction，并共同传播
EM nuisance；若只有不对称区间，则做 interval sensitivity，不伪造 Gaussian likelihood。
这是一项未来分析设计，不能称作已复现 Chen posterior 或已完成的新实验结果。

## Candidate 2: 131Xe

`knowledge/projects/131xe-low-spin-partner-crosswalk.md` 已把2020 B5、2023
yrast/yrare逐态对应和近能量异态拆开；`knowledge/research-notes/131xe-1601-parity-version-boundary.md`
保留795-keV E1与766-keV无偏振的宇称边界；`knowledge/research-notes/131xe-same-parent-strength-identifiability.md`
说明两个 `B` 商共享 `r` 与 `δ`，不能独立计票。该候选适合写成严谨的
evidence-boundary/branch-identifiability paper，前提是标题和结论明确写“未闭合的
宇称与响应条件”，而不是把候选模式写成证明。

## Candidate 3: 135Nd/134Pr

`knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`、
`knowledge/projects/chirality-shape-coexistence-companion-matrix.md` 和
`knowledge/projects/nuclear-chirality-and-multiple-chiral-doublet-bands.md` 已经
建立寿命、`B(M1)/B(E2)`、能谱、伙伴身份和 shape-mixing 的竞争矩阵。
`134Pr` 的寿命异常可以削弱理想静态手征，但仍需区分动态涨落、configuration
mixing 和 crossing。投稿前必须把同一母态、同一 operator convention、feeding 和
systematic covariance 冻结；不能用不同论文的相似 `B` 比值拼出一条独立证据向量。

Lv et al. 2025 的 `135Nd` 同谱系扩展新增 `17/2−_3`、band T 和
`B(E2,752)/B(E2,908)=2.0(5)`，可补强 P3 的 transition identity 与相对 E2 层。
由于它复用 2021 JUROGAM II 反应/阵列谱系，不能作为独立实验确认，也不能替代
partner-resolved lifetime、绝对 `B` 矩阵或共同 covariance。

## Candidate 4: Octupole

`knowledge/synthesis/shape-observable-matrix.md` 和
`knowledge/synthesis/octupole-and-rare-electromagnetic-decay.md` 已把直接 E3、
E1 links、E1 moment、交替宇称和模型 PES 分层。144/146Ba 中相近的直接 E3 中心值
与显著不同的 E1 moment，以及220Rn/224Ra中E2/E3矩阵元不能单独区分静态投影和
八极振动，是适合写成 evidence-ladder 论文的反例。投稿稿件必须保留作者解释、
模型结果和实验直接量的分层，不把 `β3` 或“梨形”从单条跃迁强度直接推出。

新取得的公开全文增加了两个可复核锚点：`148Dy` 的 GRIFFIN fast-timing/branching
分析给出 `B(E3;3−→0+)=46(3) W.u.`，并同时报告一个弱 `B(E1)` 分支；`224Ra`
的 GRIFFIN/PACES lifetime/内转换分析给出多条 `B(E1)`、`B(E3)` 和 `Q_10`，
且作者将其与先前 Coulomb-excitation 结果作为不同 observable 的独立验证。它们
适合加入 P4 的 E3-first 与 E3/E1-separation 图表，但必须保留逐实验 response、
feeding、IC 和 joint covariance，不把两种方法的误差直接合并。

`90Zr` 又提供一项方法分离的交叉检查：2024 lifetime/plunger 正文报告
`B(E3)=16(3) W.u.`，2026 safe Coulomb-excitation 正文报告
`19.6^{+1.7}_{-1.6} W.u.`。它们可以构成 P4 的“方法一致性”图，但在完成 source
version、branching、response、feeding 和 covariance 对齐前，不计算合并平均、不写
“独立精确确认”。

Crossref also identifies a 2026 `209Pb` paper on a new `15/2−` octupole-state
lifetime measurement (DOI `10.1016/j.nuclphysa.2025.123273`). It is a metadata-only
route in the current window: no lifetime number, branching table, response or
covariance was acquired, so it extends the candidate pool without changing the P4
evidence ranking. The access boundary is recorded in
[[octupole-2025-2026-new-e3-access-boundary]].

## Candidate 5: P-ADO

`knowledge/research-notes/pado-shared-alignment-null-profile.md` 对 Zobel 1983
同一 `958-keV` 纯 E2 跃迁的十个 projectile/beam-energy 条件做了真实表格
profile：共同 `sigma/J` 和共同 `rho` 在 `tau=1` 下没有共同区间，95%二维参考域
仍需约 `tau=1.72`。这为“不能把跨 reaction alignment 当一个共享 nuisance”
提供了可复核的条件性 falsifier。

该候选的安全论文形态是 P-ADO 方法/数据合同审计；它不否定 P-ADO、Zobel 单行
fit 或 feeding-aware 模型，也不提供实验 coverage。下一步应把 `alpha` 与 `12C`
family 分开 profile，并与 Ionescu 的 discrete-feeding boundary 对照；只有取得
真实 covariance 或公开 event-level input 后，才升级为正式 likelihood/coverage 论文。

## Candidate 6: `131Ce/133Ce` collective-mode identifiability

`knowledge/research-notes/131ce-133ce-mode-identifiability-boundary.md` 将这个候选限制为一个可证伪的证据程序：先绑定 Bands 1–7 的 state/transition identity，再取得连接跃迁的 measured `δ`/偏振、partner-resolved lifetime 和 absolute `B(E2)/B(M1)`，最后用未参与主排序的 holdout（g factor、quadrupole invariant 或 HD–ND linking）区分 signature/configuration coupling、γ-soft response、wobbling、chirality 和 shape coexistence。

当前最稳妥的论文主张是：公开 `131Ce/133Ce` 证据足以形成竞争解释矩阵，但现有数据不能唯一识别模式。`AW13-9` 的 `δ=0` 只产生条件派生强度，`LI04-1`–`LI04-5` 的寿命/`Q_t` 覆盖不同带，`D21-4`–`D21-9` 的 γ/PES 是模型结果；这些证据不能互相替代。该候选的 falsifier 是同一连接网络在共同 response/covariance 合同下出现一组模型不相交的预测，或新的 absolute EM/holdout 直接改变当前排序。

最可能的审稿人否证是“这只是已有 A≈130 综述的重排”。防守策略是冻结 line ledger、source lineage、branch parameterization 和 stop rule，并至少取得一项目标核独立 companion observable；在此之前，稿件定位应是 evidence/readiness method paper，不能写成新的 wobbling/chiral discovery。

## Paper Evidence Gate

五个候选都需要：

1. 每条主张对应一个具体 source page、raw identity 和 page/figure/table/level locator；
2. 同一数据谱系、复测、综述和再分析明确标记 `multiple-dependent`；
3. 给出至少一个反证、一个必要 companion observable 和一个 falsifier；
4. 对 raw/response/Cov 缺口写 readiness boundary，停止生成代理 L4 结论；
5. 保留 `needs_review`、`unreviewed` 和 `provisional`，不以 Codex self-audit 代替人工审核。

## Risks and Blockers

- P1/P2 的关键 raw response、联合协方差、原始角分布或宇称判据未全部取得。
- 现有很多数值来自同一实验谱系的再分析，若不标 lineage 会虚增独立性。
- 任何模型参数、有效电荷、g 因子、`β`/`γ`/`β3` 或拟合端点都不能替代实验观测。
- 全库 lint 仍有继承基线 errors；它阻止自动发布，但不改变科学候选的 provisional 状态。

## Writing and Analysis Order

先写 P1 的方法合同和 source-lineage 图，再根据真实输入决定是否进入联合重析；P2
作为对象身份和识别性论文候选保留；P3 需要寿命/绝对 EM producer 后再写主结论；
P4 先完成统一数据表和单位/跃迁方向审计。每篇稿件都应先有 claim-to-source
matrix 和反证表，再开始正文写作；不要以“读过的论文数”替代可复核结果。

## Next Actions

1. 先完成 P1 的公开 source-lineage/observable ledger 和最小共同响应合同。
2. 并行维持 P2 的1983 AD、794.8-keV宇称和882偏振检索，但不重复受阻端点。
3. 对 P3/P4/P5 只补缺失 primary、数据身份和方法学对照，不用 synthetic 计算填充寿命、协方差、coverage 或多态跃迁。
4. 候选获得真实输入后，再建立 claim-to-source matrix、falsifier、图表目录和投稿期刊适配表。

## Sources

- [[matta-2015-transverse-wobbling-135pr]]、[[lv-2022-evidence-against-wobbling-135pr]]、
  [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]]：P1的分支和谱系证据。
- [[chakraborty-2023-131xe-wobbling-origin]]、[[banik-2020-131xe-multiple-band-structures]]：
  P2的对象身份与版本边界。
- [[gaffney-2013-pear-shaped-rn-ra]]、[[bucher-2016-144ba-direct-octupole]]、
  [[bucher-2017-146ba-direct-octupole]]：P4的直接E3和静态/动态解释边界。

## Human Review

本页是 Codex self-audit 的研究队列，`review_status: unreviewed`。候选题目、优先级
和停止条件都需要在实际投稿或导师讨论前重新核验，不代表用户已选择投稿期刊或批准
任何未经取得的数据分析。

## Promotion or Rejection History

2026-10-30：由全库温故知新与Day28 L3研究产生。五个候选均保留为active/provisional
队列；尚未取得新的事件级数据、响应或联合协方差，未生成期刊稿件或实验新结论。
