---
type: band
title: ¹³¹Xe yrare 负宇称序列
aliases: [131Xe unfavoured signature candidate, 131Xe 9/2- 341 keV sequence]
created: 2026-07-01
updated: 2026-10-30
status: active
review_status: human-reviewed
nucleus: 131xe
band_label: negative-parity-yrare-sequence
parity: negative
signature: proposed-alpha=-1/2
spin_range: 9/2- to 21/2-
configuration_status: proposed-nu-h11-2
interpretation_status: proposed-unfavoured-signature-partner
tags: [signature-partner, negative-parity, yrare]
---

# ¹³¹Xe Yrare 负宇称序列

## Stable Identity

2023 论文 Fig.1 中由 341、1046、1862、2792 keV 能级构成的序列；文件名只记录 yrare 可观测身份，不把解释写死。

## Level and Transition Data

| Iπ | Elevel (keV) | 带内 Eγ (keV) | 到 favored 序列的 Eγ (keV) |
|---|---:|---:|---:|
| 9/2- | 341 | - | 177 |
| 13/2- | 1046 | 705 | 882 |
| 17/2- | 1862 | 816 | 1055 |
| 21/2- | 2792 | 930 | 1176 |

## Spin-Parity Evidence

带内 705、816、930 keV 被 DCO 指示为 quadrupole；连接跃迁以 dipole 为主。具体自旋宇称证据需结合更早数据复核。

## Configuration Assignment

作者提出该序列是 νh11/2 的 unfavoured signature partner。

## Proposed Interpretation

2023作者将所选小δ分支解释为普通 [[signature-partner-bands]]，并据此认为未见 wobbling 信号；这一判断受Fig.5另一负δ交点、缺失的882响应合同和未获得的绝对强度/寿命限制，不能升级为排他结论。

## Discriminating Observables

- `δ671=0.03(3)`、`δ882=0.09(8)`（882为Fig.5所选小根，不是全局唯一解）；
- 1055 keV 图内标注为 `δ=0.1(2)`；正文称其接近零，不能改写成旧的 `0.00(2)`；
- yrare 17/2- 的 `B(M1)/B(E2)=1.27(14)` 与 TPRM 1.27 一致。

## Competing Interpretations

某些邻核的类似 unfavoured 序列曾被重新解释为 wobbling，因此仍需绝对跃迁强度与独立寿命数据。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[131xe-same-parent-strength-identifiability]]
- [[131xe-882-branch-response-contract]]

## Day28 Evidence Boundary

- `δ882=0.09(8)`是Fig.5所选小解；负δ区仍有第二交点，RDCO单独不提供全局唯一性。
- `1055`的实际小解为`0.1(2)`；中心值对应约1%的E2光子份额，但区间映射不是新的置信区间。
- `B(M1)/B(E2)=1.27(14)`与模型值的对账依赖同一强度比、δ和模型能量约定；不能把两个派生量当独立确认，也不能把作者的有界signature-partner解释升级为排他证明。
- 881.8/880.1双线峰形、门选、取向、偏振响应和联合协方差仍缺失；详见 [[131xe-882-branch-response-contract]]。本节Day28新增判断保持 `needs_review: true`。

## Evolution Log

- 2026-07-01（1 source）：建立为“proposed unfavoured partner”，保留人工复核门。
- 2026-07-01（human review）：用户完成轻度科学校准，整体评价良好；关键 mixing ratio 与 B(M1)/B(E2) 仍保留来源级复核标记。
