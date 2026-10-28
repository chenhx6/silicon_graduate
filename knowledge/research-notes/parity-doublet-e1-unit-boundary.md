---
type: research-note
title: "225Ra–225Ac E1 强度单位、约化矩阵元与 CG 边界"
aliases: [parity doublet E1 unit boundary, 225Ra 225Ac E1 algebra audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
created_from: Day26 unit033 E1 unit and angular-factor audit
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, E1, Weisskopf-unit, reduced-matrix-element, CG-factor]
---

# $^{225}$Ra–$^{225}$Ac E1 强度单位、约化矩阵元与 CG 边界

## Research Trigger

前一单元得到两核评价 $B(E1)$ 与条件 $D_0$。本页只审计单位转换、初态简并因子和角动量系数，避免把由 $B(E1)$ 反演的 $D_0$ 当成直接实验观测。

## Grounded Evidence

已归档评价字段为：$^{225}$Ra 的 $3/2^-\to1/2^+$、$B(E1)=0.00081(20)$ W.u.；$^{225}$Ac 的 $3/2^+\to3/2^-$、$B(E1)=0.00171(15)$ W.u.。两者均来自 ENSDF 评价对象；Ra 的 E1 字段在 225Ra β− decay 链中带有转换电子来源，Ac 的 40.09-keV E1 字段来自 $^{225}$Ra β− decay 的 L-subshell ratios。原始实验未在本单元重读。

## Provisional Reasoning

### W.u. 到绝对 $B(E1)$

采用 $R=r_0A^{1/3}$、$r_0=1.2$ fm 的约定，

$$1\;\mathrm{W.u.}(E1)=\frac{(3/4)^2}{4\pi}R^2 e^2.$$

对 $A=225$，$R=7.306$ fm，得到 $1\;\mathrm{W.u.}=2.384497\ e^2\mathrm{fm}^2$。所以 Ra 为 $B=0.00193144\pm0.00047690\ e^2\mathrm{fm}^2$，Ac 为 $B=0.00407749\pm0.00035767\ e^2\mathrm{fm}^2$。这些是由 W.u. 误差线性传播的绝对不确定度，保留完整值见 `parity-doublet-e1-unit-audit-033.json`。

### 约化矩阵元与方向简并

采用

$$B(E1;J_i\to J_f)=\frac{|\langle J_f\Vert\mathcal M(E1)\Vert J_i\rangle|^2}{2J_i+1}.$$

因此 $|M|=\sqrt{(2J_i+1)B}$：Ra 得 $|M|=0.087896\pm0.010851\ e\mathrm{fm}$，Ac 得 $|M|=0.127710\pm0.005601\ e\mathrm{fm}$。约化振幅本身存在 $+/-$ 相位分支，B(E1) 不能选符号。反向方向的 B 值满足

$$B_{\mathrm{reverse}}=B_{\mathrm{forward}}\frac{2J_i+1}{2J_f+1}.$$

故 Ra 反向数值为 $0.00162$ W.u.（若同一矩阵元且仅改变初态），Ac 因 $J_i=J_f$ 保持 $0.00171$ W.u.。反向数值不是新的实验点。

### 转子 CG 因子与条件 $D_0$

在轴向强耦合约定下，

$$B(E1)=\frac{3}{4\pi}D_0^2|\langle IK\,10\mid I'K\rangle|^2.$$

Ra 的 $I=3/2\to1/2,K=1/2$ 给 $C^2=(I^2-K^2)/[I(2I+1)]=1/3$，条件 $|D_0|=0.155792\pm0.019234\ e\mathrm{fm}$。Ac 的 $I=3/2\to3/2,K=3/2$ 给 $C^2=K^2/[I(I+1)]=0.6$，条件 $|D_0|=0.168719\pm0.007400\ e\mathrm{fm}$。E1 偶极矩以 $e\mathrm{fm}$ 表示，不能把面积单位 $e\mathrm b$ 用作其换算。去掉 CG 因子会分别给 $0.089947$ 与 $0.130690\ e\mathrm{fm}$，显示几何假设是数值的实质来源。

### 单位和半径敏感性

$B_{\mathrm{WU}}\propto r_0^2$，而 $|D_0|\propto r_0$。将 $r_0$ 从 1.1 到 1.3 fm 改变时，E1 W.u. 从 2.00364 到 2.79847 $e^2\mathrm{fm}^2$，相对 1.2 fm 的平方比例为 0.8403 和 1.1736。因而条件 $D_0$ 不能脱离半径约定比较精度；评价 B(E1) 的 W.u. 本身也带有该约定。

## Assumptions

约化矩阵元采用 $B=|M|^2/(2J_i+1)$；$D_0$ 使用轴向强耦合、无额外分支、同一 K 和 $r_0=1.2$ fm。所有强度为评价数据，未赋予原始实验独立性。

## Competing Explanations

E1 强度受 K 混合、带混合、质子–中子偶极相消和八极振动影响。不同 $\Delta I$ 的 CG 因子差异可以改变条件 $D_0$，所以两核 $D_0$ 近似相等不意味着静态梨形相同。

## Transfer Conditions

可迁移的是 B 与约化矩阵元的 Wigner–Eckart 代数；不可迁移的是 $r_0$、K、CG 选择、带结构、相位和 E1 来源依赖。

## Failure Conditions

若把 W.u. 数字直接当 $e^2\mathrm{fm}^2$、忘记 $2J_i+1$、用错误的正逆初态，或将 $D_0$ 正负号从 B(E1) 强度中读出，结果失效。若把评价字段当新实验，也会破坏证据层级。

## Falsification or Reverse Tests

以同一核的已知寿命、分支和转换系数重建绝对矩阵元；再在多个 E1/E2/E3 支线上检验是否由同一 K、$D_0$ 与相位约定描述。失败则说明单一轴向转子反演不足。

## Open Questions

两核 E1 的转换电子来源、带混合和内禀质子–中子偶极贡献尚未由同一原始数据和统一微观模型闭合。

## Human Review

本页是 Codex source self-audit，保持 unreviewed；条件 $D_0$ 不提升为实验直接量。

## Promotion or Rejection History

2026-10-28：完成 W.u.、约化矩阵元、正逆方向简并和 CG 因子审计；保留半径、符号与转子模型边界。

## Next Actions

获取原始转换电子与寿命数据，检查同一 E1 算符矩阵元在不同方向和分支下的联合协方差。

## Sources

- [[nndc-2009-ra225-adopted-parity-doublet]]
- [[nndc-2022-ac225-adopted-parity-doublet]]
