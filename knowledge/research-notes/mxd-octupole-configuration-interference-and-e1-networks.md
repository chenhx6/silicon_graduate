---
type: research-note
title: "MχD 与八极软势面中的组态干涉及 E1 网络"
aliases: [mxd octupole configuration interference, octupole E1 network]
created: 2026-10-29
updated: 2026-10-29
status: active
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 MχD octupole configuration interference investigation
evidence_sources: [liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, petrache-1996-rotational-bands-134pr, tonev-2006-134pr-lifetime-chiral, mxd-multiple-chiral-doublets-octupole-coupling-boundary, chiral-octupole-quadruplets-symmetry-and-transition-rules]
promotion_target: mxd-octupole-coexistence
tags: [MχD, octupole, configuration-mixing, 2qp, 4qp, E1, M1, E2, 78Br, 134Pr, interference]
---

# MχD 与八极软势面中的组态干涉及 E1 网络

## Research Trigger

78Br 的 Bands 1/2 与 Bands 3/4 提供了“两对候选手征带 + 八条跨宇称 E1”的动机；134Pr 的近简并双带则提醒必须同时解释寿命和绝对电磁强度。问题是：若两组不同准粒子组态（示意为 2qp 和 4qp）共同耦合到三轴、八极软的核芯，E1 网络是否会由组态振幅的相干和控制，而非只由 `|beta3|` 控制？

## Grounded Evidence

- Liu 2016 的 78Br 直接报告正宇称 Bands 1–2、负宇称 Bands 3–4 候选双带及 Band 1 到 Band 3 的八条强 E1；MDC-CDFT/TPRM 给出 `beta30` 软性。来源页 locator 为 `L16-5`–`L16-14`；其结论支持 octupole correlation 和 quartet 研究动机，不确证静态梨形或四重简并。
- Petrache 1996 的 134Pr 结果显示 Band 2 不能由简单 unfavoured-signature partner 一致解释，三轴势面显著 gamma-soft；这是组态/形状混合必须保留的早期边界，locator `PE96-5`–`PE96-12`。
- Tonev 2006 的 134Pr 寿命给出近简并区 Band 1 带内 `B(E2)` 约为 Band 2 的 2–3 倍，`B(M1)` 无预期稳定交错，locator `TO06-D24-003`–`TO06-D24-005`。这是静态手征极限的反证压力，不是对八极机制的直接确认。
- 既有 MχD 边界笔记指出，不同组态/不同三轴极小可以产生多对候选伙伴，但绝对寿命、偏振和 partner-resolved 强度仍是必要检验；既有四重态笔记把 E1/M1/E2 规则限定为 toy 算符层。

## Provisional Reasoning

建立八维有效空间 `|c,chi,p>`，`c` 为 2qp/4qp，`chi` 为左右手征标签，`p` 为宇称。八极坐标进入软势 `V(beta3)`、宇称隧穿 `t_pi` 和组态混合 `v_cfg`。E1 算符取同组态路径与相反相位的跨组态路径，因此同一末带的两个路径可相消，另一末带可增强。M1 保持宇称并翻转手征，E2 保持宇称；扫描中 `sum B(M1)/sum B(E2)` 从约 `2.4e-4–1.51`（I=8）扩展到 `5.1e-3–9.99`（I=14），显示配置混合和转动能量重排会产生明显非简谐偏离。E1 总强度在示意参数下于 `beta3≈-0.18` 出现峰值，说明强度不必随八极形变绝对值单调增长。

以上数值来自 [可复现工件](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/mxd-octupole-interference/) 的 synthetic Hamiltonian，不是 78Br/134Pr 拟合。

## Assumptions

1. 2qp 与 4qp 只代表两类有效组态，不指定具体单粒子轨道。
2. `beta3` 是软势面的集体坐标；参数为示意量，未由 CDFT 或实验反演。
3. 相对强度取矩阵元平方，未加入角动量约化、寿命、内转换和 detector efficiency。
4. 八带是“两个组态 × 手征 × 宇称”的诊断空间，不等于实验已确认的八条带。

## Competing Explanations

- E1 网络可由八极关联、组态混合或 `f5/2–p3/2` 等轨道混合单独产生；78Br 的现有证据不能区分它们。
- 134Pr 的强弱 E2 不对称可来自 gamma-soft 形状涨落、动态手征或不同组态，而非八极坐标。
- M1/E2 非简谐也可能来自有效 g 因子、Coriolis 混合和带交叉；不能由比值单独反演 beta3。

## Transfer Conditions

只有在获得逐线自旋宇称、偏振/混合比、绝对 E1/M1/E2、partner-resolved 寿命、feeding 协方差，以及同一组态空间的三轴-八极 PRM/GCM 计算后，才可把模型参数转移到 78Br 或 134Pr。转移时应拟合 E1 网络和带内比值的联合协方差，而非只拟合能级差。

## Failure Conditions

- 用 toy 的 relative strength 宣称核素的绝对 B 值或静态 `beta3`。
- 把任意异宇称 E1 连接直接视为手征-八极 quartet 证据。
- 忽略 134Pr 的寿命不对称和无稳定 M1 交错这一反证。
- 把 2qp/4qp 标签当作已由实验唯一确定的组态。

## Falsification or Reverse Tests

1. 若同一组态空间无法同时重现 E1 分支、M1/E2 比值和逐自旋能级差，应否定八维最小模型或加入额外组态。
2. 若绝对寿命显示 E1 网络不随组态混合相位改变，且跨组态路径被实验上压低，则相消干涉解释降级。
3. 若 134Pr 式的 2–3 倍 E2 不对称在不同 gate 和自旋区稳定存在，且八极扩展不能重现，应优先采用 gamma-soft/动态手征解释。
4. 反向扫描 `a_cross=0`：若主要 E1 峰谷仍完全存在，则峰谷不是组态干涉的独特指纹。

## Open Questions

- 78Br 的八条 E1 是否能按同一 2qp/4qp 混合相位解释，并保持逐自旋连续性？
- 134Pr 的 Band 1/2 寿命差能否由含 beta3 的 GCM/PRM 在不破坏 M1 趋势下重现？
- 哪个最小 companion observable（绝对 E1、E2 lifetime 或偏振）能区分八极关联与 f-p 轨道混合？
- 组态交叉附近的 E1 相消是否会产生可测的分支比反转？

## Human Review

本页由 Codex 基于已摄入 source 页和可复现 toy 扫描完成 self-audit，`review_status: unreviewed`，未标记为 `human-reviewed`。需要后续人工裁决的重点是：2qp/4qp 的具体轨道映射、E1 算符相位约定，以及将合成相消模式与 78Br 实际八条 E1 的逐线对应是否具有唯一性。

## Promotion or Rejection History

- 2026-10-29：`supports` 将 78Br 的 E1 网络和 beta3 softness 作为组态干涉研究动机；保留 quartet 未确证边界。
- 2026-10-29：`supports provisional` 八带模型给出可检验的 E1 相消/增强与 M1/E2 非简谐预测；未晋升为核素定量结论。
- 2026-10-29：`rejects` “E1 网络 + 近简并 = 静态手征八极八重态”的过强命题；134Pr 寿命结果构成反向约束。
