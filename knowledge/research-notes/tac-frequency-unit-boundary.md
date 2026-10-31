---
type: research-note
title: "132La 3D-TAC 临界频率的单位与参数敏感性边界"
aliases: [TAC frequency unit boundary, 132La omega critical sensitivity]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [olbratowski-2002-critical-frequency-preprint, starosta-2001-n75-chiral-vibrations]
created_from: Day26 TAC source audit 031
promotion_target: tilted-axis-cranking
tags: [132la, tilted-axis-cranking, critical-frequency, units, parameter-sensitivity, model-boundary]
---

# `132La` 3D-TAC 临界频率的单位与参数敏感性边界

> 本页是 Day26 条件审计；相关 Day27 仅无学分预习，不推进课程状态，也不打开 Day28。所有频率均为模型量，未将临界频率写成实验测量。

## Research Trigger

Olbratowski 2002 v1 同时给出冻结陀螺经典模型的解析临界值和 Skyrme-HF 非平面分支起点；Starosta 2001 则给出另一套混合势 3D-TAC 的 $^{132}$La Table I。需要审计 $\hbar\omega$ 的单位、惯量和陀螺参数敏感性，以及 $\gamma$ 记号不能跨模型直接互换的边界。

## Grounded Evidence

- Olbratowski v1 原件为 4 页、arXiv:nucl-th/0211075v1；PDF pp.2–3 Eqs.(2)–(7) 给出 $I=\hat J\omega+s$、$\omega\times I=0$、$\omega_m(\mu-J_m)=0$ 及解析临界式。其输入为 $J_s,J_m,J_l=(8.5,31,20)\,\hbar^2/\mathrm{MeV}$、$s_s,s_l=(5.43,5.00)\,\hbar$；PDF p.3 说 HF 非平面解从 $\hbar\omega=0.6$ MeV 出现，不能和解析值混写。
- Starosta 2001 PRL p.4 Table I 给 $^{132}$La（$Z=57$）$\epsilon=0.175,\gamma=32^\circ,\hbar\omega=350$ keV、$\vartheta=65^\circ,\varphi=36^\circ,E_b=12$ keV、$J=11.3\hbar$。该表是混合 Woods–Saxon/修正谐振子势的 3D-TAC 输出；实验两带位移约 $0.37$ MeV 来自 PDF p.3 Fig.3 的能谱系统学。
- Olbratowski v1 已归档至 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/olbratowski-2002-critical-frequency-arxiv-v1.pdf`；实际读本和归档副本 SHA256 为 `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb`。Starosta 原件 SHA256 为 `9082c1e8ced3fbfeb2248f5b18c1b646f4dc1adc77af5c27c6a988855583cbf4`。

## Provisional Reasoning

冻结陀螺模型的非平面条件为

$$
\omega_c=\sqrt{\left(\frac{s_s}{J_m-J_s}\right)^2+\left(\frac{s_l}{J_m-J_l}\right)^2},\qquad
\omega_m=\pm\sqrt{\omega^2-\omega_c^2}.
$$

若 $s$ 用 $\hbar$、$J$ 用 $\hbar^2/\mathrm{MeV}$，则 $\omega_c$ 的单位为 MeV/$\hbar$，源文报告的 $\hbar\omega_c$ 才是 MeV。连续经典 $I_c=J_m\omega_c$ 的单位为 $\hbar$；基准值约 $15.9538\hbar$ 不是实验量子自旋阈值。

代入源参数得 $\hbar\omega_c=0.514639$ MeV，且 Olbratowski Eq.(5) 的 planar 分支阈值为 $\hbar\omega_{thr}=1.282267$ MeV，两者对应不同分支，不能互换。对输入各作 $\pm10\%$ 条件扰动时，$J_m$ 给出 $\hbar\omega_c=0.692040/0.413205$ MeV，$s_s$ 给出 $0.503773/0.526388$ MeV；在该局部扫描中 $J_m$ 的影响最大。完整数值列和 Eq.(5) 对照保存在 `tac-frequency-unit-sensitivity-031.json`。

$\gamma$ 的约定也不能直接迁移：Starosta Table I 的 $\gamma=32^\circ$ 属其混合势的形变参数，Olbratowski HF 输入约 $\gamma=45^\circ$；两者还使用不同势、配对和 time-odd 处理。若仅作 irrotational-flow 示意，$J_k\propto\sin^2(\gamma-2\pi k/3)$ 的三个未归一数在 $\gamma=32^\circ$ 与 $45^\circ$ 分别为 $(0.280814,0.998782,0.220404)$ 和 $(0.500000,0.933013,0.066987)$（轴置换和尺度未指定），不能倒推出两篇原文的 $J_s,J_m,J_l$。

## Assumptions

敏感性只改变冻结经典公式的单个输入，保持其它源参数不变；这不是对 HFODD、Starosta 3D-TAC 或量子集体哈密顿量的重新运行。所有结果是条件算术，保留源文件的 `needs_review` 状态。$\hbar\omega$、$\omega$、$J$、$s$ 和 $I$ 的单位按上文定义，不将 MeV 与 MeV/$\hbar$ 混用。

## Competing Explanations

HF 非平面分支的起点可能受配对、time-odd 场、EDF、基组和组态收敛影响；Starosta 的浅势垒与实验双带位移还可能对应手征振动、隧穿、平面/轴向分支或组态混合。Olbratowski PDF p.4 Fig.6 明确保留 planar/axial-long 解释，因此一个解析 $\omega_c$ 不能排除竞争模型。

## Transfer Conditions

迁移到别的核时必须重新确定粒子/空穴占据、$J_k$、$s_k$、配对、time-odd 耦合、$\gamma$  convention 和频率到自旋映射。仅可迁移公式结构与单位检查；不能迁移 $0.514639$、$0.6$ 或 $1.282267$ MeV 作为通用阈值。

## Failure Conditions

若把 $\hbar\omega_c$ 当实测频率、把 $I_c$ 当量子 bandhead、把 Starosta 的 $0.37$ MeV 实验带位移当临界频率，或把 $\gamma=32^\circ/45^\circ$ 当同一模型坐标，则结论失效。若不检查 $J_m>J_s,J_l$ 和非零 $s_s,s_l$，Eq.(7) 的非平面分支也不适用。

## Falsification or Reverse Tests

在统一 EDF、配对和算符下，固定实验带身份分别计算 planar、axial-long、aplanar 枝，并比较绝对寿命、带内/带间 M1/E2、$S(I)$ 与双带位移。只有当非平面枝同时改善这些独立观测量，才能增强手征解释；当前审计没有执行该量子化或 HF 重算。

## Open Questions

time-odd 场和配对恢复会怎样移动 HF 的 $0.6$ MeV 起点？Starosta 的 $12$ keV 势垒在加入集体质量后对应多大振动能或隧穿劈裂？实验是否提供足够绝对电磁强度以区分非平面、平面和轴向替代？

## Human Review

本页为 Codex 条件 source/claim self-audit，未提升 `human-reviewed`。原件版本、PDF locator、模型输入和实验/模型边界均需在论文级使用前定向复核。

## Promotion or Rejection History

2026-10-28：建立 031 参数/单位审计；将 Starosta 实验带位移、Starosta 3D-TAC 势垒、Olbratowski 经典解析临界和 HF 分支起点分开；撤回任何把它们合并为实测临界频率或普适相界的写法。Day27 仍为无学分预习。
