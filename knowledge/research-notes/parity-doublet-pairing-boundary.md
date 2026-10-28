---
type: research-note
title: "225Ra–225Ac 奇 A 宇称双重态配对边界"
aliases: [parity doublet pairing boundary, 225Ra 225Ac same-spin audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
created_from: Day26 unit030 evaluated-data pairing audit
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, odd-A, Ra225, Ac225, E1, evidence-boundary]
---

# $^{225}$Ra–$^{225}$Ac 奇 A 宇称双重态配对边界

## Research Trigger

同自旋宇称能级差只有在带成员和组态相同的前提下才可作为宇称双重态指标。本页对已归档的两份 ENSDF Adopted 对象执行全配对审计，避免把不同带的最近能级误当成一条交替宇称带。

## Grounded Evidence

### 数据对象

- $^{225}$Ra：`225088001`，固定栏 L 记录归档于 `raw/data/day26-20261028/225ra-adopted-225088001-016.html`，SHA-256 `93ce30628f3f24d08bc1e69c47d2c96e739748868fd03407ddbede9e4732e31e`。
- $^{225}$Ac：`225089001`，固定栏 L/G/B 记录归档于 `raw/data/day26-20261028/225ac-adopted-225089001-028.html`，SHA-256 `fb3d87428e000397881227c3dc96973c1765310a7811062cc8c297259872a817`。

### 全笛卡尔配对算法

对每个数值 $J$，保留所有评价表中正宇称和负宇称态，构造笛卡尔积

$$\Delta E_{ab}(J)=E_a(J^-)-E_b(J^+).$$

不设置能量 cutoff；保留带标签、括号 Jπ 和暂定标记。最近能量配对只作诊断，只有当笛卡尔积大小为 1 时才称“在选定列表中唯一”。完整 pair table、输入 level 与 locator 在 `parity-doublet-pairing-audit-030.json`。

### 结果

| 核 | $J$ | 负宇称数 × 正宇称数 | 最近 $\Delta E=E_-−E_+$ (keV) | 唯一？ |
|---|---:|---:|---:|---|
| $^{225}$Ra | 1/2 | 1×1 | +55.16 | 是 |
| $^{225}$Ra | 3/2 | 2×2 | −11.21 | 否 |
| $^{225}$Ra | 5/2 | 2×3 | +23.95 | 否 |
| $^{225}$Ra | 7/2 | 1×4 | −42.24 | 否 |
| $^{225}$Ra | 9/2 | 1×2 | +103.00 | 否 |
| $^{225}$Ac | 3/2 | 1×1 | −40.10 | 是 |
| $^{225}$Ac | 5/2 | 2×2 | −34.78 | 否 |
| $^{225}$Ac | 7/2 | 2×2 | −27.88 | 否 |
| $^{225}$Ac | 9/2 | 1×2 | −21.44 | 否 |

“最近”并不证明同一内禀构型。$^{225}$Ra 的 3/2、5/2、7/2、9/2 以及 $^{225}$Ac 的 5/2–9/2 结果都存在多带歧义；只报告一个最小值会隐藏这一事实。

### E1 约化矩阵与条件 $D_0$

两核 A=225 的 E1 Weisskopf 单位按 $R=1.2A^{1/3}$ fm 为 $2.384497\ e^2\mathrm{fm}^2$。评价 E1 值转换为：

- $^{225}$Ra：$B(E1)=0.00081(20)$ W.u.，$3/2^-\to1/2^+$，若采用轴向 $K=1/2$、$I_i=3/2\to I_f=1/2$，则 $|\langle IK,1,0|I-1,K\rangle|^2=(I^2-K^2)/[I(2I+1)]=1/3$，条件 $D_0=0.155792\pm0.019234\ e\,\mathrm{fm}$。
- $^{225}$Ac：$B(E1)=0.00171(15)$ W.u.，$3/2^+\to3/2^-$，若采用轴向 $K=3/2$、$I_i=I_f=3/2$，则 $|\langle IK,1,0|IK\rangle|^2=K^2/[I(I+1)]=0.6$，条件 $D_0=0.168719\pm0.007400\ e\,\mathrm{fm}$。

二者均是从评价 B(E1) 反演的模型量，正负号不能由强度平方恢复。两条跃迁的 $\Delta I$、K 假设不同，不能比较 $D_0$ 数值来判定哪个核更静态。

## Provisional Reasoning

两核都显示低能同自旋异宇称候选，但评价表的多带结构使“宇称双重态”只能作为候选描述。$^{225}$Ac 的 3/2 pair 中心差约 40 keV，$^{225}$Ra 的 1/2 pair 约 55 keV；这两个数不具有相同的 K、带和跃迁拓扑，不能形成静态梨形的跨核硬判据。E1 数值也来自不同转移（Ra 的 $\Delta I=1$、Ac 的 $\Delta I=0$），其 CG 因子和 K 依赖不同。

## Assumptions

ENSDF 括号 Jπ 和带标记按评价原样保留；配对只依赖数值 J 与宇称。条件 $D_0$ 使用标准轴向强耦合约定、$R=1.2A^{1/3}$ fm 和无额外未观测分支。

## Competing Explanations

近简并可能由静态反射不对称、八极振动、粒子–芯耦合、Coriolis 混合或偶然能级靠近造成。E1 还受质子–中子偶极相消、K 混合和带混合影响。

## Transfer Conditions

可跨核迁移的是同自旋配对算法和 W.u. 到约化矩阵元的代数；不可迁移的是 K、解耦因子、内禀波函数、带成员和静态形变解释。

## Failure Conditions

若用最近能级替代全笛卡尔配对、忽略括号 Jπ 或把评价对象当作新原实验，则配对结果失效。若用不同 $\Delta I$ 的 E1 线直接比较 $D_0$，也会混淆 CG 几何因子。

## Falsification or Reverse Tests

需要原始寿命、转换电子、分支和组态指认来测试每个候选 pair；若同一带的交替宇称序列不能同时重现 E1/E2/E3 和自旋演化，则静态梨形解释被削弱。

## Open Questions

两核是否存在同源的 odd-particle-plus-octupole-core 计算，能够同时给出配对劈裂、E1 相消和 E3 强度？当前评价对象没有提供这一微观闭合证据。

## Human Review

本页是 Codex source self-audit，保持 unreviewed；评价层结果与条件推导分开保存。

## Promotion or Rejection History

2026-10-28：建立全笛卡尔同自旋配对审计，确认多带歧义和不同 E1 CG 因子阻止跨核静态形变硬判据。

## Next Actions

取得两核原始谱学来源与同一模型空间的阻塞计算，再检验 pair-level E1/E2/E3 联合约束。

## Sources

- [[nndc-2009-ra225-adopted-parity-doublet]]
- [[nndc-2022-ac225-adopted-parity-doublet]]
