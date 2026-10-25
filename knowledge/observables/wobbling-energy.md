---
type: observable
title: Wobbling 能量
aliases: [wobbling energy, Ewob, E_wob]
created: 2026-07-01
updated: 2026-07-03
status: active
review_status: unreviewed
observable_kind: excitation-energy-difference
symbol: E_wob
units: keV-or-MeV
tags: [wobbling, rotational-band]
---

# Wobbling 能量（Wobbling Energy）

## Definition

候选 n=1 wobbling 带相对 n=0 基带在相近角动量处的激发能量；具体插值公式和自旋对应依论文定义。

## Formula and Conventions

摄入数值前必须复制原文公式，避免奇 A/even-even 与不同 ΔI 序列间误用。

## How It Is Obtained

由候选伙伴带能级与基带相邻自旋能级计算。

## Diagnostic Use

随自旋下降常见于 TW，增加常见于 LW，但 [[frauendorf-2024-wobbling-review]] 强调应以进动锥拓扑和电磁跃迁共同分类。

## Model Dependence

对转动惯量、准粒子取向、带指认和插值方式敏感。

## Failure Modes and Ambiguities

只看升降趋势可把 signature partner 或其他带误判为 wobbling。

## Examples

[[matta-2015-transverse-wobbling-135pr]] 用
`E_wob(I)=E(I,n_w=1)-[E(I-1,n_w=0)+E(I+1,n_w=0)]/2`
计算 `135Pr`，Fig.5 inset 显示实验值在低自旋区下降后回升。该趋势依赖 zero-/one-phonon band assignment，不能脱离电磁跃迁单独裁决。

[[sensharma-2019-two-phonon-wobbling-135pr]] 以 yrast `n_w=0` 序列为参考，在 Fig.4 比较 TW1/TW2 的 wobbling energies；TW2 实验值随自旋下降。该量的 two-phonon 含义依赖 Matta 2015 的 `n_w=0/1` assignment。

[[sensharma-2020-longitudinal-wobbling-187au]] 按 Eq.1 计算 `187Au` band (2) 相对 yrast 的 `E_wobb`；Fig.4(d) 显示随自旋增加。作者将其与 E2-rich links 联合用于 LW 分类，不能脱离 band assignment 单独裁决。

## Sources

- [[frauendorf-2024-wobbling-review]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[sensharma-2020-longitudinal-wobbling-187au]]

## Evolution Log

- 2026-07-01：建立“趋势不是充分判据”的边界。
- 2026-07-03：加入 Matta 2015 的 Eq.1/Fig.5 原始实验案例。
- 2026-07-03：加入 Sensharma 2019 的 TW2 自旋演化与 assignment-dependence。
- 2026-07-03：加入 Sensharma 2020 的 `187Au` increasing-`E_wobb` LW 支持案例。


## Day22能量解释边界校准（checkpoint092）

Ewob是绑定band/spin指认的派生量。F14横向粒子例子可以先升后降，故不能仅由斜率唯一分类TW/LW。旧以135Pr某拐点“已证实剪刀交叉”替代所有模型解释、并把寿命/偏振组合称充要前提的认证撤回。具体反证必须比较实际能级身份、竞争模型和相应电磁量。来源：[[frauendorf-2014-transverse-wobbling]] F14-D22-003/004。

## Day22 checkpoint106：谐频零不等于有限谱隙零

[[frauendorf-2014-transverse-wobbling]] F14-D22-R106-1/2的人工冻结j族在HFA曲率c2=0时仍有四次回复项；完整有限spin最低隙为正，按A0J^(2/3)标度趋近quartic算符极限。此为近似/完整有限矩阵的条件反例，不是核实验软模或零能相变测量。比较实际Ewob时还要匹配不同spin能量定义，不能将固定I模型最低两级差直接当所有实验Ewob。needs_review: true。
