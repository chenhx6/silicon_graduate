---
type: research-note
title: "225Ra–225Ac 宇称双重态跨来源一致性边界"
aliases: [parity doublet cross-source consistency boundary, Ra225 Ac225 convergence audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
created_from: Day26 unit039 cross-source consistency audit
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, odd-A, consistency-audit, provenance, evidence-boundary]
---

# $^{225}$Ra–$^{225}$Ac 宇称双重态跨来源一致性边界

## Research Trigger

在多个单元分别计算 W.u.、约化矩阵元、CG 因子、条件 $D_0$ 和能量窗候选后，需要确认这些数值是否仍来自相同的 ENSDF 字段和约定，并识别 provenance 文本是否发生漂移。

## Grounded Evidence

两份 raw ENSDF 哈希、E1 评价值、W.u. 换算、正逆方向 $(2J+1)$ 因子、CG²、条件 $D_0$ 和 50/100/200-keV 候选计数均在 016/028/030/033/036 工件之间复核一致。Ra 的 E1 字段为 0.00081(20) W.u.，Ac 为 0.00171(15) W.u.；两核 $A=225$，采用同一 $r_0=1.2$ fm 约定时 1 W.u. = 2.384497 $e^2\mathrm{fm}^2$。

## Provisional Reasoning

### 代数收敛

采用 $B=|M|^2/(2J_i+1)$，Ra 得 $|M|=0.087896\pm0.010851\ e\mathrm{fm}$，Ac 得 $0.127710\pm0.005601\ e\mathrm{fm}$。Ra 的反向 B 值因初态简并因子变为 2 倍；Ac 初末自旋相同，反向值不变。采用不同跃迁的轴向 CG 因子 $C^2=1/3$（Ra）和 $0.6$（Ac），条件 $D_0$ 数值保持与 033 一致。

### 配对收敛

030 的全 Cartesian 同自旋异宇称配对与 036 的窗口筛选一致：Ra 在 50/100/200 keV 内有 3/8/15 个候选，Ac 有 6/9/11 个。候选计数不代表物理带配对；多带和括号 Jπ 仍是主要限制。

### Provenance 发现

一项文字来源需要复核：Ra raw 的 L31.56 注释写明 $(\alpha)(ce)(t)$ in $^{229}$Th $\alpha$ decay (1985Is03)，而 Ac raw 的 40.09-keV E1 注释写明来自 $^{225}$Ra β− decay 的 L-subshell ratios。E1 数值没有冲突，问题仅在既有 E1 research-note 将 Ra 的来源概括成 β− 链；后续修订应拆分两条来源，不把 Ac 的来源迁移给 Ra。

## Assumptions

数值复核沿用各工件明确写出的 $r_0$、Wigner–Eckart、CG 和评价字段约定。raw 文本中的敏感字段在终端显示可能被渲染替换，但字节级 BE1W 核对已在此前单元完成。

## Competing Explanations

任何数值一致都可能来自同一 ENSDF 评价谱系的重复引用，不等于独立实验确认。近简并仍可由静态八极形变、振动、粒子–芯耦合、Coriolis 混合或偶然能级靠近解释。

## Transfer Conditions

可迁移的是代数和审计方法；不能迁移的是原实验 provenance、带连接、K、组态和静态形变解释。条件 $D_0$ 只在指定转子约定下有意义。

## Failure Conditions

若把评价字段的重复引用当独立证据、把 Ra/Ac 的 E1 来源混写，或将候选 pair 计数升格为物理带认证，结论失效。若忽略正逆方向的初态简并因子，矩阵元和 B 值也会错配。

## Falsification or Reverse Tests

取得原始 1985Is03 等实验正文，逐条核对寿命、转换电子、分支和评价归一；再以共同模型空间的 odd/even 组态计算检验候选 pair 是否同时重现 E1/E2/E3 与能级劈裂。

## Open Questions

Ra E1 的评价 BE1W 与 $(\alpha)(ce)(t)$ 寿命来源之间的完整数据链、Ac E1 的 β− 转换电子归一以及两者的共同微观波函数仍未闭合。

## Human Review

本页为 Codex source self-audit，保持 unreviewed；唯一 provenance 措辞问题已记录，未修改既有页面。

## Promotion or Rejection History

2026-10-28：完成 016/028/030/033/036 与两份 ENSDF source 的数值收敛审计；确认一项 Ra/Ac E1 provenance 措辞需后续修订。

## Next Actions

在原始实验来源取得后修订 provenance 句子，并重做独立来源与共同评价谱系的依赖标记。

## Sources

- [[nndc-2009-ra225-adopted-parity-doublet]]
- [[nndc-2022-ac225-adopted-parity-doublet]]
- `parity-doublet-cross-source-consistency-039.json`（机器可读收敛审计）
