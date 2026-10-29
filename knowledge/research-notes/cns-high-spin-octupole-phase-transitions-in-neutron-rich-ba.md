---
type: research-note
title: "宏观-微观 CNS 框架下富中子钡核高自旋八极相变与离心退耦"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [CNS high-spin octupole Ba, cranked Nilsson-Strutinsky neutron-rich barium, Ba octupole alignment quenching]
tags: [cns, octupole, high-spin, phase-transition, barium-isotopes]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 directed study: CNS high-spin octupole phase transitions in neutron-rich Ba"
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
---

# 宏观-微观 CNS 框架下富中子钡核高自旋八极相变与离心退耦

## Research Trigger

本任务要求检验一个有明确反例空间的机制链：低自旋时离心转动能因八极形变提高有效转动惯量而倾向于稳定有限 `beta3`；更高自旋时 `nu h9/2`、`nu i13/2` 与 `pi h11/2` 高-j 组分沿推转轴对齐，破坏八极粒子—空穴相干，可能使八极势阱变浅并使交错宇称位移重新打开。目标核为 `144Ba (N=88)`、`146Ba (N=90)`，并把 `148Ba (N=92)` 作为无直接高自旋对账的探索性延伸。

本笔记把“八极高自旋相变”作为待证伪的条件模型，而不是已经由 Ba 实验建立的事实。直接实验锚点是 Bucher 2016/2017 的低自旋库仑激发 `B(E3)`；高自旋形变路径由独立模型和本次 reduced CNS 工件给出，证据层不能混并。

## Grounded Evidence

### Direct E3 and E1/D0 evidence

| 对象 | 直接/模型事实 | 定位 | 边界 |
|---|---|---|---|
| `144Ba` | `B(E3;3- -> 0+) = 48(+25/-34) W.u.`, `Q3 = 1.73(+0.45/-0.62) x 10^3 e fm^3`, rotor conversion `beta3 = 0.17(+0.04/-0.06)` | Bucher 2016, PRL 116 112503, PDF pp.3–4, Table I | `beta3` 转换依赖转子、轴对称及高阶形变约定；强 E3 不单独证明刚性静态梨形 |
| `146Ba` | `B(E3;3- -> 0+) = 48(+21/-29) W.u.`，与 `144Ba` 中心值相容；E1/D0 显著变小 | Bucher 2017, PRL 118 152504, PDF pp.2–5, Table I/Figs.3–5 | E1 主要受既有寿命/分支约束；E1 小不能推出 E3 淬灭 |
| `146Ba` 微观解释 | SCCM 将 E1 变化联系到 `nu h9/2`, `nu f7/2`, `nu i13/2` 变形轨道占据和质子—中子偶极相消 | Bucher 2017, PDF pp.4–5 | 这是作者的模型解释，不是高自旋 CNS 计算，也不提供实验高-j alignment 证据 |

### High-spin framework

Butler–Nazarewicz 综述把反射不对称旋转、交错宇称、Coriolis 项、带交叉和高自旋形状变化放在同一动力学框架，并总结了 `I(I+1)/(2 J(beta3))` 使八极形变具有离心响应的模型路线（PDF pp.363, 390–392）。同一综述强调静态平均场、八极软振动和宇称恢复后的实验谱学必须分层。它是历史框架和来源地图，不是 `144/146Ba` 高自旋新测量。

Li–Wang 2024 的独立 PC-PK1 3D-lattice cranking 结果提供一个重要反向约束：其 `144Ba` yrast 解在约 `I=24 hbar` 前保持平均 `beta30≈0.128`，但遗漏 pairing、量子角动量投影和宇称投影，不能给出交错宇称劈裂。因此它与本笔记的 alignment-quenching 分支构成竞争模型，而不是可直接合并的同一计算。

### Experimental high-spin parity-displacement ledger

Bucher 的实验高自旋覆盖和 E1 支线需要单独记录。`144Ba` 的 GRETINA 谱中明确识别到最高约 `10 hbar` 的跃迁；GOSIA 网络把正宇称基带扩展到 `14+`、负宇称序列扩展到 `15-`，共纳入 70 个 E1/E2/E3 矩阵元，E1 主要由既有 branching-ratio 与 lifetime 资料约束（Bucher 2016, PDF pp.2–4, Fig.2）。`146Ba` 本次产额覆盖正宇称带到 `10 hbar`、负宇称序列到 `9 hbar`；实验中可见的 E1 衰变主要来自 `3-` 与 `5-` 态，E1 矩阵元对本次库仑激发产额不敏感（Bucher 2017, PDF pp.2–3, Table I）。因此这两篇论文提供了低—中自旋对账和 E1 分支约束，但没有一套可直接用于 `I=12–24` 的逐线绝对 E1/lifetime 表。

`146Ba` 论文还明确把突然的 band alignment 更倾向解释为 yrast–yrare crossing，并列出反射对称转变和 aligned octupole phonon 等替代解释（PDF pp.3–4）。这直接反驳把 alignment 自动等同于八极淬灭的排他性叙述；本笔记的 alignment penalty 只是将该竞争机制参数化。

交错位移定义为

```text
S(I) = E(I-) - [E((I-1)+) + E((I+1)+)]/2.
```

现有研究笔记逐项转录的 Bucher 能级对账给出：`144Ba` 的 `S(1)=659.1–659.2 keV`、`S(13)=168.5 keV`；`146Ba` 的 `S(1)=647.4 keV`、`S(11)=78.1 keV`。前一组数存在末位舍入差异，不能伪装成更高精度。高自旋带交叉和未观测成员会改变这一差分的解释；这里不把 `S(I)` 直接等同于隧穿劈裂。

## Provisional Reasoning

### Reduced macro-microscopic CNS energy

标准推转 Nilsson–Strutinsky 思路是在形变和推转频率下构造

```text
E_CNS(beta2,gamma,beta3;I)
 = E_LD^Y+E(beta2,gamma,beta3)
 + delta E_shell^p + delta E_shell^n
 + E_rot(I; beta2,beta3)
 + E_align(I; beta3).
```

工件采用一个可审计的 reduced surrogate：

```text
E_LD = 1/2 C2 beta3^2 + 1/4 C4 beta3^4
       + C2q(beta2-beta20)^2 + Cgamma gamma^2
       + C23(beta2-beta20) beta3^2,

J_eff = J0 [1 + c2 beta2 + c3 beta3^2],
E_rot = I(I+1)/(2 J_eff).
```

壳修正用一个在 `Z=56, N=88–90` 附近的平滑八极窗口近似；其目标形变先被低—中自旋离心响应推向较大值，然后由

```text
f_align(I) = logistic[(I-Ic)/w] (I/24)^1.5
```

控制的壳相干削弱和 `E_align = k_align f_align beta3^2` 拉回反射对称侧。`Ic` 不是由现有 Ba 高自旋实验拟合，而是用于测试 N=88 到 N=90 临界自旋位移的显式假设：工件基线设置 `Ic(144)=12.5`、`Ic(146)=14.0`、`Ic(148)=15.0 hbar`。

### Grid and numerical output

自洽搜索网格为 `I=0..24`、`beta2=0.12..0.31`（步长 0.01）、`gamma=-20..20 deg`（步长 5 deg）和 `beta3=0..0.24`（步长 0.01）。输出包含 337,500 个势能点、75 个极小路径点和 75 个 `S(I)` 行；`I=0` 的交错位移标记为 undefined。运行命令为：

```bash
cd outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/cns-ba-octupole
python3 cns_ba_octupole_model.py
```

基线输出的极小路径（每四个自旋列一项）为：

| 核素 | `beta3(I=0,4,8,12,16,20,24)` | `S(I=4,8,12,16,20,24)` keV |
|---|---|---|
| `144Ba` | `0.14, 0.17, 0.18, 0.16, 0.11, 0.06, 0.02` | `324.5, 135.2, 70.6, 113.8, 253.5, 452.8` |
| `146Ba` | `0.14, 0.17, 0.19, 0.17, 0.12, 0.06, 0.02` | `319.0, 133.2, 66.1, 92.1, 248.0, 451.6` |
| `148Ba` | `0.12, 0.15, 0.16, 0.15, 0.11, 0.06, 0.01` | `306.1, 128.4, 65.2, 88.5, 241.0, 476.4` |

这组输出显示低自旋八极外移、约 `I=10–12` 后 alignment-driven 回落，以及 `S(I)` 先收敛后重新打开。它是参数化机制演示；数值不能被引用为 Bucher 的实验能级或真正 CNS 预测。

### N=88 to N=90 interpretation

在该 surrogate 中，`146Ba` 的较晚 `Ic` 和较弱 alignment penalty 表示 N=90 费米面附近的八极相干窗口在较高自旋仍能维持；这与 Bucher 2017 中“E3 保持而 E1/D0 强烈变化”的分层事实相容，但不是由实验直接测出的临界自旋。`144Ba` 的较早回落则是一个可检验假设。`148Ba` 只用于展示模型外推，当前没有相同质量区的直接 Bucher 高自旋对账。

## Assumptions

- `E_LD` 是 Y+E 思路的局部展开，不是完整 finite-range Yukawa-plus-exponential 液滴参数化。
- 壳修正用平滑窗口替代真正的 proton/neutron cranked Nilsson spectrum、Strutinsky smoothing 和 configuration tracking。
- `J_eff` 只保留 `beta2`、`beta3` 依赖，忽略 `gamma` 惯量、配对坍塌、time-odd 场和 `beta4`。
- `f_align` 将 `nu h9/2`、`nu i13/2`、`pi h11/2` 的总效应压缩成一个可扫描参数；没有逐轨道 Routhian 数据。
- `S(I)` 为低自旋实验锚点归一的 phenomenological surrogate，不是宇称投影或 WKB 计算。
- 极小点坐标步长会产生约半个网格间距的离散化误差；不能据此报告超过网格分辨率的位数。

## Competing Explanations

1. **离心八极稳定化**：若 `dJ_eff/d(beta3^2)>0` 且 shell coherence 未被 alignment 破坏，有限 `beta3` 区域的 `E_rot` 降低，`S(I)` 向零收敛。
2. **高-j alignment 淬灭**：对齐削弱 `Delta l=Delta j=3` 粒子—空穴相干并提高八极方向的有效曲率，`beta3_opt` 回落，`S(I)` 重新打开。
3. **独立的 band crossing/configuration change**：观测到的 `S(I)` 转折可能来自正负宇称带重新标记、组态交叉或带混合，不一定是同一势能面上的相变。
4. **八极软振动**：大 `B(E3)` 与高 `S(1)` 可以同时出现；直接 E3 证明强集体跃迁，不足以判定低自旋存在深的静态双阱。
5. **模型空间差异**：Li–Wang 的 unpaired PC-PK1 cranking 维持 `beta30` 到 `I≈24`，说明“高自旋必然淬灭”不是跨模型普适结论。

## Transfer Conditions

- 将 `Ic`、`beta3_opt` 或 `S(I)` 外推到另一 Ba 同位素，必须重新计算同一定义的 proton/neutron Routhian、配对、组态和惯量；不得只按 A 或 `B(E3)` 缩放。
- 比较 `144Ba` 与 `146Ba` 的 `S(I)` 必须保持同一正宇称参考带、同一自旋宇称配对和相同差分定义，并标记带交叉。
- 把直接 `B(E3)` 迁移为静态 `beta3` 需要保留转子约定、`beta4` 敏感性和软势能面零点涨落边界。
- 将本模型用于论文只能作为 hypothesis-generating calculation；正式 CNS 结果需要完整 single-particle spectrum、Strutinsky prescription、configuration labels 和频率—自旋映射。

## Failure Conditions

- 真实自洽计算若给出 `dJ/d(beta3^2)<=0`，离心外移项的方向失效。
- 若 `144/146Ba` 高自旋同一带系的寿命、alignment 和 E3 强度显示 `beta3` 保持，而 `S(I)` 转折仅由带交叉产生，alignment phase-transition 解释应降级。
- 若 pairing-restored parity-projected calculation 在 `I<=24` 保持深八极双阱，则本工件的 quenching 分支不是适用解。
- 若新的高自旋谱学修订 Bucher 能级配对或自旋指定，当前 `S(I)` 锚点必须重建。

## Falsification or Reverse Tests

1. 对 `144,146Ba` 在统一 Woods–Saxon/Nilsson 参数和 Yukawa-plus-exponential 宏观项下执行真正的 proton/neutron cranking，逐频率输出 `J^(1)`, `J^(2)`, Routhian 和 `beta3`。
2. 显式跟踪 `nu h9/2`, `nu i13/2`, `pi h11/2` 的占据、alignment 和 avoided crossings；检验转折是否与 `Ic` 同步。
3. 加入 pairing、`beta4`、`gamma` 惯量和 parity/angular-momentum projection；直接计算交错宇称能级，不使用本笔记的 `S(I)` surrogate。
4. 用同一带标签重算 Bucher/ENSDF 高自旋能级、E1/E2/E3 分支和 lifetime；检查 `S(I)` 重新打开是否与绝对强度一起出现。
5. 反向运行工件：把 `alignment_quench=0` 或 `alignment_penalty=0`，应得到高自旋 `beta3` 不回落或仅由旋转项缓慢改变；把 `J_beta3=0`，应去掉低—中自旋的离心外移趋势。

## Open Questions

- `144/146Ba` 是否存在可由同一实验带系定义的 `I≈12–20` 交错宇称高自旋序列？当前可用证据不足以把模型转折与实测组态一一对应。
- Bucher 2016/2017 的直接 E3 网络能否与高自旋 lifetime 和 alignment 结合，区分八极声子、静态梨形和 configuration crossing？
- N=90 附近 `nu i13/2` 的费米面位置与 `146Ba` E1 相消之间的关系，是否会把 alignment 临界点推迟，还是只影响偶极矩而不影响 `beta3`？
- 148Ba 是否有足够的直接 E3、负宇称带和高自旋数据来检验本次外推？
- 现象学 `S(I)` 的再打开是否可由 parity-projected GCM 的 tunnelling action 独立重建？

## Human Review

`review_status: unreviewed`。本页由 Codex self-audit 建立，保留直接实验、作者模型解释、既有理论综述和本任务 surrogate 的分层。需要人工审阅的重点是：Bucher 高自旋能级配对的原始表格、Butler–Nazarewicz 页级转述的原始定位、以及把 N=88→N=90 的 `Ic` 位移写入论文时的措辞。任何 `beta3_opt`、势垒或 `S(I)` 数值均应视为工件输出，不是实验测量。

## Promotion or Rejection History

2026-10-29：建立本研究笔记和 reduced CNS worker。保留“离心稳定化与高-j alignment 淬灭可竞争”的条件性机制；未将题设中的 alignment-driven octupole quenching 晋升为 Ba 的已证实高自旋相变。若后续统一自洽 cranked Nilsson–Strutinsky 加宇称/角动量投影计算支持同一转折，并与可追溯高自旋谱学、lifetime 和 E3/E1 数据一致，再考虑提升 reasoning status。
