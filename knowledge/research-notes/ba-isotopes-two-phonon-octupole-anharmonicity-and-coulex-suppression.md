---
type: research-note
title: "140–150Ba 双声子八极多重态的非简谐分裂、Pauli/4p–4h 淬灭与库仑激发抑制"
aliases: [ba-two-phonon-octupole, barium-two-octupole-phonon]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 investigation of two-phonon octupole multiplets in Ba isotopes"
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, ba-e1-e3-sccm-orbital-occupancy-and-static-shape-audit, two-phonon-octupole-multiplets-damping-and-coulex-suppression]
tags: [140-150Ba, octupole, two-phonon, anharmonicity, Pauli-blocking, 4p-4h, Coulomb-excitation, GOSIA]
---

# 140–150Ba 双声子八极多重态的非简谐分裂、Pauli/4p–4h 淬灭与库仑激发抑制

## Research Trigger

本页回答一个可检验问题：富中子 Ba 从反射不对称振动走向更强形变关联时，理想 `[3−×3−]^{J=0,2,4,6}` 如何被微观费米子效应改写，以及为什么多步库仑激发很难把高能二声子退激作为一组完整峰分离出来。

## Grounded Evidence

本页回答一个可检验问题：富中子 Ba 从反射不对称振动走向更强形变关联时，理想
`[3−×3−]^{J=0,2,4,6}` 如何被微观费米子效应改写，以及为什么多步库仑激发很难把
高能二声子退激作为一组完整峰分离出来。Bucher 2016/2017 的直接结果是单八极声子
基态 E3 基准：`144Ba` 为 `48(+25/−34) W.u.`，`146Ba` 为 `48(+21/−29) W.u.`
（分别见两篇 PRL 的 Table I、PDF pp.3–4 和 pp.2–3）。它们证明强 E3 集体性，
不等于已经观测到二声子 quartet；146Ba 的 E1 变小也不能单独当作八极淬灭证据。

本页的新数值来自工件中的显式 toy scan。`E(3−)`、背景态密度、doorway 耦合、
4p–4h 混合和 GDR 有效振幅都不是 140–150Ba 的采用实验输入，故结果标签为
`illustrative_model_scan_not_experimental_data`。

## Provisional Reasoning

### 1. 代数基准与非简谐劈裂

对一个 `l=3` 八极玻色子和线性算符 `T(E3)=t(a†+ã)`，产生第二个声子带来
`sqrt(2)` 的振幅因子。剥离实验室角动量重耦合后，常说的二倍增强是
`B_ideal(two phonon)/B(single phonon)=2`；这不是每个 `J` 分量都等于 2，
也不能把 `B(0+→3−)` 与 `B(3−→0+)` 混写。有限费米子空间中该因子改为

`B_J/B_single = 2 Q_B(J)`, `Q_B=|Q_amp|² < 1`.

相互作用可写为 `H=H_ph+V_Pauli+V_4p4h+V_β2β3`。`V_Pauli` 阻止两个声子重复使用
相同的准粒子对；`V_4p4h` 把集体 doorway 与四粒子—四空穴背景混合；四极—八极
耦合和形变旋转惯量再使不同 `J` 发生不同位移。因此 `E_J=2E_3+δ_J`，并不要求
四个成员简并。工件采用示意 `δ_J=(-0.55,-0.10,0.28,0.72) a`（J=0,2,4,6），
其中 `a` 随形变和 4p–4h 混合增强；这只给出机制方向，尚非微观 Ba 计算。

## Pauli and 4p–4h quenching model

工件把 Pauli 重叠 `p` 与 4p–4h 混合 `v_4` 映射为

`Q_amp = exp[-0.62 p − 0.78 v_4]`, `Q_B=Q_amp²`.

这是一个透明的参数化，而非从反对称化波函数拟合出的普适定律。它的物理含义是
二声子 doorway 的 E3 振幅同时受到占据阻塞和组态泄漏；若要升级为微观结果，必须
用同一核素的 QRPA/QPM/GCM 或 shell-model transition kernel 计算 `p(E)`、`V_α`
和 4p–4h 态密度，不能把一个 Ba 的 `Q` 跨链复制。

## Fragmentation and spreading

doorway 与背景态的耦合给出

`Γ↓ ≈ 2π <|V|²> ρ(E)`.

当 `Γ↓` 大于相邻本征态间距时，理想二声子强度分散到许多本征态，单条高能 γ 线
的峰高下降；只有包含全部碎片和 feeding 的闭合能量窗才可能恢复总强度。当前扫描
中的 `Γ↓` 约为 `0.53–0.79 MeV`（140–150Ba），是由设定的 `σ_V` 和 `ρ` 算得，
不是 Bucher 数据给出的 spreading width。实验上还会叠加峰重叠、未观测分支、探测
效率和 GOSIA 参数协方差。

### 3. 多步库仑激发布居抑制机制

两步库仑激发跃迁几率由中间态矩阵元求和给出：
$$P_{0 \to 2\text{-ph}} \propto |M_{0^+ \to 3^-_1} M_{3^-_1 \to 2\text{-ph}} + \sum_k M_{0^+ \to k} M_{k \to 2\text{-ph}}|^2$$
当不同路径之间存在相消干涉且双声子态发生剧烈的 doorway 态展宽（$\Gamma_{\text{spread}} \sim 0.5-0.8\text{ MeV}$）时，单个末态的退激光子产额被极度压低，使得高能量分支很难作为一组独立谱线被检出。

## Assumptions

- 假定双声子八极态可由多极相互作用在单声子基底上做微扰/非简谐展开；
- 假定 4p-4h 态密度采用费米气体模型外推；
- 假定库仑激发两步振幅干涉为主导通道。

## Competing Explanations

二声子峰不可见可由多步库激振幅相消干涉、强 doorway 态展宽离域、或多声子八极向静态形变凝聚三种机制共同解释。

## Transfer Conditions

适用于富中子钡同位素（140-150Ba）与稀土八极过渡核区；不得直接迁移至轻核或球形闭壳层核。

## Failure Conditions

若微观 GCM 或大规模壳模型显示双声子态保持纯玻色子二倍增强（$Q_B \approx 1.0$），则本费米子淬灭与 doorway 阻尼机制失效。

## Falsification or Reverse Tests

在重离子非弹性散射与库仑激发实验中，系统测量 $0^+_2$ 与 $2^+_2$ 态向 $3^-_1$ 态的直接 $B(E3)$ 分支比与绝对能级寿命。

## Open Questions

- 在更高自旋（$J=4, 6$）的二声子多重态成员中，转动离心力对 Pauli 淬灭是增强还是削弱？
- 四极-八极非轴对称自由度对多重态简并解除的贡献大小。

## Human Review

本笔记由自主研学模型计算生成，保持 unreviewed。

## Promotion or Rejection History

- 2026-10-29: 完成 140-150Ba 双声子八极多重态非简谐分裂、Pauli 淬灭与库激抑制微观建模。
